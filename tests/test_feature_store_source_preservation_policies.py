from advanced_feature_store_integration.feature_store_source_preservation_policies import (
    build_feature_store_source_preservation_policy_registry,
    validate_source_preservation_policy,
    summarize_feature_store_source_preservation_policies,
)

def test_source_preservation_policies():
    df, s = build_feature_store_source_preservation_policy_registry()
    assert not df.empty
    assert s["source_preserved"] is True
    assert s["destructive_action_allowed"] is False

    safe_action = "append_snapshot"
    assert validate_source_preservation_policy(safe_action)["is_safe"] is True

    prohibited_action = "overwrite_source"
    assert validate_source_preservation_policy(prohibited_action)["is_safe"] is False
    assert validate_source_preservation_policy("delete_source")["is_safe"] is False
    assert validate_source_preservation_policy("destructive_clean")["is_safe"] is False
    assert validate_source_preservation_policy("auto_impute_overwrite")["is_safe"] is False
    assert validate_source_preservation_policy("auto_drop_feature")["is_safe"] is False
