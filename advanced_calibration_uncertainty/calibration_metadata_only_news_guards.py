# -*- coding: utf-8 -*-
"""Phase 141: Calibration Metadata-Only News Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

FORBIDDEN_NEWS_CONTENT_TERMS = [
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


def build_calibration_metadata_only_news_guard_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration metadata-only news guards."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = [
        {
            "guard_id": "calib_guard_no_full_text",
            "rule_name": "prohibit_raw_article_body_and_full_text",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "guard_id": "calib_guard_no_embeddings",
            "rule_name": "prohibit_embedding_vectors_and_vector_dbs",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "guard_id": "calib_guard_no_sentiment_scores",
            "rule_name": "prohibit_sentiment_model_outputs",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_calibration_metadata_only_news_guards(df)
    return df, summary


def validate_calibration_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate column names ensuring zero raw news content or embeddings."""
    violations = []
    for col in column_names:
        c_lower = col.lower()
        for term in FORBIDDEN_NEWS_CONTENT_TERMS:
            if term in c_lower:
                violations.append(f"Column '{col}' violates metadata-only policy (matches '{term}')")

    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violations": violations,
        "status": "PASS" if is_valid else "METADATA_ONLY_VIOLATION_DETECTED",
        "non_signal": True,
    }


def summarize_calibration_metadata_only_news_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration metadata-only news guards DataFrame."""
    return {
        "total_guards": len(df),
        "guards": df["guard_id"].tolist() if not df.empty else [],
        "all_active": bool(df["is_active"].all()) if not df.empty else True,
        "all_blocking": bool(df["blocking"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
