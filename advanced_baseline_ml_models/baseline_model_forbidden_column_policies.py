# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Forbidden Column Policies.

Defines and enforces the strict blacklist of column names and patterns that must
never appear in baseline model input or output contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FORBIDDEN_COLUMNS_LIST = [
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
    "html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
]


def build_baseline_model_forbidden_column_policy_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build forbidden column policy registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for col in FORBIDDEN_COLUMNS_LIST:
        rows.append({
            "forbidden_column": col,
            "policy": "STRICT_FORBIDDEN",
            "enforced": True,
            "category": "trading_signal" if col in ["signal", "buy", "sell", "long", "short", "position", "recommendation"]
            else "target_label" if col in ["target", "label", "prediction", "future_return", "forward_return", "next_return"]
            else "raw_news_or_nlp",
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_forbidden_column_policies(df)
    return df, summary


def validate_baseline_model_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate a list of column names against the forbidden columns blacklist."""
    violations = []
    for col in column_names:
        c_lower = col.lower().strip()
        if c_lower in FORBIDDEN_COLUMNS_LIST:
            violations.append(f"Forbidden column exact match: '{col}'")
        else:
            for f in FORBIDDEN_COLUMNS_LIST:
                if f in c_lower and len(f) > 3:
                    violations.append(f"Column '{col}' contains forbidden token '{f}'")
                    break

    valid = len(violations) == 0
    return {
        "valid": valid,
        "violations": violations,
        "total_columns_inspected": len(column_names),
        "status": "PASS_CLEAN_COLUMNS" if valid else "FAIL_FORBIDDEN_COLUMNS_DETECTED",
        "non_signal": True,
    }


def summarize_baseline_model_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column policies."""
    return {
        "total_forbidden_columns": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
