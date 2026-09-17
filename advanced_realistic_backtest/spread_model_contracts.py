# -*- coding: utf-8 -*-
"""Phase 146: Spread Model Contracts.

Defines specifications for bid-ask spread modeling (fixed pips, percentage, historical quotes, volatility-dependent).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

SPREAD_MODELS: List[Dict[str, Any]] = [
    {
        "spread_model_name": "fixed_pip_spread_model",
        "category": "FIXED",
        "description": "Sabit pip veya cent alis-satis araligi sozlesmesi (orn: EUR/USD 1.2 pip, Petrol $0.03).",
        "formula": "spread_in_pips * pip_size",
        "default_value": 1.5,
        "is_dynamic": False,
    },
    {
        "spread_model_name": "percentage_spread_model",
        "category": "PERCENTAGE",
        "description": "Varlik fiyatinin belirli bir yuzdesi kadar alis-satis farki (orn: 0.02%).",
        "formula": "price * (spread_pct / 100.0)",
        "default_value": 0.02,
        "is_dynamic": False,
    },
    {
        "spread_model_name": "historical_quote_spread_model",
        "category": "HISTORICAL",
        "description": "Gecmis gercek quote verisindeki (Ask - Bid) farkinin dogrudan kullanimi.",
        "formula": "ask_quote - bid_quote",
        "default_value": None,
        "is_dynamic": True,
    },
    {
        "spread_model_name": "volatility_dependent_spread_model",
        "category": "DYNAMIC",
        "description": "Yuksek volatilite ve haber donemlerinde genisleyen alis-satis farki modeli.",
        "formula": "base_spread * (1.0 + k * normalized_volatility)",
        "default_value": 2.0,
        "is_dynamic": True,
    },
]


def build_spread_model_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of spread model contracts."""
    rows = []
    for s in SPREAD_MODELS:
        rows.append(
            {
                "spread_model_name": s["spread_model_name"],
                "category": s["category"],
                "description": s["description"],
                "formula": s["formula"],
                "default_value": s["default_value"],
                "is_dynamic": s["is_dynamic"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_spread_model_contracts(df)
    return df, summary


def summarize_spread_model_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize spread model contracts."""
    return {
        "total_spread_models": len(df),
        "zero_spread_assumption_forbidden": True,
        "dynamic_models_supported": bool(df["is_dynamic"].any()) if not df.empty else False,
        "non_signal": True,
    }
