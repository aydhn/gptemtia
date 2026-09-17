# -*- coding: utf-8 -*-
"""Phase 140: Run Ensemble Model Health Check Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.ensemble_model_health import (
    check_ensemble_model_health,
    summarize_ensemble_model_health_report,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    health = check_ensemble_model_health()
    s_health = summarize_ensemble_model_health_report(health)
    df_health = pd.DataFrame([{"check_name": k, "passed": v} for k, v in health.get("checks", {}).items()])
    data_lake.save_ensemble_model_health_check(df_health, s_health)

    print("=" * 70)
    print("PHASE 140: ENSEMBLE MODEL HEALTH CHECK")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Health Status       : {s_health['status']}")
    print(f"Passed Checks       : {s_health['passed_checks']} / {s_health['total_checks']}")
    print(f"All Passed          : {s_health['all_passed']}")
    print(f"Non-Signal Verified : {s_health['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
