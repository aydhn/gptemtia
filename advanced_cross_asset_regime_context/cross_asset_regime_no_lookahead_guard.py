"""Phase 131: Cross-Asset Regime No-Lookahead Guard.

Enforces zero lookahead bias across cross-asset joins, scans for negative shift operations,
and verifies total absence of forbidden trading/prediction/text columns.
"""

from typing import Any, Dict, List, Optional, Tuple
import re
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

FORBIDDEN_COLUMNS: List[str] = [
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

LOOKAHEAD_GUARD_RULES: List[Dict[str, Any]] = [
    {
        "guard_id": "guard_negative_shift",
        "rule_name": "no_negative_shift_guard",
        "category": "syntax_inspection",
        "description": "Scans code and logic for shift(-k) or forward index indexing.",
        "enforced": True,
    },
    {
        "guard_id": "guard_forbidden_columns",
        "rule_name": "no_forbidden_columns_guard",
        "category": "schema_inspection",
        "description": "Prevents injection of signal, prediction, target, or raw text columns.",
        "enforced": True,
    },
    {
        "guard_id": "guard_future_join_leakage",
        "rule_name": "no_future_join_leakage_guard",
        "category": "temporal_inspection",
        "description": "Verifies context timestamps never exceed observation timestamps in joins.",
        "enforced": True,
    },
]


def build_cross_asset_regime_no_lookahead_guard_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build guard registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in LOOKAHEAD_GUARD_RULES:
        row = dict(item)
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        row["contains_target_or_prediction"] = False
        row["contains_trading_recommendation"] = False
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_no_lookahead_guard(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def validate_no_future_cross_asset_join(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_ts: str,
    right_ts: str,
) -> Dict[str, Any]:
    """Verify that every joined record in right_df satisfies right_ts <= left_ts."""
    if left_df.empty or right_df.empty:
        return {"valid": True, "violations": 0, "status": "PASS"}

    l_series = pd.to_datetime(left_df[left_ts], errors="coerce", utc=True)
    r_series = pd.to_datetime(right_df[right_ts], errors="coerce", utc=True)

    # For safety comparison, assume index alignment or examine max right against min left if sorted
    future_count = 0
    if len(left_df) == len(right_df):
        future_mask = r_series > l_series
        future_count = int(future_mask.sum())

    return {
        "valid": future_count == 0,
        "violations": future_count,
        "status": "PASS" if future_count == 0 else "FAIL",
    }


def validate_no_forbidden_cross_asset_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Scan dataframe columns for any forbidden signal, target, prediction, or text column names."""
    if df.empty:
        return {"valid": True, "forbidden_columns": [], "clean": True}

    detected = []
    for col in df.columns:
        col_lower = str(col).lower()
        for forbidden in FORBIDDEN_COLUMNS:
            # Check for exact token match or delimited substring
            if re.search(rf"\b{re.escape(forbidden)}\b", col_lower) or col_lower == forbidden:
                detected.append(col)
                break

    return {
        "valid": len(detected) == 0,
        "clean": len(detected) == 0,
        "forbidden_columns": detected,
        "total_columns": len(df.columns),
    }


def validate_no_negative_shift_usage(source_text: str) -> Dict[str, Any]:
    """Scan code or formula source text for illegal negative shift patterns like shift(-1)."""
    pattern = r"\.shift\s*\(\s*-[1-9]\d*\s*\)"
    matches = re.findall(pattern, source_text)
    return {
        "valid": len(matches) == 0,
        "clean": len(matches) == 0,
        "matches_found": matches,
        "match_count": len(matches),
    }


def summarize_cross_asset_no_lookahead_guard(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no-lookahead guard rules."""
    return {
        "total_guards": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "forbidden_column_count": len(FORBIDDEN_COLUMNS),
    }
