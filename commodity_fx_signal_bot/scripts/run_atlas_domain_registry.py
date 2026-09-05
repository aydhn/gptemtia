"""run_atlas_domain_registry script."""
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
    data_lake = DataLake(str(project_root))
    pipeline = LocalProjectAtlasPipeline(data_lake, settings, project_root, profile)

    pipeline.build_atlas_domain_registry(save=args.save)
    
    print("Done")

if __name__ == "__main__":
    main()
