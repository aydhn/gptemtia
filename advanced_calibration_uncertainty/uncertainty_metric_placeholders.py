# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Metric Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

UNCERTAINTY_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "interval_coverage_placeholder",
        "metric_family": "empirical_coverage",
        "formula_description": "Fraction of true observations captured within prediction intervals; uncalculated.",
    },
    {
        "metric_name": "interval_width_placeholder",
        "metric_family": "interval_efficiency",
        "formula_description": "Average width (upper - lower) of prediction intervals; uncalculated.",
    },
    {
        "metric_name": "prediction_interval_coverage_probability_placeholder",
        "metric_family": "picp_evaluation",
        "formula_description": "Percentage of test points falling into the computed prediction interval; uncalculated.",
    },
    {
        "metric_name": "conformal_coverage_placeholder",
        "metric_family": "conformal_empirical_coverage",
        "formula_description": "Empirical coverage error vs 1 - alpha nominal target; uncalculated.",
    },
    {
        "metric_name": "sharpness_placeholder",
        "metric_family": "dispersion_concentration",
        "formula_description": "Concentration of uncertainty distribution (mean interval width); uncalculated.",
    },
    {
        "metric_name": "uncertainty_calibration_placeholder",
        "metric_family": "error_vs_uncertainty_correlation",
        "formula_description": "Correlation between model error magnitude and estimated uncertainty; uncalculated.",
    },
    {
        "metric_name": "out_of_distribution_uncertainty_placeholder",
        "metric_family": "ood_detection_score",
        "formula_description": "Separation score of uncertainty metrics between in-distribution and OOD inputs; uncalculated.",
    },
]


def build_uncertainty_metric_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for uncertainty metric placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in UNCERTAINTY_METRIC_PLACEHOLDERS:
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
    summary = summarize_uncertainty_metric_placeholders(df)
    return df, summary


def summarize_uncertainty_metric_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty metric placeholders DataFrame."""
    return {
        "total_metrics": len(df),
        "metrics": df["metric_name"].tolist() if not df.empty else [],
        "all_uncalculated": bool((~df["calculated"]).all()) if not df.empty else True,
        "all_zero_performance_claim": bool((~df["performance_claim"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
