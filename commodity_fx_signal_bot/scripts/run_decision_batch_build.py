import argparse
import sys
from pathlib import Path
import logging

from config.symbols import get_symbol_spec, get_enabled_symbols
from config.settings import settings
from data.storage.data_lake import DataLake
from decisions import DecisionPipeline, get_decision_profile
from reports.report_builder import build_decision_batch_report

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Batch build decision candidates for universe"
    )
    parser.add_argument("--limit", type=int, help="Limit number of symbols to process")
    parser.add_argument("--asset-class", help="Filter by asset class")
    parser.add_argument("--symbol", help="Process only specific symbol")
    parser.add_argument("--timeframe", default="1d", help="Timeframe (e.g., 1d, 1h)")
    parser.add_argument(
        "--profile", default="balanced_directional_decision", help="Decision profile"
    )
    parser.add_argument("--no-save", action="store_true", help="Do not save outputs")

    args = parser.parse_args()

    try:
        profile = get_decision_profile(args.profile)
    except Exception as e:
        logger.error(f"Error getting decision profile: {e}")
        return

    specs = []
    if args.symbol:
        try:
            specs.append(get_symbol_spec(args.symbol))
        except Exception as e:
            logger.error(f"Symbol not found: {args.symbol}")
            return
    elif args.asset_class:
        specs = [
            s
            for s in get_enabled_symbols()
            if s.asset_class.lower() == args.asset_class.lower()
        ]
    else:
        specs = get_enabled_symbols()

    data_lake = DataLake()
    pipeline = DecisionPipeline(data_lake, settings, profile)

    logger.info(f"Starting batch build for {len(specs)} symbols (limit: {args.limit})")

    summary = pipeline.build_for_universe(
        specs=specs,
        timeframe=args.timeframe,
        profile=profile,
        limit=args.limit,
        save=not args.no_save,
    )

    report = build_decision_batch_report(summary)
    print("\n" + report)

    from config.paths import DECISION_REPORTS_DIR

    DECISION_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = (
        DECISION_REPORTS_DIR
        / f"decision_batch_summary_{args.timeframe}_{args.profile}.txt"
    )
    report_path.write_text(report, encoding="utf-8")
    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
