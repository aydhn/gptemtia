"""
Script to build and save timeline validation and quality reports.
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
    parser = argparse.ArgumentParser(description="Run Timeline Quality Report")
    parser.add_argument("--profile", type=str, default="balanced_local_timeline", help="Local Timeline Profile name")
    parser.add_argument("--no-save", action="store_true", help="Do not save the results")
    args = parser.parse_args()

    try:
        settings = Settings()
        data_lake = DataLake(settings)
        profile = get_local_timeline_profile(args.profile)

        logger.info(f"Initializing LocalTimelinePipeline with profile: {profile.name}")
        pipeline = LocalTimelinePipeline(data_lake, settings, PROJECT_ROOT, profile)

        logger.info("Building timeline quality report...")
        quality, manifest = pipeline.build_timeline_quality_report(save=not args.no_save)

        logger.info(f"Successfully processed timeline quality. Passed: {quality.get('passed', False)}")

    except Exception as e:
        logger.error(f"Error building timeline quality report: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
