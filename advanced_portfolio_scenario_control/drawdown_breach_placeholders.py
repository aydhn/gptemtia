# -*- coding: utf-8 -*-
"""Phase 156: Drawdown Breach Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_BREACH_PLACEHOLDERS = [
    {
        "breach_placeholder_id": "BRCH-PLH-001",
        "breach_tier": "LEVEL_1_BREACH",
        "threshold_pct": 10.0,
        "containment_action": "EXPOSURE_CURTAILMENT",
        "status": "PLACEHOLDER_ONLY",
        "triggered": False,
    },
    {
        "breach_placeholder_id": "BRCH-PLH-002",
        "breach_tier": "LEVEL_2_CRITICAL_BREACH",
        "threshold_pct": 15.0,
        "containment_action": "PORTFOLIO_CIRCUIT_BREAKER",
        "status": "PLACEHOLDER_ONLY",
        "triggered": False,
    },
]


def build_drawdown_breach_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for breach placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_BREACH_PLACEHOLDERS)
    summary = {
        "total_breach_placeholders": len(df),
        "all_untriggered": bool((~df["triggered"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
