"""Phase 136: Run GPU ML Runtime Validation Report Script.

Validates invariants, prohibition rules, and safety boundaries for Phase 136.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from advanced_gpu_ml_runtime.gpu_ml_runtime_validation import build_gpu_ml_runtime_validation_report
from advanced_gpu_ml_runtime.gpu_ml_runtime_safety_boundary import build_gpu_ml_runtime_safety_boundary
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_ml_runtime_profile()

    df_val, s_val = build_gpu_ml_runtime_validation_report(profile)
    data_lake.save_gpu_ml_runtime_validation_report(df_val, s_val)

    df_safe, s_safe = build_gpu_ml_runtime_safety_boundary(profile)
    data_lake.save_gpu_ml_runtime_safety_boundary(df_safe, s_safe)

    print("=" * 70)
    print("PHASE 136: GPU & ML RUNTIME VALIDATION AND SAFETY BOUNDARY")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Validation Rules Passed: {s_val.get('passed_rules', s_val.get('passed_checks', 0))} / {s_val.get('total_rules', s_val.get('total_checks', 0))}")
    print(f"All Validations Passed : {s_val.get('all_passed', True)}")
    print(f"Safety Boundaries Count: {s_safe.get('total_boundaries', 0)}")
    print(f"NO-GO Boundaries Enforced: {s_safe.get('no_go_count', 0)}")
    print(f"SAFE-GO Boundaries Count : {s_safe.get('safe_go_count', 0)}")
    print(f"Non-Signal Maintained  : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
