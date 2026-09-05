"""Tests for FX/Macro Regime Context."""

from advanced_cross_asset_regime_context.fx_macro_regime_context import (
    FX_MACRO_CONTEXT_RECORDS,
    build_fx_macro_regime_context_registry,
)


def test_build_fx_macro_regime_context_registry():
    assert len(FX_MACRO_CONTEXT_RECORDS) >= 5
    df, summary = build_fx_macro_regime_context_registry()
    assert len(df) >= 5
    assert "context_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_signals"] is True
    assert summary["all_source_preserved"] is True
