import argparse
import logging

from config.paths import LAKE_DIR, REPORTS_DIR
from config.settings import settings
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from reports.report_builder import build_strategy_pool_preview_report
from strategies.strategy_config import get_strategy_selection_profile
from strategies.strategy_pipeline import StrategyPipeline
from strategies.strategy_pool import StrategyCandidatePool

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Preview strategy candidate pool")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument(
        "--profile",
        type=str,
        default="balanced_strategy_selection",
        help="Strategy profile",
    )
    parser.add_argument("--top", type=int, default=20, help="Top N candidates to show")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild pool")
    args = parser.parse_args()

    data_lake = DataLake(LAKE_DIR)

    try:
        profile = get_strategy_selection_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        return

    pool_df = None
    if not args.rebuild and data_lake.has_strategy_pool(args.timeframe, profile.name):
        logger.info("Loading existing strategy pool")
        pool_df = data_lake.load_strategy_pool(args.timeframe, profile.name)

    if pool_df is None or pool_df.empty:
        logger.info("Rebuilding strategy pool...")
        pipeline = StrategyPipeline(data_lake, settings, profile)
        summary = pipeline.build_for_universe(
            get_enabled_symbols(), args.timeframe, profile
        )
        if data_lake.has_strategy_pool(args.timeframe, profile.name):
            pool_df = data_lake.load_strategy_pool(args.timeframe, profile.name)

    if pool_df is None or pool_df.empty:
        logger.warning("No strategy pool available")
        return

    pool = StrategyCandidatePool.from_dataframe(pool_df)
    summary = pool.summarize()

    top_candidates = pool.rank(args.top)

    top_pool = StrategyCandidatePool()
    top_pool.extend(top_candidates)
    top_df = top_pool.to_dataframe()

    report = build_strategy_pool_preview_report(
        args.timeframe, args.profile, summary, top_df
    )
    print("\n" + report + "\n")

    out_dir = REPORTS_DIR / "strategy_reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"strategy_pool_preview_{args.timeframe}_{args.profile}.txt"
    out_file.write_text(report, encoding="utf-8")
    logger.info(f"Report saved to {out_file}")


if __name__ == "__main__":
    main()
