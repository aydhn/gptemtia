"""Tests for Macro/Calendar Cross-Asset Context."""

from advanced_cross_asset_regime_context.macro_calendar_cross_asset_context import (
    MACRO_CALENDAR_CONTEXT_RECORDS,
    build_macro_calendar_cross_asset_context_registry,
)


def test_build_macro_calendar_cross_asset_context_registry():
    assert len(MACRO_CALENDAR_CONTEXT_RECORDS) >= 4
    df, summary = build_macro_calendar_cross_asset_context_registry()
    assert len(df) >= 4
    assert "context_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
