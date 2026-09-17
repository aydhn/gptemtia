# -*- coding: utf-8 -*-
"""Phase 158: No Live Trading Boundaries.

Enforces strict prohibitions against live trading and account execution.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

LIVE_TRADING_RULES = [
    ("NLT-001", "live_trading_boundary", "no_live_capital_allocation", "capital", False, "Allocating live capital is prohibited."),
    ("NLT-002", "live_trading_boundary", "no_live_portfolio_rebalance", "portfolio", False, "Triggering live rebalance orders is prohibited."),
    ("NLT-003", "live_trading_boundary", "no_live_risk_derisking_execution", "risk", False, "Automated live derisking executions are prohibited."),
    ("NLT-004", "live_trading_boundary", "local_offline_enforcement", "runtime", True, "System strictly operates offline."),
]


def build_no_live_trading_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-live-trading boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in LIVE_TRADING_RULES:
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
