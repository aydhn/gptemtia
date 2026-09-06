"""Tests for Phase 132 Post-Event Regime Context."""

from advanced_macro_event_news_regime.post_event_regime_context import (
    build_post_event_regime_context_registry,
    summarize_post_event_regime_context,
)


def test_build_post_event_regime_context():
    df, summary = build_post_event_regime_context_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "post_event_id" in df.columns
    assert "buffer_minutes" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_post_event_regime_context():
    df, _ = build_post_event_regime_context_registry()
    summary = summarize_post_event_regime_context(df)
    assert summary["total_post_events"] >= 3
    assert summary["absorption_tiers"] >= 2
    assert summary["all_non_signal"] is True
