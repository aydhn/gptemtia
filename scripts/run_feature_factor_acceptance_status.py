"""Phase 125: Run Feature Factor Acceptance Status Script.

Executes the end-to-end acceptance pipeline and displays comprehensive block status.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_pipeline import (
    FeatureFactorAcceptancePipeline,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_factor_acceptance_profile()
    pipeline = FeatureFactorAcceptancePipeline(data_lake=data_lake, profile=profile)

    res = pipeline.run_full_acceptance_pipeline(save=True)

    print("=" * 70)
    print("PHASE 125: MASTER FEATURE FACTOR ACCEPTANCE STATUS")
    print("=" * 70)
    print(f"Active Profile    : {res['profile']}")
    print(f"Overall Status    : {res['overall_status']}")
    print(f"Acceptance Score  : {res['acceptance_score']}")
    print(f"Total Modules     : {res['total_modules']}")
    print(f"Total Gates       : {res['total_gates']}")
    print(f"Health Status     : {res['health_status']}")
    print(f"Validation Status : {res['validation_status']}")
    print(f"Handoff Status    : {res['handoff_status']}")
    print(f"Non-Signal        : {res['non_signal']}")
    print(f"Official Approval : {res['official_approval']}")
    print(f"Production Ready  : {res['production_ready']}")
    print(f"Broker Ready      : {res['broker_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
