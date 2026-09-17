# -*- coding: utf-8 -*-
"""Phase 156: Regime Shift Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_REGIME_SHIFT_SCENARIOS = [
    {
        "scenario_id": "RGM-SCN-001",
        "transition_name": "Low Vol Bull to High Vol Bear Transition",
        "source_regime": "LOW_VOL_BULL",
        "target_regime": "HIGH_VOL_BEAR",
        "volatility_multiplier": 2.8,
        "correlation_shift": "CROSS_ASSET_CORR_UP_TO_0.85",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "RGM-SCN-002",
        "transition_name": "Trending to Sideways Volatile Chop",
        "source_regime": "TRENDING_EXPANSION",
        "target_regime": "CHOPPY_HIGH_VOL",
        "volatility_multiplier": 2.0,
        "correlation_shift": "DECOUPLING_COMMODITY_FX",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_regime_shift_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for regime shift scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_REGIME_SHIFT_SCENARIOS)
    summary = {
        "total_regime_shift_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
