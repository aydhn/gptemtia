from advanced_feature_store_integration.feature_store_integration_safety_boundary import (
    build_feature_store_integration_safety_boundary,
    build_feature_store_integration_no_go_conditions,
    build_feature_store_integration_safe_go_conditions,
    summarize_feature_store_integration_safety_boundary,
)

def test_safety_boundary():
    df_no_go = build_feature_store_integration_no_go_conditions()
    assert len(df_no_go) >= 15

    df_safe_go = build_feature_store_integration_safe_go_conditions()
    assert len(df_safe_go) >= 8

    df, s = build_feature_store_integration_safety_boundary()
    assert not df.empty
    assert s["safety_status"] == "SECURE"
    assert s["non_signal"] is True
    assert s["source_preserved"] is True
    assert s["destructive_action_allowed"] is False
