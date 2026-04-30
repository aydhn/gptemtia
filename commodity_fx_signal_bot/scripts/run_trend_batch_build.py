import argparse
import logging
from typing import Optional

from config.scan_config import get_scan_profile
from config.settings import settings
from config.symbols import (
    get_symbols_by_asset_class,
    get_symbol_spec,
    DEFAULT_SYMBOL_UNIVERSE,
)
from data.storage.data_lake import DataLake
from indicators.feature_builder import FeatureBuilder
from indicators.indicator_pipeline import IndicatorPipeline
from reports.report_builder import build_trend_batch_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Batch build trend features")
    parser.add_argument("--limit", type=int, help="Limit number of combinations")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Single symbol to process")
    parser.add_argument("--timeframe", type=str, help="Single timeframe to process")
    parser.add_argument(
        "--profile",
        type=str,
        default=settings.default_scan_profile,
        help="Scan profile",
    )
    parser.add_argument(
        "--full", action="store_true", help="Build full feature set instead of compact"
    )
    parser.add_argument("--no-events", action="store_true", help="Skip event columns")
    parser.add_argument(
        "--save", action="store_true", default=True, help="Save to data lake"
    )
    parser.add_argument(
        "--use-processed",
        action="store_true",
        default=True,
        help="Use processed data if available",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    from config.paths import LAKE_DIR, TREND_REPORTS_DIR

    lake = DataLake(LAKE_DIR)
    builder = FeatureBuilder()
    pipeline = IndicatorPipeline(lake, builder, settings)

    specs = []
    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if spec:
            specs = [spec]
    elif args.asset_class:
        specs = get_symbols_by_asset_class(args.asset_class)
    else:
        specs = DEFAULT_SYMBOL_UNIVERSE

    if not specs:
        logger.error("No symbols found.")
        return

    profile = get_scan_profile(args.profile)
    timeframes_by_symbol = {}

    for s in specs:
        if args.timeframe:
            timeframes_by_symbol[s.symbol] = (args.timeframe,)
        else:
            tfs = tuple(profile.timeframes)
            timeframes_by_symbol[s.symbol] = tfs

    logger.info(f"Starting batch trend build for {len(specs)} symbols...")

    results = pipeline.build_trend_for_universe(
        specs=specs,
        timeframes_by_symbol=timeframes_by_symbol,
        limit=args.limit,
        use_processed=args.use_processed,
        save=args.save,
        compact=not args.full,
        include_events=not args.no_events,
    )

    report_str = build_trend_batch_report(results)
    print("\n" + report_str)

    out_file = TREND_REPORTS_DIR / "trend_batch_summary.txt"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w") as f:
        f.write(report_str)

    # Optional CSV
    import pandas as pd

    if results["details"]:
        df_res = pd.DataFrame(results["details"])
        csv_file = TREND_REPORTS_DIR / "trend_batch_summary.csv"
        df_res.to_csv(csv_file, index=False)

    logger.info(
        f"Batch completed. Success: {results['success_count']}, Failed: {results['failure_count']}, Skipped: {results['skipped_count']}"
    )


if __name__ == "__main__":
    main()
