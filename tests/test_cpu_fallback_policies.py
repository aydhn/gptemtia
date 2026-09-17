"""Test suite for Phase 139 CPU Fallback Policies."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.cpu_fallback_policies import (
    build_cpu_fallback_policy_registry,
    summarize_cpu_fallback_policies,
)


def test_build_cpu_fallback_policy_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_cpu_fallback_policy_registry(profile)

    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["all_fallback_allowed"] is True
    assert summary["all_dry_run"] is True
    assert summary["non_signal"] is True


def test_summarize_cpu_fallback_policies():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_cpu_fallback_policy_registry(profile)
    summary = summarize_cpu_fallback_policies(df)

    assert summary["total_policies"] == 3
    assert summary["all_fallback_allowed"] is True
    assert summary["non_signal"] is True
