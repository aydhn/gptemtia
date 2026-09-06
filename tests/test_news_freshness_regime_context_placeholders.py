"""Tests for Phase 132 News Freshness Regime Context Placeholders."""

from advanced_macro_event_news_regime.news_freshness_regime_context_placeholders import (
    build_news_freshness_regime_context_placeholder_registry,
    summarize_news_freshness_regime_context_placeholders,
)


def test_build_news_freshness_regime_context_placeholders():
    df, summary = build_news_freshness_regime_context_placeholder_registry()
    assert not df.empty
    assert len(df) >= 2
    assert "placeholder_id" in df.columns
    assert "half_life_hours" in df.columns
    assert summary["strictly_metadata_only"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_news_freshness_regime_context_placeholders():
    df, _ = build_news_freshness_regime_context_placeholder_registry()
    summary = summarize_news_freshness_regime_context_placeholders(df)
    assert summary["total_placeholders"] >= 2
    assert summary["mean_half_life"] > 0
    assert summary["all_non_signal"] is True
