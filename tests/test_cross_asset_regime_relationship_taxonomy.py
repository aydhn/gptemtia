"""Tests for Cross-Asset Relationship Taxonomy."""

from advanced_cross_asset_regime_context.cross_asset_regime_relationship_taxonomy import (
    TAXONOMY_ITEMS,
    build_cross_asset_regime_relationship_taxonomy_registry,
)


def test_build_cross_asset_regime_relationship_taxonomy_registry():
    assert len(TAXONOMY_ITEMS) >= 10
    df, summary = build_cross_asset_regime_relationship_taxonomy_registry()
    assert len(df) >= 10
    assert "relationship_type" in df.columns
    assert summary["zero_trading_signals_allowed"] is True
    assert summary["zero_predictions_allowed"] is True
    assert summary["all_require_no_lookahead"] is True
