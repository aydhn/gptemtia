import argparse
import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from macro.macro_config import get_macro_profile
from macro.macro_pipeline import MacroPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Preview Macro Features")
    parser.add_argument("--profile", type=str, default="turkey_inflation_fx")
    parser.add_argument("--last", type=int, default=24)
    return parser.parse_args()


def main():
    args = parse_args()
    lake = DataLake(settings)
    profile = get_macro_profile(args.profile)
    pipeline = MacroPipeline(data_lake=lake, settings=settings, profile=profile)

    logger.info(f"Building macro features for profile {profile.name}...")
    df, summary = pipeline.build_macro_features(save=False)

    if not df.empty:
        print(f"\n--- MACRO FEATURES (Last {args.last}) ---")
        print(df.tail(args.last).to_string())
    else:
        logger.warning("No data returned.")


if __name__ == "__main__":
    main()
