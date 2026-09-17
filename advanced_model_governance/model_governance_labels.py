# -*- coding: utf-8 -*-
"""Phase 144: Model Governance, Model Cards and Audit Trail Labels."""

from typing import List

MODEL_GOVERNANCE_DOMAIN_LABELS: List[str] = [
    "model_governance_profile_domain",
    "model_governance_domain",
    "model_governance_contract_domain",
    "model_card_contract_domain",
    "model_card_template_domain",
    "model_card_section_domain",
    "model_card_limitation_domain",
    "model_card_intended_use_domain",
    "model_card_prohibited_use_domain",
    "model_card_risk_disclosure_domain",
    "model_card_validation_evidence_domain",
    "model_card_data_dependency_domain",
    "model_card_feature_dependency_domain",
    "model_card_model_dependency_domain",
    "model_card_runtime_dependency_domain",
    "governance_approval_boundary_domain",
    "governance_release_boundary_domain",
    "governance_non_production_boundary_domain",
    "governance_manual_review_gate_domain",
    "governance_validation_evidence_domain",
    "governance_risk_register_domain",
    "governance_control_checklist_domain",
    "governance_compliance_placeholder_domain",
    "governance_audit_trail_placeholder_domain",
    "governance_decision_log_placeholder_domain",
    "governance_change_log_placeholder_domain",
    "governance_owner_responsibility_placeholder_domain",
    "governance_model_lifecycle_placeholder_domain",
    "governance_model_version_placeholder_domain",
    "model_registry_write_disabled_domain",
    "model_artifact_disabled_domain",
    "deployment_disabled_domain",
    "production_approval_disabled_domain",
    "broker_ready_disabled_domain",
    "live_trading_disabled_domain",
    "prediction_disabled_domain",
    "training_disabled_domain",
    "signal_generation_disabled_domain",
    "performance_claim_disabled_domain",
    "dataset_dependency_domain",
    "baseline_model_dependency_domain",
    "gpu_training_dependency_domain",
    "ensemble_dependency_domain",
    "calibration_uncertainty_dependency_domain",
    "drift_dependency_domain",
    "explainability_dependency_domain",
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
    "phase_145_handoff_domain",
    "unknown_model_governance_domain",
]

MODEL_GOVERNANCE_STATUS_LABELS: List[str] = [
    "governance_contract_ready",
    "governance_contract_ready_with_warnings",
    "governance_contract_placeholder_only",
    "governance_contract_manual_review_required",
    "governance_contract_blocked_by_safety",
    "governance_contract_unknown",
]

MODEL_GOVERNANCE_APPROVAL_LABELS: List[str] = [
    "approval_blocked_non_production",
    "approval_blocked_manual_review",
    "approval_blocked_no_broker_ready",
    "approval_blocked_no_production_ready",
    "approval_contract_only",
    "approval_unknown",
]


def list_model_governance_domain_labels() -> List[str]:
    """Return all valid domain labels."""
    return list(MODEL_GOVERNANCE_DOMAIN_LABELS)


def list_model_governance_status_labels() -> List[str]:
    """Return all valid status labels."""
    return list(MODEL_GOVERNANCE_STATUS_LABELS)


def list_model_governance_approval_labels() -> List[str]:
    """Return all valid approval labels."""
    return list(MODEL_GOVERNANCE_APPROVAL_LABELS)


def validate_model_governance_domain_label(label: str) -> bool:
    """Validate a domain label."""
    return label in MODEL_GOVERNANCE_DOMAIN_LABELS


def validate_model_governance_status_label(label: str) -> bool:
    """Validate a status label."""
    return label in MODEL_GOVERNANCE_STATUS_LABELS


def validate_model_governance_approval_label(label: str) -> bool:
    """Validate an approval label."""
    return label in MODEL_GOVERNANCE_APPROVAL_LABELS
