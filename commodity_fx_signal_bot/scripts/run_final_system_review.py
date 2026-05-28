#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from data.storage.data_lake import DataLake
from final_review.final_review_config import get_final_review_profile
from final_review.final_review_pipeline import FinalReviewPipeline

def main():
    parser = argparse.ArgumentParser(description="Run Final System Review")
    parser.add_argument("--profile", type=str, default="balanced_final_review", help="Final review profile name")
    parser.add_argument("--save", action="store_true", default=True, help="Save outputs")
    parser.add_argument("--no-save", action="store_false", dest="save", help="Do not save outputs")

    args = parser.parse_args()

    try:
        profile = get_final_review_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return 1

    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(project_root)

    pipeline = FinalReviewPipeline(data_lake, settings, project_root, profile)

    print(f"Running Final System Review using profile: {args.profile}...")
    tables, summary = pipeline.build_final_system_review(save=args.save)

    print("\n--- Final System Review Summary ---")
    print(f"Passed: {summary.get('passed')}")
    print(f"Readiness: {summary.get('snapshot', {}).get('readiness_label')}")
    print(f"Acceptance Score: {summary.get('snapshot', {}).get('acceptance_score')}")
    print(f"Safety Score: {summary.get('snapshot', {}).get('safety_score')}")

    if args.save:
        print("\nOutputs saved to data/lake/final_review and reports/output/final_review")

    return 0

if __name__ == "__main__":
    sys.exit(main())
