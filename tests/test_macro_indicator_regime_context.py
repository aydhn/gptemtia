"""Tests for Phase 132 Macro Indicator Regime Context."""

from advanced_macro_event_news_regime.macro_indicator_regime_context import (
    build_macro_indicator_regime_context_registry,
    summarize_macro_indicator_regime_context,
)


def test_build_macro_indicator_context():
    df, summary = build_macro_indicator_regime_context_registry()
    assert not df.empty
    assert len(df) >= 5
    assert "context_name" in df.columns
    assert "inflation_regime_context" in df["context_name"].values
    assert "rate_regime_context" in df["context_name"].values
    assert "growth_regime_context" in df["context_name"].values
    assert summary["all_non_signal"] is True


def test_summarize_macro_indicator_context():
    df, _ = build_macro_indicator_regime_context_registry()
    summary = summarize_macro_indicator_regime_context(df)
    assert summary["total_contexts"] >= 5
    assert summary["all_non_signal"] is True
