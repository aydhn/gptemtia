# -*- coding: utf-8 -*-
"""Phase 144: Governance Performance Claim Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_PERFORMANCE_TERMS = [
    "performance_claim",
    "accuracy",
    "sharpe",
    "win_rate",
    "profit_factor",
    "calmar",
]


def build_governance_performance_claim_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled performance claims."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "performance_claim", "is_disabled": True, "reason": "Model performance claims are prohibited in governance contract phase."},
        {"action": "accuracy_metric_claim", "is_disabled": True, "reason": "Predictive accuracy claims are prohibited without live verification."},
        {"action": "sharpe_ratio_claim", "is_disabled": True, "reason": "Trading Sharpe ratio claims are prohibited."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_performance_claim_disabled(df)
    return df, summary


def summarize_governance_performance_claim_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize performance claim disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "PERFORMANCE_CLAIM_DISABLED_ENFORCED",
    }


def validate_no_performance_claim_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any performance claim requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_PERFORMANCE_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Performance claims are prohibited in governance phase.",
    }
