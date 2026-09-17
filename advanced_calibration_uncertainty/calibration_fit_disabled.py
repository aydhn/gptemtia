# -*- coding: utf-8 -*-
"""Phase 141: Calibration Fit Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

FORBIDDEN_FIT_KEYWORDS = [
    "fit",
    "train",
    "calibration_fit",
    "fit_transform",
    "calibrate",
    "platt",
    "isotonic",
    "target",
    "label",
]


def build_calibration_fit_disabled_report(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report certifying all calibration fitting is disabled."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = [
        {
            "fit_operation": "platt_scaling_fit",
            "is_fit_disabled": True,
            "policy": "PHASE_141_NO_CALIBRATION_FIT",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "fit_operation": "isotonic_regression_fit",
            "is_fit_disabled": True,
            "policy": "PHASE_141_NO_CALIBRATION_FIT",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "fit_operation": "temperature_scaling_fit",
            "is_fit_disabled": True,
            "policy": "PHASE_141_NO_CALIBRATION_FIT",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "fit_operation": "beta_calibration_fit",
            "is_fit_disabled": True,
            "policy": "PHASE_141_NO_CALIBRATION_FIT",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_calibration_fit_disabled(df)
    return df, summary


def validate_no_calibration_fit_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensuring no calibration fit is initiated."""
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    detected = [kw for kw in FORBIDDEN_FIT_KEYWORDS if kw in req_str]
    is_blocked = len(detected) > 0

    return {
        "fit_allowed": False,
        "is_blocked": is_blocked,
        "policy_status": "execution_blocked_no_calibration_fit" if is_blocked else "execution_contract_only",
        "detected_violations": detected,
        "blocked_reason": "Calibration fit request strictly blocked by Phase 141 policy."
        if is_blocked
        else "No fit requested; contract only.",
        "non_signal": True,
    }


def summarize_calibration_fit_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration fit disabled DataFrame."""
    return {
        "total_fit_operations_audited": len(df),
        "all_fit_disabled": bool(df["is_fit_disabled"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
