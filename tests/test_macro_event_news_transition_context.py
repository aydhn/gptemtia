"""Tests for Phase 132 Macro/Event/News Transition Context."""

from advanced_macro_event_news_regime.macro_event_news_transition_context import (
    build_macro_event_news_transition_context_registry,
    summarize_macro_event_news_transition_context,
)


def test_build_macro_event_news_transition_context():
    df, summary = build_macro_event_news_transition_context_registry()
    assert not df.empty
    assert len(df) >= 6
    assert "transition_context_id" in df.columns
    assert "transition_type" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_macro_event_news_transition_context():
    df, _ = build_macro_event_news_transition_context_registry()
    summary = summarize_macro_event_news_transition_context(df)
    assert summary["total_contexts"] >= 6
    assert summary["transition_types"] >= 4
    assert summary["all_non_signal"] is True
