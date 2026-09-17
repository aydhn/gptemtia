# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Labels and Domain Taxonomy."""

from typing import List

# Domain labels
ENSEMBLE_MODEL_DOMAIN_LABELS: List[str] = [
    "ensemble_model_profile_domain",
    "ensemble_model_domain",
    "candidate_model_family_domain",
    "candidate_model_contract_domain",
    "candidate_model_input_contract_domain",
    "candidate_model_output_contract_domain",
    "candidate_model_eligibility_gate_domain",
    "candidate_model_compatibility_matrix_domain",
    "candidate_model_resource_dependency_domain",
    "candidate_model_dataset_dependency_domain",
    "candidate_model_baseline_dependency_domain",
    "candidate_model_gpu_governance_dependency_domain",
    "ensemble_strategy_contract_domain",
    "ensemble_voting_placeholder_domain",
    "ensemble_blending_placeholder_domain",
    "ensemble_stacking_placeholder_domain",
    "ensemble_weighting_policy_placeholder_domain",
    "ensemble_meta_model_placeholder_domain",
    "ensemble_selection_policy_domain",
    "ensemble_input_contract_domain",
    "ensemble_output_contract_domain",
    "ensemble_execution_disabled_domain",
    "candidate_training_disabled_domain",
    "candidate_prediction_disabled_domain",
    "candidate_target_label_disabled_domain",
    "candidate_artifact_disabled_domain",
    "candidate_registry_write_disabled_domain",
    "ensemble_metric_placeholder_domain",
    "ensemble_evaluation_placeholder_domain",
    "validation_dependency_domain",
    "quality_dependency_domain",
    "lineage_domain",
    "experiment_linkage_domain",
    "no_lookahead_guard_domain",
    "metadata_only_news_guard_domain",
    "source_preservation_guard_domain",
    "forbidden_column_policy_domain",
    "audit_placeholder_domain",
    "manual_review_domain",
    "finding_domain",
    "readiness_score_domain",
    "manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_141_handoff_domain",
    "unknown_ensemble_model_domain",
]

# Status labels
ENSEMBLE_MODEL_STATUS_LABELS: List[str] = [
    "ensemble_contract_ready",
    "ensemble_contract_ready_with_warnings",
    "ensemble_contract_placeholder_only",
    "ensemble_contract_manual_review_required",
    "ensemble_contract_blocked_by_safety",
    "ensemble_contract_unknown",
]

# Candidate model status labels
CANDIDATE_MODEL_STATUS_LABELS: List[str] = [
    "candidate_metadata_ready",
    "contract_registered",
    "candidate_contract_placeholder_only",
    "candidate_contract_manual_review_required",
    "candidate_contract_blocked_by_safety",
    "candidate_contract_unknown",
]

# Execution labels
ENSEMBLE_EXECUTION_LABELS: List[str] = [
    "execution_blocked_no_training",
    "execution_blocked_no_prediction",
    "execution_blocked_no_ensemble",
    "execution_blocked_no_calibration",
    "execution_blocked_no_target_label",
    "execution_blocked_no_artifact",
    "execution_contract_only",
    "execution_unknown",
]

# Aliases
ENSEMBLE_MODEL_DOMAINS = ENSEMBLE_MODEL_DOMAIN_LABELS
CANDIDATE_MODEL_STATUSES = CANDIDATE_MODEL_STATUS_LABELS
ENSEMBLE_MODEL_STATUSES = ENSEMBLE_MODEL_STATUS_LABELS


def list_ensemble_model_domain_labels() -> List[str]:
    """List all registered domain labels."""
    return list(ENSEMBLE_MODEL_DOMAIN_LABELS)


def list_ensemble_model_status_labels() -> List[str]:
    """List all registered status labels."""
    return list(ENSEMBLE_MODEL_STATUS_LABELS)


def list_candidate_model_status_labels() -> List[str]:
    """List all registered candidate model status labels."""
    return list(CANDIDATE_MODEL_STATUS_LABELS)


def list_ensemble_execution_labels() -> List[str]:
    """List all registered execution labels."""
    return list(ENSEMBLE_EXECUTION_LABELS)


def validate_ensemble_model_domain_label(label: str) -> bool:
    """Validate whether label is a recognized domain label."""
    return label in ENSEMBLE_MODEL_DOMAIN_LABELS


validate_ensemble_domain_label = validate_ensemble_model_domain_label


def validate_ensemble_model_status_label(label: str) -> bool:
    """Validate whether label is a recognized status label."""
    return label in ENSEMBLE_MODEL_STATUS_LABELS


def validate_candidate_model_status_label(label: str) -> bool:
    """Validate whether label is a recognized candidate model status label."""
    return label in CANDIDATE_MODEL_STATUS_LABELS


def validate_ensemble_execution_label(label: str) -> bool:
    """Validate whether label is a recognized execution label."""
    return label in ENSEMBLE_EXECUTION_LABELS

