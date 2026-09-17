# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Metadata-Only News Guards."""

import pytest
from advanced_model_drift_monitoring.drift_metadata_only_news_guards import (
    build_drift_metadata_only_news_guards,
    validate_news_feature_metadata_only,
)


def test_metadata_only_news_guards():
    guards = build_drift_metadata_only_news_guards()
    assert len(guards) == 1
    assert guards[0].is_active is True


def test_validate_news_feature_columns():
    safe_cols = ["headline_length", "sentiment_score_ref", "article_count"]
    res_safe = validate_news_feature_metadata_only(safe_cols)
    assert res_safe["valid"] is True

    unsafe_cols = ["article_count", "article_body", "raw_html"]
    res_unsafe = validate_news_feature_metadata_only(unsafe_cols)
    assert res_unsafe["valid"] is False
    assert "article_body" in res_unsafe["violating_columns"]
