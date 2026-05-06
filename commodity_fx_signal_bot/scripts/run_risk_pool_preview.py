"""
Risk Pool Preview
"""

import argparse
from pathlib import Path
import sys

from config.settings import settings
from config.paths import ensure_project_directories, REPORTS_RISK_REPORTS_DIR
from data.storage.data_lake import DataLake
from risk.risk_pool import RiskCandidatePool
from reports.report_builder import build_risk_pool_preview_report
from core.logger import get_logger

logger = get_logger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Preview Risk Pool")
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_pretrade_risk")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--rebuild", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    ensure_project_directories()

    lake = DataLake(Path("data/lake"))

    if args.rebuild or not lake.has_risk_pool(args.timeframe, args.profile):
        logger.info("Rebuilding pool...")
        from risk.risk_pipeline import RiskPipeline
        from data.universe_analyzer import UniverseAnalyzer

        analyzer = UniverseAnalyzer(lake)
        specs = analyzer.get_full_universe()
        pipeline = RiskPipeline(lake, settings)
        pipeline.build_for_universe(specs, args.timeframe, profile=None, save=True)

    df = lake.load_risk_pool(args.timeframe, args.profile)
    if df.empty:
        logger.error("Pool is empty or not found.")
        sys.exit(1)

    pool = RiskCandidatePool.from_dataframe(df)
    summary = pool.summarize()
    top_cands = pool.rank(args.top)

    # create a df from top_cands just for report
    top_df = RiskCandidatePool()
    top_df.extend(top_cands)
    tdf = top_df.to_dataframe()

    report = build_risk_pool_preview_report(args.timeframe, args.profile, summary, tdf)
    print("\n" + report + "\n")

    report_file = (
        REPORTS_RISK_REPORTS_DIR
        / f"risk_pool_preview_{args.timeframe}_{args.profile}.txt"
    )
    report_file.write_text(report)
    logger.info(f"Saved {report_file}")


if __name__ == "__main__":
    main()
