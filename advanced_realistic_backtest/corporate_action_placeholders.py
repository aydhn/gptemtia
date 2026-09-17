# -*- coding: utf-8 -*-
"""Phase 146: Corporate Action Placeholders.

Defines specifications for dividends, splits, and futures contract rolls.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

CORPORATE_ACTIONS: List[Dict[str, Any]] = [
    {
        "action_type": "dividend_adjustment_placeholder",
        "description": "Temettu odemelerinde spot ve vadeli fiyatin duzeltilmesi yer tutucusu.",
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "action_type": "futures_roll_adjustment_placeholder",
        "description": "Vadesi dolan emtia/fx vadeli kontratlarinin sonraki vadeye tasinma (roll) maliyeti yer tutucusu.",
        "is_placeholder": True,
        "execution_allowed": False,
    },
]


def build_corporate_action_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of corporate action placeholders."""
    rows = []
    for a in CORPORATE_ACTIONS:
        rows.append(
            {
                "action_type": a["action_type"],
                "description": a["description"],
                "is_placeholder": a["is_placeholder"],
                "execution_allowed": a["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_corporate_action_placeholders(df)
    return df, summary


def summarize_corporate_action_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize corporate action placeholders."""
    return {
        "total_corporate_actions": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "non_signal": True,
    }
