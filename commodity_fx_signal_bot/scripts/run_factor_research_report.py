import argparse
import sys
import logging
import pandas as pd
from pathlib import Path

# Fix python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from config.paths import DATA_DIR
from data.storage.data_lake import DataLake
from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from factor_research.factor_pipeline import FactorResearchPipeline
from factor_research.factor_config import get_factor_research_profile


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run full factor research pipeline")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Run for single symbol (usually not useful for cross-sectional)")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (default 1d)")
    parser.add_argument("--profile", type=str, default="balanced_factor_research", help="Factor research profile")
    parser.add_argument("--no-save", action="store_true", help="Do not save reports to disk")
    args = parser.parse_args()

    data_lake = DataLake(DATA_DIR / "lake")

    universe = DEFAULT_SYMBOL_UNIVERSE

    if args.asset_class:
        universe = [s for s in universe if s.asset_class == args.asset_class]

    if args.symbol:
        universe = [s for s in universe if s.symbol == args.symbol]

    if args.limit:
        universe = universe[:args.limit]

    if not universe:
        logger.error("No symbols matched criteria.")
        sys.exit(1)

    try:
        profile = get_factor_research_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        sys.exit(1)

    logger.info(f"Running factor research pipeline for {len(universe)} symbols using profile {profile.name} on timeframe {args.timeframe}")

    pipeline = FactorResearchPipeline(data_lake, settings, profile)

    save = not args.no_save
    summary, status = pipeline.build_factor_research_report(universe, timeframe=args.timeframe, save=save)

    if status.get("warnings"):
        for w in status["warnings"]:
            logger.warning(w)

    if save and "composite_ranking" in locals(): # In the real code tables dict is accessible or we load it from datalake
         # Load to output text report
         try:
             rank_df = data_lake.load_factor_rank_table(args.timeframe, profile.name)
             backtest_df = data_lake.load_factor_backtest_results(args.timeframe, profile.name)

             tables = {}
             if not rank_df.empty: tables["composite_ranking"] = rank_df
             if not backtest_df.empty: tables["backtest_results"] = backtest_df

             from reports import report_builder
             txt = report_builder.build_factor_research_text_report(summary, tables)

             txt_path = settings.paths.factor_research_reports_txt / f"factor_research_{args.timeframe}_{profile.name}.txt"
             with open(txt_path, "w", encoding="utf-8") as f:
                 f.write(txt)

             logger.info(f"Text report saved to {txt_path}")
         except Exception as e:
             logger.error(f"Error saving text report: {e}")

    logger.info("Factor research complete.")

if __name__ == "__main__":
    main()
