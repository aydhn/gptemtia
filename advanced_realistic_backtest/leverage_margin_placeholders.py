# -*- coding: utf-8 -*-
"""Phase 146: Leverage & Margin Placeholders.

Defines specifications for leverage multipliers, initial margin, and maintenance margin placeholders.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

MARGIN_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "margin_type": "initial_margin_placeholder",
        "description": "Yeni bir pozisyon acilabilmesi icin gereken asgari teminat orani.",
        "nominal_rate": 0.10,
        "is_placeholder": True,
    },
    {
        "margin_type": "maintenance_margin_placeholder",
        "description": "Pozisyonun tasinabilmesi icin gereken surdurme teminati orani.",
        "nominal_rate": 0.05,
        "is_placeholder": True,
    },
    {
        "margin_type": "margin_call_liquidation_placeholder",
        "description": "Teminatin surdurme sinirinin altina inmesi durumunda otomatik tasfiye kurali.",
        "nominal_rate": 0.03,
        "is_placeholder": True,
    },
]


def build_leverage_margin_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of leverage and margin placeholders."""
    rows = []
    for m in MARGIN_PLACEHOLDERS:
        rows.append(
            {
                "margin_type": m["margin_type"],
                "description": m["description"],
                "nominal_rate": m["nominal_rate"],
                "is_placeholder": m["is_placeholder"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_leverage_margin_placeholders(df)
    return df, summary


def summarize_leverage_margin_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize leverage and margin placeholders."""
    return {
        "total_margin_types": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "non_signal": True,
    }
