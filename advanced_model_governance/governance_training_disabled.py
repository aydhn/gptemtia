# -*- coding: utf-8 -*-
"""Phase 144: Governance Training Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_TRAINING_TERMS = [
    "train",
    "fit",
    "retrain",
    "fine_tune",
    "backprop",
]


def build_governance_training_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled training execution."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "model_fit", "is_disabled": True, "reason": "Real model fitting is disabled in governance phase."},
        {"action": "model_training", "is_disabled": True, "reason": "Model training execution is disabled in governance phase."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_training_disabled(df)
    return df, summary


def summarize_governance_training_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize training disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "TRAINING_DISABLED_ENFORCED",
    }


def validate_no_governance_training_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any training execution requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_TRAINING_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Model training execution is prohibited in governance phase.",
    }
