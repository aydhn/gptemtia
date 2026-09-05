"""Tests for Cross-Asset Regime Asof Join Policies."""

from advanced_cross_asset_regime_context.cross_asset_regime_asof_join_policies import (
    ASOF_JOIN_POLICIES,
    build_cross_asset_regime_asof_join_policy_registry,
)


def test_build_cross_asset_regime_asof_join_policy_registry():
    assert len(ASOF_JOIN_POLICIES) >= 2
    df, summary = build_cross_asset_regime_asof_join_policy_registry()
    assert len(df) >= 2
    assert "asof_policy_id" in df.columns
    assert summary["all_backward_direction"] is True
    assert summary["zero_forward_allowed"] is True
    assert summary["all_enforce_zero_lookahead"] is True
