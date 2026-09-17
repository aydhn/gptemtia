# -*- coding: utf-8 -*-
"""Phase 144: Governance Metadata-Only News Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_NEWS_COLUMNS = [
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "html",
    "news_content",
    "body",
]


def build_governance_metadata_only_news_guard_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for metadata-only news guards."""
    prof = profile or get_model_governance_profile()
    records = [
        {"guard_name": "no_raw_article_body_guard", "enforcement": "Reject raw news text or article body fields.", "status": "ACTIVE"},
        {"guard_name": "no_scraped_html_guard", "enforcement": "Reject HTML, web page dumps, or scraped payloads.", "status": "ACTIVE"},
        {"guard_name": "metadata_only_schema_guard", "enforcement": "Allow only headline, timestamp, category, and source metadata.", "status": "ACTIVE"},
    ]
    for r in records:
        r["phase"] = prof.current_phase
        r["is_enforced"] = True

    df = pd.DataFrame(records)
    summary = summarize_governance_metadata_only_news_guards(df)
    return df, summary


def summarize_governance_metadata_only_news_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize metadata-only news guards."""
    return {
        "total_guards": len(df),
        "all_enforced": bool(df["is_enforced"].all()),
        "status": "METADATA_ONLY_GUARDS_ACTIVE",
    }


def validate_governance_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that news column list does not contain full text or HTML."""
    violations = []
    for col in column_names:
        col_lower = str(col).lower()
        if any(f_col in col_lower for f_col in FORBIDDEN_NEWS_COLUMNS):
            violations.append(col)

    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violations": violations,
        "status": "PASS" if is_valid else "FAIL_FULL_TEXT_DETECTED",
    }
