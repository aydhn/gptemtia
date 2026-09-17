# -*- coding: utf-8 -*-
"""Phase 146: Rejected Order Placeholders.

Defines specifications for conditions leading to simulated order rejection.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

REJECTION_CONDITIONS: List[Dict[str, Any]] = [
    {
        "condition_name": "insufficient_margin_rejection",
        "reason": "Serbest teminatin (free margin) emir teminat gereksinimini karsilamamasi.",
        "action": "ORDER_REJECTED",
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "condition_name": "market_closed_rejection",
        "reason": "Piyasa seans saatleri disinda veya tatil gununde iletilen piyasa emri.",
        "action": "ORDER_REJECTED",
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "condition_name": "price_band_limit_rejection",
        "reason": "Fiyatin gunluk tavan/taban limitlerine takilmasi veya volatilite durdurucusu (circuit breaker).",
        "action": "ORDER_REJECTED",
        "is_placeholder": True,
        "execution_allowed": False,
    },
]


def build_rejected_order_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of rejected order placeholders."""
    rows = []
    for c in REJECTION_CONDITIONS:
        rows.append(
            {
                "condition_name": c["condition_name"],
                "reason": c["reason"],
                "action": c["action"],
                "is_placeholder": c["is_placeholder"],
                "execution_allowed": c["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_rejected_order_placeholders(df)
    return df, summary


def summarize_rejected_order_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize rejected order placeholders."""
    return {
        "total_rejection_conditions": len(df),
        "rejections_supported": True,
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "non_signal": True,
    }
