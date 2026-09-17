# -*- coding: utf-8 -*-
"""Phase 141: Run Calibration & Uncertainty Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.confidence_score_placeholders import (
    build_confidence_score_placeholder_registry,
    summarize_confidence_score_placeholders,
)
from advanced_calibration_uncertainty.confidence_interval_placeholders import (
    build_confidence_interval_placeholder_registry,
    summarize_confidence_interval_placeholders,
)
from advanced_calibration_uncertainty.prediction_interval_placeholders import (
    build_prediction_interval_placeholder_registry,
    summarize_prediction_interval_placeholders,
)
from advanced_calibration_uncertainty.quantile_placeholders import (
    build_quantile_placeholder_registry,
    summarize_quantile_placeholders,
)
from advanced_calibration_uncertainty.conformal_prediction_placeholders import (
    build_conformal_prediction_placeholder_registry,
    summarize_conformal_prediction_placeholders,
)
from advanced_calibration_uncertainty.calibration_metric_placeholders import (
    build_calibration_metric_placeholder_registry,
    summarize_calibration_metric_placeholders,
)
from advanced_calibration_uncertainty.uncertainty_metric_placeholders import (
    build_uncertainty_metric_placeholder_registry,
    summarize_uncertainty_metric_placeholders,
)
from advanced_calibration_uncertainty.calibration_evaluation_placeholders import (
    build_calibration_evaluation_placeholder_registry,
    summarize_calibration_evaluation_placeholders,
)
from advanced_calibration_uncertainty.uncertainty_evaluation_placeholders import (
    build_uncertainty_evaluation_placeholder_registry,
    summarize_uncertainty_evaluation_placeholders,
)
from advanced_calibration_uncertainty.calibration_uncertainty_audit_placeholders import (
    build_calibration_uncertainty_audit_placeholder_registry,
    summarize_calibration_uncertainty_audit_placeholders,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_cs, s_cs = build_confidence_score_placeholder_registry()
    data_lake.save_confidence_score_placeholder_registry(df_cs, s_cs)

    df_ci, s_ci = build_confidence_interval_placeholder_registry()
    data_lake.save_confidence_interval_placeholder_registry(df_ci, s_ci)

    df_pi, s_pi = build_prediction_interval_placeholder_registry()
    data_lake.save_prediction_interval_placeholder_registry(df_pi, s_pi)

    df_q, s_q = build_quantile_placeholder_registry()
    data_lake.save_quantile_placeholder_registry(df_q, s_q)

    df_cp, s_cp = build_conformal_prediction_placeholder_registry()
    data_lake.save_conformal_prediction_placeholder_registry(df_cp, s_cp)

    df_cm, s_cm = build_calibration_metric_placeholder_registry()
    data_lake.save_calibration_metric_placeholder_registry(df_cm, s_cm)

    df_um, s_um = build_uncertainty_metric_placeholder_registry()
    data_lake.save_uncertainty_metric_placeholder_registry(df_um, s_um)

    df_ce, s_ce = build_calibration_evaluation_placeholder_registry()
    data_lake.save_calibration_evaluation_placeholder_registry(df_ce, s_ce)

    df_ue, s_ue = build_uncertainty_evaluation_placeholder_registry()
    data_lake.save_uncertainty_evaluation_placeholder_registry(df_ue, s_ue)

    df_aud, s_aud = build_calibration_uncertainty_audit_placeholder_registry()
    data_lake.save_calibration_uncertainty_audit_placeholder_registry(df_aud, s_aud)

    print("=" * 70)
    print("PHASE 141: CALIBRATION & UNCERTAINTY PLACEHOLDERS")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Confidence Score Placeholders     : {s_cs.get('total_placeholders', 0)}")
    print(f"Confidence Interval Placeholders  : {s_ci.get('total_placeholders', 0)}")
    print(f"Prediction Interval Placeholders  : {s_pi.get('total_placeholders', 0)}")
    print(f"Quantile Placeholders             : {s_q.get('total_placeholders', 0)}")
    print(f"Conformal Pred Placeholders       : {s_cp.get('total_placeholders', 0)}")
    print(f"Calibration Metric Placeholders   : {s_cm.get('total_metrics', 0)}")
    print(f"Uncertainty Metric Placeholders   : {s_um.get('total_metrics', 0)}")
    print(f"Calibration Eval Placeholders     : {s_ce.get('total_evaluations', 0)}")
    print(f"Uncertainty Eval Placeholders     : {s_ue.get('total_evaluations', 0)}")
    print(f"Audit Placeholders                : {s_aud.get('total_audits', 0)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
