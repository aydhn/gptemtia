import os
from pathlib import Path

def create_scripts():
    base_dir = Path("scripts")
    base_dir.mkdir(exist_ok=True)
    
    scripts = {
        "run_redteam_domain_registry.py": "build_redteam_domain_registry",
        "run_final_local_redteam_rehearsal.py": "build_final_local_redteam_rehearsal",
        "run_misuse_scenario_library.py": "build_misuse_scenario_library",
        "run_adversarial_prompt_safety_checklist.py": "build_adversarial_prompt_safety_checklist",
        "run_safety_assurance_summary.py": "build_safety_assurance_summary",
        "run_redteam_quality_report.py": "build_redteam_quality_report",
        "run_redteam_status.py": "build_redteam_status"
    }

    template = """import argparse
import sys
import logging
from pathlib import Path

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_redteam.redteam_config import get_local_redteam_profile
from local_redteam.redteam_pipeline import LocalRedTeamPipeline

def main():
    parser = argparse.ArgumentParser(description="Run {func_name}")
    parser.add_argument("--profile", type=str, default="balanced_local_redteam")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        settings = Settings()
        data_lake = DataLake()
        project_root = Path(__file__).parent.parent.resolve()
        profile = get_local_redteam_profile(args.profile)
        
        pipeline = LocalRedTeamPipeline(data_lake, settings, project_root, profile)
        logger.info("Running {func_name} with profile %s", args.profile)
        pipeline.{func_name}(save=args.save)
        logger.info("Done.")
    except Exception as e:
        logger.error("Failed: %s", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
"""

    for filename, func_name in scripts.items():
        (base_dir / filename).write_text(template.replace("{func_name}", func_name), encoding="utf-8")

    print("Created run_ scripts")

if __name__ == "__main__":
    create_scripts()
