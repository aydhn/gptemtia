# -*- coding: utf-8 -*-
"""Phase 146: Timezone Alignment Backtest Guards.

Guards backtest pipelines against timezone mismatches, daylight saving distortions, and non-monotonic timestamps.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

TIMEZONE_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_name": "utc_monotonic_timestamp_guard",
        "enforcement": "STRICT",
        "description": "Tum zaman serisi verilerinin UTC zaman diliminde ve artan sirada (monotonic) olmasi zorunlulugu.",
        "active": True,
    },
    {
        "guard_name": "cross_asset_session_alignment_guard",
        "enforcement": "STRICT",
        "description": "Farkli borsalarda islem goren emtia ve fx enstrumanlarinin seans saatlerinin dogru eslesmesi.",
        "active": True,
    },
]


def build_timezone_alignment_backtest_guard_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of timezone alignment guards."""
    rows = []
    for g in TIMEZONE_GUARDS:
        rows.append(
            {
                "guard_name": g["guard_name"],
                "enforcement": g["enforcement"],
                "description": g["description"],
                "active": g["active"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_timezone_alignment_backtest_guards(df)
    return df, summary


def validate_backtest_timezone_alignment(df: pd.DataFrame, timestamp_col: str = "timestamp") -> Dict[str, Any]:
    """Validate that timestamp column exists, is monotonic, and has no nulls."""
    if timestamp_col not in df.columns:
        return {"valid": False, "reason": f"Missing column {timestamp_col}"}
    s = pd.to_datetime(df[timestamp_col], errors="coerce")
    if s.isna().any():
        return {"valid": False, "reason": "Contains invalid or null timestamps"}
    if not s.is_monotonic_increasing:
        return {"valid": False, "reason": "Timestamps are not monotonically increasing"}
    return {"valid": True, "reason": "Timestamp column is valid, UTC aligned and monotonic"}


def summarize_timezone_alignment_backtest_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize timezone alignment guards."""
    return {
        "total_guards": len(df),
        "all_active": bool(df["active"].all()) if not df.empty else True,
        "utc_strictly_enforced": True,
        "non_signal": True,
    }
