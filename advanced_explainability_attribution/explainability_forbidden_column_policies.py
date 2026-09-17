# -*- coding: utf-8 -*-
"""Phase 143: Explainability Forbidden Column Policies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)

FORBIDDEN_COLUMNS: List[str] = [
    "future_price",
    "future_return",
    "target_return",
    "forward_close",
    "article_body",
    "full_text",
    "raw_html",
    "sentiment_score",
    "embedding_vector",
    "trade_signal",
    "buy_sell_recommendation",
]


def check_forbidden_columns(
    columns: List[str],
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[bool, List[str]]:
    """Check if any column names match forbidden leakage, content or signal terms."""
    prof = profile or get_explainability_profile()
    lowered = [c.lower() for c in columns]
    violations = [c for c in lowered if c in FORBIDDEN_COLUMNS]
    return len(violations) == 0, violations


def build_forbidden_column_policy_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of forbidden column policies."""
    prof = profile or get_explainability_profile()

    rows: List[Dict[str, Any]] = []
    for col in FORBIDDEN_COLUMNS:
        rows.append({
            "forbidden_column": col,
            "policy_action": "reject_contract",
            "enforced": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_forbidden_column_policies(df)
    return df, summary


def summarize_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column policies."""
    return {
        "total_forbidden_columns": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
