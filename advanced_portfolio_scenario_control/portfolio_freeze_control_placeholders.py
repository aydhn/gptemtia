# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Freeze Control Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_FREEZE_PLACEHOLDERS = [
    {
        "action_id": "ACT-FRZ-001",
        "action_type": "FREEZE_CONTROL",
        "target_scope": "ALL_NEW_ORDERS",
        "activation_trigger": "CRITICAL_CIRCUIT_BREAKER_15PCT",
        "execution_enabled": False,
        "status": "PLACEHOLDER_ONLY",
    },
]


def build_portfolio_freeze_control_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for freeze control placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_FREEZE_PLACEHOLDERS)
    summary = {
        "total_freeze_placeholders": len(df),
        "execution_disabled": bool((~df["execution_enabled"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
