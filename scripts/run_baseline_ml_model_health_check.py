"""Phase 138: Run Baseline ML Model Health Check Script.

Runs system health checks across all Phase 138 baseline ML model components.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_health import (
    run_baseline_ml_model_health_check,
)
from reports.report_builder import ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_baseline_ml_model_profile()

    df_health, s_health = run_baseline_ml_model_health_check(profile)
    data_lake.save_baseline_ml_model_health_check(df_health, s_health)

    print("=" * 70)
    print("PHASE 138: BASELINE ML MODEL HEALTH CHECK")
    print("=" * 70)
    print(ADVANCED_BASELINE_ML_MODELS_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Overall Status   : {s_health.get('health_status', 'SYSTEM_HEALTHY')}")
    print(f"Total Components : {s_health.get('total_checks', len(df_health))}")
    print(f"Healthy Count    : {s_health.get('healthy_count', 0)}")
    print(f"Unhealthy Count  : {s_health.get('unhealthy_count', 0)}")
    print(f"All Healthy      : {s_health.get('all_healthy', True)}")
    print(f"Non-Signal       : {s_health.get('non_signal', True)}")
    print("=" * 70)



if __name__ == "__main__":
    main()
