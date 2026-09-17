"""Test suite for Phase 138 Baseline ML Model Profile Registry."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_profile_registry import (
    build_baseline_ml_model_profile_registry,
    summarize_baseline_ml_model_profiles,
)


def test_build_profile_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_baseline_ml_model_profile_registry(profile)

    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["all_dry_run"] is True
    assert summary["zero_real_training"] is True
    assert summary["zero_prediction"] is True
    assert summary["non_signal"] is True
    assert "profile_name" in df.columns
    assert "dry_run_default" in df.columns
    assert "allow_real_model_training" in df.columns


def test_summarize_profiles():
    profile = get_default_baseline_ml_model_profile()
    df, _ = build_baseline_ml_model_profile_registry(profile)
    summary = summarize_baseline_ml_model_profiles(df)
    assert summary["total_profiles"] == 3
    assert summary["enabled_profiles"] == 3
    assert summary["all_dry_run"] is True
