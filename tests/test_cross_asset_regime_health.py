"""Tests for Cross-Asset Regime Health Check."""

from advanced_cross_asset_regime_context.cross_asset_regime_health import (
    build_cross_asset_regime_health_check,
)


def test_build_cross_asset_regime_health_check():
    df, summary = build_cross_asset_regime_health_check()
    assert len(df) >= 10
    assert summary["overall_status"] == "HEALTHY"
    assert summary["all_healthy"] is True
    assert summary["degraded_checks"] == 0
