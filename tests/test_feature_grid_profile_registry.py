from advanced_feature_grid.feature_grid_profile_registry import build_feature_grid_profile_registry
from advanced_feature_grid.feature_grid_config import get_default_feature_grid_profile


def test_feature_grid_profile_registry():
    profile = get_default_feature_grid_profile()
    df, summary = build_feature_grid_profile_registry(profile)

    assert not df.empty
    assert summary["total_profiles"] == len(df)
    assert summary["current_phase"] == 118
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 119
    assert summary["local_only"] is True
    assert summary["research_only"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"
