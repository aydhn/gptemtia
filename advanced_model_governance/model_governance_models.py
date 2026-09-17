# -*- coding: utf-8 -*-
"""Phase 144: Model Governance, Model Cards and Audit Trail Models."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ModelGovernanceProfileItem:
    profile_name: str
    display_name: str
    description: str
    current_phase: int = 144
    target_final_phase: int = 160
    next_phase: int = 145
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    min_readiness_score: float = 0.45


@dataclass
class ModelGovernanceContract:
    contract_name: str
    governance_family: str
    dataset_contract_ref: str
    baseline_model_ref: str
    candidate_model_ref: str
    ensemble_ref: str
    calibration_uncertainty_ref: str
    drift_monitoring_ref: str
    explainability_ref: str
    model_card_ref: str
    audit_trail_ref: str
    approval_boundary_ref: str
    required_no_lookahead_guard_ref: str
    required_metadata_only_news_guard_ref: str
    required_source_preservation_guard_ref: str
    production_approval_allowed: bool = False
    broker_ready_approval_allowed: bool = False
    live_trading_approval_allowed: bool = False
    deployment_allowed: bool = False
    model_registry_write_allowed: bool = False
    artifact_persistence_allowed: bool = False
    signal_generation_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True


@dataclass
class ModelCardContract:
    contract_name: str
    model_family: str
    template_ref: str
    limitations_ref: str
    intended_use_ref: str
    prohibited_use_ref: str
    risk_disclosure_ref: str
    validation_evidence_ref: str
    data_dependency_ref: str
    feature_dependency_ref: str
    model_dependency_ref: str
    runtime_dependency_ref: str
    production_ready_claim: bool = False
    broker_ready_claim: bool = False
    official_approval_claim: bool = False
    signal_claim: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True


@dataclass
class ModelCardTemplate:
    template_name: str
    model_family: str
    sections: List[str]
    is_dry_run: bool = True
    manual_review_required: bool = True


@dataclass
class ModelCardSection:
    section_id: str
    section_name: str
    description: str
    required: bool = True
    manual_review_gate: str = "review_required"


@dataclass
class GovernanceBoundary:
    boundary_name: str
    boundary_type: str
    enforcement_rule: str
    action_permitted: bool = False
    manual_review_required: bool = True
    error_message: str = "Action blocked by governance boundary policy."


@dataclass
class GovernanceRiskItem:
    risk_id: str
    risk_category: str
    description: str
    impact_level: str
    mitigation_strategy: str
    residual_risk: str
    manual_review_required: bool = True


@dataclass
class GovernanceChecklistItem:
    check_id: str
    category: str
    description: str
    status: str = "PASSED"
    is_prohibited_action: bool = True
    enforced: bool = True


@dataclass
class GovernanceAuditPlaceholder:
    audit_id: str
    governance_contract_ref: str
    model_card_ref: str
    approval_boundary_ref: str
    validation_evidence_ref: str
    risk_register_ref: str
    control_checklist_ref: str
    dry_run_only: bool = True
    real_audit_log: bool = False
    production_approved: bool = False
    broker_ready_approved: bool = False
    live_trading_approved: bool = False
    model_registry_written: bool = False
    artifact_persisted: bool = False
    model_deployed: bool = False
    manual_review_required: bool = True


@dataclass
class GovernanceDisabledExecutionItem:
    report_name: str
    prohibited_action: str
    is_disabled: bool = True
    safeguard_rule: str = "Execution strictly disabled in non-production local offline governance."
    status: str = "ENFORCED"


@dataclass
class GovernanceFinding:
    finding_id: str
    finding_type: str
    governance_domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True


@dataclass
class GovernanceReadinessScore:
    readiness_score: float
    classification: str
    meets_threshold: bool
    findings_count: int
    manual_review_count: int
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    release_approved: bool = False
    model_performance_claim: bool = False


@dataclass
class GovernanceManualReviewItem:
    queue_id: str
    component_name: str
    reason: str
    recommended_action: str
    blocked_actions: List[str]
    resolved: bool = False


@dataclass
class ModelGovernanceManifest:
    manifest_id: str
    current_phase: int = 144
    target_final_phase: int = 160
    next_phase: int = 145
    non_signal: bool = True
    source_preserved: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    production_approved: bool = False
    broker_ready_approved: bool = False
    live_trading_approved: bool = False
    release_approved: bool = False
    real_audit_log: bool = False
    dataset_materialized: bool = False
    feature_snapshot_materialized: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    contains_article_body: bool = False
    contains_raw_content: bool = False
    contains_scraped_html: bool = False
    contains_embedding: bool = False
    contains_vector: bool = False
    sentiment_model_output: bool = False
    real_training_executed: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    model_inference_executed: bool = False
    probability_prediction_executed: bool = False
    calibration_executed: bool = False
    uncertainty_estimation_executed: bool = False
    drift_calculation_executed: bool = False
    explainability_calculation_executed: bool = False
    feature_attribution_calculation_executed: bool = False
    metric_calculation_executed: bool = False
    performance_claim_generated: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    production_deployed: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    governance_contract_count: int = 0
    model_card_count: int = 0
    disabled_execution_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 1.0
    manual_review_required: bool = True
