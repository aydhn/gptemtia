"""Tests for Phase 132 Macro Release Regime Context."""

from advanced_macro_event_news_regime.macro_release_regime_context import (
    build_macro_release_regime_context_registry,
    summarize_macro_release_regime_context,
)


def test_build_macro_release_context():
    df, summary = build_macro_release_regime_context_registry()
    assert not df.empty
    assert len(df) >= 4
    assert "scheduled_time_utc" in df.columns
    assert "release_lag_days" in df.columns
    assert summary["all_non_signal"] is True


def test_summarize_macro_release_context():
    df, _ = build_macro_release_regime_context_registry()
    summary = summarize_macro_release_regime_context(df)
    assert summary["total_release_contexts"] >= 4
    assert summary["all_non_signal"] is True
