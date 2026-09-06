"""Tests for Phase 132 Event Regime Context Taxonomy."""

from advanced_macro_event_news_regime.event_regime_context_taxonomy import (
    build_event_regime_context_taxonomy_registry,
    summarize_event_regime_context_taxonomy,
)


def test_build_event_regime_context_taxonomy():
    df, summary = build_event_regime_context_taxonomy_registry()
    assert not df.empty
    assert len(df) >= 7
    assert "taxonomy_name" in df.columns
    assert "scheduled_event_context" in df["taxonomy_name"].values
    assert "actual_release_context" in df["taxonomy_name"].values
    assert "pre_event_context" in df["taxonomy_name"].values
    assert "post_event_context" in df["taxonomy_name"].values
    assert summary["all_non_signal"] is True


def test_summarize_event_context_taxonomy():
    df, _ = build_event_regime_context_taxonomy_registry()
    summary = summarize_event_regime_context_taxonomy(df)
    assert summary["total_taxonomies"] >= 7
    assert summary["all_non_signal"] is True
