"""Tests for Cross-Asset Regime Profile Registry."""

from advanced_cross_asset_regime_context.cross_asset_regime_profile_registry import (
    build_cross_asset_regime_profile_registry,
)


def test_build_cross_asset_regime_profile_registry():
    df, summary = build_cross_asset_regime_profile_registry()
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert summary["total_profiles"] >= 3
    assert summary["all_local_only"] is True
    assert summary["all_non_signal"] is True
    assert summary["zero_trading_allowed"] is True
