import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_validation.feature_validation_health import check_feature_validation_health
from advanced_feature_validation.feature_validation_safety_boundary import validate_feature_validation_safety_boundary


def main():
    settings = get_settings()
    data_lake = DataLake()

    health = check_feature_validation_health()
    safety = validate_feature_validation_safety_boundary()

    data_lake.save_feature_validation_health_check(health)
    data_lake.save_feature_validation_safety_boundary(safety)

    print("=" * 70)
    print("PHASE 121: HEALTH CHECK & SAFETY BOUNDARIES")
    print("=" * 70)
    print(f"Health Status      : {health['status']}")
    print(f"Subsystems Checked : {health.get('subsystems_checked', 0)}")
    print(f"Safety Status      : {safety['status']}")
    print(f"NO-GO Invariants   : {safety['no_go_count']} ENFORCED")
    print(f"SAFE-GO Principles : {safety['safe_go_count']} ACTIVE")
    print(f"Non-Signal Mandate : {safety['non_signal_mandate']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
