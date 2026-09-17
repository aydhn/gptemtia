# -*- coding: utf-8 -*-
"""Phase 142: Model Drift Monitoring and Drift Linkage Labels and Taxonomy."""

from typing import List, Set

MODEL_DRIFT_DOMAIN_LABELS: Set[str] = {
    "model_drift_profile_domain",
    "model_drift_domain",
    "model_drift_monitoring_contract_domain",
    "data_drift_monitoring_contract_domain",
    "feature_drift_monitoring_contract_domain",
    "feature_drift_linkage_domain",
    "feature_quality_drift_linkage_domain",
    "featurestore_drift_linkage_domain",
    "regime_drift_linkage_domain",
    "calibration_drift_contract_domain",
    "uncertainty_drift_contract_domain",
    "prediction_distribution_drift_placeholder_domain",
    "reference_window_policy_domain",
    "current_window_policy_domain",
    "rolling_window_placeholder_policy_domain",
    "drift_threshold_placeholder_policy_domain",
    "drift_segment_policy_domain",
    "drift_monitoring_schedule_placeholder_domain",
    "drift_metric_placeholder_domain",
    "psi_metric_placeholder_domain",
    "ks_metric_placeholder_domain",
    "js_divergence_metric_placeholder_domain",
    "wasserstein_metric_placeholder_domain",
    "correlation_drift_metric_placeholder_domain",
    "missingness_drift_metric_placeholder_domain",
    "categorical_drift_metric_placeholder_domain",
    "numerical_drift_metric_placeholder_domain",
    "calibration_drift_metric_placeholder_domain",
    "uncertainty_drift_metric_placeholder_domain",
    "drift_execution_disabled_domain",
    "drift_metric_calculation_disabled_domain",
    "drift_alerting_disabled_domain",
    "drift_retraining_trigger_disabled_domain",
    "drift_model_action_disabled_domain",
    "drift_prediction_disabled_domain",
    "drift_input_contract_domain",
    "drift_output_contract_domain",
    "validation_dependency_domain",
    "quality_dependency_domain",
    "runtime_dependency_domain",
    "candidate_model_dependency_domain",
    "ensemble_dependency_domain",
    "calibration_uncertainty_dependency_domain",
    "no_lookahead_guard_domain",
    "metadata_only_news_guard_domain",
    "source_preservation_guard_domain",
    "forbidden_column_policy_domain",
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
    "phase_143_handoff_domain",
    "candidate_model_drift_monitoring_contract",
    "ensemble_drift_monitoring_contract",
    "feature_drift_linkage",
    "regime_drift_linkage",
    "unknown_model_drift_domain",
}

MODEL_DRIFT_STATUS_LABELS: Set[str] = {
    "drift_contract_ready",
    "drift_contract_ready_with_warnings",
    "drift_contract_placeholder_only",
    "drift_contract_manual_review_required",
    "drift_contract_blocked_by_safety",
    "active",
    "placeholder",
    "drift_contract_unknown",
}

MODEL_DRIFT_EXECUTION_LABELS: Set[str] = {
    "execution_blocked_no_drift_calculation",
    "execution_blocked_no_metric_calculation",
    "execution_blocked_no_alerting",
    "execution_blocked_no_retraining_trigger",
    "execution_blocked_no_model_action",
    "execution_blocked_no_prediction",
    "drift_calculation_disabled",
    "drift_alerting_disabled",
    "execution_contract_only",
    "execution_unknown",
}


def list_model_drift_domain_labels() -> List[str]:
    """Return sorted list of valid domain labels."""
    return sorted(list(MODEL_DRIFT_DOMAIN_LABELS))


def list_model_drift_status_labels() -> List[str]:
    """Return sorted list of valid status labels."""
    return sorted(list(MODEL_DRIFT_STATUS_LABELS))


def list_model_drift_execution_labels() -> List[str]:
    """Return sorted list of valid execution labels."""
    return sorted(list(MODEL_DRIFT_EXECUTION_LABELS))


def validate_model_drift_domain_label(label: str) -> bool:
    """Validate whether label is a recognized domain label."""
    return label in MODEL_DRIFT_DOMAIN_LABELS


def validate_model_drift_status_label(label: str) -> bool:
    """Validate whether label is a recognized status label."""
    return label in MODEL_DRIFT_STATUS_LABELS


def validate_model_drift_execution_label(label: str) -> bool:
    """Validate whether label is a recognized execution label."""
    return label in MODEL_DRIFT_EXECUTION_LABELS


DRIFT_DOMAIN_LABELS = MODEL_DRIFT_DOMAIN_LABELS
DRIFT_STATUS_LABELS = MODEL_DRIFT_STATUS_LABELS
DRIFT_EXECUTION_LABELS = MODEL_DRIFT_EXECUTION_LABELS
is_valid_drift_domain_label = validate_model_drift_domain_label
is_valid_drift_status_label = validate_model_drift_status_label
is_valid_drift_execution_label = validate_model_drift_execution_label

