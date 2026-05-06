"""
Single symbol Risk Precheck Preview
"""

import argparse
from pathlib import Path
import sys

from config.settings import settings
from config.paths import ensure_project_directories, REPORTS_RISK_REPORTS_DIR
from data.storage.data_lake import DataLake
from data.universe_analyzer import UniverseAnalyzer
from risk.risk_pipeline import RiskPipeline
from risk.risk_config import get_risk_precheck_profile
from reports.report_builder import build_risk_precheck_preview_report
from core.logger import get_logger

logger = get_logger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run Risk Precheck Preview for a symbol"
    )
    parser.add_argument("--symbol", type=str, required=True, help="Symbol ticker")
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)"
    )
    parser.add_argument(
        "--profile",
        type=str,
        default="balanced_pretrade_risk",
        help="Risk profile name",
    )
    parser.add_argument(
        "--last", type=int, default=10, help="Number of recent candidates to display"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save the feature dataframe to DataLake"
    )
    return parser.parse_args()


def main():

    args = parse_args()

    ensure_project_directories()

    lake = DataLake(Path("data/lake"))
    analyzer = UniverseAnalyzer(lake)
    specs = analyzer.get_full_universe()

    spec = next((s for s in specs if s.symbol == args.symbol), None)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in universe.")
        sys.exit(1)

    try:
        profile = get_risk_precheck_profile(args.profile)
    except Exception as e:
        logger.error(f"Invalid risk profile: {e}")
        sys.exit(1)

    pipeline = RiskPipeline(lake, settings, profile)

    logger.info(
        f"Running risk precheck for {args.symbol} ({args.timeframe}) with profile {args.profile}..."
    )
    df, summary = pipeline.build_for_symbol_timeframe(
        spec, args.timeframe, profile, save=args.save
    )

    tail_df = df.tail(args.last) if not df.empty else df
    report = build_risk_precheck_preview_report(
        args.symbol, args.timeframe, args.profile, summary, tail_df
    )

    print("\n" + report + "\n")

    report_file = (
        REPORTS_RISK_REPORTS_DIR
        / f"risk_precheck_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
    )
    report_file.write_text(report)
    logger.info(f"Report saved to {report_file}")


if __name__ == "__main__":
    main()
