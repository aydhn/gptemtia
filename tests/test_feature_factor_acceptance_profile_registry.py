from advanced_feature_factor_acceptance.feature_factor_acceptance_profile_registry import (
    build_feature_factor_acceptance_profile_registry,
    summarize_feature_factor_acceptance_profile_registry,
)

def test_acceptance_profile_registry():
    df, summary = build_feature_factor_acceptance_profile_registry()
    assert not df.empty
    assert summary["total_profiles"] >= 3
    assert summary["current_phase"] == 125
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 126
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s = summarize_feature_factor_acceptance_profile_registry(df)
    assert s["total_profiles"] >= 3
    assert s["non_signal"] is True
