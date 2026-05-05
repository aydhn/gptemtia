import argparse
import sys
from pathlib import Path
import logging

from config.symbols import get_enabled_symbols
from config.settings import settings
from data.storage.data_lake import DataLake
from decisions import DecisionPipeline, get_decision_profile, DecisionCandidatePool
from ml.feature_store import FeatureStore
from reports.report_builder import build_decision_pool_preview_report

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Preview decision pool")
    parser.add_argument("--timeframe", default="1d", help="Timeframe (e.g., 1d, 1h)")
    parser.add_argument(
        "--profile", default="balanced_directional_decision", help="Decision profile"
    )
    parser.add_argument(
        "--top", type=int, default=20, help="Number of top decisions to show"
    )
    parser.add_argument(
        "--rebuild", action="store_true", help="Rebuild pool before previewing"
    )

    args = parser.parse_args()

    try:
        profile = get_decision_profile(args.profile)
    except Exception as e:
        logger.error(f"Error getting decision profile: {e}")
        return

    data_lake = DataLake()

    if args.rebuild:
        logger.info("Rebuilding universe pool...")
        pipeline = DecisionPipeline(data_lake, settings, profile)
        pipeline.build_for_universe(
            get_enabled_symbols(), args.timeframe, profile, save=True
        )

    fs = FeatureStore(data_lake)
    df = fs.load_decision_pool(args.timeframe, args.profile)

    if df.empty:
        logger.warning(f"No decision pool found for {args.timeframe} {args.profile}")
        return

    pool = DecisionCandidatePool.from_dataframe(df)
    summary = pool.summarize()
    top_decisions = pool.rank(args.top)

    # Create top df
    from decisions.decision_candidate import decision_candidate_to_dict
    import pandas as pd

    top_df = pd.DataFrame([decision_candidate_to_dict(d) for d in top_decisions])

    report = build_decision_pool_preview_report(
        args.timeframe, args.profile, summary, top_df
    )

    print("\n" + report)

    from config.paths import DECISION_REPORTS_DIR

    DECISION_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = (
        DECISION_REPORTS_DIR
        / f"decision_pool_preview_{args.timeframe}_{args.profile}.txt"
    )
    report_path.write_text(report, encoding="utf-8")
    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
