# -*- coding: utf-8 -*-
"""Unit tests for baseline model metadata-only news guards."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_metadata_only_news_guards import (
    METADATA_ONLY_GUARDS,
    build_baseline_model_metadata_only_news_guard_registry,
    summarize_baseline_model_metadata_only_news_guards,
    validate_baseline_model_metadata_only_news_columns,
)


def test_build_baseline_model_metadata_only_news_guard_registry():
    df, summary = build_baseline_model_metadata_only_news_guard_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(METADATA_ONLY_GUARDS)
    assert len(df) == 4
    assert summary["total_guards"] == 4
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
    assert (df["enforced"] == True).all()


def test_validate_baseline_model_metadata_only_news_columns():
    clean_news = ["news_id", "timestamp", "source_id", "category_tag", "headline_length"]
    res_clean = validate_baseline_model_metadata_only_news_columns(clean_news)
    assert res_clean["valid"] is True
    assert res_clean["violations"] == []
    assert res_clean["status"] == "VALID_METADATA_ONLY"

    dirty_news = ["news_id", "full_text", "scraped_html", "sentiment_score", "vector"]
    res_dirty = validate_baseline_model_metadata_only_news_columns(dirty_news)
    assert res_dirty["valid"] is False
    assert len(res_dirty["violations"]) >= 4
    assert res_dirty["status"] == "METADATA_ONLY_VIOLATION_DETECTED"
