import argparse
import sys
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore
from local_review_governance.review_config import get_local_review_governance_profile, LocalReviewGovernanceProfile
from local_review_governance.review_pipeline import LocalReviewGovernancePipeline

def get_profile(name: str | None = None) -> LocalReviewGovernanceProfile:
    from local_review_governance.review_config import get_default_local_review_governance_profile
    if not name:
        return get_default_local_review_governance_profile()
    return get_local_review_governance_profile(name)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_review_governance")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    data_lake = DataLake('data/lake')
    project_root = Path(__file__).parent.parent
    profile = get_profile(args.profile)

    pipeline = LocalReviewGovernancePipeline(data_lake, settings, project_root, profile)
    return pipeline, args

if __name__ == "__main__":
    pipeline, args = main()
    pipeline.build_manual_approval_ledger(save=args.save)
    print('Manual approval ledger generated.')
