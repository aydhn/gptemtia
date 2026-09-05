"""Tests for Cross-Asset Trend Linkage."""

from advanced_cross_asset_regime_context.cross_asset_trend_linkage import (
    TREND_LINKAGE_RECORDS,
    build_cross_asset_trend_linkage_registry,
)


def test_build_cross_asset_trend_linkage_registry():
    assert len(TREND_LINKAGE_RECORDS) >= 4
    df, summary = build_cross_asset_trend_linkage_registry()
    assert len(df) >= 4
    assert "linkage_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
    assert summary["zero_directional_claims"] is True
