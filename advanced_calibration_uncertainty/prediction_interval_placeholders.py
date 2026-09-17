# -*- coding: utf-8 -*-
"""Phase 141: Prediction Interval Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

PREDICTION_INTERVAL_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "ols_prediction_interval_90_placeholder",
        "nominal_coverage": 0.90,
        "method": "ols_residual_variance",
        "description": "90% OLS residual prediction interval placeholder; uncalculated.",
    },
    {
        "placeholder_name": "gradient_boosting_prediction_interval_95_placeholder",
        "nominal_coverage": 0.95,
        "method": "dual_quantile_loss",
        "description": "95% Dual quantile loss gradient boosting prediction interval; uncalculated.",
    },
    {
        "placeholder_name": "ensemble_spread_prediction_interval_placeholder",
        "nominal_coverage": 0.95,
        "method": "ensemble_interquartile_spread",
        "description": "Ensemble candidate interquartile range prediction interval; uncalculated.",
    },
]


def build_prediction_interval_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for prediction interval placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in PREDICTION_INTERVAL_PLACEHOLDERS:
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
    summary = summarize_prediction_interval_placeholders(df)
    return df, summary


def summarize_prediction_interval_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize prediction interval placeholders DataFrame."""
    return {
        "total_placeholders": len(df),
        "placeholders": df["placeholder_name"].tolist() if not df.empty else [],
        "all_uncalculated": bool((~df["calculated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
