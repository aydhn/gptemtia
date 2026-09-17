"""Phase 137: Run Advanced ML Dataset Profile and Domain Registry Script.

Builds and persists dataset profiles and domain registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_profile_registry import (
    build_advanced_ml_dataset_profile_registry,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_domain_registry import (
    build_advanced_ml_dataset_domain_registry,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()

    df_profiles, s_profiles = build_advanced_ml_dataset_profile_registry(profile)
    data_lake.save_advanced_ml_dataset_profile_registry(df_profiles, s_profiles)

    df_domains, s_domains = build_advanced_ml_dataset_domain_registry(profile)
    data_lake.save_advanced_ml_dataset_domain_registry(df_domains, s_domains)

    print("=" * 70)
    print("PHASE 137: ADVANCED ML DATASET PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
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
