"""Tests for Cross-Asset Regime Timestamp Policies."""

from advanced_cross_asset_regime_context.cross_asset_regime_timestamp_policies import (
    TIMESTAMP_POLICIES,
    build_cross_asset_regime_timestamp_policy_registry,
)


def test_build_cross_asset_regime_timestamp_policy_registry():
    assert len(TIMESTAMP_POLICIES) >= 3
    df, summary = build_cross_asset_regime_timestamp_policy_registry()
    assert len(df) >= 3
    assert "policy_id" in df.columns
    assert summary["all_utc"] is True
    assert summary["all_enforce_no_future_leakage"] is True
