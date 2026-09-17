# -*- coding: utf-8 -*-
"""Phase 144: Governance Production Approval Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_PRODUCTION_APPROVAL_TERMS = [
    "approve_production",
    "production_ready",
    "signoff_production",
    "certify_production",
]


def build_governance_production_approval_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled production approval."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "approve_production", "is_disabled": True, "reason": "Production approval is disabled in non-production research layer."},
        {"action": "production_ready_claim", "is_disabled": True, "reason": "Claiming production readiness is strictly prohibited."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_production_approval_disabled(df)
    return df, summary


def summarize_governance_production_approval_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize production approval disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "PRODUCTION_APPROVAL_DISABLED_ENFORCED",
    }


def validate_no_production_approval_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any production approval requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_PRODUCTION_APPROVAL_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Production approval requests are prohibited.",
    }
