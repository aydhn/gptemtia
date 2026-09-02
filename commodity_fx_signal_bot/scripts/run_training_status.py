import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.settings import settings
from config.paths import PROJECT_ROOT
from data.storage.data_lake import DataLake
from local_training.training_pipeline import LocalTrainingPipeline
from local_training.training_config import get_local_training_profile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_training")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()
    profile = get_local_training_profile(args.profile)
    import config.paths as paths
    pipeline = LocalTrainingPipeline(DataLake(paths.LAKE_DIR), settings, PROJECT_ROOT, profile)
    pipeline.build_training_status(save=args.save)
    print("Training status built.")

if __name__ == "__main__":
    main()
