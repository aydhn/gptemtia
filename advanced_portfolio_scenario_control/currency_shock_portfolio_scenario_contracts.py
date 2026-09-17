# -*- coding: utf-8 -*-
"""Phase 156: Currency Shock Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_CURRENCY_SHOCK_SCENARIOS = [
    {
        "scenario_id": "FX-SCN-001",
        "shock_name": "USD Surge Shock",
        "description": "DXY endeksinde %12 ani sicrama soku",
        "shock_magnitude_pct": 12.0,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "FX-SCN-002",
        "shock_name": "Emerging FX Devaluation Shock",
        "description": "Gelisipte olan ulke kurlarinda %25 devaluasyon soku",
        "shock_magnitude_pct": -25.0,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_currency_shock_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for currency shock scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_CURRENCY_SHOCK_SCENARIOS)
    summary = {
        "total_currency_shock_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
