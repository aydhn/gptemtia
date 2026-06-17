"""
Script to check timeline status.
"""

import argparse
import sys
from pathlib import Path
import traceback

from config.paths import PROJECT_ROOT
from config.settings import Settings
from data.storage.data_lake import DataLake
from core.logger import get_logger
from local_timeline.timeline_config import get_local_timeline_profile
from local_timeline.timeline_pipeline import LocalTimelinePipeline

logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run Timeline Status")
    parser.add_argument("--profile", type=str, default="balanced_local_timeline", help="Local Timeline Profile name")
    parser.add_argument("--no-save", action="store_true", help="Do not save the results")
    args = parser.parse_args()

    try:
        settings = Settings()
        data_lake = DataLake(settings)
        profile = get_local_timeline_profile(args.profile)

        logger.info(f"Initializing LocalTimelinePipeline with profile: {profile.name}")
        pipeline = LocalTimelinePipeline(data_lake, settings, PROJECT_ROOT, profile)

        logger.info("Checking timeline status...")
        df, summary = pipeline.build_timeline_status(save=not args.no_save)

        logger.info(f"Successfully checked timeline status. Found {summary.get('total_files', 0)} files.")

    except Exception as e:
        logger.error(f"Error checking timeline status: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
