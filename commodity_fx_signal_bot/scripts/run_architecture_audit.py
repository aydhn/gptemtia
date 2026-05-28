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
    parser = argparse.ArgumentParser(description="Run Architecture Audit")
    parser.add_argument("--profile", type=str, default="balanced_final_review")
    args = parser.parse_args()

    profile = get_final_review_profile(args.profile)
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(project_root)

    pipeline = FinalReviewPipeline(data_lake, settings, project_root, profile)

    print(f"Running Architecture Audit...")
    df, summary = pipeline.build_architecture_audit(save=True)

    print("\n--- Architecture Audit Summary ---")
    print(f"Passed: {summary.get('overall_passed')}")
    print(f"Total Warnings: {summary.get('total_warnings')}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
