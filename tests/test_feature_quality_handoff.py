from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_quality_handoff import (
    build_feature_quality_handoff_registry,
    summarize_feature_quality_handoff,
)


def test_feature_quality_handoff():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_quality_handoff_registry(profile)

    assert not df.empty
    assert len(df) >= 8
    assert "handoff_area" in df.columns
    assert "source_phase" in df.columns
    assert "target_phase" in df.columns
    assert summary["all_handoff_defined"] is True
