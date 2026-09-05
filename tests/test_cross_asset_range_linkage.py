"""Tests for Cross-Asset Range Linkage."""

from advanced_cross_asset_regime_context.cross_asset_range_linkage import (
    RANGE_LINKAGE_RECORDS,
    build_cross_asset_range_linkage_registry,
)


def test_build_cross_asset_range_linkage_registry():
    assert len(RANGE_LINKAGE_RECORDS) >= 4
    df, summary = build_cross_asset_range_linkage_registry()
    assert len(df) >= 4
    assert "linkage_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
    assert summary["mean_linkage_score"] > 0.0
