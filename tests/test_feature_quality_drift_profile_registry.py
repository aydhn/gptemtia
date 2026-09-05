import pytest
from advanced_feature_quality_drift.feature_quality_drift_profile_registry import build_feature_quality_drift_profile_registry


def test_build_feature_quality_drift_profile_registry():
    df, summary = build_feature_quality_drift_profile_registry()
    assert not df.empty
    assert summary["total_profiles"] >= 3
    assert summary["current_phase"] == 123
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 124
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["local_only"] is True
    assert summary["research_only"] is True

    profile_names = list(df["profile_name"])
    assert "balanced_local_feature_quality_drift" in profile_names
    assert "strict_non_signal_quality_drift_safety" in profile_names
    assert "dry_run_quality_drift_diagnostics_focus" in profile_names
