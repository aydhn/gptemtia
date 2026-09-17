# -*- coding: utf-8 -*-
"""Phase 146: Currency Conversion Placeholders.

Defines specifications for multi-currency conversion to portfolio base currency.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

CONVERSION_RULES: List[Dict[str, Any]] = [
    {
        "conversion_rule": "cross_rate_conversion_placeholder",
        "description": "Farkli para birimlerindeki enstruman PnL ve nosyonelinin portfoy temel para birimine (USD) donusturulmesi.",
        "base_currency": "USD",
        "is_placeholder": True,
    },
]


def build_currency_conversion_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of currency conversion placeholders."""
    rows = []
    for c in CONVERSION_RULES:
        rows.append(
            {
                "conversion_rule": c["conversion_rule"],
                "description": c["description"],
                "base_currency": c["base_currency"],
                "is_placeholder": c["is_placeholder"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_currency_conversion_placeholders(df)
    return df, summary


def summarize_currency_conversion_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize currency conversion placeholders."""
    return {
        "total_conversion_rules": len(df),
        "base_currency": "USD",
        "non_signal": True,
    }
