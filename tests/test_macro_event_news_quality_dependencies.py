"""Tests for Phase 132 Macro/Event/News Quality Dependencies."""

from advanced_macro_event_news_regime.macro_event_news_quality_dependencies import (
    build_macro_event_news_quality_dependency_registry,
    summarize_macro_event_news_quality_dependencies,
)


def test_build_macro_event_news_quality_dependencies():
    df, summary = build_macro_event_news_quality_dependency_registry()
    assert not df.empty
    assert len(df) >= 7
    assert "dependency_id" in df.columns
    assert "min_score" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_macro_event_news_quality_dependencies():
    df, _ = build_macro_event_news_quality_dependency_registry()
    summary = summarize_macro_event_news_quality_dependencies(df)
    assert summary["total_dependencies"] >= 7
    assert summary["min_required_score"] > 0
    assert summary["all_non_signal"] is True
