"""Tests for Phase 132 Pre-Event Regime Context."""

from advanced_macro_event_news_regime.pre_event_regime_context import (
    build_pre_event_regime_context_registry,
    summarize_pre_event_regime_context,
)


def test_build_pre_event_regime_context():
    df, summary = build_pre_event_regime_context_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "pre_event_id" in df.columns
    assert "buffer_minutes" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_pre_event_regime_context():
    df, _ = build_pre_event_regime_context_registry()
    summary = summarize_pre_event_regime_context(df)
    assert summary["total_pre_events"] >= 3
    assert summary["anticipation_tiers"] >= 2
    assert summary["all_non_signal"] is True
