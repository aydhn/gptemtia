"""Forbidden Feature Column Registry and Validator.

Detects prohibited column names such as signals, trading directives, targets,
predictions, future returns, and scraped text/embeddings.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import re
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)

FORBIDDEN_FEATURE_PATTERNS: List[str] = [
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
    "embedding",
    "vector",
]

_PATTERN_CATEGORIES: Dict[str, str] = {
    "signal": "trading_signal",
    "buy": "trading_directive",
    "sell": "trading_directive",
    "long": "position_directive",
    "short": "position_directive",
    "position": "position_directive",
    "target": "target_label",
    "label": "target_label",
    "prediction": "ml_prediction",
    "recommendation": "trading_recommendation",
    "future_return": "lookahead_leakage",
    "forward_return": "lookahead_leakage",
    "next_return": "lookahead_leakage",
    "full_text": "copyrighted_content",
    "article_body": "copyrighted_content",
    "raw_content": "scraped_content",
    "scraped_html": "scraped_content",
    "page_html": "scraped_content",
    "embedding": "vector_embedding",
    "vector": "vector_embedding",
}


def get_forbidden_feature_column_patterns() -> List[str]:
    """Return the list of forbidden feature column patterns."""
    return list(FORBIDDEN_FEATURE_PATTERNS)


def build_forbidden_feature_column_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of forbidden column specifications."""
    active_profile = profile or get_default_feature_validation_profile()

    records = []
    for pattern in FORBIDDEN_FEATURE_PATTERNS:
        category = _PATTERN_CATEGORIES.get(pattern, "prohibited_term")
        records.append({
            "pattern": pattern,
            "category": category,
            "severity": "validation_critical",
            "enforced": True,
            "action_on_detection": "flag_finding_require_manual_review",
            "destructive_cleaning_allowed": False,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_patterns": len(records),
        "pattern_categories": list({r["category"] for r in records}),
        "enforced": True,
        "destructive_cleaning_allowed": False,
        "non_signal": True,
    }
    return df, summary


def validate_forbidden_column_names(column_names: List[str]) -> Dict[str, Any]:
    """Inspect a list of column names for forbidden terms."""
    violations: List[Dict[str, str]] = []
    clean_columns: List[str] = []

    for col in column_names:
        col_lower = col.lower()
        matched_patterns = []
        for pat in FORBIDDEN_FEATURE_PATTERNS:
            # Word boundary or substring token check
            token_pattern = rf"(?:^|_){re.escape(pat)}(?:_|$)"
            if re.search(token_pattern, col_lower) or pat in col_lower:
                matched_patterns.append(pat)

        if matched_patterns:
            for m in matched_patterns:
                violations.append({
                    "column": col,
                    "matched_pattern": m,
                    "category": _PATTERN_CATEGORIES.get(m, "prohibited_term"),
                    "severity": "validation_critical",
                })
        else:
            clean_columns.append(col)

    passed = len(violations) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "total_columns_inspected": len(column_names),
        "clean_column_count": len(clean_columns),
        "violation_count": len(violations),
        "violations": violations,
        "clean_columns": clean_columns,
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def validate_forbidden_feature_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Scan a DataFrame's columns for forbidden patterns."""
    return validate_forbidden_column_names(list(df.columns))


def summarize_forbidden_feature_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate a high-level summary of forbidden column compliance for a DataFrame."""
    res = validate_forbidden_feature_columns(df)
    return {
        "passed": res["passed"],
        "status": res["status_label"],
        "total_columns": res["total_columns_inspected"],
        "forbidden_columns_found": res["violation_count"],
        "manual_review_required": res["manual_review_required"],
    }


FORBIDDEN_FEATURE_COLUMN_PATTERNS = FORBIDDEN_FEATURE_PATTERNS


def get_forbidden_feature_columns() -> List[str]:
    return get_forbidden_feature_column_patterns()


def check_forbidden_feature_columns(df: pd.DataFrame) -> Dict[str, Any]:
    res = validate_forbidden_feature_columns(df)
    found_cols = list({v["column"] for v in res["violations"]})
    return {
        "is_valid": res["passed"],
        "passed": res["passed"],
        "forbidden_columns_found": found_cols,
        "violations": res["violations"],
    }

