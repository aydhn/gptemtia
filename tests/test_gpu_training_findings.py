"""Test suite for Phase 139 GPU Training Findings."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_findings import (
    build_gpu_training_findings_registry,
    create_gpu_training_finding,
    summarize_gpu_training_findings,
)


def test_build_gpu_training_findings_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_findings_registry(profile)

    assert len(df) == 3
    assert summary["total_findings"] == 3
    assert summary["critical_count"] == 0
    assert summary["destructive_allowed"] is False
    assert summary["auto_fix_allowed"] is False
    assert summary["non_signal"] is True


def test_create_gpu_training_finding():
    f = create_gpu_training_finding(
        finding_type="test_finding",
        governance_domain="resource_policy_domain",
        severity_label="INFO",
        message="test message",
        recommendation="test rec",
    )
    assert f.finding_type == "test_finding"
    assert f.severity_label == "INFO"
    assert f.destructive_action_allowed is False
    assert f.auto_fix_allowed is False
    assert f.non_signal is True
