"""Run deprecation rehearsal"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from local_longterm_operations.longterm_config import get_local_longterm_operations_profile
from local_longterm_operations.lifecycle_pipeline import LocalLongTermOperationsPipeline
from config.settings import Settings
from config.paths import ensure_project_directories, PROJECT_ROOT, LAKE_DIR
from data.storage.data_lake import DataLake

def main():
    parser = argparse.ArgumentParser(description="Run deprecation rehearsal")
    parser.add_argument("--profile", type=str, default="balanced_local_longterm_operations")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()
    
    ensure_project_directories()
    settings = Settings()
    data_lake = DataLake(LAKE_DIR)
    profile = get_local_longterm_operations_profile(args.profile)
    
    pipeline = LocalLongTermOperationsPipeline(data_lake, settings, PROJECT_ROOT, profile)
    
    print(f"Running Run deprecation rehearsal with profile {args.profile}...")
    pipeline.build_deprecation_rehearsal(save=args.save)
    print("Done.")

if __name__ == "__main__":
    main()
