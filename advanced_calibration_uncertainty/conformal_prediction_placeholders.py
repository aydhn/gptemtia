# -*- coding: utf-8 -*-
"""Phase 141: Conformal Prediction Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CONFORMAL_PREDICTION_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "split_conformal_regression_placeholder",
        "conformal_type": "inductive_split_conformal",
        "nominal_error_rate_alpha": 0.10,
        "description": "Inductive split conformal interval at alpha=0.10 (90% coverage); uncalculated.",
    },
    {
        "placeholder_name": "conformalized_quantile_regression_placeholder",
        "conformal_type": "cqr_quantile_residuals",
        "nominal_error_rate_alpha": 0.05,
        "description": "Conformalized quantile regression interval at alpha=0.05 (95% coverage); uncalculated.",
    },
    {
        "placeholder_name": "adaptive_prediction_sets_placeholder",
        "conformal_type": "aps_classification_set",
        "nominal_error_rate_alpha": 0.05,
        "description": "Adaptive prediction sets for multiclass classification at alpha=0.05; uncalculated.",
    },
]


def build_conformal_prediction_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for conformal prediction placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CONFORMAL_PREDICTION_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_name": item["placeholder_name"],
                "conformal_type": item["conformal_type"],
                "nominal_error_rate_alpha": item["nominal_error_rate_alpha"],
                "description": item["description"],
                "executed": False,
                "conformal_set": None,
                "non_signal": True,
                "production_ready": False,
                "phase": prof.current_phase,
                "status": "calibration_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_conformal_prediction_placeholders(df)
    return df, summary


def summarize_conformal_prediction_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize conformal prediction placeholders DataFrame."""
    return {
        "total_placeholders": len(df),
        "placeholders": df["placeholder_name"].tolist() if not df.empty else [],
        "all_unexecuted": bool((~df["executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
