# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Labels and Domain Enums."""

from typing import List

# Domain labels
ADVANCED_ML_ACCEPTANCE_PROFILE_DOMAIN = "advanced_ml_acceptance_profile_domain"
ADVANCED_ML_ACCEPTANCE_DOMAIN = "advanced_ml_acceptance_domain"
ACCEPTANCE_SCOPE_DOMAIN = "acceptance_scope_domain"
COMPONENT_REGISTRY_DOMAIN = "component_registry_domain"
COMPONENT_CHECKPOINT_DOMAIN = "component_checkpoint_domain"
PHASE_136_GPU_RUNTIME_ACCEPTANCE_DOMAIN = "phase_136_gpu_runtime_acceptance_domain"
PHASE_137_DATASET_CONTRACT_ACCEPTANCE_DOMAIN = "phase_137_dataset_contract_acceptance_domain"
PHASE_138_BASELINE_MODEL_ACCEPTANCE_DOMAIN = "phase_138_baseline_model_acceptance_domain"
PHASE_139_GPU_TRAINING_GOVERNANCE_ACCEPTANCE_DOMAIN = "phase_139_gpu_training_governance_acceptance_domain"
PHASE_140_ENSEMBLE_CANDIDATE_ACCEPTANCE_DOMAIN = "phase_140_ensemble_candidate_acceptance_domain"
PHASE_141_CALIBRATION_UNCERTAINTY_ACCEPTANCE_DOMAIN = "phase_141_calibration_uncertainty_acceptance_domain"
PHASE_142_DRIFT_MONITORING_ACCEPTANCE_DOMAIN = "phase_142_drift_monitoring_acceptance_domain"
PHASE_143_EXPLAINABILITY_ACCEPTANCE_DOMAIN = "phase_143_explainability_acceptance_domain"
PHASE_144_MODEL_GOVERNANCE_ACCEPTANCE_DOMAIN = "phase_144_model_governance_acceptance_domain"
DEPENDENCY_ACCEPTANCE_DOMAIN = "dependency_acceptance_domain"
VALIDATION_EVIDENCE_DOMAIN = "validation_evidence_domain"
SAFETY_BOUNDARY_ACCEPTANCE_DOMAIN = "safety_boundary_acceptance_domain"
NON_PRODUCTION_BOUNDARY_DOMAIN = "non_production_boundary_domain"
MANUAL_REVIEW_GATE_DOMAIN = "manual_review_gate_domain"
GO_NO_GO_BOUNDARY_DOMAIN = "go_no_go_boundary_domain"
BLOCKER_DOMAIN = "blocker_domain"
GAP_DOMAIN = "gap_domain"
WARNING_DOMAIN = "warning_domain"
FINDING_DOMAIN = "finding_domain"
READINESS_SCORE_DOMAIN = "readiness_score_domain"
MANIFEST_DOMAIN = "manifest_domain"
HEALTH_DOMAIN = "health_domain"
VALIDATION_DOMAIN = "validation_domain"
SAFETY_DOMAIN = "safety_domain"
PHASE_146_HANDOFF_DOMAIN = "phase_146_handoff_domain"
UNKNOWN_ADVANCED_ML_ACCEPTANCE_DOMAIN = "unknown_advanced_ml_acceptance_domain"

ALL_DOMAINS = [
    ADVANCED_ML_ACCEPTANCE_PROFILE_DOMAIN,
    ADVANCED_ML_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_SCOPE_DOMAIN,
    COMPONENT_REGISTRY_DOMAIN,
    COMPONENT_CHECKPOINT_DOMAIN,
    PHASE_136_GPU_RUNTIME_ACCEPTANCE_DOMAIN,
    PHASE_137_DATASET_CONTRACT_ACCEPTANCE_DOMAIN,
    PHASE_138_BASELINE_MODEL_ACCEPTANCE_DOMAIN,
    PHASE_139_GPU_TRAINING_GOVERNANCE_ACCEPTANCE_DOMAIN,
    PHASE_140_ENSEMBLE_CANDIDATE_ACCEPTANCE_DOMAIN,
    PHASE_141_CALIBRATION_UNCERTAINTY_ACCEPTANCE_DOMAIN,
    PHASE_142_DRIFT_MONITORING_ACCEPTANCE_DOMAIN,
    PHASE_143_EXPLAINABILITY_ACCEPTANCE_DOMAIN,
    PHASE_144_MODEL_GOVERNANCE_ACCEPTANCE_DOMAIN,
    DEPENDENCY_ACCEPTANCE_DOMAIN,
    VALIDATION_EVIDENCE_DOMAIN,
    SAFETY_BOUNDARY_ACCEPTANCE_DOMAIN,
    NON_PRODUCTION_BOUNDARY_DOMAIN,
    MANUAL_REVIEW_GATE_DOMAIN,
    GO_NO_GO_BOUNDARY_DOMAIN,
    BLOCKER_DOMAIN,
    GAP_DOMAIN,
    WARNING_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_146_HANDOFF_DOMAIN,
]

# Status labels
ACCEPTANCE_READY = "acceptance_ready"
ACCEPTANCE_READY_WITH_WARNINGS = "acceptance_ready_with_warnings"
ACCEPTANCE_MANUAL_REVIEW_REQUIRED = "acceptance_manual_review_required"
ACCEPTANCE_BLOCKED_BY_SAFETY = "acceptance_blocked_by_safety"
ACCEPTANCE_MISSING_DEPENDENCY = "acceptance_missing_dependency"
ACCEPTANCE_CONTRACT_ONLY = "acceptance_contract_only"
ACCEPTANCE_UNKNOWN = "acceptance_unknown"

ALL_STATUSES = [
    ACCEPTANCE_READY,
    ACCEPTANCE_READY_WITH_WARNINGS,
    ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
    ACCEPTANCE_BLOCKED_BY_SAFETY,
    ACCEPTANCE_MISSING_DEPENDENCY,
    ACCEPTANCE_CONTRACT_ONLY,
    ACCEPTANCE_UNKNOWN,
]

# Boundary labels
GO_CONTRACT_ONLY = "go_contract_only"
NO_GO_LIVE_TRADING = "no_go_live_trading"
NO_GO_BROKER_EXECUTION = "no_go_broker_execution"
NO_GO_PRODUCTION_DEPLOYMENT = "no_go_production_deployment"
NO_GO_MODEL_REGISTRY_WRITE = "no_go_model_registry_write"
NO_GO_MODEL_TRAINING = "no_go_model_training"
NO_GO_PREDICTION = "no_go_prediction"
NO_GO_SIGNAL_GENERATION = "no_go_signal_generation"
NO_GO_BACKTEST_EXECUTION = "no_go_backtest_execution"
NO_GO_UNKNOWN = "no_go_unknown"

ALL_BOUNDARIES = [
    GO_CONTRACT_ONLY,
    NO_GO_LIVE_TRADING,
    NO_GO_BROKER_EXECUTION,
    NO_GO_PRODUCTION_DEPLOYMENT,
    NO_GO_MODEL_REGISTRY_WRITE,
    NO_GO_MODEL_TRAINING,
    NO_GO_PREDICTION,
    NO_GO_SIGNAL_GENERATION,
    NO_GO_BACKTEST_EXECUTION,
    NO_GO_UNKNOWN,
]


def list_advanced_ml_acceptance_domain_labels() -> List[str]:
    """List all valid advanced ML acceptance domain labels."""
    return list(ALL_DOMAINS)


def list_advanced_ml_acceptance_status_labels() -> List[str]:
    """List all valid advanced ML acceptance status labels."""
    return list(ALL_STATUSES)


def list_advanced_ml_acceptance_boundary_labels() -> List[str]:
    """List all valid advanced ML acceptance boundary labels."""
    return list(ALL_BOUNDARIES)


def validate_advanced_ml_acceptance_domain_label(label: str) -> bool:
    """Validate domain label against known set."""
    if label not in ALL_DOMAINS:
        raise ValueError(f"Invalid domain label: {label}")
    return True


def validate_advanced_ml_acceptance_status_label(label: str) -> bool:
    """Validate status label against known set."""
    if label not in ALL_STATUSES:
        raise ValueError(f"Invalid status label: {label}")
    return True


def validate_advanced_ml_acceptance_boundary_label(label: str) -> bool:
    """Validate boundary label against known set."""
    if label not in ALL_BOUNDARIES:
        raise ValueError(f"Invalid boundary label: {label}")
    return True
