import argparse
import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from config.symbols import get_enabled_symbols
from synthetic_indices.index_config import get_synthetic_index_profile
from synthetic_indices.index_pipeline import SyntheticIndexPipeline
from synthetic_indices.index_universe import filter_symbols_by_asset_class

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("run_leadership_laggard_report")

def main():
    parser = argparse.ArgumentParser(description="Run leadership laggard report")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--profile", type=str, default="balanced_synthetic_index_research", help="Profile name")
    parser.add_argument("--asset-class", type=str, default=None, help="Filter by asset class")
    parser.add_argument("--limit", type=int, default=None, help="Limit periods")
    parser.add_argument("--save", type=bool, default=True, help="Save outputs")

    args = parser.parse_args()

    data_lake = DataLake(settings)
    profile = get_synthetic_index_profile(args.profile)
    pipeline = SyntheticIndexPipeline(data_lake, settings, profile)

    specs = get_enabled_symbols()
    if args.asset_class:
         specs = filter_symbols_by_asset_class(specs, args.asset_class)

    if not specs:
         logger.error("No symbols found.")
         return

    logger.info(f"Running leadership laggard report. Profile: {args.profile}")
    df, summary = pipeline.build_leadership_laggard_report(
         specs=specs,
         timeframe=args.timeframe,
         limit=args.limit,
         save=args.save
    )

    logger.info("Report complete.")
    for k, v in summary.items():
         if k != "warnings":
              logger.info(f"  {k}: {v}")

if __name__ == "__main__":
    main()
