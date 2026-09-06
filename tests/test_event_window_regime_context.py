"""Tests for Phase 132 Event Window Regime Context."""

from advanced_macro_event_news_regime.event_window_regime_context import (
    build_event_window_regime_context_registry,
    summarize_event_window_regime_context,
)


def test_build_event_window_regime_context():
    df, summary = build_event_window_regime_context_registry()
    assert not df.empty
    assert len(df) >= 4
    assert "window_id" in df.columns
    assert "event_id" in df.columns
    assert "total_window_mins" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_event_window_regime_context():
    df, _ = build_event_window_regime_context_registry()
    summary = summarize_event_window_regime_context(df)
    assert summary["total_event_windows"] >= 4
    assert summary["mean_total_mins"] > 0
    assert summary["all_non_signal"] is True
