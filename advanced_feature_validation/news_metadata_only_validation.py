"""News Metadata-Only Validation and Full-Text Prohibitions.

Enforces metadata-only boundaries across news-derived features, blocking
full article texts, scraped contents, and copyright-infringing fields.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import re
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)

PROHIBITED_NEWS_FIELDS = [
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "raw_html",
    "news_body",
    "article_text",
    "scraped_text",
    "embedding",
    "vector",
]


def build_news_metadata_only_validation_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of news metadata-only rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "field_pattern": pat,
            "prohibition_reason": "copyright_and_scraping_boundary",
            "severity": "validation_critical",
            "enforced": True,
        }
        for pat in PROHIBITED_NEWS_FIELDS
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_prohibitions": len(records),
        "metadata_only_required": True,
        "non_signal": True,
    }
    return df, summary


FORBIDDEN_NEWS_COLUMNS = PROHIBITED_NEWS_FIELDS


def validate_news_metadata_only_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Inspect DataFrame columns to verify absence of full text or scraped news fields."""
    violations: List[Dict[str, str]] = []

    for col in df.columns:
        c_lower = str(col).lower()
        for pat in PROHIBITED_NEWS_FIELDS:
            if pat in c_lower:
                violations.append({
                    "column": str(col),
                    "matched_pattern": pat,
                    "severity": "validation_critical",
                })

    passed = len(violations) == 0
    forbidden_found = [v["column"] for v in violations]
    return {
        "passed": passed,
        "is_valid": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "violations": violations,
        "violation_count": len(violations),
        "forbidden_found": forbidden_found,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }



def validate_news_timestamp_not_future(
    df: pd.DataFrame, base_ts: str, news_ts: str
) -> Dict[str, Any]:
    """Verify that news published timestamp is on or before market base timestamp."""
    if base_ts not in df.columns or news_ts not in df.columns:
        return {
            "passed": False,
            "status_label": "validation_fail",
            "error": f"Columns '{base_ts}' or '{news_ts}' not in DataFrame.",
            "leakage_count": 0,
            "manual_review_required": True,
        }

    b = pd.to_datetime(df[base_ts])
    n = pd.to_datetime(df[news_ts])
    valid = b.notna() & n.notna()
    leakage = valid & (n > b)
    leakage_count = int(leakage.sum())
    passed = leakage_count == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "base_ts_field": base_ts,
        "news_ts_field": news_ts,
        "total_rows": len(df),
        "valid_pairs": int(valid.sum()),
        "future_news_leakage_count": leakage_count,
        "message": "All news publications on or before market base time."
        if passed
        else f"Failed: {leakage_count} records associate future news publication with past market bars.",
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def summarize_news_metadata_only_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate high-level summary of news metadata-only compliance."""
    res_cols = validate_news_metadata_only_columns(df)
    return {
        "passed": res_cols["passed"],
        "status": res_cols["status_label"],
        "prohibited_columns_found": res_cols["violation_count"],
        "manual_review_required": res_cols["manual_review_required"],
    }
