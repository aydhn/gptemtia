import argparse
import sys
import traceback
from pathlib import Path

from config.paths import PROJECT_ROOT
from config.settings import Settings
from data.storage.data_lake import DataLake
from core.logger import get_logger
from local_simplification.simplification_config import get_local_simplification_profile
from local_simplification.simplification_pipeline import LocalSimplificationPipeline

logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Simplification status")
    parser.add_argument("--profile", type=str, default="balanced_local_simplification", help="Local Simplification Profile name")
    parser.add_argument("--no-save", action="store_true", help="Do not save the results")
    args = parser.parse_args()

    try:
        settings = Settings()
        data_lake = DataLake(settings)
        profile = get_local_simplification_profile(args.profile)

        logger.info(f"Initializing LocalSimplificationPipeline with profile: {profile.name}")
        pipeline = LocalSimplificationPipeline(data_lake, settings, PROJECT_ROOT, profile)

        logger.info("Running Simplification status...")
        pipeline.build_simplification_status(save=not args.no_save)

        logger.info(f"Successfully finished Simplification status")

    except Exception as e:
        logger.error(f"Error running Simplification status: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
