# -*- coding: utf-8 -*-
"""Phase 156: Liquidity Crunch Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_LIQ_CRUNCH_SCENARIOS = [
    {
        "scenario_id": "LIQ-SCN-001",
        "crunch_type": "BID_ASK_SPREAD_EXPANSION_5X",
        "description": "Alis-satis makasinda 5 kat genisleme",
        "spread_multiplier": 5.0,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "LIQ-SCN-002",
        "crunch_type": "MARKET_DEPTH_EVAPORATION_80PCT",
        "description": "Emir defteri derinliginde %80 buharlasmasi",
        "depth_reduction_pct": 80.0,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_liquidity_crunch_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for liquidity crunch scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_LIQ_CRUNCH_SCENARIOS)
    summary = {
        "total_liquidity_crunch_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
