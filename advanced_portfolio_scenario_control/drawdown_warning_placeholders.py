# -*- coding: utf-8 -*-
"""Phase 156: Drawdown Warning Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_WARNING_PLACEHOLDERS = [
    {
        "warning_placeholder_id": "WARN-PLH-001",
        "warning_type": "EARLY_WARNING_DRAWDOWN",
        "trigger_level_pct": 5.0,
        "notification_channel": "NONE_DISABLED",
        "status": "PLACEHOLDER_ONLY",
        "active": False,
    },
]


def build_drawdown_warning_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for warning placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_WARNING_PLACEHOLDERS)
    summary = {
        "total_warning_placeholders": len(df),
        "all_inactive": bool((~df["active"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
