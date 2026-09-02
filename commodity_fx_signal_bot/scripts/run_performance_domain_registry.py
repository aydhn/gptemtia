import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.settings import Settings
from config.paths import ProjectPaths, ensure_project_directories, LAKE_DIR
from data.storage.data_lake import DataLake
from local_performance.performance_config import get_local_performance_profile, get_default_local_performance_profile
from local_performance.performance_pipeline import LocalPerformancePipeline

def main():
    parser = argparse.ArgumentParser(description="Run Performance Domain Registry")
    parser.add_argument("--profile", type=str, default="balanced_local_performance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    ensure_project_directories()
    data_lake = DataLake(LAKE_DIR)
    
    try:
        profile = get_local_performance_profile(args.profile)
    except Exception:
        profile = get_default_local_performance_profile()

    pipeline = LocalPerformancePipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    pipeline.build_performance_domain_registry(save=args.save)
    print("Performance domain registry generated.")

if __name__ == "__main__":
    main()
