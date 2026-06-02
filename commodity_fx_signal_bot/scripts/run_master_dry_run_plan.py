#!/usr/bin/env python
"""
Run Master Dry Run Execution Plan script.
"""

import argparse
import sys
import logging
from pathlib import Path

from config.paths import PROJECT_ROOT
from config.settings import Settings
from data.storage.data_lake import DataLake
from master_orchestration.master_pipeline import MasterOrchestrationPipeline
from master_orchestration.master_config import get_master_orchestration_profile

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Generate Master Dry Run Execution Plan.")
    parser.add_argument("--mode", type=str, default="daily_offline_review_mode", help="Operating mode to use")
    parser.add_argument("--profile", type=str, default="balanced_offline_master", help="Master orchestration profile to use")
    parser.add_argument("--no-save", action="store_true", help="Do not save reports to disk")
    args = parser.parse_args()

    logger.info(f"Initializing Master Dry Run Plan for mode: {args.mode}")
    settings = Settings()

    if not settings.master_orchestration_enabled:
        logger.warning("Master Orchestration is disabled in settings.")
        sys.exit(0)

    try:
        profile = get_master_orchestration_profile(args.profile)
    except Exception as e:
        logger.error(f"Failed to load profile {args.profile}: {e}")
        sys.exit(1)

    data_lake = DataLake(PROJECT_ROOT)
    pipeline = MasterOrchestrationPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=PROJECT_ROOT,
        profile=profile
    )

    try:
        plan_df, summary = pipeline.build_master_dry_run_plan(operating_mode=args.mode, save=not args.no_save)
        logger.info(f"Master Dry Run Plan generation complete. Summary: {summary}")
    except Exception as e:
        logger.error(f"Failed to generate dry run plan: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
