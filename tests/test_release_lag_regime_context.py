"""Tests for Phase 132 Release Lag Regime Context."""

from advanced_macro_event_news_regime.release_lag_regime_context import (
    build_release_lag_regime_context_registry,
    summarize_release_lag_regime_context,
)


def test_build_release_lag_regime_context():
    df, summary = build_release_lag_regime_context_registry()
    assert not df.empty
    assert len(df) >= 4
    assert "lag_id" in df.columns
    assert "nominal_lag_days" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_release_lag_regime_context():
    df, _ = build_release_lag_regime_context_registry()
    summary = summarize_release_lag_regime_context(df)
    assert summary["total_lag_entries"] >= 4
    assert summary["max_nominal_lag"] >= 30
    assert summary["all_non_signal"] is True
