# -*- coding: utf-8 -*-
"""Phase 142: Run Drift Disabled Execution Reports Script."""

import sys
from dataclasses import asdict
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.drift_execution_disabled import (
    build_all_drift_disabled_execution_items,
    summarize_drift_disabled_executions,
)
from advanced_model_drift_monitoring.drift_metric_calculation_disabled import build_drift_metric_calculation_disabled_item
from advanced_model_drift_monitoring.drift_alerting_disabled import build_drift_alerting_disabled_item
from advanced_model_drift_monitoring.drift_retraining_trigger_disabled import build_drift_retraining_trigger_disabled_item
from advanced_model_drift_monitoring.drift_model_action_disabled import build_drift_model_action_disabled_item
from advanced_model_drift_monitoring.drift_prediction_disabled import build_drift_prediction_disabled_item
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    items = build_all_drift_disabled_execution_items()
    summary = summarize_drift_disabled_executions(items)

    df_all = pd.DataFrame([asdict(item) for item in items])
    data_lake.save_drift_execution_disabled_report(df_all, summary)

    data_lake.save_drift_metric_calculation_disabled_report(pd.DataFrame([asdict(build_drift_metric_calculation_disabled_item())]))
    data_lake.save_drift_alerting_disabled_report(pd.DataFrame([asdict(build_drift_alerting_disabled_item())]))
    data_lake.save_drift_retraining_trigger_disabled_report(pd.DataFrame([asdict(build_drift_retraining_trigger_disabled_item())]))
    data_lake.save_drift_model_action_disabled_report(pd.DataFrame([asdict(build_drift_model_action_disabled_item())]))
    data_lake.save_drift_prediction_disabled_report(pd.DataFrame([asdict(build_drift_prediction_disabled_item())]))

    print("=" * 70)
    print("PHASE 142: DRIFT DISABLED EXECUTION SAFEGUARDS REPORT")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Safeguards Monitored : {summary.get('total_enforcements', 0)}")
    print(f"All Disabled Verified      : {summary.get('all_disabled_verified', True)}")
    print(f"Governance Status          : {summary.get('governance_status', 'FULLY_PROTECTED')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
