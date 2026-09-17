# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Metadata-Only News Guards.

Enforces strict metadata-only boundaries on news streams, rejecting copyrighted
full article text, raw HTML, sentiment model outputs, embeddings, and vectors.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FORBIDDEN_NEWS_CONTENT_PATTERNS = [
    "full_text", "article_body", "raw_content", "scraped_html", "page_html",
    "html", "body_text", "embedding", "vector", "sentiment", "sentiment_score",
    "scraped_text",
]

METADATA_ONLY_GUARDS = [
    {"guard_id": "guard_no_full_text", "scope": "copyright_protection", "enforced": True, "description": "Blocks article bodies and full texts"},
    {"guard_id": "guard_no_scraped_html", "scope": "scraping_protection", "enforced": True, "description": "Blocks raw HTML and scraped web content"},
    {"guard_id": "guard_no_sentiment_model_output", "scope": "model_output_boundary", "enforced": True, "description": "Blocks NLP sentiment outputs and polarities"},
    {"guard_id": "guard_no_vector_embeddings", "scope": "embedding_boundary", "enforced": True, "description": "Blocks high-dimensional embeddings and vectors"},
]


def build_baseline_model_metadata_only_news_guard_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build metadata-only news guards registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for g in METADATA_ONLY_GUARDS:
        rows.append({
            "guard_id": g["guard_id"],
            "scope": g["scope"],
            "enforced": g["enforced"],
            "description": g["description"],
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_metadata_only_news_guards(df)
    return df, summary


def validate_baseline_model_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Inspect columns to ensure no raw text, scraping, sentiment, or embeddings exist."""
    violations = []
    for col in column_names:
        c_lower = col.lower()
        for pattern in FORBIDDEN_NEWS_CONTENT_PATTERNS:
            if pattern in c_lower:
                violations.append(f"Column '{col}' violates metadata-only policy with pattern '{pattern}'")

    valid = len(violations) == 0
    return {
        "valid": valid,
        "violations": violations,
        "total_columns_checked": len(column_names),
        "status": "VALID_METADATA_ONLY" if valid else "METADATA_ONLY_VIOLATION_DETECTED",
        "non_signal": True,
    }


def summarize_baseline_model_metadata_only_news_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize metadata-only news guards."""
    return {
        "total_guards": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
