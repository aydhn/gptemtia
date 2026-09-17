# -*- coding: utf-8 -*-
"""Phase 158: No Production Deployment Boundaries.

Enforces prohibitions against deploying to production environments.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

DEPLOYMENT_RULES = [
    ("NPD-001", "deployment_boundary", "no_cloud_container_deploy", "deployment", False, "Deploying containers to cloud services is blocked."),
    ("NPD-002", "deployment_boundary", "no_production_service_spawn", "deployment", False, "Spawning daemon background services for production is blocked."),
    ("NPD-003", "deployment_boundary", "no_production_approval_signoff", "governance", False, "Signing off production approval is blocked in Phase 158."),
    ("NPD-004", "deployment_boundary", "local_research_boundary", "runtime", True, "System strictly isolated to local research environment."),
]


def build_no_production_deployment_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-production-deployment boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in DEPLOYMENT_RULES:
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
