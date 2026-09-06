"""Tests for Phase 132 News Topic Regime Context."""

from advanced_macro_event_news_regime.news_topic_regime_context import (
    build_news_topic_regime_context_registry,
    summarize_news_topic_regime_context,
)


def test_build_news_topic_regime_context():
    df, summary = build_news_topic_regime_context_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "topic_context_id" in df.columns
    assert "tag_id" in df.columns
    assert summary["strictly_metadata_only"] is True
    assert summary["zero_sentiment"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_news_topic_regime_context():
    df, _ = build_news_topic_regime_context_registry()
    summary = summarize_news_topic_regime_context(df)
    assert summary["total_topics"] >= 3
    assert summary["zero_article_text"] is True
    assert summary["all_non_signal"] is True
