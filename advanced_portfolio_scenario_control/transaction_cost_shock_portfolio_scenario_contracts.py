# -*- coding: utf-8 -*-
"""Phase 156: Transaction Cost Shock Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_COST_SCENARIOS = [
    {
        "scenario_id": "COST-SCN-001",
        "cost_type": "MARGIN_REQUIREMENT_ESCALATION",
        "description": "Borsa teminat zorunlulugunda 2.5x artis soku",
        "multiplier": 2.5,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_transaction_cost_shock_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for transaction cost shock scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_COST_SCENARIOS)
    summary = {
        "total_cost_shock_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
