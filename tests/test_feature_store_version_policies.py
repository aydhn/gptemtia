from advanced_feature_store_integration.feature_store_version_policies import (
    build_feature_store_version_policy_registry,
    validate_store_version_policy,
    summarize_feature_store_version_policies,
)

def test_version_policies():
    df, s = build_feature_store_version_policy_registry()
    assert not df.empty
    assert s["total_version_policies"] >= 3
    assert s["destructive_overwrite_forbidden"] is True

    safe_policy = {"policy_name": "p1", "destructive_overwrite_allowed": False, "production_release_tag_allowed": False, "source_preserved": True}
    res_safe = validate_store_version_policy(safe_policy)
    assert res_safe["is_safe"] is True

    unsafe_policy = {"policy_name": "p2", "destructive_overwrite_allowed": True}
    res_unsafe = validate_store_version_policy(unsafe_policy)
    assert res_unsafe["is_safe"] is False
