from advanced_feature_store_integration.feature_store_partition_policies import (
    build_feature_store_partition_policy_registry,
    summarize_feature_store_partition_policies,
)

def test_partition_policies():
    df, s = build_feature_store_partition_policy_registry()
    assert not df.empty
    assert s["total_partition_policies"] >= 6
    assert "by_source_phase" in s["supported_strategies"]
    assert "by_entity_type" in s["supported_strategies"]
    assert "by_feature_family" in s["supported_strategies"]
