import argparse
import sys
import logging
from pathlib import Path

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_redteam.redteam_config import get_local_redteam_profile
from local_redteam.redteam_pipeline import LocalRedTeamPipeline

def main():
    parser = argparse.ArgumentParser(description="Run build_safety_assurance_summary")
    parser.add_argument("--profile", type=str, default="balanced_local_redteam")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        settings = Settings()
        project_root = Path(__file__).parent.parent.resolve()
        data_lake = DataLake(project_root / 'data' / 'lake')
        profile = get_local_redteam_profile(args.profile)
        
        pipeline = LocalRedTeamPipeline(data_lake, settings, project_root, profile)
        logger.info("Running build_safety_assurance_summary with profile %s", args.profile)
        pipeline.build_safety_assurance_summary(save=args.save)
        logger.info("Done.")
    except Exception as e:
        logger.error("Failed: %s", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
