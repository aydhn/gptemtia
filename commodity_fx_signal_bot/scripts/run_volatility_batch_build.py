import argparse
import logging
import sys

import pandas as pd

from config.paths import VOLATILITY_REPORTS_DIR
from config.settings import settings
from config.symbols import get_enabled_symbols, get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.feature_builder import FeatureBuilder
from indicators.indicator_pipeline import IndicatorPipeline
from reports.report_builder import build_volatility_batch_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Batch build volatility features.")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Run for specific symbol")
    parser.add_argument("--timeframe", type=str, help="Run for specific timeframe")
    parser.add_argument(
        "--profile",
        type=str,
        default=settings.default_scan_profile,
        help="Scan profile to use",
    )
    parser.add_argument(
        "--full", action="store_true", help="Build full volatility feature set"
    )
    parser.add_argument("--no-events", action="store_true", help="Skip event columns")
    parser.add_argument("--no-save", action="store_true", help="Do not save to disk")
    parser.add_argument(
        "--no-use-processed", action="store_true", help="Do not use processed data"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if not spec:
            logger.error(f"Symbol {args.symbol} not found")
            sys.exit(1)
        specs = [spec]
    else:
        specs = get_enabled_symbols()
        if args.asset_class:
            specs = [s for s in specs if s.asset_class == args.asset_class]

    # For now just use standard timeframes if profile not fully hooked up
    timeframes_by_symbol = {}
    default_tfs = ["1d"]
    if args.timeframe:
        default_tfs = [args.timeframe]

    for s in specs:
        timeframes_by_symbol[s.symbol] = tuple(default_tfs)

    from config.paths import DATA_DIR

    pipeline = IndicatorPipeline(DataLake(DATA_DIR), FeatureBuilder())

    compact = not args.full
    include_events = not args.no_events
    save = not args.no_save
    use_processed = not args.no_use_processed

    logger.info(
        f"Starting batch build for {len(specs)} symbols (compact={compact}, events={include_events})"
    )

    results = pipeline.build_volatility_for_universe(
        specs=specs,
        timeframes_by_symbol=timeframes_by_symbol,
        limit=args.limit,
        use_processed=use_processed,
        save=save,
        compact=compact,
        include_events=include_events,
    )

    report = build_volatility_batch_report(results)

    VOLATILITY_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = VOLATILITY_REPORTS_DIR / "volatility_batch_summary.txt"
    csv_file = VOLATILITY_REPORTS_DIR / "volatility_batch_summary.csv"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    if results["details"]:
        df = pd.DataFrame(results["details"])
        df.to_csv(csv_file, index=False)

    print(report)
    print(f"\nReports saved to {VOLATILITY_REPORTS_DIR}")


if __name__ == "__main__":
    main()
