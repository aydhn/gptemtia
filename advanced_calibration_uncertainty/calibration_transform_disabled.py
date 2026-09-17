# -*- coding: utf-8 -*-
"""Phase 141: Calibration Transform Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

FORBIDDEN_TRANSFORM_KEYWORDS = [
    "transform",
    "calibration_transform",
    "calibrate",
    "calibrated_probability",
    "predict_proba",
    "predict",
    "inference",
]


def build_calibration_transform_disabled_report(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report certifying all calibration transformations are disabled."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = [
        {
            "transform_operation": "platt_scaling_transform",
            "is_transform_disabled": True,
            "policy": "PHASE_141_NO_CALIBRATION_TRANSFORM",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "transform_operation": "isotonic_regression_transform",
            "is_transform_disabled": True,
            "policy": "PHASE_141_NO_CALIBRATION_TRANSFORM",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "transform_operation": "temperature_scaling_transform",
            "is_transform_disabled": True,
            "policy": "PHASE_141_NO_CALIBRATION_TRANSFORM",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_calibration_transform_disabled(df)
    return df, summary


def validate_no_calibration_transform_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensuring no calibration transform is initiated."""
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    detected = [kw for kw in FORBIDDEN_TRANSFORM_KEYWORDS if kw in req_str]
    is_blocked = len(detected) > 0

    return {
        "transform_allowed": False,
        "is_blocked": is_blocked,
        "policy_status": "execution_blocked_no_calibration_transform" if is_blocked else "execution_contract_only",
        "detected_violations": detected,
        "blocked_reason": "Calibration transform request strictly blocked by Phase 141 policy."
        if is_blocked
        else "No transform requested; contract only.",
        "non_signal": True,
    }


def summarize_calibration_transform_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration transform disabled DataFrame."""
    return {
        "total_transform_operations_audited": len(df),
        "all_transform_disabled": bool(df["is_transform_disabled"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
