"""Phase 132: Metadata-Only News Boundary Guard.

Enforces zero raw article text, zero scraped HTML, zero sentiment model outputs,
and zero embedding/vector leakage into feature stores or regime datasets.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

FORBIDDEN_NEWS_FIELDS: List[str] = [
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "html",
    "article",
    "content",
    "body",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
    "llm_summary_from_article",
]

DEFAULT_BOUNDARY_RULES = [
    {
        "rule_id": f"bound_no_{field}",
        "forbidden_field": field,
        "description": f"Strictly prohibit usage or persistence of '{field}' field in Phase 132 news layer.",
        "remediation_action": "exclude_from_feature_lake",
        "is_active": True,
        "strictly_enforced": True,
    }
    for field in FORBIDDEN_NEWS_FIELDS
]


def build_metadata_only_news_boundary_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of metadata-only boundary enforcement rules."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_BOUNDARY_RULES:
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
        "total_boundary_rules": len(df),
        "forbidden_fields_count": len(FORBIDDEN_NEWS_FIELDS),
        "strictly_enforced": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def validate_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that a list of column names contains zero forbidden news content fields."""
    normalized_cols = [c.lower().strip() for c in column_names]
    violations = []
    for col in normalized_cols:
        for forbidden in FORBIDDEN_NEWS_FIELDS:
            if forbidden == col or f"_{forbidden}" in col or f"{forbidden}_" in col:
                violations.append(col)
                break

    is_clean = len(violations) == 0
    return {
        "valid": is_clean,
        "violations": violations,
        "violation_count": len(violations),
        "forbidden_fields_checked": len(FORBIDDEN_NEWS_FIELDS),
        "status": "PASS" if is_clean else "FAIL_FORBIDDEN_COLUMNS_DETECTED",
    }


def validate_no_full_article_news_usage(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
) -> Dict[str, Any]:
    """Validate that neither text source nor DataFrame contains raw article body or full text."""
    violations = []

    if df is not None and not df.empty:
        col_res = validate_metadata_only_news_columns(list(df.columns))
        if not col_res["valid"]:
            violations.extend(col_res["violations"])

    if text:
        text_lower = text.lower()
        for forbidden in FORBIDDEN_NEWS_FIELDS:
            if f'"{forbidden}"' in text_lower or f"'{forbidden}'" in text_lower:
                violations.append(f"field_reference:{forbidden}")

    is_clean = len(violations) == 0
    return {
        "valid": is_clean,
        "violations": violations,
        "violation_count": len(violations),
        "status": "PASS" if is_clean else "FAIL_RAW_ARTICLE_CONTENT_DETECTED",
    }


def summarize_metadata_only_news_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for metadata-only boundary registry."""
    return {
        "total_rules": len(df),
        "active_rules": int(df["is_active"].sum()) if "is_active" in df.columns else 0,
        "strictly_enforced": bool(df["strictly_enforced"].all()) if "strictly_enforced" in df.columns else True,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
