"""Tests for Cross-Asset Regime Validation Dependencies."""

from advanced_cross_asset_regime_context.cross_asset_regime_validation_dependencies import (
    VALIDATION_DEPENDENCIES,
    build_cross_asset_regime_validation_dependency_registry,
)


def test_build_cross_asset_regime_validation_dependency_registry():
    assert len(VALIDATION_DEPENDENCIES) >= 5
    df, summary = build_cross_asset_regime_validation_dependency_registry()
    assert len(df) >= 5
    assert "dependency_id" in df.columns
    assert summary["all_verified"] is True
    assert summary["all_non_signal"] is True
