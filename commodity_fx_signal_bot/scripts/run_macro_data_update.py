import argparse
import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from macro.macro_config import get_macro_profile
from macro.macro_pipeline import MacroPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Update Macro Data")
    parser.add_argument("--profile", type=str, default="turkey_inflation_fx")
    parser.add_argument("--start-date", type=str, default="2010-01-01")
    return parser.parse_args()


def main():
    args = parse_args()
    lake = DataLake(settings)
    profile = get_macro_profile(args.profile)
    pipeline = MacroPipeline(data_lake=lake, settings=settings, profile=profile)

    logger.info(f"Updating macro data for profile {profile.name}...")
    results, summary = pipeline.update_macro_data(start_date=args.start_date, save=True)

    logger.info(f"Update complete: {summary}")


if __name__ == "__main__":
    main()
