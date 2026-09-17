# -*- coding: utf-8 -*-
"""Phase 141: Calibration Execution Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

FORBIDDEN_CALIBRATION_EXECUTION_KEYWORDS = [
    "predict_proba",
    "probability",
    "calibrated_probability",
    "calibrate",
    "calibration_fit",
    "calibration_transform",
    "platt",
    "isotonic",
    "temperature_scaling",
    "confidence_score",
    "confidence",
    "class_probability",
    "fit",
    "train",
    "predict",
    "inference",
    "transform",
    "target",
    "label",
    "signal",
    "buy",
    "sell",
    "long",
    "short",
]


def build_calibration_execution_disabled_report(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report certifying all calibration execution is disabled by policy."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = [
        {
            "operation": "probability_calibration_execution",
            "is_disabled": True,
            "policy": "PHASE_141_NON_EXECUTING_CALIBRATION_POLICY",
            "blocked_action": "calibrate_models_or_scores",
            "reason": "Phase 141 is strictly a contract and governance layer; calibration execution is prohibited.",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "operation": "probability_prediction_execution",
            "is_disabled": True,
            "policy": "PHASE_141_ZERO_PROBABILITY_PREDICTION_POLICY",
            "blocked_action": "predict_proba_or_confidence",
            "reason": "Probability inference and class likelihood calculations are disabled.",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "operation": "calibration_parameter_optimization",
            "is_disabled": True,
            "policy": "PHASE_141_NO_OPTIMIZATION_POLICY",
            "blocked_action": "optimize_calibration_hyperparameters",
            "reason": "Calibration parameter fitting is disabled.",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_calibration_execution_disabled(df)
    return df, summary


def validate_no_calibration_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate incoming request ensuring no calibration execution or forbidden keywords exist."""
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    detected_violations = [kw for kw in FORBIDDEN_CALIBRATION_EXECUTION_KEYWORDS if kw in req_str]
    is_blocked = len(detected_violations) > 0

    return {
        "execution_allowed": False,
        "is_blocked": is_blocked,
        "policy_status": "execution_blocked_no_calibration_fit" if is_blocked else "execution_contract_only",
        "detected_violations": detected_violations,
        "blocked_reason": "Calibration execution request blocked by Phase 141 non-executing safety boundary."
        if is_blocked
        else "No execution requested; contract only.",
        "non_signal": True,
    }


def summarize_calibration_execution_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration execution disabled DataFrame."""
    return {
        "total_operations_audited": len(df),
        "all_disabled": bool(df["is_disabled"].all()) if not df.empty else True,
        "all_enforced": bool((df["enforcement"] == "STRICT_BLOCK").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
