"""Drift Metadata-Only News Guards for Phase 142.

Enforces metadata-only contracts for textual and news sentiment drift features:
zero raw HTML scrapes, zero full-text articles, zero unstructured textual dumps.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftGuardItem


def build_drift_metadata_only_news_guards() -> List[DriftGuardItem]:
    """Builds metadata-only guards for news and textual features in drift monitoring."""
    guards = [
        DriftGuardItem(
            guard_id="guard_metadata_only_news_text",
            guard_name="Metadata-Only News Drift Guard",
            guard_type="metadata_only",
            status="active",
            is_active=True,
            description="Prohibits full-text articles, raw HTML bodies, and scraped news corpora in drift monitoring contracts.",
            validation_rule="allow_metadata_fields_only",
            metadata={
                "forbidden_fields": ["article_body", "raw_html", "scraped_text", "full_content", "story_body"],
                "allowed_fields": ["headline_length", "sentiment_score_ref", "article_count", "source_domain"],
            },
        ),
    ]
    return guards


def validate_news_feature_metadata_only(feature_columns: List[str]) -> Dict[str, Any]:
    """Validates that news/sentiment feature columns do not contain full-text fields."""
    forbidden = {"article_body", "raw_html", "scraped_text", "full_content", "story_body", "text_payload"}
    violating = [col for col in feature_columns if col.lower() in forbidden]

    return {
        "valid": len(violating) == 0,
        "violating_columns": violating,
        "error": f"Forbidden text columns found: {violating}" if violating else None,
    }
