"""Tests for Commodity/Macro Regime Context."""

from advanced_cross_asset_regime_context.commodity_macro_regime_context import (
    COMMODITY_MACRO_CONTEXT_RECORDS,
    build_commodity_macro_regime_context_registry,
)


def test_build_commodity_macro_regime_context_registry():
    assert len(COMMODITY_MACRO_CONTEXT_RECORDS) >= 5
    df, summary = build_commodity_macro_regime_context_registry()
    assert len(df) >= 5
    assert "context_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
    assert summary["mean_readiness_score"] > 0.0
