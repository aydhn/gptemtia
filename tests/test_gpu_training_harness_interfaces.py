"""Test suite for Phase 139 GPU Training Harness Interfaces."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_harness_interfaces import (
    build_gpu_training_harness_interface_registry,
    summarize_gpu_training_harness_interfaces,
)


def test_build_gpu_training_harness_interface_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_harness_interface_registry(profile)

    assert len(df) == 8
    assert summary["total_interfaces"] == 8
    assert summary["all_enforces_dry_run"] is True
    assert summary["all_real_training_disabled"] is True
    assert summary["non_signal"] is True


def test_summarize_gpu_training_harness_interfaces():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_gpu_training_harness_interface_registry(profile)
    summary = summarize_gpu_training_harness_interfaces(df)

    assert summary["total_interfaces"] == 8
    assert summary["all_enforces_dry_run"] is True
    assert summary["non_signal"] is True
