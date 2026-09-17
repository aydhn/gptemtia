# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Execution Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

FORBIDDEN_UNCERTAINTY_KEYWORDS = [
    "uncertainty",
    "estimate_uncertainty",
    "prediction_interval",
    "confidence_interval",
    "quantile",
    "conformal",
    "bootstrap",
    "monte_carlo",
    "dropout",
    "bayesian",
    "ensemble_variance",
    "fit",
    "predict",
    "inference",
    "transform",
    "target",
    "label",
    "signal",
]


def build_uncertainty_execution_disabled_report(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report certifying all uncertainty estimation execution is disabled."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = [
        {
            "operation": "prediction_interval_calculation",
            "is_disabled": True,
            "policy": "PHASE_141_NO_UNCERTAINTY_EXECUTION",
            "blocked_action": "calculate_prediction_interval",
            "reason": "Phase 141 uncertainty estimation is contract-only; interval calculation is blocked.",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "operation": "conformal_prediction_execution",
            "is_disabled": True,
            "policy": "PHASE_141_NO_UNCERTAINTY_EXECUTION",
            "blocked_action": "generate_conformal_sets",
            "reason": "Conformal set generation is disabled.",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "operation": "quantile_estimation_execution",
            "is_disabled": True,
            "policy": "PHASE_141_NO_UNCERTAINTY_EXECUTION",
            "blocked_action": "estimate_conditional_quantiles",
            "reason": "Quantile estimation is disabled.",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "operation": "bayesian_approximation_execution",
            "is_disabled": True,
            "policy": "PHASE_141_NO_UNCERTAINTY_EXECUTION",
            "blocked_action": "sample_posterior_weights",
            "reason": "Bayesian inference is disabled.",
            "enforcement": "STRICT_BLOCK",
            "non_signal": True,
            "phase": prof.current_phase,
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_uncertainty_execution_disabled(df)
    return df, summary


def validate_no_uncertainty_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensuring no uncertainty estimation is requested."""
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    detected = [kw for kw in FORBIDDEN_UNCERTAINTY_KEYWORDS if kw in req_str]
    is_blocked = len(detected) > 0

    return {
        "execution_allowed": False,
        "is_blocked": is_blocked,
        "policy_status": "execution_blocked_no_uncertainty_estimation" if is_blocked else "execution_contract_only",
        "detected_violations": detected,
        "blocked_reason": "Uncertainty execution request strictly blocked by Phase 141 policy."
        if is_blocked
        else "No uncertainty execution requested; contract only.",
        "non_signal": True,
    }


def summarize_uncertainty_execution_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty execution disabled DataFrame."""
    return {
        "total_operations_audited": len(df),
        "all_disabled": bool(df["is_disabled"].all()) if not df.empty else True,
        "all_enforced": bool((df["enforcement"] == "STRICT_BLOCK").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
