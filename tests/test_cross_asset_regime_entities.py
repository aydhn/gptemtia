"""Tests for Cross-Asset Regime Entities."""

from advanced_cross_asset_regime_context.cross_asset_regime_entities import (
    CANONICAL_ENTITIES,
    build_cross_asset_regime_entity_registry,
)


def test_build_cross_asset_regime_entity_registry():
    assert len(CANONICAL_ENTITIES) >= 25
    df, summary = build_cross_asset_regime_entity_registry()
    assert len(df) >= 25
    assert "entity_id" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True
