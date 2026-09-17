# -*- coding: utf-8 -*-
"""Phase 156: Drawdown Recovery Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_RECOVERY_PLACEHOLDERS = [
    {
        "recovery_placeholder_id": "RCV-PLH-001",
        "recovery_phase": "GRADUAL_REALLOCATION",
        "trigger_recovery_pct": 50.0,
        "step_size_pct": 10.0,
        "status": "PLACEHOLDER_ONLY",
        "in_recovery": False,
    },
]


def build_drawdown_recovery_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for recovery placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_RECOVERY_PLACEHOLDERS)
    summary = {
        "total_recovery_placeholders": len(df),
        "all_placeholders_inactive": bool((~df["in_recovery"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
