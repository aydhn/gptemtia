# -*- coding: utf-8 -*-
"""Phase 141: Probability Prediction Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

FORBIDDEN_PREDICTION_KEYWORDS = [
    "predict_proba",
    "probability",
    "class_probability",
    "confidence_score",
    "confidence",
    "posterior_probability",
    "calibrated_prob",
]


def build_probability_prediction_disabled_report(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report certifying probability prediction generation is disabled."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = [
        {
            "prediction_type": "binary_class_probability",
            "is_prediction_disabled": True,
            "policy": "PHASE_141_NO_PROBABILITY_PREDICTION",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "prediction_type": "multiclass_posterior_probability",
            "is_prediction_disabled": True,
            "policy": "PHASE_141_NO_PROBABILITY_PREDICTION",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "prediction_type": "calibrated_score_mapping",
            "is_prediction_disabled": True,
            "policy": "PHASE_141_NO_PROBABILITY_PREDICTION",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_probability_prediction_disabled(df)
    return df, summary


def validate_no_probability_prediction_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensuring no probability prediction is requested."""
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    detected = [kw for kw in FORBIDDEN_PREDICTION_KEYWORDS if kw in req_str]
    is_blocked = len(detected) > 0

    return {
        "prediction_allowed": False,
        "is_blocked": is_blocked,
        "policy_status": "execution_blocked_no_probability_prediction" if is_blocked else "execution_contract_only",
        "detected_violations": detected,
        "blocked_reason": "Probability prediction request strictly blocked by Phase 141 policy."
        if is_blocked
        else "No probability prediction requested; contract only.",
        "non_signal": True,
    }


def summarize_probability_prediction_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize probability prediction disabled DataFrame."""
    return {
        "total_prediction_types_audited": len(df),
        "all_prediction_disabled": bool(df["is_prediction_disabled"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
