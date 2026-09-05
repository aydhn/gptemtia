"""Tests for Cross-Asset Regime Context Contracts."""

from advanced_cross_asset_regime_context.cross_asset_regime_context_contracts import (
    CONTEXT_CONTRACTS,
    build_cross_asset_regime_context_contract_registry,
)


def test_build_cross_asset_regime_context_contract_registry():
    assert len(CONTEXT_CONTRACTS) >= 5
    df, summary = build_cross_asset_regime_context_contract_registry()
    assert len(df) >= 5
    assert "contract_name" in df.columns
    assert summary["all_non_signal_required"] is True
    assert summary["all_no_lookahead_required"] is True
    assert summary["all_source_preserved"] is True
