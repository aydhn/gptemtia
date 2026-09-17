# -*- coding: utf-8 -*-
"""Phase 156: Hedge Control Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_HEDGE_PLACEHOLDERS = [
    {
        "action_id": "ACT-HDG-001",
        "action_type": "HEDGE_CONTROL",
        "target_scope": "TAIL_RISK_OVERLAY",
        "hedge_ratio_target": 0.20,
        "activation_trigger": "CRITICAL_DRAWDOWN_WARNING",
        "execution_enabled": False,
        "status": "PLACEHOLDER_ONLY",
    },
]


def build_hedge_control_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for hedge control placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_HEDGE_PLACEHOLDERS)
    summary = {
        "total_hedge_placeholders": len(df),
        "execution_disabled": bool((~df["execution_enabled"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
