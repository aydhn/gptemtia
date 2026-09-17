# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Models.

Defines dataclasses and validation models representing contracts, components, inventories,
evidence, boundaries, findings, manifest, and 160-phase completion.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from advanced_final_delivery.final_delivery_labels import (
    FINAL_DELIVERY_PROFILE_DOMAIN,
    FINAL_PACKAGE_DOMAIN,
    FINAL_COMPONENT_DOMAIN,
    FINAL_INVENTORY_DOMAIN,
    FINAL_EVIDENCE_DOMAIN,
    FINAL_PHASE_SUMMARY_DOMAIN,
    FINAL_BOUNDARY_DOMAIN,
    FINAL_DISABLED_EXECUTION_DOMAIN,
    FINAL_FINDING_DOMAIN,
    FINAL_READINESS_SCORE_DOMAIN,
    FINAL_MANIFEST_DOMAIN,
    FINAL_COMPLETION_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    SEVERITY_INFO,
)


@dataclass
class FinalDeliveryProfileItem:
    """Represents an active profile configuration item."""
    profile_name: str
    description: str
    current_phase: int = 160
    target_final_phase: int = 160
    next_phase: Optional[int] = None
    min_readiness_score: float = 0.50
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    domain: str = FINAL_DELIVERY_PROFILE_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryPackageContract:
    """Represents a final delivery package contract."""
    contract_name: str
    delivery_family: str
    phase_ref: str
    profile_ref: str
    final_hardening_ref: str
    full_system_integration_ref: str
    portfolio_acceptance_ref: str
    backtest_acceptance_ref: str
    safety_boundary_ref: str
    validation_report_ref: str
    release_candidate_ref: str
    operator_runbook_ref: str
    final_completion_ref: str
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
    domain: str = FINAL_PACKAGE_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryComponentItem:
    """Represents a delivery component item across Phase 1-160."""
    component_name: str
    phase_range: str
    description: str
    verified: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    domain: str = FINAL_COMPONENT_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryInventoryItem:
    """Represents an inventory record item (module, script, test, doc, report)."""
    item_name: str
    category: str
    location: str
    item_count: int = 1
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    domain: str = FINAL_INVENTORY_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryEvidenceItem:
    """Represents an acceptance/validation evidence record item."""
    evidence_name: str
    phase_ref: str
    description: str
    verified: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    domain: str = FINAL_EVIDENCE_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryPhaseSummaryItem:
    """Represents a phase block summary record item."""
    block_name: str
    phase_range: str
    description: str
    completed: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    domain: str = FINAL_PHASE_SUMMARY_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryBoundaryItem:
    """Represents a boundary rule item (no-go, go, safety, non-production)."""
    boundary_name: str
    category: str
    description: str
    enforced: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    domain: str = FINAL_BOUNDARY_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryDisabledExecutionItem:
    """Represents a disabled execution record item."""
    action_name: str
    description: str
    disabled: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    domain: str = FINAL_DISABLED_EXECUTION_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryFinding:
    """Represents an audit finding or manual review requirement."""
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
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class FinalDeliveryReadinessScore:
    """Represents the final delivery completeness readiness score."""
    readiness_score: float
    classification: str
    min_readiness_score: float = 0.50
    threshold_met: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    domain: str = FINAL_READINESS_SCORE_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY

    def __post_init__(self):
        if not (0.0 <= self.readiness_score <= 1.0):
            raise ValueError(f"Readiness score must be between 0.0 and 1.0, got: {self.readiness_score}")


@dataclass
class FinalDeliveryManifest:
    """Comprehensive final delivery manifest."""
    manifest_id: str = "MNF-160-FINAL-DELIVERY-001"
    current_phase: int = 160
    target_final_phase: int = 160
    next_phase: Optional[int] = None
    phase_160_completed: bool = True
    full_advanced_bot_final_delivery_completed: bool = True
    final_delivery_contract_ready: bool = True
    final_manifest_ready: bool = True
    final_operator_handover_ready: bool = True
    final_safety_summary_ready: bool = True
    final_manual_review_summary_ready: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
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
    final_plan_closed: bool = True
    final_delivery_completed: bool = True
    domain: str = FINAL_MANIFEST_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY


@dataclass
class Final160PhaseCompletionItem:
    """Represents completion of the 160-phase plan."""
    current_phase: int = 160
    target_final_phase: int = 160
    next_phase: Optional[int] = None
    plan_status: str = "completed_contract_governance_documentation_acceptance_level"
    mvp_block_status: str = "completed"
    advanced_block_status: str = "completed"
    backtest_acceptance_block_status: str = "completed_contract_level"
    portfolio_acceptance_block_status: str = "completed_contract_level"
    full_system_integration_status: str = "completed_contract_level"
    final_hardening_status: str = "completed_contract_level"
    final_delivery_status: str = "completed_contract_level"
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    live_trading_ready: bool = False
    broker_ready: bool = False
    production_ready: bool = False
    investment_advice: bool = False
    signal_generation: bool = False
    model_prediction: bool = False
    deployment: bool = False
    manual_review_required: bool = True
    final_delivery_completed: bool = True
    domain: str = FINAL_COMPLETION_DOMAIN
    status: str = FULL_ADVANCED_BOT_FINAL_DELIVERY_READY
