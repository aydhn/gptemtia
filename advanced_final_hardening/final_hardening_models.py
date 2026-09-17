# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Models.

Data models representing final hardening profiles, contracts, runbooks, freezes,
checkpoints, boundaries, findings, manifests, and readiness scores.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from advanced_final_hardening.final_hardening_labels import (
    FINAL_HARDENING_CONTRACT_READY,
    RELEASE_CANDIDATE_CONTRACT_READY,
    OPERATOR_RUNBOOK_CONTRACT_READY,
    FINAL_HARDENING_PROFILE_DOMAIN,
    FINAL_HARDENING_CONTRACT_DOMAIN,
    OPERATOR_RUNBOOK_DOMAIN,
    RELEASE_CANDIDATE_DOMAIN,
    CONFIGURATION_FREEZE_DOMAIN,
    INVENTORY_DOMAIN,
    OPERATOR_PROTOCOL_DOMAIN,
    RELEASE_CANDIDATE_CHECKPOINT_DOMAIN,
    RELEASE_CANDIDATE_BOUNDARY_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
)


@dataclass
class FinalHardeningProfileItem:
    profile_name: str
    description: str
    current_phase: int = 159
    target_final_phase: int = 160
    next_phase: int = 160
    domain: str = FINAL_HARDENING_PROFILE_DOMAIN
    dry_run: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_production_deployment: bool = False
    allow_release_deployment: bool = False
    status: str = FINAL_HARDENING_CONTRACT_READY


@dataclass
class FinalHardeningContract:
    contract_name: str
    hardening_family: str
    full_system_integration_ref: str = "PHASE_158_FULL_SYSTEM_INTEGRATION"
    portfolio_acceptance_ref: str = "PHASE_157_PORTFOLIO_ACCEPTANCE"
    backtest_acceptance_ref: str = "PHASE_151_BACKTEST_ACCEPTANCE"
    safety_boundary_ref: str = "PHASE_159_SAFETY_BOUNDARY"
    validation_report_ref: str = "PHASE_159_VALIDATION_REPORT"
    manifest_ref: str = "PHASE_159_RELEASE_CANDIDATE_MANIFEST"
    operator_runbook_ref: str = "PHASE_159_OPERATOR_RUNBOOK"
    release_candidate_ref: str = "PHASE_159_RELEASE_CANDIDATE"
    phase_160_handoff_ref: str = "PHASE_160_FULL_ADVANCED_BOT_FINAL_DELIVERY"
    domain: str = FINAL_HARDENING_CONTRACT_DOMAIN
    system_execution_allowed: bool = False
    release_deployment_allowed: bool = False
    production_deployment_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    order_generation_allowed: bool = False
    model_training_allowed: bool = False
    prediction_allowed: bool = False
    model_registry_write_allowed: bool = False
    artifact_persistence_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = FINAL_HARDENING_CONTRACT_READY


@dataclass
class OperatorRunbookContract:
    runbook_name: str
    category: str
    description: str
    domain: str = OPERATOR_RUNBOOK_DOMAIN
    execution_instructions_allowed: bool = False
    live_bot_execution_allowed: bool = False
    broker_execution_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = OPERATOR_RUNBOOK_CONTRACT_READY


@dataclass
class ReleaseCandidateContract:
    candidate_id: str
    candidate_name: str
    version_tag: str = "RC-PHASE-159"
    current_phase: int = 159
    target_final_phase: int = 160
    domain: str = RELEASE_CANDIDATE_DOMAIN
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    deployment_ready: bool = False
    signal_ready: bool = False
    official_approval: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = RELEASE_CANDIDATE_CONTRACT_READY


@dataclass
class FinalFreezeContract:
    freeze_name: str
    freeze_category: str
    target_scope: str
    frozen: bool = True
    actual_lock_enacted: bool = False
    modifications_allowed_without_review: bool = False
    domain: str = CONFIGURATION_FREEZE_DOMAIN
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = FINAL_HARDENING_CONTRACT_READY


@dataclass
class FinalInventoryItem:
    item_id: str
    inventory_type: str
    item_name: str
    item_path_or_identifier: str
    domain: str = INVENTORY_DOMAIN
    metadata_only: bool = True
    item_count: int = 1
    description: str = ""
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = FINAL_HARDENING_CONTRACT_READY


@dataclass
class OperatorProtocolItem:
    protocol_id: str
    protocol_name: str
    protocol_type: str
    description: str
    action_blocked: str
    domain: str = OPERATOR_PROTOCOL_DOMAIN
    safe_alternative: str = "local_offline_dry_run_inspection"
    manual_review_required: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = OPERATOR_RUNBOOK_CONTRACT_READY


@dataclass
class ReleaseCandidateCheckpoint:
    checkpoint_name: str
    checkpoint_family: str
    expected_artifact: str
    expected_status: str
    validation_ref: str = "PHASE_159_VALIDATION"
    safety_ref: str = "PHASE_159_SAFETY_BOUNDARY"
    runbook_ref: str = "PHASE_159_OPERATOR_RUNBOOK"
    domain: str = RELEASE_CANDIDATE_CHECKPOINT_DOMAIN
    manual_review_required: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_ready: bool = False
    deployment_ready: bool = False
    signal_ready: bool = False
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = RELEASE_CANDIDATE_CONTRACT_READY


@dataclass
class ReleaseCandidateBoundaryItem:
    boundary_id: str
    boundary_type: str
    action_name: str
    policy: str
    reason: str
    domain: str = RELEASE_CANDIDATE_BOUNDARY_DOMAIN
    enforced: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = FINAL_HARDENING_CONTRACT_READY


@dataclass
class ReleaseCandidateFinding:
    finding_id: str
    finding_type: str
    domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = FINAL_HARDENING_CONTRACT_READY


@dataclass
class ReleaseCandidateReadinessScore:
    score: float
    classification: str
    domain: str = READINESS_SCORE_DOMAIN
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    is_trading_signal: bool = False
    is_investment_advice: bool = False
    is_release_deployment_authorization: bool = False
    status: str = RELEASE_CANDIDATE_CONTRACT_READY

    def __post_init__(self):
        if not (0.0 <= self.score <= 1.0):
            raise ValueError(f"Score must be between 0.0 and 1.0, got: {self.score}")
        if self.is_trading_signal or self.is_investment_advice:
            raise ValueError("Readiness score must never be used as a trading signal or investment advice.")
        if self.broker_ready or self.production_ready or self.live_trading_ready:
            raise ValueError("Readiness score cannot claim broker, production, or live readiness.")


@dataclass
class ReleaseCandidateManifest:
    manifest_id: str = "MNF-159-RELEASE-CANDIDATE-001"
    current_phase: int = 159
    target_final_phase: int = 160
    next_phase: int = 160
    final_hardening_completed: bool = True
    release_candidate_contract_ready: bool = True
    operator_runbook_contract_ready: bool = True
    domain: str = MANIFEST_DOMAIN
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    system_executed: bool = False
    end_to_end_run_executed: bool = False
    release_deployed: bool = False
    production_deployed: bool = False
    live_trading_executed: bool = False
    broker_execution_executed: bool = False
    order_generation_executed: bool = False
    signal_generation_executed: bool = False
    model_training_executed: bool = False
    model_predict_executed: bool = False
    prediction_generated: bool = False
    target_label_generated: bool = False
    backtest_executed: bool = False
    benchmark_executed: bool = False
    portfolio_executed: bool = False
    risk_executed: bool = False
    scenario_executed: bool = False
    metric_calculated: bool = False
    optimizer_executed: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    source_preserved: bool = True
    source_overwritten: bool = False
    destructive_action_executed: bool = False
    manual_review_required: bool = True
    phase_160_handoff_ready: bool = True
    status: str = RELEASE_CANDIDATE_CONTRACT_READY


@dataclass
class ReleaseCandidateManualReviewItem:
    item_id: str
    gate_name: str
    review_scope: str
    required_reviewer_role: str
    sign_off_status: str = "PENDING_LOCAL_REVIEW"
    domain: str = "release_candidate_review_gate"
    blocks_phase_160_handoff: bool = False
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    status: str = FINAL_HARDENING_CONTRACT_READY
