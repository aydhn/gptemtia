"""
Risk Batch Build for universe
"""

import argparse
from pathlib import Path
import sys
import pandas as pd

from config.settings import settings
from config.paths import ensure_project_directories, REPORTS_RISK_REPORTS_DIR
from data.storage.data_lake import DataLake
from data.universe_analyzer import UniverseAnalyzer
from risk.risk_pipeline import RiskPipeline
from risk.risk_config import get_risk_precheck_profile
from reports.report_builder import build_risk_batch_report
from core.logger import get_logger

logger = get_logger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Run Risk Batch Build")
    parser.add_argument("--limit", type=int, help="Limit number of symbols to process")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Process a specific symbol")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument(
        "--profile",
        type=str,
        default="balanced_pretrade_risk",
        help="Risk profile name",
    )
    parser.add_argument(
        "--save", action="store_true", default=True, help="Save to DataLake"
    )
    return parser.parse_args()


def main():

    args = parse_args()

    ensure_project_directories()

    lake = DataLake(Path("data/lake"))
    analyzer = UniverseAnalyzer(lake)
    specs = analyzer.get_full_universe()

    if args.symbol:
        specs = [s for s in specs if s.symbol == args.symbol]
    elif args.asset_class:
        specs = [s for s in specs if s.asset_class.lower() == args.asset_class.lower()]

    try:
        profile = get_risk_precheck_profile(args.profile)
    except Exception as e:
        logger.error(f"Invalid risk profile: {e}")
        sys.exit(1)

    pipeline = RiskPipeline(lake, settings, profile)

    logger.info(
        f"Running risk batch build for {len(specs)} symbols with profile {args.profile}..."
    )
    summary = pipeline.build_for_universe(
        specs, args.timeframe, profile, args.limit, save=args.save
    )

    report = build_risk_batch_report(summary)
    print("\n" + report + "\n")

    report_file = REPORTS_RISK_REPORTS_DIR / "risk_batch_summary.txt"
    report_file.write_text(report)

    csv_file = REPORTS_RISK_REPORTS_DIR / "risk_batch_summary.csv"
    if summary.get("symbol_summaries"):
        df = pd.DataFrame.from_dict(summary["symbol_summaries"], orient="index")
        df.to_csv(csv_file)

    logger.info(f"Reports saved to {REPORTS_RISK_REPORTS_DIR}")


if __name__ == "__main__":
    main()
