# -*- coding: utf-8 -*-
"""Phase 146: Partial Fill Placeholders.

Defines specifications for handling partial execution of large orders.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

PARTIAL_FILL_RULES: List[Dict[str, Any]] = [
    {
        "rule_name": "volume_limit_partial_fill_placeholder",
        "description": "Emir hacmi bar hacminin %10'undan buyukse ilk bar yalnizca %10 doldurulur.",
        "behavior": "FILL_PORTION_AND_LEAVE_REST",
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "rule_name": "fill_or_kill_rejection_placeholder",
        "description": "FOK tipi emirlerde tam dolum saglanamazsa emrin tamamen iptal edilmesi kurali.",
        "behavior": "REJECT_IF_NOT_FULL",
        "is_placeholder": True,
        "execution_allowed": False,
    },
]


def build_partial_fill_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of partial fill placeholders."""
    rows = []
    for r in PARTIAL_FILL_RULES:
        rows.append(
            {
                "rule_name": r["rule_name"],
                "description": r["description"],
                "behavior": r["behavior"],
                "is_placeholder": r["is_placeholder"],
                "execution_allowed": r["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_partial_fill_placeholders(df)
    return df, summary


def summarize_partial_fill_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize partial fill placeholders."""
    return {
        "total_partial_fill_rules": len(df),
        "partial_fill_possible": True,
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "non_signal": True,
    }
