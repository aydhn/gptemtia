# -*- coding: utf-8 -*-
"""Phase 144: Governance Broker Ready Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_BROKER_READY_TERMS = [
    "broker_ready",
    "broker_certified",
    "broker_connect",
    "broker_gateway_ready",
]


def build_governance_broker_ready_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled broker-ready status."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "broker_ready_claim", "is_disabled": True, "reason": "Broker readiness claim is permanently prohibited."},
        {"action": "broker_gateway_connection", "is_disabled": True, "reason": "Connecting broker order gateways is prohibited."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_broker_ready_disabled(df)
    return df, summary


def summarize_governance_broker_ready_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize broker ready disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "BROKER_READY_DISABLED_ENFORCED",
    }


def validate_no_broker_ready_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any broker-ready requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_BROKER_READY_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Broker readiness requests are prohibited.",
    }
