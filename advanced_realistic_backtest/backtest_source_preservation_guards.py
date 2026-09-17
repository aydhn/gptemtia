# -*- coding: utf-8 -*-
"""Phase 146: Backtest Source Preservation Guards.

Guards raw historical datasets against overwrite, destructive modification, and silent deletion.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

FORBIDDEN_ACTIONS = [
    "overwrite",
    "delete",
    "destructive_cleaning",
    "auto_imputation",
    "auto_feature_drop",
    "truncate",
    "drop_table",
]


def build_backtest_source_preservation_guard_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of source preservation guards."""
    rules = [
        {
            "guard_name": "immutable_historical_data_guard",
            "enforcement": "STRICT",
            "description": "Ham piyasa verilerinin uzerine yazilmasi veya degistirilmesi kesinlikle engellenir.",
            "forbidden_actions": str(FORBIDDEN_ACTIONS),
            "active": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rules)
    summary = summarize_backtest_source_preservation_guards(df)
    return df, summary


def validate_backtest_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate that requested action is non-destructive."""
    act_lower = action.lower().strip()
    for forbidden in FORBIDDEN_ACTIONS:
        if forbidden in act_lower:
            return {
                "action": action,
                "is_permitted": False,
                "reason": f"Action contains forbidden destructive keyword: {forbidden}",
            }
    return {
        "action": action,
        "is_permitted": True,
        "reason": "Action is non-destructive and source-preserving",
    }


def summarize_backtest_source_preservation_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation guards."""
    return {
        "total_guards": len(df),
        "source_preservation_enforced": True,
        "destructive_actions_blocked": True,
        "non_signal": True,
    }
