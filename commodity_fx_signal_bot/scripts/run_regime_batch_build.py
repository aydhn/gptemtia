"""
Batch script to build regime features for multiple symbols.
"""

import argparse
import logging

from config.symbols import DEFAULT_SYMBOL_UNIVERSE, get_symbol_spec
from config.settings import settings
from config.paths import REGIME_REPORTS_DIR
from data.storage.data_lake import DataLake
from regimes.regime_config import get_regime_profile
from regimes.regime_pipeline import RegimePipeline
from reports.report_builder import build_regime_batch_report, save_text_report

logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Batch build regime features.")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Specific symbol to process")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--profile", type=str, default="balanced_regime", help="Regime profile")
    parser.add_argument("--no-save", action="store_true", help="Do not save to Data Lake")
    parser.add_argument("--no-events", action="store_true", help="Do not generate events")
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    args = parse_args()

    specs = []
    if args.symbol:
        try:
            specs = [get_symbol_spec(args.symbol)]
        except Exception as e:
            logger.error(f"Symbol error: {e}")
            return
    else:
        specs = DEFAULT_SYMBOL_UNIVERSE
        if args.asset_class:
            specs = [s for s in specs if s.asset_class == args.asset_class]

    # Filter out synthetic and macro
    specs = [s for s in specs if not s.is_synthetic() and not s.is_macro()]

    try:
        profile = get_regime_profile(args.profile)
    except Exception as e:
        logger.error(f"Profile error: {e}")
        return

    lake = DataLake()
    pipeline = RegimePipeline(lake, settings, profile)

    logger.info(f"Starting regime batch build for {len(specs)} symbols (max {args.limit if args.limit else 'all'})")

    summary = pipeline.build_for_universe(
        specs=specs,
        timeframe=args.timeframe,
        profile=profile,
        limit=args.limit,
        save=not args.no_save,
        include_events=not args.no_events
    )

    report = build_regime_batch_report(summary)
    print(report)

    report_path = REGIME_REPORTS_DIR / "regime_batch_summary.txt"
    save_text_report(report, report_path)
    logger.info(f"Batch report saved to {report_path}")

if __name__ == "__main__":
    main()
