import os
from pathlib import Path

def main():
    base_dir = Path("commodity_fx_signal_bot")
    scripts_dir = base_dir / "scripts"
    
    script_template = """import argparse
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
    parser = argparse.ArgumentParser(description="{desc}")
    parser.add_argument("--profile", type=str, default="{default_profile}", help="Local Simplification Profile name")
    parser.add_argument("--no-save", action="store_true", help="Do not save the results")
    args = parser.parse_args()

    try:
        settings = Settings()
        data_lake = DataLake(settings)
        profile = get_local_simplification_profile(args.profile)

        logger.info(f"Initializing LocalSimplificationPipeline with profile: {{profile.name}}")
        pipeline = LocalSimplificationPipeline(data_lake, settings, PROJECT_ROOT, profile)

        logger.info("Running {desc}...")
        {pipeline_call}

        logger.info(f"Successfully finished {desc}")

    except Exception as e:
        logger.error(f"Error running {desc}: {{e}}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
"""

    scripts = [
        ("run_simplification_domain_registry", "Simplification domain registry", "balanced_local_simplification", "pipeline.build_simplification_domain_registry(save=not args.no_save)"),
        ("run_final_modular_complexity_map", "Final modular complexity map", "complexity_map_focus", "pipeline.build_final_modular_complexity_map(save=not args.no_save)"),
        ("run_optional_slimming_plan", "Optional slimming plan", "slimming_plan_focus", "pipeline.build_optional_slimming_plan(save=not args.no_save)"),
        ("run_repo_ergonomics_rehearsal", "Repo ergonomics rehearsal", "balanced_local_simplification", "pipeline.build_repo_ergonomics_rehearsal(save=not args.no_save)"),
        ("run_maintainability_seed", "Maintainability seed", "balanced_local_simplification", "pipeline.build_maintainability_seed(save=not args.no_save)"),
        ("run_simplification_quality_report", "Simplification quality report", "balanced_local_simplification", "pipeline.build_simplification_quality_report(save=not args.no_save)"),
        ("run_simplification_status", "Simplification status", "balanced_local_simplification", "pipeline.build_simplification_status(save=not args.no_save)")
    ]

    for script_name, desc, default_profile, pipeline_call in scripts:
        content = script_template.format(
            desc=desc,
            default_profile=default_profile,
            pipeline_call=pipeline_call
        )
        (scripts_dir / f"{script_name}.py").write_text(content, encoding="utf-8")

    print("Created phase 82 scripts again")

if __name__ == "__main__":
    main()
