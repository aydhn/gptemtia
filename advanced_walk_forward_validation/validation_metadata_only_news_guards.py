# -*- coding: utf-8 -*-
"""Phase 147: Validation Metadata-Only News Guards.

Guards ensuring only metadata is used from news sources, blocking raw text, scraped HTML, and embeddings.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

FORBIDDEN_NEWS_COLUMNS = [
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


def build_validation_metadata_only_news_guard_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for metadata-only news guards."""
    rows = [
        {
            "guard_name": "metadata_only_news_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Haber tam metni, scraped html veya embedding kullanimini engelleyen muhafiz.",
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_guards": len(df),
        "all_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_validation_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that columns do not contain prohibited full text or embedding fields."""
    violations = []
    for col in column_names:
        c_lower = col.lower().strip()
        for forbidden in FORBIDDEN_NEWS_COLUMNS:
            if forbidden in c_lower:
                violations.append(col)
                break
    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violating_columns": violations,
        "message": "Gecerli kolonlar" if is_valid else f"Yasak haber/metin kolonlari saptandi: {violations}",
        "non_signal": True,
    }
