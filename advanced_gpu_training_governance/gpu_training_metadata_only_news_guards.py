# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Metadata-Only News Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

FORBIDDEN_NEWS_CONTENT_TERMS: List[str] = [
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


def build_gpu_training_metadata_only_news_guard_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build metadata-only news guard registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    guards = [
        {
            "guard_id": "NEWS_GRD_001",
            "guard_name": "raw_article_body_exclusion_guard",
            "check_type": "content_exclusion",
            "enforced": True,
            "non_signal": True,
            "description": "Excludes full article text, copyrighted copy, and raw news bodies.",
            "status": "gpu_governance_ready",
        },
        {
            "guard_id": "NEWS_GRD_002",
            "guard_name": "scraped_html_exclusion_guard",
            "check_type": "content_exclusion",
            "enforced": True,
            "non_signal": True,
            "description": "Excludes scraped HTML DOM trees and unparsed web payloads.",
            "status": "gpu_governance_ready",
        },
        {
            "guard_id": "NEWS_GRD_003",
            "guard_name": "sentiment_embedding_exclusion_guard",
            "check_type": "nlp_payload_exclusion",
            "enforced": True,
            "non_signal": True,
            "description": "Excludes LLM embeddings, sentiment scores, and dense NLP vectors.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(guards)
    summary = summarize_gpu_training_metadata_only_news_guards(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_gpu_training_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that input columns contain metadata only and no raw news text or NLP vectors."""
    violating_columns = []
    for col in column_names:
        c_lower = col.lower()
        for term in FORBIDDEN_NEWS_CONTENT_TERMS:
            if term in c_lower:
                violating_columns.append(col)
                break

    is_clean = len(violating_columns) == 0
    return {
        "is_clean": is_clean,
        "violating_columns": violating_columns,
        "total_columns_checked": len(column_names),
        "non_signal": True,
        "status": "PASS" if is_clean else "FAIL_RAW_NEWS_OR_NLP",
    }


def summarize_gpu_training_metadata_only_news_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize metadata-only news guards DataFrame."""
    if df.empty:
        return {"total_guards": 0, "non_signal": True}
    return {
        "total_guards": len(df),
        "all_enforced": bool((df["enforced"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
