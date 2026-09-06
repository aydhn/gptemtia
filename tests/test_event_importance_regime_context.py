"""Tests for Phase 132 Event Importance Regime Context."""

from advanced_macro_event_news_regime.event_importance_regime_context import (
    build_event_importance_regime_context_registry,
    summarize_event_importance_regime_context,
)


def test_build_event_importance_regime_context():
    df, summary = build_event_importance_regime_context_registry()
    assert not df.empty
    assert len(df) >= 4
    assert "importance_tier" in df.columns
    assert "weight_rank" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_event_importance_regime_context():
    df, _ = build_event_importance_regime_context_registry()
    summary = summarize_event_importance_regime_context(df)
    assert summary["total_tiers"] >= 4
    assert summary["highest_tier"] == "critical"
    assert summary["all_non_signal"] is True
