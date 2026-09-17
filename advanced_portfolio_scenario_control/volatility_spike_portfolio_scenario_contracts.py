# -*- coding: utf-8 -*-
"""Phase 156: Volatility Spike Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_VOL_SPIKE_SCENARIOS = [
    {
        "scenario_id": "VOL-SCN-001",
        "spike_type": "IMPLIED_VOL_DOUBLING",
        "description": "Opsiyon ima edilen volatilitesinde 2x artis soku",
        "vol_multiplier": 2.0,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "VOL-SCN-002",
        "spike_type": "COMMODITY_VOL_SUPER_SPIKE",
        "description": "Emtia vadeli sozlesmelerinde 3.5x gerceklesen volatilite patlamasi",
        "vol_multiplier": 3.5,
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_volatility_spike_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for volatility spike scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_VOL_SPIKE_SCENARIOS)
    summary = {
        "total_volatility_spike_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
