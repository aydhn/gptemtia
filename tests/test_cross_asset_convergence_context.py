"""Tests for Cross-Asset Convergence Context."""

from advanced_cross_asset_regime_context.cross_asset_convergence_context import (
    CONVERGENCE_CONTEXT_RECORDS,
    build_cross_asset_convergence_context_registry,
)


def test_build_cross_asset_convergence_context_registry():
    assert len(CONVERGENCE_CONTEXT_RECORDS) >= 3
    df, summary = build_cross_asset_convergence_context_registry()
    assert len(df) >= 3
    assert "convergence_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
    assert summary["zero_mean_reversion_strategies"] is True
