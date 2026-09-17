# -*- coding: utf-8 -*-
"""Phase 156: Spread Widening Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_SPREAD_SCENARIOS = [
    {
        "scenario_id": "SPRD-SCN-001",
        "spread_type": "CALENDAR_ROLL_SPREAD_DISLOCATION",
        "description": "Vadeler arasi roll spreadinde 4x acilma soku",
        "spread_factor": 4.0,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_spread_widening_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for spread widening scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_SPREAD_SCENARIOS)
    summary = {
        "total_spread_widening_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
