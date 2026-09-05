from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_profile_registry import (
    build_feature_engine_profile_registry,
    summarize_feature_engine_profile_registry,
)


def test_feature_engine_profile_registry():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_engine_profile_registry(profile)

    assert not df.empty
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert "non_signal" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_local_only"] is True
    assert summary["current_phase"] == 116
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 117
