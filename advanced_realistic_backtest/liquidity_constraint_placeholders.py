# -*- coding: utf-8 -*-
"""Phase 146: Liquidity Constraint Placeholders.

Defines specifications for liquidity and volume participation constraints in backtest simulations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

LIQUIDITY_CONSTRAINTS: List[Dict[str, Any]] = [
    {
        "constraint_name": "bar_volume_cap_placeholder",
        "description": "Tek bir bar icinde gerceklesebilecek maksimum hacim orani (%10 max participation).",
        "max_participation_rate": 0.10,
        "is_placeholder": True,
        "execution_allowed": False,
    },
    {
        "constraint_name": "adv_threshold_placeholder",
        "description": "Ortalama gunluk hacmi belirli bir sinirin altinda olan illikit enstrumanlarda islem kisiti.",
        "min_adv_usd": 1000000.0,
        "is_placeholder": True,
        "execution_allowed": False,
    },
]


def build_liquidity_constraint_placeholder_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of liquidity constraint placeholders."""
    rows = []
    for c in LIQUIDITY_CONSTRAINTS:
        rows.append(
            {
                "constraint_name": c["constraint_name"],
                "description": c["description"],
                "is_placeholder": c["is_placeholder"],
                "execution_allowed": c["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_liquidity_constraint_placeholders(df)
    return df, summary


def summarize_liquidity_constraint_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize liquidity constraint placeholders."""
    return {
        "total_liquidity_constraints": len(df),
        "infinite_liquidity_assumption_forbidden": True,
        "all_placeholders": bool(df["is_placeholder"].all()) if not df.empty else True,
        "non_signal": True,
    }
