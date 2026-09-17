# -*- coding: utf-8 -*-
"""Phase 142: Run Drift Metric Placeholders Script."""

import sys
from dataclasses import asdict
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.drift_metric_placeholders import (
    build_all_drift_metric_placeholders,
    summarize_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.psi_metric_placeholders import build_psi_metric_placeholders
from advanced_model_drift_monitoring.ks_metric_placeholders import build_ks_metric_placeholders
from advanced_model_drift_monitoring.js_divergence_metric_placeholders import build_js_divergence_metric_placeholders
from advanced_model_drift_monitoring.wasserstein_metric_placeholders import build_wasserstein_metric_placeholders
from advanced_model_drift_monitoring.correlation_drift_metric_placeholders import build_correlation_drift_metric_placeholders
from advanced_model_drift_monitoring.missingness_drift_metric_placeholders import build_missingness_drift_metric_placeholders
from advanced_model_drift_monitoring.categorical_drift_metric_placeholders import build_categorical_drift_metric_placeholders
from advanced_model_drift_monitoring.numerical_drift_metric_placeholders import build_numerical_drift_metric_placeholders
from advanced_model_drift_monitoring.calibration_drift_metric_placeholders import build_calibration_drift_metric_placeholders
from advanced_model_drift_monitoring.uncertainty_drift_metric_placeholders import build_uncertainty_drift_metric_placeholders
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    all_metrics = build_all_drift_metric_placeholders()
    summary = summarize_drift_metric_placeholders(all_metrics)

    df_all = pd.DataFrame([asdict(m) for m in all_metrics])
    data_lake.save_drift_metric_placeholder_registry(df_all, summary)

    # Save individual registries
    data_lake.save_psi_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_psi_metric_placeholders()]))
    data_lake.save_ks_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_ks_metric_placeholders()]))
    data_lake.save_js_divergence_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_js_divergence_metric_placeholders()]))
    data_lake.save_wasserstein_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_wasserstein_metric_placeholders()]))
    data_lake.save_correlation_drift_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_correlation_drift_metric_placeholders()]))
    data_lake.save_missingness_drift_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_missingness_drift_metric_placeholders()]))
    data_lake.save_categorical_drift_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_categorical_drift_metric_placeholders()]))
    data_lake.save_numerical_drift_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_numerical_drift_metric_placeholders()]))
    data_lake.save_calibration_drift_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_calibration_drift_metric_placeholders()]))
    data_lake.save_uncertainty_drift_metric_placeholder_registry(pd.DataFrame([asdict(m) for m in build_uncertainty_drift_metric_placeholders()]))

    print("=" * 70)
    print("PHASE 142: DRIFT METRIC PLACEHOLDERS (10 CATEGORIES)")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Metric Placeholders : {summary.get('total_metrics', 0)}")
    print(f"Calculations Disabled     : {summary.get('all_calculation_disabled', True)}")
    print(f"Metric Scopes Monitored   : {list(summary.get('by_scope', {}).keys())}")
    print(f"Metric Types Covered      : {len(summary.get('by_type', {}))}")
    print("=" * 70)


if __name__ == "__main__":
    main()
