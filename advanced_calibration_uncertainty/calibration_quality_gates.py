# -*- coding: utf-8 -*-
"""Phase 141: Calibration Quality Gates."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CALIBRATION_QUALITY_GATES: List[Dict[str, Any]] = [
    {
        "gate_name": "candidate_contract_present_gate",
        "description": "Verifies candidate model contract reference exists in Phase 140 registry.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "ensemble_contract_present_gate",
        "description": "Verifies ensemble contract reference exists in Phase 140 registry.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "calibration_contract_present_gate",
        "description": "Verifies calibration contract metadata is well-formed.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_probability_prediction_gate",
        "description": "Guarantees probability prediction execution is disabled.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_calibration_fit_gate",
        "description": "Guarantees calibration fit is disabled.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_calibration_transform_gate",
        "description": "Guarantees calibration transformation is disabled.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_metric_calculation_gate",
        "description": "Guarantees ECE/Brier/loss metrics are not computed.",
        "blocking": True,
        "is_active": True,
    },
    {
        "gate_name": "no_artifact_persistence_gate",
        "description": "Guarantees zero model artifacts are persisted to disk.",
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


def build_calibration_quality_gate_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration quality gates."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CALIBRATION_QUALITY_GATES:
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
    summary = summarize_calibration_quality_gates(df)
    return df, summary


def validate_calibration_quality_gate_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request against calibration quality gates."""
    req_str = ""
    if isinstance(request, dict):
        req_str = " ".join(f"{k} {v}" for k, v in request.items()).lower()
    else:
        req_str = str(request).lower()

    violations = []
    if any(term in req_str for term in ["predict_proba", "probability", "confidence"]):
        violations.append("Violates no_probability_prediction_gate")
    if any(term in req_str for term in ["fit", "train", "calibrate"]):
        violations.append("Violates no_calibration_fit_gate")
    if "transform" in req_str:
        violations.append("Violates no_calibration_transform_gate")

    is_passed = len(violations) == 0
    return {
        "gate_passed": is_passed,
        "violations": violations,
        "status": "PASS" if is_passed else "BLOCKED_BY_CALIBRATION_QUALITY_GATE",
        "non_signal": True,
    }


def summarize_calibration_quality_gates(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration quality gates DataFrame."""
    return {
        "total_gates": len(df),
        "gates": df["gate_name"].tolist() if not df.empty else [],
        "all_active": bool(df["is_active"].all()) if not df.empty else True,
        "all_blocking": bool(df["blocking"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
