from advanced_feature_store_integration.feature_store_integration_profile_registry import (
    build_feature_store_integration_profile_registry,
    summarize_feature_store_integration_profile_registry,
)

def test_profile_registry():
    df, s = build_feature_store_integration_profile_registry()
    assert not df.empty
    assert s["total_profiles"] >= 3
    assert s["current_phase"] == 124
    assert s["target_final_phase"] == 160
    assert s["next_phase"] == 125
    assert s["non_signal"] is True
    assert s["source_preserved"] is True
    summary = summarize_feature_store_integration_profile_registry(df)
    assert summary["total_profiles"] >= 3
