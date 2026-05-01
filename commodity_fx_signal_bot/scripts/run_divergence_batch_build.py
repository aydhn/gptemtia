import argparse
import logging
from pathlib import Path
import pandas as pd

from config.paths import ensure_project_directories, DIVERGENCE_REPORTS_DIR
from config.settings import settings
from config.symbols import (
    get_symbol_spec,
    get_symbols_by_asset_class,
    get_enabled_symbols,
)
from config.symbols import get_allowed_timeframes_for_symbol
from indicators.indicator_pipeline import IndicatorPipeline
from reports.report_builder import build_divergence_batch_report

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    ensure_project_directories()

    parser = argparse.ArgumentParser(description="Batch build divergence features.")
    parser.add_argument(
        "--limit", type=int, default=None, help="Max symbols to process"
    )
    parser.add_argument(
        "--asset-class", type=str, default=None, help="Filter by asset class"
    )
    parser.add_argument("--symbol", type=str, default=None, help="Filter by symbol")
    parser.add_argument(
        "--timeframe", type=str, default=None, help="Filter by timeframe"
    )
    parser.add_argument("--profile", type=str, default=settings.default_scan_profile)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--no-events", action="store_true")
    parser.add_argument("--save", action="store_true", default=True)
    parser.add_argument("--use-processed", action="store_true", default=True)
    parser.add_argument("--merge-saved-features", action="store_true", default=True)

    args = parser.parse_args()

    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if not spec:
            logger.error(f"Symbol {args.symbol} not found.")
            return
        specs = [spec]
    elif args.asset_class:
        specs = get_symbols_by_asset_class(args.asset_class)
    else:
        specs = get_enabled_symbols()

    timeframes_by_symbol = {}
    for spec in specs:
        if args.timeframe:
            timeframes_by_symbol[spec.name] = (args.timeframe,)
        else:
            timeframes_by_symbol[spec.name] = get_allowed_timeframes_for_symbol(spec)

    logger.info(f"Starting batch divergence build for {len(specs)} symbols.")

    pipeline = IndicatorPipeline()

    results = pipeline.build_divergence_for_universe(
        specs,
        timeframes_by_symbol,
        limit=args.limit,
        use_processed=args.use_processed,
        save=args.save,
        compact=not args.full,
        include_events=not args.no_events,
    )

    if not isinstance(results, dict):
        logger.error("Pipeline returned unexpected format.")
        return

    if results.get("status") == "disabled":
        logger.info("Divergence features disabled in settings.")
        return

    report_text = build_divergence_batch_report(results)

    print(report_text)

    DIVERGENCE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    txt_path = DIVERGENCE_REPORTS_DIR / "divergence_batch_summary.txt"
    with open(txt_path, "w") as f:
        f.write(report_text)

    logger.info(f"Batch report saved to {txt_path}")


if __name__ == "__main__":
    main()
