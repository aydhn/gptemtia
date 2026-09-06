"""Tests for Phase 132 Metadata-Only News Boundary Guard."""

import pandas as pd
from advanced_macro_event_news_regime.metadata_only_news_boundary import (
    build_metadata_only_news_boundary_registry,
    validate_metadata_only_news_columns,
    validate_no_full_article_news_usage,
    summarize_metadata_only_news_boundary,
)


def test_build_metadata_only_news_boundary():
    df, summary = build_metadata_only_news_boundary_registry()
    assert not df.empty
    assert len(df) >= 10
    assert "forbidden_field" in df.columns
    assert summary["strictly_enforced"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_validate_metadata_only_news_columns():
    clean_cols = ["topic_id", "timestamp_utc", "asset_tag", "relevance_score"]
    res_clean = validate_metadata_only_news_columns(clean_cols)
    assert res_clean["valid"] is True
    assert res_clean["status"] == "PASS"

    dirty_cols = ["topic_id", "article_body", "raw_content", "sentiment_score"]
    res_dirty = validate_metadata_only_news_columns(dirty_cols)
    assert res_dirty["valid"] is False
    assert res_dirty["violation_count"] >= 3


def test_validate_no_full_article_news_usage():
    clean_df = pd.DataFrame({"tag": ["inflation"], "timestamp": ["2026-01-01"]})
    res_clean = validate_no_full_article_news_usage(text="clean metadata tags", df=clean_df)
    assert res_clean["valid"] is True

    dirty_df = pd.DataFrame({"full_text": ["some article"], "tag": ["rates"]})
    res_dirty = validate_no_full_article_news_usage(df=dirty_df)
    assert res_dirty["valid"] is False


def test_summarize_metadata_only_news_boundary():
    df, _ = build_metadata_only_news_boundary_registry()
    summary = summarize_metadata_only_news_boundary(df)
    assert summary["total_rules"] >= 10
    assert summary["strictly_enforced"] is True
    assert summary["all_non_signal"] is True
