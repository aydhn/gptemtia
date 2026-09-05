"""Tests for Cross-Asset Regime Quality Dependencies."""

from advanced_cross_asset_regime_context.cross_asset_regime_quality_dependencies import (
    QUALITY_DEPENDENCIES,
    build_cross_asset_regime_quality_dependency_registry,
)


def test_build_cross_asset_regime_quality_dependency_registry():
    assert len(QUALITY_DEPENDENCIES) >= 5
    df, summary = build_cross_asset_regime_quality_dependency_registry()
    assert len(df) >= 5
    assert "quality_dep_id" in df.columns
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
