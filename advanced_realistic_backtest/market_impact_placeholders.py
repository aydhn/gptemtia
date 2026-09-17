# -*- coding: utf-8 -*-
"""Phase 146: Market Impact Placeholders.

Defines specifications and formula placeholders for market impact modeling (Almgren-Chriss, square-root law).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

MARKET_IMPACT_MODELS: List[Dict[str, Any]] = [
    {
        "model_name": "square_root_market_impact_placeholder",
        "description": "Emir boyutunun gunluk hacme oraninin karekoku ile olceklenen standart piyasa etki kurali.",
        "formula_placeholder": "Y * sigma * sqrt(order_size / ADV)",
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "model_name": "linear_temporary_impact_placeholder",
        "description": "Islem aninda piyasayi gecici olarak iten dogrusal etki modeli.",
        "formula_placeholder": "eta * (order_size / bar_volume)",
        "is_placeholder": True,
        "execution_allowed": False,
    },
]


def build_market_impact_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of market impact placeholders."""
    rows = []
    for m in MARKET_IMPACT_MODELS:
        rows.append(
            {
                "model_name": m["model_name"],
                "description": m["description"],
                "formula_placeholder": m["formula_placeholder"],
                "is_placeholder": m["is_placeholder"],
                "execution_allowed": m["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_market_impact_placeholders(df)
    return df, summary


def summarize_market_impact_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize market impact placeholders."""
    return {
        "total_impact_models": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "all_execution_blocked": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
    }
