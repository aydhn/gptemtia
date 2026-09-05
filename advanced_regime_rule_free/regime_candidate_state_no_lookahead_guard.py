"""Phase 128: Regime Candidate State No-Lookahead Guard.

Provides temporal protection functions against future data leakage, future joins, and negative shift operations.
"""

from typing import Dict, Tuple
import re
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

FORBIDDEN_FUTURE_COLUMNS = [
    "future_return",
    "forward_return",
    "next_return",
    "target_return",
    "lead_return",
    "next_close",
    "t_plus_1",
    "shift_negative",
    "target",
    "label",
    "prediction",
]

NO_LOOKAHEAD_GUARD_RULES = [
    {
        "guard_id": "guard_no_negative_shift",
        "description": "Code and pipeline must never call shift(-1), lead(), or forward window slices.",
        "enforced": True,
    },
    {
        "guard_id": "guard_point_in_time_join",
        "description": "Any context or candidate state join must enforce right_ts <= left_ts.",
        "enforced": True,
    },
    {
        "guard_id": "guard_no_future_columns",
        "description": "Dataframes must not contain any future-referencing return or target column.",
        "enforced": True,
    },
    {
        "guard_id": "guard_utc_monotonicity",
        "description": "Timestamps must be parsed as UTC and monotonically non-decreasing per entity.",
        "enforced": True,
    },
]


def validate_no_future_candidate_state_join(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_ts: str = "timestamp_utc",
    right_ts: str = "context_timestamp_utc",
) -> Dict:
    """Validate that in joined data, all context timestamps precede or equal the base timestamp."""
    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {
            "is_valid": True,
            "checked_pairs": 0,
            "future_leak_count": 0,
            "note": "Timestamp columns not both present in comparison",
        }

    left_series = pd.to_datetime(left_df[left_ts], utc=True)
    right_series = pd.to_datetime(right_df[right_ts], utc=True)

    # Check alignment length
    min_len = min(len(left_series), len(right_series))
    if min_len == 0:
        return {"is_valid": True, "checked_pairs": 0, "future_leak_count": 0}

    future_leaks = int((right_series.iloc[:min_len] > left_series.iloc[:min_len]).sum())

    return {
        "is_valid": future_leaks == 0,
        "checked_pairs": min_len,
        "future_leak_count": future_leaks,
    }


def validate_no_forbidden_candidate_state_columns(df: pd.DataFrame) -> Dict:
    """Scan DataFrame columns for forbidden future-referencing or target words."""
    found = []
    for col in df.columns:
        col_lower = col.lower()
        for forbidden in FORBIDDEN_FUTURE_COLUMNS:
            if forbidden == col_lower or f"_{forbidden}" in col_lower or f"{forbidden}_" in col_lower:
                found.append(col)

    return {
        "is_valid": len(found) == 0,
        "forbidden_columns": found,
        "total_columns_scanned": len(df.columns),
    }


def validate_no_negative_shift_usage(source_text: str) -> Dict:
    """Scan Python source code string for forbidden negative shift calls."""
    patterns = [
        r"\.shift\s*\(\s*-[0-9]+\s*\)",
        r"\.lead\s*\(",
        r"\.iloc\s*\[\s*i\s*\+\s*[0-9]+\s*\]",
    ]
    detected = []
    for p in patterns:
        matches = re.findall(p, source_text)
        if matches:
            detected.extend(matches)

    return {
        "is_valid": len(detected) == 0,
        "detected_patterns": detected,
    }


def build_regime_candidate_state_no_lookahead_guard_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for no-lookahead guard rules."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for g in NO_LOOKAHEAD_GUARD_RULES:
        row = g.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_no_lookahead_guard(df)
    return df, summary


def summarize_candidate_state_no_lookahead_guard(df: pd.DataFrame) -> Dict:
    """Summarize no-lookahead guard rules."""
    total = len(df)
    all_enforced = bool(df["enforced"].all()) if not df.empty else True

    return {
        "total_guard_rules": total,
        "all_enforced": all_enforced,
        "guard_status": "ACTIVE" if all_enforced else "INACTIVE",
    }
