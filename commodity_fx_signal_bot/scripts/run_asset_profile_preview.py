"""
Script to preview asset profile for a single symbol.
"""

import argparse
import logging
from pathlib import Path

from config.settings import settings
from config.paths import LAKE_DIR, ASSET_PROFILE_REPORTS_DIR
from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from data.storage.data_lake import DataLake
from asset_profiles.asset_profile_pipeline import AssetProfilePipeline
import reports.report_builder as report_builder

logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Preview asset profile for a symbol")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 1h)"
    )
    parser.add_argument("--last", type=int, default=10, help="Number of rows to show")
    parser.add_argument("--no-events", action="store_true", help="Skip event detection")
    parser.add_argument(
        "--save", action="store_true", help="Save features to data lake"
    )
    args = parser.parse_args()

    spec = next((s for s in DEFAULT_SYMBOL_UNIVERSE if s.symbol == args.symbol), None)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in universe.")
        return

    data_lake = DataLake(LAKE_DIR)
    pipeline = AssetProfilePipeline(data_lake, settings, args.timeframe)

    logger.info(f"Building asset profile for {args.symbol} ({args.timeframe})")

    df, summary = pipeline.build_for_symbol(
        spec=spec,
        all_symbols=DEFAULT_SYMBOL_UNIVERSE,
        timeframe=args.timeframe,
        save=args.save,
        include_events=not args.no_events,
    )

    if df.empty:
        logger.error(f"Failed to build asset profile for {args.symbol}")
        for w in summary.get("warnings", []):
            logger.error(f"Warning: {w}")
        return

    tail_df = df.tail(args.last)

    report = report_builder.build_asset_profile_preview_report(
        args.symbol, args.timeframe, summary, tail_df
    )

    print("\n" + report + "\n")

    # Save report
    ASSET_PROFILE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = (
        ASSET_PROFILE_REPORTS_DIR
        / f"asset_profile_preview_{args.symbol.replace('=', '_')}_{args.timeframe}.txt"
    )
    report_path.write_text(report)
    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
