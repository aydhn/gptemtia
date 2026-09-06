"""Tests for Phase 132 News Macro Tag Regime Context."""

from advanced_macro_event_news_regime.news_macro_tag_regime_context import (
    build_news_macro_tag_regime_context_registry,
    summarize_news_macro_tag_regime_context,
)


def test_build_news_macro_tag_regime_context():
    df, summary = build_news_macro_tag_regime_context_registry()
    assert not df.empty
    assert len(df) >= 2
    assert "macro_tag_context_id" in df.columns
    assert "macro_theme" in df.columns
    assert summary["strictly_metadata_only"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_news_macro_tag_regime_context():
    df, _ = build_news_macro_tag_regime_context_registry()
    summary = summarize_news_macro_tag_regime_context(df)
    assert summary["total_tags"] >= 2
    assert summary["macro_themes"] >= 2
    assert summary["all_non_signal"] is True
