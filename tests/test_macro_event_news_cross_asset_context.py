"""Tests for Phase 132 Macro/Event/News Cross-Asset Context."""

from advanced_macro_event_news_regime.macro_event_news_cross_asset_context import (
    build_macro_event_news_cross_asset_context_registry,
    summarize_macro_event_news_cross_asset_context,
)


def test_build_macro_event_news_cross_asset_context():
    df, summary = build_macro_event_news_cross_asset_context_registry()
    assert not df.empty
    assert len(df) >= 7
    assert "cross_asset_context_id" in df.columns
    assert "target_asset_class" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_summarize_macro_event_news_cross_asset_context():
    df, _ = build_macro_event_news_cross_asset_context_registry()
    summary = summarize_macro_event_news_cross_asset_context(df)
    assert summary["total_contexts"] >= 7
    assert summary["asset_classes"] >= 3
    assert summary["all_non_signal"] is True
