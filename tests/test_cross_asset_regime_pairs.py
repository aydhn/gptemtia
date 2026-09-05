"""Tests for Cross-Asset Regime Pairs."""

from advanced_cross_asset_regime_context.cross_asset_regime_pairs import (
    CANONICAL_PAIRS,
    build_cross_asset_regime_pair_registry,
)


def test_build_cross_asset_regime_pair_registry():
    assert len(CANONICAL_PAIRS) >= 10
    df, summary = build_cross_asset_regime_pair_registry()
    assert len(df) >= 10
    assert "pair_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["zero_arbitrage_claims"] is True
