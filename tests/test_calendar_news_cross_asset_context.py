"""Tests for Calendar/News Cross-Asset Context."""

from advanced_cross_asset_regime_context.calendar_news_cross_asset_context import (
    CALENDAR_NEWS_CONTEXT_RECORDS,
    build_calendar_news_cross_asset_context_registry,
)


def test_build_calendar_news_cross_asset_context_registry():
    assert len(CALENDAR_NEWS_CONTEXT_RECORDS) >= 4
    df, summary = build_calendar_news_cross_asset_context_registry()
    assert len(df) >= 4
    assert "context_id" in df.columns
    assert summary["all_metadata_only"] is True
    assert summary["zero_full_article_text"] is True
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
