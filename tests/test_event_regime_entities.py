"""Tests for Phase 132 Event Regime Entities."""

from advanced_macro_event_news_regime.event_regime_entities import (
    build_event_regime_entity_registry,
    summarize_event_regime_entities,
)


def test_build_event_regime_entities():
    df, summary = build_event_regime_entity_registry()
    assert not df.empty
    assert len(df) >= 8
    assert "entity_type" in df.columns
    assert "calendar_event" in df["entity_type"].values
    assert "scheduled_release" in df["entity_type"].values
    assert "pre_event_window" in df["entity_type"].values
    assert "post_event_window" in df["entity_type"].values
    assert summary["all_non_signal"] is True


def test_summarize_event_regime_entities():
    df, _ = build_event_regime_entity_registry()
    summary = summarize_event_regime_entities(df)
    assert summary["total_event_entities"] >= 8
    assert summary["all_non_signal"] is True
