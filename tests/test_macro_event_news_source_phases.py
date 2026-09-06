"""Tests for Phase 132 Macro/Event/News Source Phases."""

from advanced_macro_event_news_regime.macro_event_news_source_phases import (
    build_macro_event_news_source_phase_registry,
    summarize_macro_event_news_source_phases,
)


def test_build_macro_event_news_source_phases():
    df, summary = build_macro_event_news_source_phase_registry()
    assert not df.empty
    assert len(df) >= 10
    assert "phase_number" in df.columns
    assert "phase_name" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_macro_event_news_source_phases():
    df, _ = build_macro_event_news_source_phase_registry()
    summary = summarize_macro_event_news_source_phases(df)
    assert summary["total_phases"] >= 10
    assert summary["min_phase"] == 120
    assert summary["max_phase"] == 131
    assert summary["all_non_signal"] is True
