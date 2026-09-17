# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Labels and Taxonomies."""

from typing import List

GPU_TRAINING_GOVERNANCE_DOMAINS: List[str] = [
    "gpu_training_governance_profile_domain",
    "gpu_training_governance_domain",
    "resource_policy_domain",
    "device_selection_policy_domain",
    "memory_budget_policy_domain",
    "cpu_fallback_policy_domain",
    "timeout_policy_domain",
    "batch_size_placeholder_domain",
    "dataloader_placeholder_domain",
    "training_loop_stub_contract_domain",
    "harness_interface_domain",
    "harness_stub_domain",
    "dry_run_resource_check_domain",
    "dry_run_device_selection_domain",
    "dry_run_memory_guard_domain",
    "dry_run_timeout_guard_domain",
    "dry_run_execution_block_domain",
    "no_real_training_domain",
    "no_prediction_domain",
    "no_target_label_domain",
    "artifact_disabled_domain",
    "model_registry_write_disabled_domain",
    "dataset_dependency_domain",
    "baseline_model_dependency_domain",
    "runtime_dependency_domain",
    "featurestore_input_dependency_domain",
    "no_lookahead_guard_domain",
    "metadata_only_news_guard_domain",
    "source_preservation_guard_domain",
    "forbidden_column_policy_domain",
    "resource_audit_placeholder_domain",
    "experiment_audit_placeholder_domain",
    "manual_review_domain",
    "finding_domain",
    "readiness_score_domain",
    "manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_140_handoff_domain",
    "unknown_gpu_training_governance_domain",
]

GPU_TRAINING_GOVERNANCE_STATUS_LABELS: List[str] = [
    "gpu_governance_ready",
    "gpu_governance_ready_with_warnings",
    "gpu_governance_placeholder_only",
    "gpu_governance_manual_review_required",
    "gpu_governance_blocked_by_safety",
    "gpu_governance_unknown",
]

GPU_TRAINING_EXECUTION_LABELS: List[str] = [
    "execution_blocked_no_real_training",
    "execution_blocked_no_prediction",
    "execution_blocked_no_target_label",
    "execution_blocked_no_artifact",
    "execution_blocked_resource_policy",
    "execution_contract_only",
    "execution_unknown",
]


def list_gpu_training_governance_domain_labels() -> List[str]:
    """Return all valid GPU training governance domain labels."""
    return list(GPU_TRAINING_GOVERNANCE_DOMAINS)


def list_gpu_training_governance_status_labels() -> List[str]:
    """Return all valid GPU training governance status labels."""
    return list(GPU_TRAINING_GOVERNANCE_STATUS_LABELS)


def list_gpu_training_execution_labels() -> List[str]:
    """Return all valid GPU training execution labels."""
    return list(GPU_TRAINING_EXECUTION_LABELS)


def validate_gpu_training_governance_domain_label(label: str) -> bool:
    """Validate whether domain label belongs to known domains."""
    return label in GPU_TRAINING_GOVERNANCE_DOMAINS


def validate_gpu_training_governance_status_label(label: str) -> bool:
    """Validate whether status label belongs to known status labels."""
    return label in GPU_TRAINING_GOVERNANCE_STATUS_LABELS


def validate_gpu_training_execution_label(label: str) -> bool:
    """Validate whether execution label belongs to known execution labels."""
    return label in GPU_TRAINING_EXECUTION_LABELS
