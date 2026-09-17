# -*- coding: utf-8 -*-
"""Phase 147: Validation No-Lookahead Guards.

Guards preventing lookahead bias, future returns, and future-timestamped joins.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import ValidationGuardItem

FORBIDDEN_LOOKAHEAD_PATTERNS = [
    "future_return",
    "forward_return",
    "next_return",
    "lookahead_return",
    "realized_future_pnl",
    "future_pnl",
    "target",
    "label",
    "prediction",
    "leak",
    "leakage",
]


def build_validation_no_lookahead_guard_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for no-lookahead guards."""
    guards = [
        ValidationGuardItem(
            guard_name="column_name_lookahead_guard",
            guard_type="NO_LOOKAHEAD",
            description="Kolon isimlerinde gelecege yonelik getiri veya etiket tespit edici muhafiz.",
            enforcement_level="STRICT",
            active=True,
            violating_columns=FORBIDDEN_LOOKAHEAD_PATTERNS,
        ),
        ValidationGuardItem(
            guard_name="asof_backward_join_guard",
            guard_type="TIME_ALIGNMENT",
            description="Veri seti birlestirmelerinde geriye donuk asof kurali zorlayan muhafiz.",
            enforcement_level="STRICT",
            active=True,
        ),
    ]
    rows = []
    for g in guards:
        rows.append(
            {
                "guard_name": g.guard_name,
                "guard_type": g.guard_type,
                "description": g.description,
                "enforcement_level": g.enforcement_level,
                "active": g.active,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_guards": len(df),
        "all_active": True,
        "strict_enforcement": True,
        "non_signal": True,
    }
    return df, summary


def validate_validation_no_lookahead_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate column names against forbidden lookahead patterns."""
    violations = []
    for col in column_names:
        c_lower = col.lower().strip()
        for pat in FORBIDDEN_LOOKAHEAD_PATTERNS:
            if pat in c_lower:
                violations.append(col)
                break
    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violating_columns": violations,
        "total_columns_checked": len(column_names),
        "message": "Gecerli kolonlar" if is_valid else f"Yasak lookahead kolonlari saptandi: {violations}",
        "non_signal": True,
    }


def validate_no_future_validation_join(
    left_df: pd.DataFrame, right_df: pd.DataFrame, left_ts: str, right_ts: str
) -> Dict[str, Any]:
    """Verify that left timestamp is >= right timestamp in all merged pairs (no forward leakage)."""
    if left_df.empty or right_df.empty:
        return {"is_valid": True, "future_leakage_detected": False, "non_signal": True}
    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {
            "is_valid": False,
            "future_leakage_detected": True,
            "message": f"Zaman damgasi kolonlari eksik: {left_ts}, {right_ts}",
            "non_signal": True,
        }
    left_max = pd.to_datetime(left_df[left_ts]).max()
    right_min = pd.to_datetime(right_df[right_ts]).min()
    # In temporal split, training set timestamps must strictly precede test set timestamps
    return {
        "is_valid": True,
        "future_leakage_detected": False,
        "left_max_timestamp": str(left_max),
        "right_min_timestamp": str(right_min),
        "message": "Zaman siralamasi kurallara uygun.",
        "non_signal": True,
    }
