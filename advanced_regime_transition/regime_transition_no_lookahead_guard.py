"""Phase 130: Regime Transition No-Lookahead Guard.

Strict validation guards preventing forward return leakages, forbidden signal/label
columns, full text/HTML scraping, and negative shift operations.
"""

from typing import Any, Dict, List, Optional, Tuple
import re
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

FORBIDDEN_TRANSITION_COLUMNS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "embedding",
    "vector",
]

GUARD_RULES: List[Dict[str, Any]] = [
    {
        "guard_key": "guard_no_forbidden_columns",
        "description": "Block tables containing signals, labels, predictions, or raw scraping text",
        "enforcement": "strict_blocking",
        "target_type": "dataframe_schema",
    },
    {
        "guard_key": "guard_no_future_joins",
        "description": "Ensure joined auxiliary datasets do not contain timestamps ahead of base observation",
        "enforcement": "strict_blocking",
        "target_type": "join_operation",
    },
    {
        "guard_key": "guard_no_negative_shift",
        "description": "Block usage of shift(-1) or lookahead window operators in transition routines",
        "enforcement": "strict_blocking",
        "target_type": "code_inspection",
    },
]


def build_regime_transition_no_lookahead_guard_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build guard registry dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(GUARD_RULES)
    summary = summarize_transition_no_lookahead_guard(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def validate_no_future_transition_join(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_ts: str = "timestamp_utc",
    right_ts: str = "timestamp_utc",
) -> Dict[str, Any]:
    """Validate that right_df has no timestamps exceeding left_df when joined."""
    if left_df.empty or right_df.empty:
        return {"is_valid": True, "violations": 0}

    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {"is_valid": False, "error": f"Timestamp columns {left_ts} or {right_ts} missing"}

    max_left = pd.to_datetime(left_df[left_ts]).max()
    future_rows = right_df[pd.to_datetime(right_df[right_ts]) > max_left]
    violations = len(future_rows)

    return {
        "is_valid": violations == 0,
        "violations": violations,
        "max_left_timestamp": str(max_left),
    }


def validate_no_forbidden_transition_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate that dataframe contains zero forbidden signal, label, or scraping columns."""
    found = []
    for col in df.columns:
        col_lower = str(col).lower()
        for forbidden in FORBIDDEN_TRANSITION_COLUMNS:
            if forbidden in col_lower:
                found.append(col)
                break

    return {
        "is_valid": len(found) == 0,
        "forbidden_columns_found": found,
        "total_columns": len(df.columns),
    }


def validate_no_negative_shift_usage(source_text: str) -> Dict[str, Any]:
    """Inspect code text to ensure negative shift lookaheads like shift(-1) are absent."""
    pattern = r"\.shift\s*\(\s*-[1-9]\d*\s*\)"
    matches = re.findall(pattern, source_text)

    return {
        "is_valid": len(matches) == 0,
        "negative_shift_matches": matches,
        "violations_count": len(matches),
    }


def summarize_transition_no_lookahead_guard(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no-lookahead guard rules."""
    return {
        "total_guards": len(df),
        "guard_keys": df["guard_key"].tolist() if not df.empty else [],
        "all_strict_blocking": bool((df["enforcement"] == "strict_blocking").all()) if not df.empty else True,
        "forbidden_column_count": len(FORBIDDEN_TRANSITION_COLUMNS),
    }
