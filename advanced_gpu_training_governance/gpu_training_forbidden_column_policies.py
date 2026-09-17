# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Forbidden Column Policies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

FORBIDDEN_COLUMNS_LIST: List[str] = [
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


def build_gpu_training_forbidden_column_policy_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build forbidden column policy registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    rows = []
    for col in FORBIDDEN_COLUMNS_LIST:
        category = "signal" if col in ["signal", "buy", "sell", "long", "short", "position", "recommendation"] else (
            "target_prediction" if col in ["target", "label", "prediction", "future_return", "forward_return", "next_return"] else
            "unprocessed_nlp"
        )
        rows.append(
            {
                "forbidden_column": col,
                "category": category,
                "enforced": True,
                "non_signal": True,
                "description": f"Column '{col}' is strictly forbidden in Phase 139 ML training contracts.",
                "status": "gpu_governance_ready",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_gpu_training_forbidden_column_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_gpu_training_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that input column names contain no forbidden columns."""
    violating_columns = []
    for col in column_names:
        c_clean = col.strip().lower()
        if c_clean in FORBIDDEN_COLUMNS_LIST:
            violating_columns.append(col)

    is_clean = len(violating_columns) == 0
    return {
        "is_clean": is_clean,
        "violating_columns": violating_columns,
        "total_columns_checked": len(column_names),
        "non_signal": True,
        "status": "PASS" if is_clean else "FAIL_FORBIDDEN_COLUMNS",
    }


def summarize_gpu_training_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column policies DataFrame."""
    if df.empty:
        return {"total_forbidden_columns": 0, "non_signal": True}
    return {
        "total_forbidden_columns": len(df),
        "all_enforced": bool((df["enforced"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
