# -*- coding: utf-8 -*-
"""Phase 156: Recovery Plan Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_RECOVERY_PLANS = [
    {
        "plan_id": "REC-PLAN-001",
        "plan_name": "post_breach_stabilization_plan",
        "waiting_period_days": 14,
        "minimum_volatility_settlement_pct": 20.0,
        "status": "PLACEHOLDER_ONLY",
        "plan_active": False,
    },
]


def build_recovery_plan_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for recovery plans."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_RECOVERY_PLANS)
    summary = {
        "total_recovery_plans": len(df),
        "all_plans_inactive": bool((~df["plan_active"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
