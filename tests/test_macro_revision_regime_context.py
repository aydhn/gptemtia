"""Tests for Phase 132 Macro Revision Regime Context."""

from advanced_macro_event_news_regime.macro_revision_regime_context import (
    build_macro_revision_regime_context_registry,
    summarize_macro_revision_regime_context,
)


def test_build_macro_revision_context():
    df, summary = build_macro_revision_regime_context_registry()
    assert not df.empty
    assert len(df) >= 5
    assert "revision_context_id" in df.columns
    assert "revision_cycle" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_macro_revision_context():
    df, _ = build_macro_revision_regime_context_registry()
    summary = summarize_macro_revision_regime_context(df)
    assert summary["total_revision_contexts"] >= 5
    assert summary["indicators_tracked"] >= 2
    assert summary["all_non_signal"] is True
