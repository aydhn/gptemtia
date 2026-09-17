"""Test suite for Phase 139 Dataloader Placeholder Policies."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.dataloader_placeholder_policies import (
    build_dataloader_placeholder_policy_registry,
    summarize_dataloader_placeholder_policies,
)


def test_build_dataloader_placeholder_policy_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_dataloader_placeholder_policy_registry(profile)

    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["all_reads_real_data_disabled"] is True
    assert summary["all_shuffle_disabled"] is True
    assert summary["all_dry_run"] is True
    assert summary["non_signal"] is True


def test_summarize_dataloader_placeholder_policies():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_dataloader_placeholder_policy_registry(profile)
    summary = summarize_dataloader_placeholder_policies(df)

    assert summary["total_policies"] == 3
    assert summary["all_reads_real_data_disabled"] is True
    assert summary["non_signal"] is True
