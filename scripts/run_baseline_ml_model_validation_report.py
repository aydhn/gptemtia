"""Phase 138: Run Baseline ML Model Validation Report Script.

Validates all Phase 138 invariants, safety rules, non-signal guarantees, and contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_validation import (
    run_baseline_ml_model_validation,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_baseline_ml_model_profile()

    df_val, s_val = run_baseline_ml_model_validation(profile)
    data_lake.save_baseline_ml_model_validation_report(df_val, s_val)

    print("=" * 70)
    print("PHASE 138: BASELINE ML MODEL VALIDATION REPORT")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Status : {s_val['validation_status']}")
    print(f"Total Checks      : {s_val.get('total_validations', 0)}")
    print(f"Passed Checks     : {s_val.get('passed_validations', 0)}")
    print(f"Failed Checks     : {s_val.get('total_validations', 0) - s_val.get('passed_validations', 0)}")
    print(f"All Passed        : {s_val['all_passed']}")

    print(f"Non-Signal        : {s_val['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
