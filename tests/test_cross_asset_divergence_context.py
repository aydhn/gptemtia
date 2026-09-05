"""Tests for Cross-Asset Divergence Context."""

from advanced_cross_asset_regime_context.cross_asset_divergence_context import (
    DIVERGENCE_CONTEXT_RECORDS,
    build_cross_asset_divergence_context_registry,
)


def test_build_cross_asset_divergence_context_registry():
    assert len(DIVERGENCE_CONTEXT_RECORDS) >= 3
    df, summary = build_cross_asset_divergence_context_registry()
    assert len(df) >= 3
    assert "divergence_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
    assert summary["zero_pairs_trading_rules"] is True
