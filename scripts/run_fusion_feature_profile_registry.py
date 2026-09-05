import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_fusion.fusion_feature_profile_registry import (
    get_fusion_feature_profiles_registry,
    get_fusion_feature_profiles_summary,
)


def main():
    settings = get_settings()
    data_lake = DataLake()

    profiles = get_fusion_feature_profiles_registry()
    summary = get_fusion_feature_profiles_summary()

    data_lake.save_fusion_feature_profile_registry(summary)

    print("=" * 70)
    print("PHASE 120: FUSION FEATURE PROFILE REGISTRY")
    print("=" * 70)
    print(f"Total Profiles  : {summary['total_profiles']}")
    print(f"Default Profile : {summary['default_profile']}")
    print(f"Current Phase   : {summary['current_phase']}")
    print(f"Target Phase    : {summary['target_final_phase']}")
    print(f"Next Phase      : {summary['next_phase']}")
    print(f"Dry Run Only    : {summary['dry_run_mandate']}")
    print(f"Non-Signal Mandate: {summary['non_signal_mandate']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
