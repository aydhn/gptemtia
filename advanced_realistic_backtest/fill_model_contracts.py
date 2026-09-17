# -*- coding: utf-8 -*-
"""Phase 146: Fill Model Contracts.

Defines specifications for order fill mechanics (next bar open, next tick, VWAP, participation-capped).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

FILL_MODELS: List[Dict[str, Any]] = [
    {
        "fill_model_name": "next_bar_open_fill_model",
        "category": "BAR_LEVEL",
        "description": "Sinyal uretildikten sonraki ilk barin acilis fiyatinda gerceklesme sozlesmesi.",
        "assumes_instant_fill": False,
        "spread_applied": True,
        "slippage_applied": True,
    },
    {
        "fill_model_name": "next_tick_fill_model",
        "category": "TICK_LEVEL",
        "description": "Zaman damgali emir gonderiminden sonra gelen ilk gercek tick verisinde gerceklesme.",
        "assumes_instant_fill": False,
        "spread_applied": True,
        "slippage_applied": True,
    },
    {
        "fill_model_name": "vwap_slice_fill_model",
        "category": "EXECUTION_ALGO",
        "description": "Belirli bir zaman penceresi boyunca hacim agirlikli ortalama fiyata gore dilimleme.",
        "assumes_instant_fill": False,
        "spread_applied": True,
        "slippage_applied": True,
    },
    {
        "fill_model_name": "participation_capped_fill_model",
        "category": "LIQUIDITY_AWARE",
        "description": "Piyasa hacminin maksimum %10'u kadar tek seferde gerceklesme, kalani bekletme.",
        "assumes_instant_fill": False,
        "spread_applied": True,
        "slippage_applied": True,
    },
]


def build_fill_model_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of fill model contracts."""
    rows = []
    for m in FILL_MODELS:
        rows.append(
            {
                "fill_model_name": m["fill_model_name"],
                "category": m["category"],
                "description": m["description"],
                "assumes_instant_fill": m["assumes_instant_fill"],
                "spread_applied": m["spread_applied"],
                "slippage_applied": m["slippage_applied"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_fill_model_contracts(df)
    return df, summary


def summarize_fill_model_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize fill model contracts."""
    return {
        "total_fill_models": len(df),
        "zero_instant_fill_assumed": bool((~df["assumes_instant_fill"]).all()) if not df.empty else True,
        "spread_always_applied": bool(df["spread_applied"].all()) if not df.empty else True,
        "slippage_always_applied": bool(df["slippage_applied"].all()) if not df.empty else True,
        "non_signal": True,
    }
