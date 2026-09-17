# -*- coding: utf-8 -*-
"""Phase 156: Rebalance Control Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_REBALANCE_PLACEHOLDERS = [
    {
        "action_id": "ACT-REB-001",
        "action_type": "REBALANCE_CONTROL",
        "target_scope": "RISK_PARITY_RESET",
        "rebalance_threshold_pct": 5.0,
        "activation_trigger": "WEIGHT_DRIFT_EXCEEDANCE",
        "execution_enabled": False,
        "status": "PLACEHOLDER_ONLY",
    },
]


def build_rebalance_control_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for rebalance control placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_REBALANCE_PLACEHOLDERS)
    summary = {
        "total_rebalance_placeholders": len(df),
        "execution_disabled": bool((~df["execution_enabled"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
