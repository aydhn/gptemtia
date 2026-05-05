"""
Script to build asset profiles for multiple symbols.
"""

import argparse
import logging
import pandas as pd

from config.settings import settings
from config.paths import LAKE_DIR, ASSET_PROFILE_REPORTS_DIR
from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from data.storage.data_lake import DataLake
from asset_profiles.asset_profile_pipeline import AssetProfilePipeline
import reports.report_builder as report_builder

logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Batch build asset profiles")
    parser.add_argument("--limit", type=int, help="Limit number of symbols to process")
    parser.add_argument("--asset-class", type=str, help="Process specific asset class")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument(
        "--save", action="store_true", default=True, help="Save features"
    )
    parser.add_argument("--no-events", action="store_true", help="Skip event detection")
    args = parser.parse_args()

    data_lake = DataLake(LAKE_DIR)
    pipeline = AssetProfilePipeline(data_lake, settings, args.timeframe)

    logger.info(f"Starting batch build for timeframe {args.timeframe}")

    if args.asset_class:
        logger.info(f"Filtering to asset class: {args.asset_class}")
        symbols = [
            s for s in DEFAULT_SYMBOL_UNIVERSE if s.asset_class == args.asset_class
        ]
        if args.limit:
            symbols = symbols[: args.limit]

        summary = pipeline.build_for_asset_class(
            asset_class=args.asset_class,
            symbols=DEFAULT_SYMBOL_UNIVERSE,  # Need full universe for group context
            timeframe=args.timeframe,
            save=args.save,
            include_events=not args.no_events,
        )
        # Format to match build_for_universe output for reporting
        formatted_summary = {
            "processed": sum(
                1 for s in summary["symbols"].values() if not s.get("warnings")
            ),
            "errors": sum(1 for s in summary["symbols"].values() if s.get("warnings")),
            "asset_classes": {args.asset_class: summary},
        }
        report = report_builder.build_asset_profile_batch_report(formatted_summary)
    else:
        summary = pipeline.build_for_universe(
            symbols=DEFAULT_SYMBOL_UNIVERSE,
            timeframe=args.timeframe,
            limit=args.limit,
            save=args.save,
            include_events=not args.no_events,
        )
        report = report_builder.build_asset_profile_batch_report(summary)

    print("\n" + report + "\n")

    ASSET_PROFILE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = ASSET_PROFILE_REPORTS_DIR / "asset_profile_batch_summary.txt"
    report_path.write_text(report)
    logger.info(f"Report saved to {report_path}")

    # Save CSV summary
    rows = []
    for ac, ac_sum in summary.get("asset_classes", {}).items():
        if isinstance(ac_sum, dict) and "symbols" in ac_sum:
            for sym, sym_sum in ac_sum["symbols"].items():
                rows.append(
                    {
                        "symbol": sym,
                        "asset_class": ac,
                        "profile": sym_sum.get("asset_profile"),
                        "regime": sym_sum.get("latest_asset_regime"),
                        "group_regime": sym_sum.get("latest_group_regime"),
                        "warnings": len(sym_sum.get("warnings", [])),
                    }
                )

    if rows:
        df = pd.DataFrame(rows)
        csv_path = ASSET_PROFILE_REPORTS_DIR / "asset_profile_batch_summary.csv"
        df.to_csv(csv_path, index=False)
        logger.info(f"CSV summary saved to {csv_path}")


if __name__ == "__main__":
    main()
