# -*- coding: utf-8 -*-
"""Phase 142: Run Model Drift Monitoring Health Check Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.model_drift_health import run_model_drift_health_check
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    health = run_model_drift_health_check()
    df_health = pd.DataFrame(health["checks"])
    data_lake.save_model_drift_health_check(df_health, health)

    print("=" * 70)
    print("PHASE 142: MODEL DRIFT MONITORING HEALTH CHECK")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Overall Health Status : {health.get('overall_health', 'UNKNOWN')}")
    print(f"Total Checks          : {health.get('total_checks', 0)}")
    print(f"All Checks Passed     : {health.get('all_passed', False)}")
    print("-" * 70)
    for c in health.get("checks", []):
        print(f"[{c.get('status').upper()}] {c.get('check')}: {c.get('details')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
