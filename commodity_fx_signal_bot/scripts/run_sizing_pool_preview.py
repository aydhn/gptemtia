import argparse
import sys
import logging
import pandas as pd
from pathlib import Path

from config.settings import settings
from config.paths import REPORTS_SIZING_REPORTS_DIR
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from sizing.sizing_pipeline import SizingPipeline
from sizing.sizing_config import get_sizing_profile
from sizing.sizing_pool import SizingCandidatePool
from reports.report_builder import build_sizing_pool_preview_report

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Preview Sizing Pool")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_theoretical_sizing", help="Sizing profile name")
    parser.add_argument("--top", type=int, default=20, help="Number of top candidates to show")
    parser.add_argument("--rebuild", action="store_true", help="Force rebuild of pool")

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)

    try:
        profile = get_sizing_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        sys.exit(1)

    data_lake = DataLake()

    u_df = pd.DataFrame()
    pool = SizingCandidatePool()

    if not args.rebuild:
        try:
            if hasattr(data_lake, "load_sizing_pool"):
                u_df = data_lake.load_sizing_pool(args.timeframe, args.profile)
            else:
                logger.warning("load_sizing_pool not available on DataLake. Falling back to rebuild.")
        except FileNotFoundError:
            logger.info("Saved sizing pool not found. Falling back to rebuild.")

    if u_df.empty or args.rebuild:
        logger.info(f"Building sizing pool for {args.timeframe} with profile {args.profile}")
        pipeline = SizingPipeline(data_lake, settings, profile)
        specs = get_enabled_symbols()
        res = pipeline.build_for_universe(specs, args.timeframe, profile, save=True)
        try:
            if hasattr(data_lake, "load_sizing_pool"):
                u_df = data_lake.load_sizing_pool(args.timeframe, args.profile)
        except FileNotFoundError:
            logger.error("Failed to load pool even after build.")
            sys.exit(1)

    if u_df.empty:
        logger.warning("Sizing pool is empty.")
        sys.exit(0)

    pool = SizingCandidatePool.from_dataframe(u_df)
    summary = pool.summarize()

    top_candidates = pool.rank(top_n=args.top)
    top_df = pd.DataFrame([c.__dict__ for c in top_candidates])

    report_text = build_sizing_pool_preview_report(args.timeframe, args.profile, summary, top_df)
    print(report_text)

    REPORTS_SIZING_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_SIZING_REPORTS_DIR / f"sizing_pool_preview_{args.timeframe}_{args.profile}.txt"
    with open(report_path, "w") as f:
        f.write(report_text)

    logger.info(f"Saved pool preview report to {report_path}")

if __name__ == "__main__":
    main()
