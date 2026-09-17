# -*- coding: utf-8 -*-
"""Phase 156: Hypothetical Portfolio Scenario Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_HYPOTHETICAL_SCENARIOS = [
    {
        "scenario_id": "HYPO-SCN-001",
        "scenario_title": "Severe Stagflation Multi-Asset Shock",
        "rationale": "Durgunluk ve yuksek enflasyonun ayni anda gelismesi",
        "shock_vector": "Emtia +30%, Buyume duyarliligi -25%, FX volatilite 2.5x",
        "extreme_tail_probability": "1_IN_50_YEARS",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "HYPO-SCN-002",
        "scenario_title": "Commodity Supply Chain Freeze",
        "rationale": "Kritik deniz gecitlerinde tikanma ve lojistik durma",
        "shock_vector": "Navlun +200%, Enerji +45%, Tarim +35%",
        "extreme_tail_probability": "1_IN_25_YEARS",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "HYPO-SCN-003",
        "scenario_title": "Sudden Global Dollar Shortage",
        "rationale": "Bankalararasi USD likidite krizinin bas gostermesi",
        "shock_vector": "DXY +15%, Gelismekte olan FX -20%, Emtia -18%",
        "extreme_tail_probability": "1_IN_20_YEARS",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "scenario_id": "HYPO-SCN-004",
        "scenario_title": "Coordinated Central Bank Tightening Shock",
        "rationale": "Beklenmedik 150 bps eszamanli faiz artisi",
        "shock_vector": "Tahvil getirileri +120 bps, Emtia -22%, Volatilite +80%",
        "extreme_tail_probability": "1_IN_30_YEARS",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_hypothetical_portfolio_scenario_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for hypothetical scenario contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_HYPOTHETICAL_SCENARIOS)
    summary = {
        "total_hypothetical_scenarios": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
