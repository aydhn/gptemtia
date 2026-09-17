"""Test suite for Phase 139 GPU Training Governance Labels."""

from advanced_gpu_training_governance.gpu_training_governance_labels import (
    list_gpu_training_execution_labels,
    list_gpu_training_governance_domain_labels,
    list_gpu_training_governance_status_labels,
    validate_gpu_training_execution_label,
    validate_gpu_training_governance_domain_label,
    validate_gpu_training_governance_status_label,
)


def test_domain_labels():
    domains = list_gpu_training_governance_domain_labels()
    assert len(domains) >= 30
    assert "gpu_training_governance_domain" in domains
    assert "resource_policy_domain" in domains
    assert "device_selection_policy_domain" in domains
    assert "memory_budget_policy_domain" in domains
    assert "cpu_fallback_policy_domain" in domains
    assert "timeout_policy_domain" in domains
    assert "phase_140_handoff_domain" in domains

    assert validate_gpu_training_governance_domain_label("resource_policy_domain") is True
    assert validate_gpu_training_governance_domain_label("invalid_random_domain") is False


def test_status_labels():
    statuses = list_gpu_training_governance_status_labels()
    assert "gpu_governance_ready" in statuses
    assert "gpu_governance_blocked_by_safety" in statuses

    assert validate_gpu_training_governance_status_label("gpu_governance_ready") is True
    assert validate_gpu_training_governance_status_label("unknown_status_xyz") is False


def test_execution_labels():
    exec_labels = list_gpu_training_execution_labels()
    assert "execution_blocked_no_real_training" in exec_labels
    assert "execution_contract_only" in exec_labels

    assert validate_gpu_training_execution_label("execution_blocked_no_real_training") is True
    assert validate_gpu_training_execution_label("unauthorized_execution") is False
