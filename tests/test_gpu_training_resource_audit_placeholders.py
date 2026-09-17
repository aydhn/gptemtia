"""Test suite for Phase 139 GPU Training Resource Audit Placeholders."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_resource_audit_placeholders import (
    build_gpu_training_resource_audit_placeholder_registry,
    summarize_gpu_training_resource_audit_placeholders,
)


def test_build_gpu_training_resource_audit_placeholder_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_resource_audit_placeholder_registry(profile)

    assert len(df) == 2
    assert summary["total_placeholders"] == 2
    assert summary["all_dry_run"] is True
    assert summary["all_training_disabled"] is True
    assert summary["all_artifact_disabled"] is True
    assert summary["non_signal"] is True


def test_summarize_gpu_training_resource_audit_placeholders():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_gpu_training_resource_audit_placeholder_registry(profile)
    summary = summarize_gpu_training_resource_audit_placeholders(df)

    assert summary["total_placeholders"] == 2
    assert summary["all_dry_run"] is True
    assert summary["non_signal"] is True
