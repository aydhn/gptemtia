# -*- coding: utf-8 -*-
"""Phase 158: No Investment Advice Boundaries.

Enforces boundaries ensuring outputs are never construed as investment advice.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

ADVICE_RULES = [
    ("NIA-001", "advice_boundary", "no_financial_advice_statements", "advice", False, "Financial and investment advice statements are strictly forbidden."),
    ("NIA-002", "advice_boundary", "mandatory_disclaimer_attachment", "reporting", True, "All generated reports must attach full disclaimers."),
    ("NIA-003", "advice_boundary", "research_only_classification", "classification", True, "All findings must be classified as academic/research artifacts only."),
]


def build_no_investment_advice_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-investment-advice boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in ADVICE_RULES:
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
