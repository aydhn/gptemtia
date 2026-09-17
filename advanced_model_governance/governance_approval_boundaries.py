# -*- coding: utf-8 -*-
"""Phase 144: Governance Approval Boundaries Registry."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

APPROVAL_BOUNDARY_SPECS: List[Dict[str, str]] = [
    {
        "boundary_name": "production_approval_blocked_boundary",
        "boundary_type": "production_approval",
        "enforcement_rule": "Production approval cannot be granted in offline non-production governance.",
        "error_message": "Production approval request is strictly blocked by safety policy.",
    },
    {
        "boundary_name": "broker_ready_approval_blocked_boundary",
        "boundary_type": "broker_ready_approval",
        "enforcement_rule": "Broker readiness sign-off is prohibited in local offline research.",
        "error_message": "Broker readiness approval request is strictly blocked by safety policy.",
    },
    {
        "boundary_name": "live_trading_approval_blocked_boundary",
        "boundary_type": "live_trading_approval",
        "enforcement_rule": "Live trading execution approval is permanently disabled in this repository.",
        "error_message": "Live trading approval request is strictly blocked by safety policy.",
    },
    {
        "boundary_name": "release_approval_blocked_boundary",
        "boundary_type": "release_approval",
        "enforcement_rule": "Release sign-off for deployment is blocked.",
        "error_message": "Release approval request is strictly blocked by safety policy.",
    },
    {
        "boundary_name": "official_approval_claim_blocked_boundary",
        "boundary_type": "official_approval_claim",
        "enforcement_rule": "Claiming official regulatory or institutional approval is prohibited.",
        "error_message": "Official approval claim is strictly blocked by safety policy.",
    },
    {
        "boundary_name": "manual_review_required_boundary",
        "boundary_type": "manual_review",
        "enforcement_rule": "All governance transitions require explicit human reviewer sign-off.",
        "error_message": "Automatic transition prohibited; manual review gate triggered.",
    },
]


def build_governance_approval_boundary_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance approval boundaries."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in APPROVAL_BOUNDARY_SPECS:
        row = dict(spec)
        row["action_permitted"] = False
        row["manual_review_required"] = True
        row["phase"] = prof.current_phase
        row["status"] = "ENFORCED"
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_approval_boundaries(df)
    return df, summary


def summarize_governance_approval_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance approval boundaries."""
    return {
        "total_boundaries": len(df),
        "all_actions_blocked": not bool(df["action_permitted"].any()),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "all_enforced": bool((df["status"] == "ENFORCED").all()),
    }


def validate_governance_approval_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any approval requests."""
    req_type = request if isinstance(request, str) else request.get("approval_type", "")
    req_lower = str(req_type).lower()

    prohibited_patterns = [
        "production",
        "broker",
        "live",
        "trading",
        "release",
        "official",
        "deploy",
    ]

    is_blocked = any(pat in req_lower for pat in prohibited_patterns)

    return {
        "request": str(request),
        "is_approved": False,
        "is_blocked": is_blocked,
        "approval_status": "BLOCKED_BY_POLICY" if is_blocked else "CONTRACT_ONLY",
        "message": (
            "Approval request intercepted and blocked by Governance Approval Boundary."
            if is_blocked
            else "Contract evaluation only; no approval granted."
        ),
        "manual_review_required": True,
    }
