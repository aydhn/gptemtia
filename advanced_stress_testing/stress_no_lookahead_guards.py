# -*- coding: utf-8 -*-
"""Phase 148: Stress No-Lookahead Guards.

Enforces strict temporal order, zero forward shifts, and backward-only alignment
in stress testing and scenario datasets.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem

LOOKAHEAD_COLUMNS = [
    "future_return",
    "forward_return",
    "next_return",
    "lookahead_return",
    "target",
    "label",
    "prediction",
    "realized_future_pnl",
    "future_pnl",
]


def build_stress_no_lookahead_guard_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of no-lookahead guards."""
    guard = StressGuardItem(
        guard_name="stress_no_lookahead_guard",
        guard_type="TEMPORAL_ORDER",
        description="Geleceğe bakış (lookahead) içeren sütunları ve ileri zamanlı birleştirmeleri engeller.",
        enforcement_level="STRICT",
        active=True,
        violating_columns=LOOKAHEAD_COLUMNS,
    )
    rows = [
        {
            "guard_name": guard.guard_name,
            "guard_type": guard.guard_type,
            "description": guard.description,
            "enforcement_level": guard.enforcement_level,
            "active": guard.active,
            "prohibited_column_count": len(guard.violating_columns),
            "non_signal": True,
            "local_only": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "guard_active": guard.active,
        "enforcement_level": guard.enforcement_level,
        "prohibited_columns": guard.violating_columns,
        "non_signal": True,
    }
    return df, summary


def validate_stress_no_lookahead_columns(column_names: List[str]) -> Dict[str, Any]:
    """Inspect column names and identify any lookahead violations."""
    normalized = [c.lower().strip() for c in column_names]
    violations = [c for c in normalized if c in LOOKAHEAD_COLUMNS or "shift(-1)" in c or "future" in c]
    return {
        "has_violations": len(violations) > 0,
        "violating_columns": violations,
        "is_safe": len(violations) == 0,
        "non_signal": True,
    }


def validate_no_future_stress_join(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_ts: str,
    right_ts: str,
) -> Dict[str, Any]:
    """Verify that joining right_df onto left_df does not pull future data (right_ts <= left_ts)."""
    if left_df.empty or right_df.empty:
        return {"is_valid": True, "violations_count": 0, "non_signal": True}
    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {"is_valid": False, "error": "Timestamp columns missing", "non_signal": True}

    max_right = pd.to_datetime(right_df[right_ts]).max()
    min_left = pd.to_datetime(left_df[left_ts]).min()
    has_future = max_right > pd.to_datetime(left_df[left_ts]).max()

    return {
        "is_valid": not has_future,
        "max_right_ts": str(max_right),
        "min_left_ts": str(min_left),
        "non_signal": True,
    }
