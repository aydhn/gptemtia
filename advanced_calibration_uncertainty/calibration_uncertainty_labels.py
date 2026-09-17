# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Domain, Status, and Execution Labels."""

from typing import List

CALIBRATION_UNCERTAINTY_DOMAINS: List[str] = [
    "calibration_uncertainty_profile_domain",
    "calibration_uncertainty_domain",
    "probability_calibration_contract_domain",
    "calibration_method_placeholder_domain",
    "calibration_input_contract_domain",
    "calibration_output_contract_domain",
    "calibration_execution_disabled_domain",
    "calibration_fit_disabled_domain",
    "calibration_transform_disabled_domain",
    "probability_prediction_disabled_domain",
    "uncertainty_estimation_contract_domain",
    "uncertainty_method_placeholder_domain",
    "uncertainty_input_contract_domain",
    "uncertainty_output_contract_domain",
    "uncertainty_execution_disabled_domain",
    "confidence_score_placeholder_domain",
    "confidence_interval_placeholder_domain",
    "prediction_interval_placeholder_domain",
    "quantile_placeholder_domain",
    "conformal_prediction_placeholder_domain",
    "calibration_metric_placeholder_domain",
    "uncertainty_metric_placeholder_domain",
    "calibration_evaluation_placeholder_domain",
    "uncertainty_evaluation_placeholder_domain",
    "calibration_quality_gate_domain",
    "uncertainty_quality_gate_domain",
    "candidate_model_dependency_domain",
    "ensemble_dependency_domain",
    "dataset_dependency_domain",
    "runtime_dependency_domain",
    "calibration_no_lookahead_guard_domain",
    "calibration_metadata_only_news_guard_domain",
    "calibration_source_preservation_guard_domain",
    "calibration_forbidden_column_policy_domain",
    "uncertainty_no_lookahead_guard_domain",
    "uncertainty_metadata_only_news_guard_domain",
    "uncertainty_source_preservation_guard_domain",
    "uncertainty_forbidden_column_policy_domain",
    "lineage_domain",
    "experiment_linkage_domain",
    "audit_placeholder_domain",
    "manual_review_domain",
    "finding_domain",
    "readiness_score_domain",
    "manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_142_handoff_domain",
    "unknown_calibration_uncertainty_domain",
]

CALIBRATION_UNCERTAINTY_STATUS_LABELS: List[str] = [
    "calibration_contract_ready",
    "calibration_contract_ready_with_warnings",
    "calibration_contract_placeholder_only",
    "calibration_contract_manual_review_required",
    "calibration_contract_blocked_by_safety",
    "calibration_contract_unknown",
]

CALIBRATION_UNCERTAINTY_EXECUTION_LABELS: List[str] = [
    "execution_blocked_no_probability_prediction",
    "execution_blocked_no_calibration_fit",
    "execution_blocked_no_calibration_transform",
    "execution_blocked_no_uncertainty_estimation",
    "execution_blocked_no_prediction_interval",
    "execution_blocked_no_conformal_prediction",
    "execution_contract_only",
    "execution_unknown",
]


def list_calibration_uncertainty_domain_labels() -> List[str]:
    """Return all valid domain labels."""
    return list(CALIBRATION_UNCERTAINTY_DOMAINS)


def list_calibration_uncertainty_status_labels() -> List[str]:
    """Return all valid status labels."""
    return list(CALIBRATION_UNCERTAINTY_STATUS_LABELS)


def list_calibration_uncertainty_execution_labels() -> List[str]:
    """Return all valid execution labels."""
    return list(CALIBRATION_UNCERTAINTY_EXECUTION_LABELS)


def validate_calibration_uncertainty_domain_label(label: str) -> bool:
    """Validate whether domain label is recognized."""
    return label in CALIBRATION_UNCERTAINTY_DOMAINS


def validate_calibration_uncertainty_status_label(label: str) -> bool:
    """Validate whether status label is recognized."""
    return label in CALIBRATION_UNCERTAINTY_STATUS_LABELS


def validate_calibration_uncertainty_execution_label(label: str) -> bool:
    """Validate whether execution label is recognized."""
    return label in CALIBRATION_UNCERTAINTY_EXECUTION_LABELS
