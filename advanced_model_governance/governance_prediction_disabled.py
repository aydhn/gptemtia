# -*- coding: utf-8 -*-
"""Phase 144: Governance Prediction Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_PREDICTION_TERMS = [
    "predict",
    "inference",
    "forecast",
    "probability_prediction",
]


def build_governance_prediction_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled prediction execution."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "model_predict", "is_disabled": True, "reason": "Model prediction execution is disabled in governance phase."},
        {"action": "model_inference", "is_disabled": True, "reason": "Model inference execution is disabled in governance phase."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_prediction_disabled(df)
    return df, summary


def summarize_governance_prediction_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize prediction disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "PREDICTION_DISABLED_ENFORCED",
    }


def validate_no_governance_prediction_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any prediction execution requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_PREDICTION_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Prediction execution is prohibited in governance phase.",
    }
