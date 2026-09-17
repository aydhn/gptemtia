# -*- coding: utf-8 -*-
"""Phase 144: Governance Deployment Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_DEPLOYMENT_TERMS = [
    "deploy_model",
    "publish_model",
    "release_model",
    "production_deployment",
    "stage_model",
]


def build_governance_deployment_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled deployment."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "deploy_model", "is_disabled": True, "reason": "Model deployment is permanently disabled."},
        {"action": "production_deployment", "is_disabled": True, "reason": "Production deployment is blocked by safety boundary."},
        {"action": "publish_model", "is_disabled": True, "reason": "Publishing models to serving infrastructure is prohibited."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_deployment_disabled(df)
    return df, summary


def summarize_governance_deployment_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize deployment disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "DEPLOYMENT_DISABLED_ENFORCED",
    }


def validate_no_deployment_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any deployment requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_DEPLOYMENT_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Model deployment is prohibited.",
    }
