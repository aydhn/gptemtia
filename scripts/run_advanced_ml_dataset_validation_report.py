"""Phase 137: Run Advanced ML Dataset Validation and Safety Report Script.

Builds and persists validation and safety boundary reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_safety_boundary import (
    build_advanced_ml_dataset_safety_boundary,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_validation import (
    build_advanced_ml_dataset_validation_report,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()

    df_safety, s_safety = build_advanced_ml_dataset_safety_boundary(profile)
    data_lake.save_advanced_ml_dataset_safety_boundary(df_safety, s_safety)

    tables = {
        "profiles": data_lake.load_advanced_ml_dataset_profile_registry(),
        "contracts": data_lake.load_ml_dataset_contract_registry(),
        "schemas": data_lake.load_ml_dataset_schema_registry(),
        "experiments": data_lake.load_ml_experiment_registry(),
        "manifest": data_lake.load_advanced_ml_dataset_manifest(),
    }
    df_val, s_val = build_advanced_ml_dataset_validation_report(tables, profile)
    data_lake.save_advanced_ml_dataset_validation_report(df_val, s_val)

    print("=" * 70)
    print("PHASE 137: ADVANCED ML DATASET VALIDATION & SAFETY")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Status     : {s_val['validation_status']}")
    print(f"Passed Checks         : {s_val['passed_checks']}/{s_val['total_checks']}")
    print(f"Safety Status         : {s_safety['safety_status']}")
    print(f"NO-GO Conditions      : {s_safety['no_go_count']}")
    print(f"SAFE-GO Conditions    : {s_safety['safe_go_count']}")
    print(f"Non-Signal            : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
