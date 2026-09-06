"""Tests for Phase 132 Calendar Event Regime Context."""

from advanced_macro_event_news_regime.calendar_event_regime_context import (
    build_calendar_event_regime_context_registry,
    summarize_calendar_event_regime_context,
)


def test_build_calendar_event_regime_context():
    df, summary = build_calendar_event_regime_context_registry()
    assert not df.empty
    assert len(df) >= 4
    assert "calendar_context_id" in df.columns
    assert "event_id" in df.columns
    assert "importance" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_calendar_event_regime_context():
    df, _ = build_calendar_event_regime_context_registry()
    summary = summarize_calendar_event_regime_context(df)
    assert summary["total_calendar_events"] >= 4
    assert summary["critical_events"] >= 2
    assert summary["all_non_signal"] is True
