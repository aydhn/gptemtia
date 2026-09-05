import pytest
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.phase_123_handoff import (
    build_phase_123_feature_quality_drift_handoff_report,
    summarize_phase_123_handoff,
)


def test_build_phase_123_handoff():
    profile = get_default_factor_metadata_profile()
    df, summary = build_phase_123_feature_quality_drift_handoff_report(profile)
    assert not df.empty
    assert summary["source_phase"] == 122
    assert summary["next_phase"] == 123
    assert summary["target_final_phase"] == 160
    assert summary["total_items"] >= 10
    assert summary["ready_items"] == summary["total_items"]
    assert summary["handoff_status"] == "READY"
    assert summary["non_signal"] is True

    topics = list(df["topic"])
    assert "factor_level_missingness_diagnostics_prerequisites" in topics
    assert "factor_level_infinite_value_diagnostics_prerequisites" in topics
    assert "factor_level_duplicate_namespace_diagnostics_prerequisites" in topics
    assert "factor_level_stability_diagnostics_prerequisites" in topics
    assert "factor_level_drift_diagnostics_prerequisites" in topics

    stats = summarize_phase_123_handoff(df)
    assert stats["handoff_status"] == "READY"
    assert stats["source_phase"] == 122
    assert stats["next_phase"] == 123
