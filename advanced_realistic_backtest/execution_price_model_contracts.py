# -*- coding: utf-8 -*-
"""Phase 146: Execution Price Model Contracts.

Defines specifications for determining trade execution price based on order side, quote, and spread.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

PRICE_MODELS: List[Dict[str, Any]] = [
    {
        "price_model_name": "bid_ask_quote_model",
        "description": "Alis islemleri Ask, satis islemleri Bid uzerinden gerceklesir. Sifir maliyetli orta fiyat kullanilmaz.",
        "buy_formula": "ask_price + slippage",
        "sell_formula": "bid_price - slippage",
        "requires_quotes": True,
    },
    {
        "price_model_name": "mid_price_with_half_spread_model",
        "description": "Quote verisi yoksa Mid fiyata yarim spread ve kayma eklenerek hesaplanir.",
        "buy_formula": "mid_price + (spread / 2) + slippage",
        "sell_formula": "mid_price - (spread / 2) - slippage",
        "requires_quotes": False,
    },
    {
        "price_model_name": "next_open_price_model",
        "description": "Bar seviyesinde bir sonraki barin acilis fiyatina spread ve kayma payi eklenir.",
        "buy_formula": "open_next + (spread / 2) + slippage",
        "sell_formula": "open_next - (spread / 2) - slippage",
        "requires_quotes": False,
    },
]


def build_execution_price_model_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of execution price model contracts."""
    rows = []
    for m in PRICE_MODELS:
        rows.append(
            {
                "price_model_name": m["price_model_name"],
                "description": m["description"],
                "buy_formula": m["buy_formula"],
                "sell_formula": m["sell_formula"],
                "requires_quotes": m["requires_quotes"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_execution_price_model_contracts(df)
    return df, summary


def summarize_execution_price_model_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize execution price model contracts."""
    return {
        "total_price_models": len(df),
        "mid_only_forbidden": True,
        "spread_and_slippage_included": True,
        "non_signal": True,
    }
