"""Tests for Fusion Feature Profile Registry."""

from advanced_feature_fusion.fusion_feature_profile_registry import (
    build_fusion_feature_profile_registry,
    get_fusion_feature_profiles_registry,
    get_fusion_feature_profiles_summary,
)


def test_profile_registry():
    df, summary = build_fusion_feature_profile_registry()
    assert len(df) >= 3
    assert summary["total_profiles"] >= 3
    assert summary["status"] == "READY"
    assert summary["non_signal_mandate"] is True
    assert summary["dry_run_mandate"] is True


def test_helper_functions():
    df = get_fusion_feature_profiles_registry()
    assert not df.empty
    summary = get_fusion_feature_profiles_summary()
    assert summary["total_profiles"] == len(df)
