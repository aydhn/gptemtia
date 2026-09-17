"""Test suite for Phase 139 GPU Training Governance Profile Registry."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_profile_registry import (
    build_gpu_training_governance_profile_registry,
    summarize_gpu_training_governance_profiles,
)


def test_build_gpu_training_governance_profile_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_governance_profile_registry(profile)

    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["active_profile"] == "balanced_local_gpu_training_governance"
    assert summary["all_dry_run"] is True
    assert summary["all_no_real_training"] is True
    assert summary["all_no_prediction"] is True
    assert summary["all_no_artifact_persistence"] is True
    assert summary["all_no_registry_write"] is True
    assert summary["current_phase"] == 139
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 140
    assert summary["non_signal"] is True


def test_summarize_gpu_training_governance_profiles():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_gpu_training_governance_profile_registry(profile)
    summary = summarize_gpu_training_governance_profiles(df)

    assert summary["total_profiles"] == 3
    assert summary["non_signal"] is True
