# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Models and Data Structures."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class BacktestAcceptanceProfileItem:
    """Model representing a backtest acceptance profile item."""
    profile_name: str
    description: str
    current_phase: int = 152
    target_final_phase: int = 160
    next_phase: int = 153
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    min_readiness_score: float = 0.50
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class BacktestAcceptanceComponentItem:
    """Model representing a Backtest block component (Phases 146-152)."""
    component_id: str
    component_name: str
    phase_ref: str
    primary_module: str
    description: str
    status: str = "CHECKED"
    contract_only: bool = True
    non_production: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    signal_ready: bool = False
    strategy_approved: bool = False


@dataclass
class BacktestAcceptanceCheckpoint:
    """Model representing a checkpoint verification for a component."""
    checkpoint_id: str
    component_name: str
    expected_module: str
    expected_scripts: List[str]
    expected_tests: List[str]
    expected_manifest: str
    expected_validation_report: str
    expected_safety_boundary: str
    expected_handoff: str
    contract_only: bool = True
    non_production: bool = True
    manual_review_required: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_ready: bool = False
    signal_ready: bool = False
    strategy_approved: bool = False
    status: str = "CHECKPOINT_SATISFIED"


@dataclass
class BacktestPhaseAcceptanceItem:
    """Model representing phase-level acceptance verification."""
    phase_id: str
    phase_number: int
    title: str
    primary_module: str
    checks_passed: int
    total_checks: int
    status: str = "ACCEPTED_CONTRACT_ONLY"
    contract_present: bool = True
    validation_present: bool = True
    safety_boundary_present: bool = True
    manifest_present: bool = True
    non_production: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    strategy_approved: bool = False


@dataclass
class BacktestValidationEvidenceItem:
    """Model representing validation evidence across phases."""
    evidence_id: str
    phase_ref: str
    evidence_type: str
    description: str
    status: str = "VERIFIED"
    non_signal: bool = True
    no_live_trading: bool = True
    no_backtest_execution: bool = True
    no_benchmark_execution: bool = True


@dataclass
class BacktestAcceptanceBoundaryItem:
    """Model representing safety and non-production boundaries."""
    boundary_id: str
    boundary_type: str
    description: str
    enforced: bool = True
    status: str = "SECURE"
    non_signal: bool = True


@dataclass
class BacktestAcceptanceFinding:
    """Model representing a blocker, gap, warning or review finding."""
    finding_id: str
    finding_type: str
    phase_ref: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass
class BacktestAcceptanceReadinessScore:
    """Model representing the computed diagnostic readiness score."""
    score: float
    classification: str
    meets_threshold: bool
    current_phase: int = 152
    target_final_phase: int = 160
    next_phase: int = 153
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    strategy_approved: bool = False
    performance_guaranteed: bool = False

    def __post_init__(self):
        if not (0.0 <= self.score <= 1.0):
            raise ValueError(f"Readiness score must be between 0.0 and 1.0, got {self.score}")


@dataclass
class BacktestAcceptanceManualReviewItem:
    """Model representing an item in the manual review queue."""
    gate_id: str
    phase_ref: str
    topic: str
    review_requirement: str
    action_required: str
    manual_review_required: bool = True
    status: str = "PENDING_REVIEW"


@dataclass
class BacktestAcceptanceManifest:
    """Comprehensive acceptance manifest for the entire Backtest block (Phases 146-152)."""
    manifest_name: str
    manifest_id: str
    current_phase: int = 152
    target_final_phase: int = 160
    next_phase: int = 153
    component_count: int = 7
    accepted_component_count: int = 7
    blocker_count: int = 0
    warning_count: int = 0
    gap_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 7
    readiness_score: float = 1.0
    manual_review_required: bool = True
    backtest_block_completed: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    production_approved: bool = False
    broker_ready_approved: bool = False
    live_trading_approved: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    contains_article_body: bool = False
    contains_raw_content: bool = False
    contains_scraped_html: bool = False
    contains_embedding: bool = False
    contains_vector: bool = False
    backtest_executed: bool = False
    benchmark_executed: bool = False
    metric_calculated: bool = False
    result_claim_generated: bool = False
    performance_claim_generated: bool = False
    strategy_approved: bool = False
    capital_allocation_generated: bool = False
    portfolio_constructed: bool = False
    position_sizing_generated: bool = False
    optimizer_executed: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    model_inference_executed: bool = False
    prediction_generated: bool = False
    target_label_generated: bool = False
    broker_order_sent: bool = False
    live_order_sent: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    production_deployed: bool = False
    phase_153_handoff_ready: bool = True
