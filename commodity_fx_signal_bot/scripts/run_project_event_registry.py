"""
Script to build and save the project event registry.
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
    parser = argparse.ArgumentParser(description="Run Project Event Registry Builder")
    parser.add_argument("--profile", type=str, default="balanced_local_timeline", help="Local Timeline Profile name")
    parser.add_argument("--no-save", action="store_true", help="Do not save the results")
    args = parser.parse_args()

    try:
        settings = Settings()
        data_lake = DataLake(settings)
        profile = get_local_timeline_profile(args.profile)

        logger.info(f"Initializing LocalTimelinePipeline with profile: {profile.name}")
        pipeline = LocalTimelinePipeline(data_lake, settings, PROJECT_ROOT, profile)

        logger.info("Building project event registry...")
        df, summary = pipeline.build_project_event_registry(save=not args.no_save)

        logger.info(f"Successfully processed {summary.get('total_events', 0)} events.")

    except Exception as e:
        logger.error(f"Error building project event registry: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
