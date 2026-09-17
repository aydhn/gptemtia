# -*- coding: utf-8 -*-
"""Phase 146: Transaction Cost Models.

Defines master aggregation specifications for total transaction cost models.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

TRANSACTION_COST_MODELS: List[Dict[str, Any]] = [
    {
        "cost_model_name": "standard_realistic_cost_model",
        "description": "Komisyon, borsa ucreti, alis-satis farki ve kaymayi toplayan standart maliyet modeli.",
        "aggregation_formula": "commission + exchange_fee + spread_cost + slippage_cost",
        "real_cost_calculated": False,
        "broker_connected": False,
        "execution_allowed": False,
    },
    {
        "cost_model_name": "institutional_market_impact_cost_model",
        "description": "Standart maliyetlere ek olarak buyuk emirler icin piyasa etki maliyetini toplayan kurumsal model.",
        "aggregation_formula": "commission + fee + spread_cost + slippage_cost + market_impact",
        "real_cost_calculated": False,
        "broker_connected": False,
        "execution_allowed": False,
    },
    {
        "cost_model_name": "leveraged_holding_cost_model",
        "description": "Gunici maliyetlere ek olarak gecelik tasima ve borclanma maliyetlerini iceren sozlesme.",
        "aggregation_formula": "standard_cost + borrow_fee + funding_fee",
        "real_cost_calculated": False,
        "broker_connected": False,
        "execution_allowed": False,
    },
]


def build_transaction_cost_model_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of master transaction cost models."""
    rows = []
    for m in TRANSACTION_COST_MODELS:
        rows.append(
            {
                "cost_model_name": m["cost_model_name"],
                "description": m["description"],
                "aggregation_formula": m["aggregation_formula"],
                "real_cost_calculated": m["real_cost_calculated"],
                "broker_connected": m["broker_connected"],
                "execution_allowed": m["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_transaction_cost_models(df)
    return df, summary


def summarize_transaction_cost_models(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize transaction cost model registry."""
    return {
        "total_cost_models": len(df),
        "all_real_calculation_blocked": bool((~df["real_cost_calculated"]).all()) if not df.empty else True,
        "all_broker_connections_blocked": bool((~df["broker_connected"]).all()) if not df.empty else True,
        "non_signal": True,
    }
