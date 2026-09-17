# -*- coding: utf-8 -*-
"""Phase 156: Master Portfolio Scenario Testing Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_SCENARIO_TESTING_CONTRACTS = [
    {
        "contract_id": "SCN-CON-156-001",
        "scenario_type": "HISTORICAL_CRISIS",
        "name": "Historical Crisis Stress Simulation Contract",
        "description": "GFC 2008 ve COVID 2020 gibi gecmis kriz donemleri sok sozlesmesi",
        "shock_scope": "CROSS_ASSET",
        "severity_level": "EXTREME",
        "target_asset_classes": ["COMMODITIES", "FX"],
        "offline_simulation_hook": "stubs.historical_crisis_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-002",
        "scenario_type": "HYPOTHETICAL_SHOCK",
        "name": "Hypothetical Multi-Asset Shock Contract",
        "description": "Hipotetik stagflasyon ve emtia arz soklari sozlesmesi",
        "shock_scope": "MULTI_FACTOR",
        "severity_level": "HIGH",
        "target_asset_classes": ["COMMODITIES", "FX"],
        "offline_simulation_hook": "stubs.hypothetical_shock_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-003",
        "scenario_type": "REGIME_SHIFT",
        "name": "Regime Shift Shock Contract",
        "description": "Ani rejim degisimi ve volatilite gecis sok sozlesmesi",
        "shock_scope": "REGIME_MATRIX",
        "severity_level": "HIGH",
        "target_asset_classes": ["COMMODITIES", "FX"],
        "offline_simulation_hook": "stubs.regime_shift_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-004",
        "scenario_type": "VOLATILITY_SPIKE",
        "name": "Volatility Spike Shock Contract",
        "description": "Ani ima edilen ve gerceklesen volatilite patlamasi sozlesmesi",
        "shock_scope": "VOLATILITY_SURGE",
        "severity_level": "HIGH",
        "target_asset_classes": ["COMMODITIES", "FX"],
        "offline_simulation_hook": "stubs.volatility_spike_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-005",
        "scenario_type": "LIQUIDITY_CRUNCH",
        "name": "Liquidity Crunch Shock Contract",
        "description": "Derinlik kaybi ve alis-satis makas genislemesi sozlesmesi",
        "shock_scope": "LIQUIDITY_DEPTH",
        "severity_level": "CRITICAL",
        "target_asset_classes": ["COMMODITIES", "FX"],
        "offline_simulation_hook": "stubs.liquidity_crunch_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-006",
        "scenario_type": "CORRELATION_BREAKDOWN",
        "name": "Correlation Breakdown Contract",
        "description": "Varliklar arasi korelasyon yapisi kirilmasi sozlesmesi",
        "shock_scope": "CORRELATION_MATRIX",
        "severity_level": "HIGH",
        "target_asset_classes": ["COMMODITIES", "FX"],
        "offline_simulation_hook": "stubs.correlation_breakdown_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-007",
        "scenario_type": "CURRENCY_SHOCK",
        "name": "Currency Devaluation Shock Contract",
        "description": "USD veya yerel para biriminde ani devaluasyon sozlesmesi",
        "shock_scope": "FX_CROSS",
        "severity_level": "HIGH",
        "target_asset_classes": ["FX"],
        "offline_simulation_hook": "stubs.currency_shock_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-008",
        "scenario_type": "SPREAD_WIDENING",
        "name": "Spread Widening Shock Contract",
        "description": "Fiziki/vadeli veya vadeler arasi spread acilmasi sozlesmesi",
        "shock_scope": "SPREAD",
        "severity_level": "MEDIUM",
        "target_asset_classes": ["COMMODITIES"],
        "offline_simulation_hook": "stubs.spread_widening_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-009",
        "scenario_type": "TRANSACTION_COST_SHOCK",
        "name": "Transaction Cost Escalation Contract",
        "description": "Borsa komisyon, finansman ve marjin maliyeti artisi sozlesmesi",
        "shock_scope": "COST_FACTORS",
        "severity_level": "MEDIUM",
        "target_asset_classes": ["COMMODITIES", "FX"],
        "offline_simulation_hook": "stubs.transaction_cost_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "SCN-CON-156-010",
        "scenario_type": "SLIPPAGE_SHOCK",
        "name": "Execution Slippage Shock Contract",
        "description": "Yuksek volatilitede asiri kayma ve gecikme sok sozlesmesi",
        "shock_scope": "EXECUTION_SLIPPAGE",
        "severity_level": "HIGH",
        "target_asset_classes": ["COMMODITIES", "FX"],
        "offline_simulation_hook": "stubs.slippage_shock_stub",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_portfolio_scenario_testing_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for scenario testing contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_SCENARIO_TESTING_CONTRACTS)
    summary = {
        "total_contracts": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
        "status": "SCENARIO_TESTING_CONTRACT_READY",
    }
    return df, summary
