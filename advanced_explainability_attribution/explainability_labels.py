# -*- coding: utf-8 -*-
"""Phase 143: Explainability and Feature Attribution Labels."""

from typing import List, Set

EXPLAINABILITY_DOMAIN_LABELS: List[str] = [
    "explainability_profile_domain",
    "explainability_domain",
    "explainability_report_contract_domain",
    "feature_attribution_contract_domain",
    "global_explanation_contract_domain",
    "local_explanation_contract_domain",
    "feature_importance_placeholder_domain",
    "feature_contribution_placeholder_domain",
    "shap_placeholder_domain",
    "lime_placeholder_domain",
    "permutation_importance_placeholder_domain",
    "partial_dependence_placeholder_domain",
    "ice_placeholder_domain",
    "surrogate_model_placeholder_domain",
    "counterfactual_placeholder_domain",
    "reason_code_placeholder_domain",
    "attribution_method_policy_domain",
    "attribution_scope_policy_domain",
    "attribution_input_contract_domain",
    "attribution_output_contract_domain",
    "explainability_execution_disabled_domain",
    "attribution_calculation_disabled_domain",
    "shap_execution_disabled_domain",
    "lime_execution_disabled_domain",
    "permutation_importance_disabled_domain",
    "pdp_ice_execution_disabled_domain",
    "surrogate_model_execution_disabled_domain",
    "counterfactual_execution_disabled_domain",
    "explanation_model_action_disabled_domain",
    "explainability_metric_placeholder_domain",
    "attribution_quality_gate_domain",
    "explanation_stability_placeholder_domain",
    "attribution_drift_linkage_domain",
    "featurestore_explainability_linkage_domain",
    "regime_explainability_linkage_domain",
    "drift_explainability_linkage_domain",
    "calibration_uncertainty_explainability_linkage_domain",
    "validation_dependency_domain",
    "quality_dependency_domain",
    "runtime_dependency_domain",
    "candidate_model_dependency_domain",
    "ensemble_dependency_domain",
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
    "phase_144_handoff_domain",
    "unknown_explainability_domain",
]

EXPLAINABILITY_STATUS_LABELS: List[str] = [
    "explainability_contract_ready",
    "explainability_contract_ready_with_warnings",
    "explainability_contract_placeholder_only",
    "explainability_contract_manual_review_required",
    "explainability_contract_blocked_by_safety",
    "explainability_contract_unknown",
]

EXPLAINABILITY_EXECUTION_LABELS: List[str] = [
    "execution_blocked_no_explainability_calculation",
    "execution_blocked_no_feature_attribution",
    "execution_blocked_no_shap",
    "execution_blocked_no_lime",
    "execution_blocked_no_permutation_importance",
    "execution_blocked_no_pdp_ice",
    "execution_blocked_no_surrogate_model",
    "execution_blocked_no_counterfactual",
    "execution_contract_only",
    "execution_unknown",
]

_DOMAIN_SET: Set[str] = set(EXPLAINABILITY_DOMAIN_LABELS)
_STATUS_SET: Set[str] = set(EXPLAINABILITY_STATUS_LABELS)
_EXECUTION_SET: Set[str] = set(EXPLAINABILITY_EXECUTION_LABELS)


def list_explainability_domain_labels() -> List[str]:
    """Return all valid explainability domain labels."""
    return list(EXPLAINABILITY_DOMAIN_LABELS)


def list_explainability_status_labels() -> List[str]:
    """Return all valid explainability status labels."""
    return list(EXPLAINABILITY_STATUS_LABELS)


def list_explainability_execution_labels() -> List[str]:
    """Return all valid explainability execution labels."""
    return list(EXPLAINABILITY_EXECUTION_LABELS)


def validate_explainability_domain_label(label: str) -> bool:
    """Check if domain label is valid."""
    return label in _DOMAIN_SET


def validate_explainability_status_label(label: str) -> bool:
    """Check if status label is valid."""
    return label in _STATUS_SET


def validate_explainability_execution_label(label: str) -> bool:
    """Check if execution label is valid."""
    return label in _EXECUTION_SET


# Aliases
EXPLAINABILITY_DOMAINS = EXPLAINABILITY_DOMAIN_LABELS
EXPLAINABILITY_STATUSES = EXPLAINABILITY_STATUS_LABELS
validate_explainability_domain = validate_explainability_domain_label
validate_explainability_status = validate_explainability_status_label
validate_explainability_execution = validate_explainability_execution_label
