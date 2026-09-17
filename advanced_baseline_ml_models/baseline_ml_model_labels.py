# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Labels and Domain Taxonomy.

Defines standardized taxonomy and validation functions for baseline ML model domains,
contract statuses, and execution states.
"""

from typing import List

BASELINE_ML_MODEL_DOMAIN_LABELS: List[str] = [
    "baseline_ml_model_profile_domain",
    "baseline_ml_model_domain",
    "model_family_domain",
    "model_contract_domain",
    "model_input_contract_domain",
    "model_output_contract_domain",
    "training_plan_domain",
    "dry_run_harness_contract_domain",
    "dry_run_harness_interface_domain",
    "trainer_stub_domain",
    "dry_run_policy_domain",
    "no_real_training_domain",
    "no_prediction_domain",
    "no_target_label_domain",
    "artifact_disabled_domain",
    "model_registry_write_disabled_domain",
    "metric_placeholder_domain",
    "evaluation_placeholder_domain",
    "validation_dependency_domain",
    "quality_dependency_domain",
    "lineage_domain",
    "featurestore_input_domain",
    "regime_input_domain",
    "no_lookahead_guard_domain",
    "metadata_only_news_guard_domain",
    "source_preservation_guard_domain",
    "forbidden_column_policy_domain",
    "experiment_linkage_domain",
    "manual_review_domain",
    "finding_domain",
    "readiness_score_domain",
    "manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_139_handoff_domain",
    "unknown_baseline_ml_model_domain",
]

BASELINE_ML_MODEL_STATUS_LABELS: List[str] = [
    "baseline_contract_ready",
    "baseline_contract_ready_with_warnings",
    "baseline_contract_placeholder_only",
    "baseline_contract_manual_review_required",
    "baseline_contract_blocked_by_safety",
    "baseline_contract_unknown",
]

BASELINE_EXECUTION_LABELS: List[str] = [
    "execution_blocked_no_real_training",
    "execution_blocked_no_prediction",
    "execution_blocked_no_target_label",
    "execution_blocked_no_artifact",
    "execution_contract_only",
    "execution_unknown",
]


def list_baseline_ml_model_domain_labels() -> List[str]:
    """Return all valid baseline ML model domain labels."""
    return list(BASELINE_ML_MODEL_DOMAIN_LABELS)


def list_baseline_ml_model_status_labels() -> List[str]:
    """Return all valid baseline contract status labels."""
    return list(BASELINE_ML_MODEL_STATUS_LABELS)


def list_baseline_execution_labels() -> List[str]:
    """Return all valid execution labels."""
    return list(BASELINE_EXECUTION_LABELS)


def validate_baseline_ml_model_domain_label(label: str) -> bool:
    """Validate a baseline ML model domain label."""
    return label in BASELINE_ML_MODEL_DOMAIN_LABELS


def validate_baseline_ml_model_status_label(label: str) -> bool:
    """Validate a baseline contract status label."""
    return label in BASELINE_ML_MODEL_STATUS_LABELS


def validate_baseline_execution_label(label: str) -> bool:
    """Validate an execution label."""
    return label in BASELINE_EXECUTION_LABELS
