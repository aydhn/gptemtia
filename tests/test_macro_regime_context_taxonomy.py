"""Tests for Phase 132 Macro Regime Context Taxonomy."""

from advanced_macro_event_news_regime.macro_regime_context_taxonomy import (
    build_macro_regime_context_taxonomy_registry,
    summarize_macro_regime_context_taxonomy,
)


def test_build_macro_regime_context_taxonomy():
    df, summary = build_macro_regime_context_taxonomy_registry()
    assert not df.empty
    assert len(df) >= 7
    assert "taxonomy_name" in df.columns
    assert "inflation_context" in df["taxonomy_name"].values
    assert "rate_context" in df["taxonomy_name"].values
    assert "growth_context" in df["taxonomy_name"].values
    assert summary["all_non_signal"] is True


def test_summarize_macro_context_taxonomy():
    df, _ = build_macro_regime_context_taxonomy_registry()
    summary = summarize_macro_regime_context_taxonomy(df)
    assert summary["total_taxonomies"] >= 7
    assert summary["all_non_signal"] is True
