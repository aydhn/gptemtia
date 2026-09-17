# -*- coding: utf-8 -*-
"""Phase 156: Slippage Shock Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_SLIPPAGE_SCENARIOS = [
    {
        "scenario_id": "SLIP-SCN-001",
        "slippage_type": "EXTREME_VOLATILITY_EXECUTION_DELAY",
        "description": "Kriz aninda 3x piyasa etki ve kayma carpan soku",
        "multiplier": 3.0,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_slippage_shock_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for slippage shock scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_SLIPPAGE_SCENARIOS)
    summary = {
        "total_slippage_shock_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
