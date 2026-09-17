# -*- coding: utf-8 -*-
"""Phase 146: Transaction Cost Components.

Defines specifications for individual cost components (commission, fee, spread, slippage, impact, borrow, funding).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

COST_COMPONENTS: List[Dict[str, Any]] = [
    {
        "component_name": "commission",
        "category": "DIRECT_BROKER_FEE",
        "description": "Araci kurum komisyon bedeli.",
        "is_placeholder": False,
        "calculation_required_in_real_backtest": True,
    },
    {
        "component_name": "exchange_fee",
        "category": "EXCHANGE_TARIFF",
        "description": "Borsa tescil ve takas ucreti.",
        "is_placeholder": False,
        "calculation_required_in_real_backtest": True,
    },
    {
        "component_name": "spread_cost",
        "category": "MARKET_STRUCTURE_COST",
        "description": "Alis-satis makas maliyeti.",
        "is_placeholder": False,
        "calculation_required_in_real_backtest": True,
    },
    {
        "component_name": "slippage_cost",
        "category": "EXECUTION_FRICTION",
        "description": "Beklenen fiyat ile gerceklesen fiyat arasindaki olumsuz fark.",
        "is_placeholder": False,
        "calculation_required_in_real_backtest": True,
    },
    {
        "component_name": "market_impact_placeholder",
        "category": "MICROSTRUCTURE_IMPACT",
        "description": "Buyuk emirlerin piyasa defterinde yarattigi olumsuz kayma etkisi yer tutucusu.",
        "is_placeholder": True,
        "calculation_required_in_real_backtest": False,
    },
    {
        "component_name": "borrow_fee_placeholder",
        "category": "FINANCING_COST",
        "description": "Aciga satis (short) pozisyonlar icin menkul kiymet odunc alma maliyeti yer tutucusu.",
        "is_placeholder": True,
        "calculation_required_in_real_backtest": False,
    },
    {
        "component_name": "funding_fee_placeholder",
        "category": "FINANCING_COST",
        "description": "Kaldracli pozisyonlar icin gecelik fonlama ve swap faizi yer tutucusu.",
        "is_placeholder": True,
        "calculation_required_in_real_backtest": False,
    },
    {
        "component_name": "currency_conversion_cost_placeholder",
        "category": "FX_CONVERSION",
        "description": "Farkli para birimindeki enstrumanlarin portfoy ana para birimine cevrilme masrafi yer tutucusu.",
        "is_placeholder": True,
        "calculation_required_in_real_backtest": False,
    },
]


def build_transaction_cost_component_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of transaction cost components."""
    rows = []
    for c in COST_COMPONENTS:
        rows.append(
            {
                "component_name": c["component_name"],
                "category": c["category"],
                "description": c["description"],
                "is_placeholder": c["is_placeholder"],
                "calculation_required_in_real_backtest": c["calculation_required_in_real_backtest"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_transaction_cost_components(df)
    return df, summary


def summarize_transaction_cost_components(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize transaction cost components."""
    return {
        "total_components": len(df),
        "core_components_count": int((~df["is_placeholder"]).sum()) if not df.empty else 0,
        "placeholder_components_count": int(df["is_placeholder"].sum()) if not df.empty else 0,
        "non_signal": True,
    }
