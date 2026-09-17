"""Test suite for Phase 139 GPU Training Governance Domain Registry."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_domain_registry import (
    build_gpu_training_governance_domain_registry,
    summarize_gpu_training_governance_domains,
)


def test_build_gpu_training_governance_domain_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_governance_domain_registry(profile)

    assert len(df) >= 35
    assert summary["total_domains"] == len(df)
    assert summary["all_ready"] is True
    assert summary["all_dry_run"] is True
    assert summary["current_phase"] == 139
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 140
    assert summary["non_signal"] is True


def test_summarize_gpu_training_governance_domains():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_gpu_training_governance_domain_registry(profile)
    summary = summarize_gpu_training_governance_domains(df)

    assert summary["total_domains"] == len(df)
    assert summary["all_ready"] is True
    assert summary["non_signal"] is True
