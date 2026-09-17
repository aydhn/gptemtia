# -*- coding: utf-8 -*-
"""Phase 141: Calibration Metric Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CALIBRATION_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "expected_calibration_error_placeholder",
        "metric_family": "binned_difference",
        "formula_description": "Weighted average of difference between confidence and accuracy per bin; uncalculated.",
    },
    {
        "metric_name": "maximum_calibration_error_placeholder",
        "metric_family": "worst_case_bin_difference",
        "formula_description": "Maximum absolute deviation across all probability bins; uncalculated.",
    },
    {
        "metric_name": "brier_score_placeholder",
        "metric_family": "mean_squared_probability_error",
        "formula_description": "Mean squared error between predicted probabilities and binary outcomes; uncalculated.",
    },
    {
        "metric_name": "reliability_curve_placeholder",
        "metric_family": "visual_calibration_diagram",
        "formula_description": "Reliability diagram coordinates (mean predicted prob vs fraction of positives); unplotted.",
    },
    {
        "metric_name": "log_loss_placeholder",
        "metric_family": "negative_log_likelihood",
        "formula_description": "Cross-entropy loss of predicted class probabilities; uncalculated.",
    },
    {
        "metric_name": "calibration_slope_placeholder",
        "metric_family": "logistic_calibration_curve",
        "formula_description": "Slope of logistic calibration curve (ideal = 1.0); uncalculated.",
    },
    {
        "metric_name": "calibration_intercept_placeholder",
        "metric_family": "logistic_calibration_curve",
        "formula_description": "Intercept of logistic calibration curve (ideal = 0.0); uncalculated.",
    },
]


def build_calibration_metric_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration metric placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CALIBRATION_METRIC_PLACEHOLDERS:
        rows.append(
            {
                "metric_name": item["metric_name"],
                "metric_family": item["metric_family"],
                "formula_description": item["formula_description"],
                "calculated": False,
                "metric_value": None,
                "performance_claim": False,
                "non_signal": True,
                "phase": prof.current_phase,
                "status": "calibration_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_metric_placeholders(df)
    return df, summary


def summarize_calibration_metric_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration metric placeholders DataFrame."""
    return {
        "total_metrics": len(df),
        "metrics": df["metric_name"].tolist() if not df.empty else [],
        "all_uncalculated": bool((~df["calculated"]).all()) if not df.empty else True,
        "all_zero_performance_claim": bool((~df["performance_claim"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
