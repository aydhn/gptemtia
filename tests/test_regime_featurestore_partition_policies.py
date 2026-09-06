"""Tests for Phase 134 Regime FeatureStore Partition Policies."""

from advanced_regime_featurestore_integration.regime_featurestore_partition_policies import (
    build_regime_featurestore_partition_policy_registry,
    summarize_regime_featurestore_partition_policies,
)


def test_partition_policies():
    df, summary = build_regime_featurestore_partition_policy_registry()
    assert not df.empty
    assert len(df) >= 6
    assert (df["non_signal"] == True).all()

    s_res = summarize_regime_featurestore_partition_policies(df)
    assert s_res["total_policies"] == len(df)
    assert s_res["all_non_signal"] is True
