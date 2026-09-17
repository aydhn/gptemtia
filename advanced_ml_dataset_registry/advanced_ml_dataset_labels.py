# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Label definitions and validation helpers.

Constraints:
  current_phase=137, target_final_phase=160, next_phase=138
  dry_run=True, local_only=True, non_production=True, research_only=True
  All live/broker/training/prediction/materialization flags = False
  Label sets are static str-literal lists - no IO, no model calls.
"""

from typing import Dict, List


# ---------------------------------------------------------------------------
# Label sets
# ---------------------------------------------------------------------------

ADVANCED_ML_DATASET_PROFILE_DOMAIN_LABELS: List[str] = [
    "balanced_local_ml_dataset_contracts",
    "strict_no_materialization_no_training_dataset_safety",
    "dry_run_experiment_registry_focus",
]

ADVANCED_ML_DATASET_DOMAIN_LABELS: List[str] = [
    "advanced_ml_dataset_profile_domain",
    "advanced_ml_dataset_domain",
    "dataset_contract_domain",
    "dataset_source_catalog_domain",
    "dataset_schema_domain",
    "feature_namespace_domain",
    "dataset_version_policy_domain",
    "dataset_partition_policy_domain",
    "time_index_policy_domain",
    "time_series_split_policy_domain",
    "walk_forward_split_policy_domain",
    "purged_split_placeholder_domain",
    "leakage_guard_domain",
    "no_lookahead_guard_domain",
    "metadata_only_news_guard_domain",
    "source_preservation_guard_domain",
    "forbidden_column_policy_domain",
    "target_label_disabled_policy_domain",
    "feature_snapshot_contract_domain",
    "feature_snapshot_manifest_placeholder_domain",
    "quality_gate_domain",
    "validation_dependency_domain",
    "quality_dependency_domain",
    "lineage_domain",
    "experiment_registry_domain",
    "experiment_template_domain",
    "experiment_permission_domain",
    "run_plan_placeholder_domain",
    "model_family_placeholder_domain",
    "metric_placeholder_domain",
    "training_harness_disabled_domain",
    "prediction_disabled_domain",
    "artifact_disabled_domain",
    "manual_review_domain",
    "finding_domain",
    "readiness_score_domain",
    "manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_138_handoff_domain",
    "unknown_advanced_ml_dataset_domain",
]

ML_DATASET_STATUS_LABELS: List[str] = [
    "dataset_contract_ready",
    "dataset_contract_ready_with_warnings",
    "dataset_contract_placeholder_only",
    "dataset_contract_manual_review_required",
    "dataset_contract_blocked_by_safety",
    "dataset_contract_unknown",
]

ML_EXPERIMENT_PERMISSION_LABELS: List[str] = [
    "experiment_metadata_only_allowed",
    "experiment_contract_only_allowed",
    "experiment_training_blocked",
    "experiment_prediction_blocked",
    "experiment_materialization_blocked",
    "experiment_artifact_blocked",
    "experiment_unknown",
]


# ---------------------------------------------------------------------------
# List helpers
# ---------------------------------------------------------------------------

def list_advanced_ml_dataset_domain_labels() -> List[str]:
    """Return all known Advanced ML Dataset domain labels.

    Returns
    -------
    List[str]
        Copy of :data:`ADVANCED_ML_DATASET_DOMAIN_LABELS`.
    """
    return list(ADVANCED_ML_DATASET_DOMAIN_LABELS)


def list_advanced_ml_dataset_status_labels() -> List[str]:
    """Return all known ML Dataset status labels.

    Returns
    -------
    List[str]
        Copy of :data:`ML_DATASET_STATUS_LABELS`.
    """
    return list(ML_DATASET_STATUS_LABELS)


def list_ml_experiment_permission_labels() -> List[str]:
    """Return all known ML experiment permission labels.

    Returns
    -------
    List[str]
        Copy of :data:`ML_EXPERIMENT_PERMISSION_LABELS`.
    """
    return list(ML_EXPERIMENT_PERMISSION_LABELS)


# ---------------------------------------------------------------------------
# Validate helpers
# ---------------------------------------------------------------------------

def validate_advanced_ml_dataset_domain_label(label: str) -> bool:
    """Check whether *label* is a known Advanced ML Dataset domain label."""
    return label in ADVANCED_ML_DATASET_DOMAIN_LABELS


def validate_advanced_ml_dataset_status_label(label: str) -> bool:
    """Check whether *label* is a known ML Dataset status label."""
    return label in ML_DATASET_STATUS_LABELS


def validate_ml_experiment_permission_label(label: str) -> bool:
    """Check whether *label* is a known ML experiment permission label."""
    return label in ML_EXPERIMENT_PERMISSION_LABELS
