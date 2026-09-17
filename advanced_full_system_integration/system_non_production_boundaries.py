# -*- coding: utf-8 -*-
"""Phase 158: System Non-Production Boundaries.

Enforces non-production isolation and prevents production deployment or approval claims.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

NON_PRODUCTION_RULES = [
    ("NPB-158-001", "non_production_boundary", "no_production_deployment", "deployment", False, "Production deployment is strictly prohibited."),
    ("NPB-158-002", "non_production_boundary", "no_production_ready_claim", "claim", False, "System cannot be claimed as production-ready."),
    ("NPB-158-003", "non_production_boundary", "no_broker_ready_claim", "claim", False, "System cannot be claimed as broker-ready."),
    ("NPB-158-004", "non_production_boundary", "no_live_ready_claim", "claim", False, "System cannot be claimed as live-ready."),
    ("NPB-158-005", "non_production_boundary", "no_official_approval_claim", "claim", False, "Official approval claims are strictly forbidden."),
    ("NPB-158-006", "non_production_boundary", "research_only_governance", "governance", True, "System strictly operates in research-only mode."),
]


def build_system_non_production_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system non-production boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in NON_PRODUCTION_RULES:
        item = SystemBoundaryItem(
            boundary_id=bid,
            boundary_type=btype,
            rule_name=rname,
            action_type=atype,
            is_allowed=is_allowed,
            reason=reason,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "prohibited_actions_count": int((df["is_allowed"] == False).sum()),
        "allowed_actions_count": int((df["is_allowed"] == True).sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
