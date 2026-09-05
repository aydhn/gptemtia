"""Tests for Cross-Asset Regime Safety Boundary."""

from advanced_cross_asset_regime_context.cross_asset_regime_safety_boundary import (
    NO_GO_CONDITIONS,
    SAFE_GO_CONDITIONS,
    build_cross_asset_regime_safety_boundary,
)


def test_cross_asset_regime_safety_boundary():
    assert len(NO_GO_CONDITIONS) == 18
    assert len(SAFE_GO_CONDITIONS) == 8
    df, summary = build_cross_asset_regime_safety_boundary()
    assert len(df) == 18
    assert summary["no_go_count"] == 18
    assert summary["safe_go_count"] == 8
    assert summary["safety_status"] == "SECURE"
    assert summary["all_no_go_enforced"] is True
    assert summary["live_trading_allowed"] is False
    assert summary["model_execution_allowed"] is False
