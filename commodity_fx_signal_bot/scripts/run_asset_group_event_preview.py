"""
Script to preview group events for an asset class.
"""

import argparse
import logging

from config.settings import settings
from config.paths import LAKE_DIR, ASSET_PROFILE_REPORTS_DIR
from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from data.storage.data_lake import DataLake
from asset_profiles.asset_profile_pipeline import AssetProfilePipeline
import reports.report_builder as report_builder

logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Preview asset group events")
    parser.add_argument(
        "--asset-class", type=str, required=True, help="Asset class (e.g. metals)"
    )
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--last", type=int, default=20, help="Number of rows to show")
    args = parser.parse_args()

    data_lake = DataLake(LAKE_DIR)
    pipeline = AssetProfilePipeline(data_lake, settings, args.timeframe)

    logger.info(f"Building group features for {args.asset_class} ({args.timeframe})")

    # We can use build_for_asset_class to ensure group features are generated and cached
    summary = pipeline.build_for_asset_class(
        asset_class=args.asset_class,
        symbols=DEFAULT_SYMBOL_UNIVERSE,
        timeframe=args.timeframe,
        save=True,
        include_events=True,
    )

    if not data_lake.has_group_features(args.asset_class, args.timeframe):
        logger.error(f"No group features found for {args.asset_class}")
        return

    df = data_lake.load_group_features(args.asset_class, args.timeframe)

    if df.empty:
        logger.error(f"Group features dataframe is empty for {args.asset_class}")
        return

    # Extract member info from summary if possible, else just use columns
    group_summary = {
        "rows": len(df),
        "members": [
            s.symbol
            for s in DEFAULT_SYMBOL_UNIVERSE
            if s.asset_class == args.asset_class
        ],
        "warnings": summary.get("warnings", []),
    }

    tail_df = df.tail(args.last)

    report = report_builder.build_asset_group_event_preview_report(
        args.asset_class, args.timeframe, group_summary, tail_df
    )

    print("\n" + report + "\n")

    ASSET_PROFILE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = (
        ASSET_PROFILE_REPORTS_DIR
        / f"asset_group_event_preview_{args.asset_class}_{args.timeframe}.txt"
    )
    report_path.write_text(report)
    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
