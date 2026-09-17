"""Test suite for Phase 139 GPU Training Runtime Dependencies."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_runtime_dependencies import (
    build_gpu_training_runtime_dependency_registry,
    summarize_gpu_training_runtime_dependencies,
)


def test_build_gpu_training_runtime_dependency_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_runtime_dependency_registry(profile)

    assert len(df) == 3
    assert summary["total_dependencies"] == 3
    assert summary["all_satisfied"] is True
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True


def test_summarize_gpu_training_runtime_dependencies():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_gpu_training_runtime_dependency_registry(profile)
    summary = summarize_gpu_training_runtime_dependencies(df)

    assert summary["total_dependencies"] == 3
    assert summary["all_satisfied"] is True
    assert summary["non_signal"] is True
