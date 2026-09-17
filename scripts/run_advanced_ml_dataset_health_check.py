"""Phase 137: Run Advanced ML Dataset Health Check Script.

Verifies repository component health and module integrity.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_health import (
    build_advanced_ml_dataset_health_check,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()
    project_root = Path(__file__).resolve().parent.parent

    df_health, s_health = build_advanced_ml_dataset_health_check(project_root, profile)
    data_lake.save_advanced_ml_dataset_health_check(df_health, s_health)

    print("=" * 70)
    print("PHASE 137: ADVANCED ML DATASET HEALTH CHECK")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Health Checks   : {s_health['total_checks']}")
    print(f"Passed Checks         : {s_health['passed_checks']}")
    print(f"Failed Checks         : {s_health['failed_checks']}")
    print(f"Overall Health        : {s_health['overall_health']}")
    print(f"Non-Signal            : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
