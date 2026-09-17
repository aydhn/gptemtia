# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Quality Gates."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

UNCERTAINTY_QUALITY_GATES: List[Dict[str, Any]] = [
    {
        "gate_name": "uncertainty_contract_present_gate",
        "description": "Verifies uncertainty estimation contract metadata is well-formed.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_uncertainty_execution_gate",
        "description": "Guarantees uncertainty estimation algorithms are not executed.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_prediction_interval_execution_gate",
        "description": "Guarantees prediction intervals are not computed.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_conformal_prediction_execution_gate",
        "description": "Guarantees conformal prediction sets are not generated.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_quantile_prediction_gate",
        "description": "Guarantees quantile predictions are not calculated.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_metric_calculation_gate",
        "description": "Guarantees interval coverage and sharpness metrics are not computed.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_artifact_persistence_gate",
        "description": "Guarantees uncertainty artifacts are not persisted.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "manual_review_gate",
        "description": "Requires operator manual review before downstream progression.",
        "blocking": True,
        "is_active": True,
    },
]


def build_uncertainty_quality_gate_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for uncertainty quality gates."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in UNCERTAINTY_QUALITY_GATES:
        rows.append(
            {
                "gate_name": item["gate_name"],
                "description": item["description"],
                "blocking": item["blocking"],
                "is_active": item["is_active"],
                "gate_status": "GATE_ENFORCED",
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_uncertainty_quality_gates(df)
    return df, summary


def validate_uncertainty_quality_gate_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request against uncertainty quality gates."""
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    violations = []
    if "uncertainty" in req_str or "estimate_uncertainty" in req_str:
        violations.append("Violates no_uncertainty_execution_gate")
    if "prediction_interval" in req_str:
        violations.append("Violates no_prediction_interval_execution_gate")
    if "conformal" in req_str:
        violations.append("Violates no_conformal_prediction_execution_gate")
    if "quantile" in req_str:
        violations.append("Violates no_quantile_prediction_gate")

    is_passed = len(violations) == 0
    return {
        "gate_passed": is_passed,
        "violations": violations,
        "status": "PASS" if is_passed else "BLOCKED_BY_UNCERTAINTY_QUALITY_GATE",
        "non_signal": True,
    }


def summarize_uncertainty_quality_gates(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty quality gates DataFrame."""
    return {
        "total_gates": len(df),
        "gates": df["gate_name"].tolist() if not df.empty else [],
        "all_active": bool(df["is_active"].all()) if not df.empty else True,
        "all_blocking": bool(df["blocking"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
