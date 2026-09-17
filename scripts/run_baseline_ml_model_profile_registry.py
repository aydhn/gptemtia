"""Phase 138: Run Baseline ML Model Profile and Domain Registry Script.

Builds and persists baseline model profiles and domain registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_profile_registry import (
    build_baseline_ml_model_profile_registry,
)
from advanced_baseline_ml_models.baseline_ml_model_domain_registry import (
    build_baseline_ml_model_domain_registry,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_baseline_ml_model_profile()

    df_profiles, s_profiles = build_baseline_ml_model_profile_registry(profile)
    data_lake.save_baseline_ml_model_profile_registry(df_profiles, s_profiles)

    df_domains, s_domains = build_baseline_ml_model_domain_registry(profile)
    data_lake.save_baseline_ml_model_domain_registry(df_domains, s_domains)

    print("=" * 70)
    print("PHASE 138: BASELINE ML MODEL PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Active Profile  : {profile.name}")
    print(f"Total Profiles  : {s_profiles['total_profiles']}")
    print(f"Total Domains   : {s_domains['total_domains']}")
    print(f"Current Phase   : {profile.current_phase}")
    print(f"Next Phase      : {profile.next_phase}")
    print(f"Non-Signal      : {s_profiles['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
