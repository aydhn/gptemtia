#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from data.storage.data_lake import DataLake
from final_review.final_review_config import get_final_review_profile
from final_review.final_review_pipeline import FinalReviewPipeline

def main():
    parser = argparse.ArgumentParser(description="Run Release Readiness Dry Run")
    parser.add_argument("--profile", type=str, default="balanced_final_review")
    args = parser.parse_args()

    profile = get_final_review_profile(args.profile)
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(project_root)

    pipeline = FinalReviewPipeline(data_lake, settings, project_root, profile)

    print(f"Running Release Readiness Dry Run...")
    df, summary = pipeline.build_release_readiness_dry_run(save=True)

    print("\n--- Release Readiness Dry Run Summary ---")
    print(f"Ready: {summary.get('is_ready')}")
    print(f"Passed steps: {summary.get('passed_steps')}/{summary.get('total_steps')}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
