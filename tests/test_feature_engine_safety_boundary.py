from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_safety_boundary import (
    build_feature_engine_safety_boundary,
    build_feature_engine_no_go_conditions,
    build_feature_engine_safe_go_conditions,
    summarize_feature_engine_safety_boundary,
)


def test_feature_engine_safety_boundary():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_engine_safety_boundary(profile)

    assert not df.empty
    assert len(df) >= 45
    assert summary["safety_status"] == "ACTIVE"
    assert summary["total_no_go_rules"] >= 35
    assert summary["total_safe_go_rules"] >= 10
    assert summary["all_no_go_enforced"] is True
    assert summary["current_phase"] == 116
    assert summary["target_final_phase"] == 160
