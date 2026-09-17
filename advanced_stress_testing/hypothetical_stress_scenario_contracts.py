# -*- coding: utf-8 -*-
"""Phase 148: Hypothetical Stress Scenario Contracts.

Provides specifications and registry for forward-looking hypothetical crisis scenario contracts
(Stagflation 2.0, Shipping Chokepoint Closure, Sovereign Debt Crisis, Trade War Tariff Shock).
Contract and metadata definition only; no actual scenario simulation or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

HYPOTHETICAL_SCENARIOS: List[Dict[str, Any]] = [
    {
        "scenario_name": "hypothetical_stagflation_2_0",
        "scenario_family": "MACRO_STAGFLATION",
        "description": "Küresel Stagflasyon 2.0: Yüksek enflasyon, negatif büyüme, merkez bankası faiz açmazı.",
        "assumed_commodity_drift": "+35%",
        "assumed_fx_volatility": "+60%",
        "assumed_liquidity_drop": "-40%",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "hypothetical_shipping_chokepoint_blockade",
        "scenario_family": "GEOPOLITICAL_LOGISTICS",
        "description": "Kritik Boğaz Kapanması (Hürmüz / Malakka): Enerji ve yük taşımacılığında anlık arz kesintisi.",
        "assumed_commodity_drift": "+50%",
        "assumed_fx_volatility": "+45%",
        "assumed_liquidity_drop": "-30%",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "hypothetical_sovereign_debt_restructuring",
        "scenario_family": "SOVEREIGN_CREDIT",
        "description": "Gelişmekte Olan Ülke Borç Krizi: Sermaye kaçışı, yerel para birimlerinde devalüasyon şoku.",
        "assumed_commodity_drift": "-20%",
        "assumed_fx_volatility": "+80%",
        "assumed_liquidity_drop": "-55%",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "hypothetical_extreme_tariff_retaliation",
        "scenario_family": "GLOBAL_TRADE",
        "description": "Geniş Çaplı Ticaret Savaşı ve Tarife Şoku: Küresel ticaret hacminde ani daralma ve kur manipülasyonu.",
        "assumed_commodity_drift": "-15%",
        "assumed_fx_volatility": "+50%",
        "assumed_liquidity_drop": "-25%",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
    {
        "scenario_name": "hypothetical_clearing_house_outage",
        "scenario_family": "MARKET_INFRASTRUCTURE",
        "description": "Takas Merkezi ve Borsa Altyapı Kesintisi: Çoklu gün mutabakat durması ve teminat çağrısı şoku.",
        "assumed_commodity_drift": "0%",
        "assumed_fx_volatility": "+70%",
        "assumed_liquidity_drop": "-85%",
        "execution_allowed": False,
        "pnl_calculation_allowed": False,
    },
]


def build_hypothetical_stress_scenario_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of hypothetical crisis scenario contracts."""
    rows: List[Dict[str, Any]] = []
    for s in HYPOTHETICAL_SCENARIOS:
        rows.append(
            {
                "scenario_name": s["scenario_name"],
                "scenario_family": s["scenario_family"],
                "description": s["description"],
                "assumed_commodity_drift": s["assumed_commodity_drift"],
                "assumed_fx_volatility": s["assumed_fx_volatility"],
                "assumed_liquidity_drop": s["assumed_liquidity_drop"],
                "execution_allowed": s["execution_allowed"],
                "pnl_calculation_allowed": s["pnl_calculation_allowed"],
                "non_signal": True,
                "local_only": True,
                "manual_review_required": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_hypothetical_scenarios": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_pnl_calculation_blocked": not bool(df["pnl_calculation_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
