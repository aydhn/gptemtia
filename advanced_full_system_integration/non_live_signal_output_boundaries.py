# -*- coding: utf-8 -*-
"""Phase 158: Non-Live Signal Output Boundaries.

Enforces boundaries against outputting live trading signals or recommendations.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

SIGNAL_RULES = [
    ("NLS-001", "signal_boundary", "no_buy_sell_signals", "signal", False, "Generating BUY/SELL signals is strictly prohibited."),
    ("NLS-002", "signal_boundary", "no_long_short_recommendations", "recommendation", False, "Generating directional trading recommendations is prohibited."),
    ("NLS-003", "signal_boundary", "no_position_recommendations", "position", False, "Recommending real market positions is prohibited."),
    ("NLS-004", "signal_boundary", "non_signal_contract_certification", "certification", True, "Outputs are certified non-signal research artifacts."),
]


def build_non_live_signal_output_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build non-live signal output boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in SIGNAL_RULES:
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
