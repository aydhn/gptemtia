"""Non-Signal Feature and Report Validation.

Enforces zero trade signals, zero directional recommendations, and zero official approval claims
across column naming, report text, and pipeline outputs.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import re
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)

PROHIBITED_CLAIM_PHRASES: List[str] = [
    "kesin al",
    "kesin sat",
    "buy signal",
    "sell signal",
    "long aç",
    "short aç",
    "position aç",
    "yatırım tavsiyesi",
    "production ready",
    "broker ready",
    "official approval",
    "model prediction",
    "target label",
]

PROHIBITED_NAME_KEYWORDS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "recommendation",
    "target",
    "prediction",
]


def build_non_signal_feature_validation_report(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of non-signal validation mandates."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "mandate_type": "column_name_prohibition",
            "enforced": True,
            "prohibited_terms": PROHIBITED_NAME_KEYWORDS,
            "severity": "validation_critical",
            "status_label": "validation_pass",
        },
        {
            "mandate_type": "report_text_claim_prohibition",
            "enforced": True,
            "prohibited_terms": PROHIBITED_CLAIM_PHRASES,
            "severity": "validation_critical",
            "status_label": "validation_pass",
        },
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_mandates": len(records),
        "non_signal": True,
        "zero_signal_tolerance": True,
    }
    return df, summary


def validate_non_signal_feature_names(feature_columns: List[str]) -> Dict[str, Any]:
    """Inspect column names for any forbidden signal or directional terms."""
    violations = []

    for col in feature_columns:
        c_lower = str(col).lower()
        for kw in PROHIBITED_NAME_KEYWORDS:
            token_pattern = rf"(?:^|_){re.escape(kw)}(?:_|$)"
            if re.search(token_pattern, c_lower) or kw == c_lower:
                violations.append({
                    "column": col,
                    "matched_keyword": kw,
                    "severity": "validation_critical",
                })

    passed = len(violations) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "total_columns_inspected": len(feature_columns),
        "violation_count": len(violations),
        "violations": violations,
        "manual_review_required": not passed,
        "non_signal": passed,
    }


def validate_non_signal_report_text(text: str) -> Dict[str, Any]:
    """Inspect report or text content for prohibited directional claims or approvals."""
    violations = []
    text_lower = text.lower()

    for phrase in PROHIBITED_CLAIM_PHRASES:
        if phrase in text_lower:
            violations.append({
                "matched_phrase": phrase,
                "severity": "validation_critical",
            })

    passed = len(violations) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "violations": violations,
        "violation_count": len(violations),
        "manual_review_required": not passed,
        "non_signal": passed,
    }


def summarize_non_signal_feature_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary of non-signal validation."""
    feat_cols = list(df.columns)
    res = validate_non_signal_feature_names(feat_cols)
    return {
        "passed": res["passed"],
        "status": res["status_label"],
        "violations_found": res["violation_count"],
        "non_signal": res["non_signal"],
        "manual_review_required": res["manual_review_required"],
    }


def check_signal_like_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Check for columns containing signal-like, order, or recommendation keywords."""
    res = validate_non_signal_feature_names(list(df.columns))
    signal_cols = [v["column"] for v in res.get("violations", [])]
    is_valid = len(signal_cols) == 0

    return {
        "is_valid": is_valid,
        "signal_columns_detected": signal_cols,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }


def validate_non_signal_invariants(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate that DataFrame strictly enforces non-signal mandates."""
    res = check_signal_like_columns(df)
    return {
        "is_valid": res["is_valid"],
        "non_signal": True,
        "current_phase": 121,
        "destructive_action_allowed": False,
        "signal_columns_detected": res["signal_columns_detected"],
    }

