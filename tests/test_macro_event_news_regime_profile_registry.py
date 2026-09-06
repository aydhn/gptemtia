"""Tests for Phase 132 Profile Registry."""

from advanced_macro_event_news_regime.macro_event_news_regime_profile_registry import (
    build_macro_event_news_regime_profile_registry,
    summarize_macro_event_news_regime_profiles,
)


def test_build_profile_registry():
    df, summary = build_macro_event_news_regime_profile_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["current_phase"] == 132
    assert summary["target_final_phase"] == 160


def test_summarize_profile_registry():
    df, _ = build_macro_event_news_regime_profile_registry()
    summary = summarize_macro_event_news_regime_profiles(df)
    assert summary["total_profiles"] >= 3
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True
