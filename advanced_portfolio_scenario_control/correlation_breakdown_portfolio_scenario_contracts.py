# -*- coding: utf-8 -*-
"""Phase 156: Correlation Breakdown Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_CORR_BREAK_SCENARIOS = [
    {
        "scenario_id": "CORR-SCN-001",
        "breakdown_type": "FLIGHT_TO_CASH_CONVERGENCE",
        "description": "Tum riskli varliklar arasi korelasyonun 1.0'e yaklasmasi",
        "target_correlation": 0.95,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "CORR-SCN-002",
        "breakdown_type": "SAFE_HAVEN_DECOUPLING",
        "description": "Altin ve tahvil gibi guvenli liman korelasyonunun kopmasi",
        "target_correlation": -0.40,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_correlation_breakdown_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for correlation breakdown contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_CORR_BREAK_SCENARIOS)
    summary = {
        "total_correlation_breakdown_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
