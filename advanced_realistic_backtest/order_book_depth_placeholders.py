# -*- coding: utf-8 -*-
"""Phase 146: Order Book Depth Placeholders.

Defines specifications for L2/L3 order book depth simulation and multi-level fill contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

ORDER_BOOK_DEPTH_MODELS: List[Dict[str, Any]] = [
    {
        "depth_model_name": "l2_depth_ladder_placeholder",
        "description": "5 veya 10 kademeli alis-satis derinlik merdiveni sozlesmesi.",
        "levels_simulated": 5,
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "depth_model_name": "book_liquidity_sweep_placeholder",
        "description": "Buyuk emirlerin kademeleri supurerek gerceklesme agirlikli ortalama fiyati (sweep VWAP) modeli.",
        "levels_simulated": 10,
        "is_placeholder": True,
        "execution_allowed": False,
    },
]


def build_order_book_depth_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of order book depth placeholders."""
    rows = []
    for d in ORDER_BOOK_DEPTH_MODELS:
        rows.append(
            {
                "depth_model_name": d["depth_model_name"],
                "description": d["description"],
                "levels_simulated": d["levels_simulated"],
                "is_placeholder": d["is_placeholder"],
                "execution_allowed": d["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_order_book_depth_placeholders(df)
    return df, summary


def summarize_order_book_depth_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize order book depth placeholders."""
    return {
        "total_depth_models": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "non_signal": True,
    }
