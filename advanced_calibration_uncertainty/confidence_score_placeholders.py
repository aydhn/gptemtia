# -*- coding: utf-8 -*-
"""Phase 141: Confidence Score Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CONFIDENCE_SCORE_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "max_probability_confidence_placeholder",
        "score_type": "top_class_max_prob",
        "description": "Maximum class probability score placeholder; uncalculated.",
    },
    {
        "placeholder_name": "margin_confidence_placeholder",
        "score_type": "top_two_class_margin",
        "description": "Difference between top two class probabilities; uncalculated.",
    },
    {
        "placeholder_name": "entropy_confidence_placeholder",
        "score_type": "predictive_entropy",
        "description": "Information entropy across predicted class distribution; uncalculated.",
    },
]


def build_confidence_score_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for confidence score placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CONFIDENCE_SCORE_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_name": item["placeholder_name"],
                "score_type": item["score_type"],
                "description": item["description"],
                "calculated": False,
                "score_value": None,
                "non_signal": True,
                "production_ready": False,
                "phase": prof.current_phase,
                "status": "calibration_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_confidence_score_placeholders(df)
    return df, summary


def summarize_confidence_score_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize confidence score placeholders DataFrame."""
    return {
        "total_placeholders": len(df),
        "placeholders": df["placeholder_name"].tolist() if not df.empty else [],
        "all_uncalculated": bool((~df["calculated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
