# -*- coding: utf-8 -*-
"""Phase 156: Stop Control Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_STOP_PLACEHOLDERS = [
    {
        "action_id": "ACT-STP-001",
        "action_type": "STOP_CONTROL",
        "target_scope": "SINGLE_ASSET_STOP_LOSS",
        "stop_loss_pct": 7.5,
        "activation_trigger": "ASSET_DRAWDOWN_LIMIT",
        "execution_enabled": False,
        "status": "PLACEHOLDER_ONLY",
    },
]


def build_stop_control_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for stop control placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_STOP_PLACEHOLDERS)
    summary = {
        "total_stop_placeholders": len(df),
        "execution_disabled": bool((~df["execution_enabled"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
