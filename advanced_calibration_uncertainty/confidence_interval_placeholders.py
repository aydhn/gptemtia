# -*- coding: utf-8 -*-
"""Phase 141: Confidence Interval Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CONFIDENCE_INTERVAL_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "normal_confidence_interval_95_placeholder",
        "nominal_coverage": 0.95,
        "method": "wald_normal_approximation",
        "description": "95% Wald normal approximation confidence interval; uncalculated.",
    },
    {
        "placeholder_name": "bootstrap_confidence_interval_95_placeholder",
        "nominal_coverage": 0.95,
        "method": "percentile_bootstrap",
        "description": "95% Percentile bootstrap confidence interval; uncalculated.",
    },
    {
        "placeholder_name": "student_t_confidence_interval_99_placeholder",
        "nominal_coverage": 0.99,
        "method": "student_t_distribution",
        "description": "99% Student-t confidence interval; uncalculated.",
    },
]


def build_confidence_interval_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for confidence interval placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CONFIDENCE_INTERVAL_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_name": item["placeholder_name"],
                "nominal_coverage": item["nominal_coverage"],
                "method": item["method"],
                "description": item["description"],
                "calculated": False,
                "lower_bound": None,
                "upper_bound": None,
                "non_signal": True,
                "production_ready": False,
                "phase": prof.current_phase,
                "status": "calibration_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_confidence_interval_placeholders(df)
    return df, summary


def summarize_confidence_interval_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize confidence interval placeholders DataFrame."""
    return {
        "total_placeholders": len(df),
        "placeholders": df["placeholder_name"].tolist() if not df.empty else [],
        "all_uncalculated": bool((~df["calculated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
