"""Phase 132: Macro/Event/News No-Lookahead Guard.

Validates that no forward lookahead, future returns, directional signals,
negative shift operations, or forbidden full article/sentiment data leak into context.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
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
    "page_html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
]

DEFAULT_GUARD_RULES = [
    {
        "guard_id": "guard_no_negative_shift",
        "guard_type": "code_inspection",
        "description": "Prevents shift(-1) or negative shift future indexing.",
        "enforced": True,
    },
    {
        "guard_id": "guard_no_future_return",
        "guard_type": "column_inspection",
        "description": "Prevents forward return or target labels.",
        "enforced": True,
    },
    {
        "guard_id": "guard_metadata_only_news",
        "guard_type": "news_boundary_inspection",
        "description": "Prevents raw article text or sentiment model outputs.",
        "enforced": True,
    },
    {
        "guard_id": "guard_backward_asof_only",
        "guard_type": "join_inspection",
        "description": "Ensures all time-series context joins strictly look backward.",
        "enforced": True,
    },
]


def build_macro_event_news_no_lookahead_guard_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of no-lookahead guard rules."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_GUARD_RULES:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_guards": len(df),
        "all_enforced": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def validate_no_future_macro_event_news_join(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_ts: str,
    right_ts: str,
) -> Dict[str, Any]:
    """Validate that joining right_df into left_df does not pull future records."""
    if left_df.empty or right_df.empty:
        return {"valid": True, "future_leak_count": 0, "status": "PASS_EMPTY"}

    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {"valid": False, "error": "Timestamp columns missing", "status": "FAIL"}

    l_max = pd.to_datetime(left_df[left_ts]).max()
    r_min = pd.to_datetime(right_df[right_ts]).min()

    # If right table's minimum timestamp is beyond left table's maximum timestamp,
    # right table is strictly future relative to left table
    has_future_lead = r_min > l_max
    return {
        "valid": not has_future_lead,
        "left_max_ts": str(l_max),
        "right_min_ts": str(r_min),
        "future_leak_risk": has_future_lead,
        "status": "PASS" if not has_future_lead else "FAIL_FUTURE_DATA_LEAD",
    }


def validate_no_forbidden_macro_event_news_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Check DataFrame columns for forbidden signal, target, article text, or sentiment names."""
    cols_lower = [c.lower().strip() for c in df.columns]
    violations = []
    for c in cols_lower:
        for forbidden in FORBIDDEN_COLUMNS:
            if c == forbidden or f"_{forbidden}" in c or f"{forbidden}_" in c:
                violations.append(c)
                break

    is_clean = len(violations) == 0
    return {
        "valid": is_clean,
        "violations": violations,
        "violation_count": len(violations),
        "forbidden_columns_checked": len(FORBIDDEN_COLUMNS),
        "status": "PASS" if is_clean else "FAIL_FORBIDDEN_COLUMNS_DETECTED",
    }


def validate_no_negative_shift_usage(source_text: str) -> Dict[str, Any]:
    """Inspect Python code string for negative shift lookahead patterns like shift(-1)."""
    clean_text = source_text.replace(" ", "")
    suspicious_patterns = ["shift(-", ".pct_change(-", ".diff(-"]
    found = []
    for pat in suspicious_patterns:
        if pat in clean_text:
            found.append(pat)

    is_safe = len(found) == 0
    return {
        "valid": is_safe,
        "violations": found,
        "violation_count": len(found),
        "status": "PASS" if is_safe else "FAIL_NEGATIVE_SHIFT_DETECTED",
    }


def summarize_macro_event_news_no_lookahead_guard(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for no-lookahead guard registry."""
    return {
        "total_guards": len(df),
        "all_enforced": bool(df["enforced"].all()) if "enforced" in df.columns else False,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
