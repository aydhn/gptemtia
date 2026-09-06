"""Tests for Phase 132 Macro Regime Entities."""

from advanced_macro_event_news_regime.macro_regime_entities import (
    build_macro_regime_entity_registry,
    summarize_macro_regime_entities,
)


def test_build_macro_regime_entities():
    df, summary = build_macro_regime_entity_registry()
    assert not df.empty
    assert len(df) >= 8
    assert "entity_type" in df.columns
    assert "inflation_indicator" in df["entity_type"].values
    assert "rate_indicator" in df["entity_type"].values
    assert "growth_indicator" in df["entity_type"].values
    assert summary["all_non_signal"] is True


def test_summarize_macro_regime_entities():
    df, _ = build_macro_regime_entity_registry()
    summary = summarize_macro_regime_entities(df)
    assert summary["total_macro_entities"] >= 8
    assert summary["entity_types"] >= 4
    assert summary["all_non_signal"] is True
