import argparse
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_consistency.consistency_config import get_local_consistency_profile
from local_consistency.consistency_pipeline import LocalConsistencyPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_consistency")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    settings = Settings()
    paths = ProjectPaths()
    data_lake = DataLake(paths.lake_dir)
    profile = get_local_consistency_profile(args.profile)

    pipeline = LocalConsistencyPipeline(data_lake, settings, paths.project_root, profile)
    pipeline.build_system_coherence_report(save=args.save)
    print("System coherence report generated.")

if __name__ == "__main__":
    main()
