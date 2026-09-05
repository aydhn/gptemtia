from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_metadata_registry import (
    build_feature_metadata_registry,
    summarize_feature_metadata_registry,
)


def test_feature_metadata_registry():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_metadata_registry(profile)

    assert not df.empty
    assert len(df) >= 15
    assert "schema_id" in df.columns
    assert "warmup_rows_required" in df.columns
    assert "lookahead_bias_risk" in df.columns
    assert summary["all_guarded_against_lookahead"] is True
    assert summary["all_non_signal"] is True
