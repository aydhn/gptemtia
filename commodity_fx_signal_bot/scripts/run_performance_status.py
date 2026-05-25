import argparse
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.settings import settings
from data.storage.data_lake import DataLake
from performance.performance_config import get_performance_profile
from performance.performance_pipeline import PerformancePipeline

def main():
    parser = argparse.ArgumentParser(description="Run Performance Status Report")
    parser.add_argument("--profile", type=str, default="balanced_local_performance", help="Performance profile name")
    parser.add_argument("--save", action="store_true", default=True, help="Save outputs")

    args = parser.parse_args()

    print(f"Loading performance profile: {args.profile}")
    try:
        profile = get_performance_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile: {e}")
        sys.exit(1)

    project_root = Path(__file__).parent.parent
    data_lake = DataLake(project_root / "data" / "lake")

    print("Initializing Performance Pipeline...")
    pipeline = PerformancePipeline(data_lake, settings, project_root, profile)

    print("Checking Performance Reports Status...")
    df, summary = pipeline.build_performance_status(save=args.save)

    print("\n--- Performance Status Summary ---")
    for k, v in summary.items():
        print(f"{k}: {v}")

    print("\nPerformance Status check complete.")

if __name__ == "__main__":
    main()
