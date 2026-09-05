import os
from pathlib import Path

base_dir = Path("commodity_fx_signal_bot/scripts")

common_script = '''"""{name} script."""
import argparse
import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_project_atlas.atlas_config import get_local_project_atlas_profile
from local_project_atlas.atlas_pipeline import LocalProjectAtlasPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_project_atlas")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    settings = Settings()
    if not settings.local_project_atlas_enabled:
        print("Local Project Atlas disabled.")
        return

    profile = get_local_project_atlas_profile(args.profile)
    data_lake = DataLake(settings)
    pipeline = LocalProjectAtlasPipeline(data_lake, settings, project_root, profile)

    {call}
    
    print("Done")

if __name__ == "__main__":
    main()
'''

scripts = {
    "run_atlas_domain_registry": "pipeline.build_atlas_domain_registry(save=args.save)",
    "run_final_meta_index": "pipeline.build_final_meta_index(save=args.save)",
    "run_universal_navigation_map": "pipeline.build_universal_navigation_map(save=args.save)",
    "run_cross_phase_lookup_engine": "pipeline.build_cross_phase_lookup_engine(save=args.save)",
    "run_offline_semantic_toc": "pipeline.build_offline_semantic_toc(save=args.save)",
    "run_terminal_project_atlas": "pipeline.build_terminal_project_atlas(save=args.save)",
    "run_atlas_quality_report": "pipeline.build_atlas_quality_report(save=args.save)",
    "run_atlas_status": "pipeline.build_atlas_status(save=args.save)"
}

for name, call in scripts.items():
    content = common_script.format(name=name, call=call)
    with open(base_dir / f"{name}.py", "w", encoding="utf-8") as f:
        f.write(content)

print("Created scripts")
