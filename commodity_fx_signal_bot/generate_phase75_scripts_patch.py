import os
from pathlib import Path

base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")
scripts_dir = base_dir / "scripts"

script_base = """\
import argparse
import sys
from pathlib import Path

# Adjust path to import local_synthesis and others
sys.path.append(str(Path(__file__).parent.parent))

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_synthesis.synthesis_config import get_local_synthesis_profile
from local_synthesis.synthesis_pipeline import LocalSynthesisPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_synthesis")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()
    
    settings = Settings()
    paths = ProjectPaths(settings)
    paths.ensure_project_directories()
    data_lake = DataLake(paths, settings)
    
    profile = get_local_synthesis_profile(args.profile)
    pipeline = LocalSynthesisPipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    
"""

scripts_info = {
    "run_synthesis_profile_registry.py": """\
    pipeline.build_synthesis_profile_registry(save=args.save)
    print(f"Synthesis profile registry finished. Profile: {args.profile}")
""",
    "run_master_index_unification.py": """\
    pipeline.build_master_index_unification(save=args.save)
    print(f"Master index unification finished. Profile: {args.profile}")
""",
    "run_cross_phase_final_map.py": """\
    pipeline.build_cross_phase_final_map(save=args.save)
    print(f"Cross phase final map finished. Profile: {args.profile}")
""",
    "run_project_completion_dossier.py": """\
    pipeline.build_project_completion_dossier(save=args.save)
    print(f"Project completion dossier finished. Profile: {args.profile}")
""",
    "run_end_state_documentation.py": """\
    pipeline.build_end_state_documentation(save=args.save)
    print(f"End state documentation finished. Profile: {args.profile}")
""",
    "run_synthesis_quality_report.py": """\
    pipeline.build_synthesis_quality_report(save=args.save)
    print(f"Synthesis quality report finished. Profile: {args.profile}")
""",
    "run_synthesis_status.py": """\
    pipeline.build_synthesis_status(save=args.save)
    print(f"Synthesis status finished. Profile: {args.profile}")
"""
}

for s, body in scripts_info.items():
    with open(scripts_dir / s, "w", encoding="utf-8") as f:
        f.write(script_base + body + "\nif __name__ == '__main__':\n    main()\n")
