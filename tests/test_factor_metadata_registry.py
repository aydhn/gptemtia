from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.factor_metadata_registry import (
    build_factor_metadata_registry,
    summarize_factor_metadata_registry,
)


def test_factor_metadata_registry():
    profile = get_default_feature_engine_profile()
    df, summary = build_factor_metadata_registry(profile)

    assert not df.empty
    assert len(df) >= 8
    assert "factor_id" in df.columns
    assert "future_phase_owner" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["target_phase_owner"] == "Phase 122"
