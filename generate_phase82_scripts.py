import os
from pathlib import Path

def main():
    base_dir = Path("commodity_fx_signal_bot")
    scripts_dir = base_dir / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    
    script_template = """import argparse
import sys
from pathlib import Path
from core.container import Container
from local_simplification.simplification_config import get_local_simplification_profile
from local_simplification.simplification_pipeline import LocalSimplificationPipeline

def parse_args():
    parser = argparse.ArgumentParser(description="{desc}")
    parser.add_argument("--profile", type=str, default="{default_profile}")
    parser.add_argument("--save", action="store_true", default=True)
    parser.add_argument("--no-save", dest="save", action="store_false")
    return parser.parse_args()

def main():
    args = parse_args()
    container = Container()
    container.start()
    
    try:
        profile = get_local_simplification_profile(args.profile)
        pipeline = LocalSimplificationPipeline(
            data_lake=container.data_lake,
            settings=container.settings,
            project_root=Path(".").resolve(),
            profile=profile
        )
        {pipeline_call}
        print(f"Successfully finished {desc}")
    except Exception as e:
        print(f"Error: {{e}}")
        sys.exit(1)
    finally:
        container.stop()

if __name__ == "__main__":
    main()
"""

    scripts = [
        ("run_simplification_domain_registry", "Simplification domain registry", "balanced_local_simplification", "pipeline.build_simplification_domain_registry(save=args.save)"),
        ("run_final_modular_complexity_map", "Final modular complexity map", "complexity_map_focus", "pipeline.build_final_modular_complexity_map(save=args.save)"),
        ("run_optional_slimming_plan", "Optional slimming plan", "slimming_plan_focus", "pipeline.build_optional_slimming_plan(save=args.save)"),
        ("run_repo_ergonomics_rehearsal", "Repo ergonomics rehearsal", "balanced_local_simplification", "pipeline.build_repo_ergonomics_rehearsal(save=args.save)"),
        ("run_maintainability_seed", "Maintainability seed", "balanced_local_simplification", "pipeline.build_maintainability_seed(save=args.save)"),
        ("run_simplification_quality_report", "Simplification quality report", "balanced_local_simplification", "pipeline.build_simplification_quality_report(save=args.save)"),
        ("run_simplification_status", "Simplification status", "balanced_local_simplification", "pipeline.build_simplification_status(save=args.save)")
    ]

    for script_name, desc, default_profile, pipeline_call in scripts:
        content = script_template.format(
            desc=desc,
            default_profile=default_profile,
            pipeline_call=pipeline_call
        )
        (scripts_dir / f"{script_name}.py").write_text(content, encoding="utf-8")

    print("Created phase 82 scripts")

if __name__ == "__main__":
    main()
