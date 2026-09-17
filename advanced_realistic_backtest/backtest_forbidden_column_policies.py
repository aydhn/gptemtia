# -*- coding: utf-8 -*-
"""Phase 146: Backtest Forbidden Column Policies.

Defines strict quarantine and validation policies for forbidden columns in backtest datasets.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

FORBIDDEN_COLUMNS = [
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
    "lookahead_return",
    "realized_future_pnl",
    "future_pnl",
    "perfect_fill",
    "leak",
    "leakage",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
]


def build_backtest_forbidden_column_policy_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of forbidden column policy rules."""
    rows = []
    for col in FORBIDDEN_COLUMNS:
        rows.append(
            {
                "forbidden_column": col,
                "policy": "QUARANTINE_AND_REJECT",
                "reason": "Prevents directional claims, lookahead bias, unapproved predictions, or copyright leakage.",
                "enforced": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_forbidden_column_policies(df)
    return df, summary


def validate_backtest_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that input column list does not contain any forbidden terms."""
    violations = []
    col_lower = [c.lower() for c in column_names]
    for forbidden in FORBIDDEN_COLUMNS:
        for c in col_lower:
            if c == forbidden or c.startswith(f"{forbidden}_") or c.endswith(f"_{forbidden}"):
                violations.append(c)
    violations = sorted(list(set(violations)))
    return {
        "is_clean": len(violations) == 0,
        "violations": violations,
        "checked_columns_count": len(column_names),
    }


def validate_dataframe_no_forbidden_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate that DataFrame does not contain any forbidden columns."""
    res = validate_backtest_forbidden_columns(df.columns.tolist())
    return {
        "is_clean": res["is_clean"],
        "forbidden_columns_found": res["violations"],
        "checked_columns_count": res["checked_columns_count"],
    }


def summarize_backtest_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column policies."""
    return {
        "total_forbidden_columns": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "quarantine_active": True,
        "non_signal": True,
    }

