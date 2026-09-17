# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Data Models.

Provides dataclass definitions enforcing strict non-production invariants,
safety boundaries, and governance constraints for Phase 157.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class PortfolioAcceptanceProfileItem:
    """Represents a portfolio acceptance profile registration."""
    profile_name: str
    description: str
    current_phase: int = 157
    target_final_phase: int = 160
    next_phase: int = 158
    min_readiness_score: float = 0.50
    non_signal: bool = True
    dry_run: bool = True
    local_only: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False


@dataclass(frozen=True)
class PortfolioAcceptanceComponentItem:
    """Represents a component registered within the portfolio block."""
    component_id: str
    component_name: str
    phase_number: int
    module_name: str
    status: str
    contract_only: bool = True
    non_production: bool = True
    dry_run: bool = True
    local_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_ready: bool = False
    signal_ready: bool = False
    strategy_approved: bool = False
    portfolio_approved: bool = False
    allocation_approved: bool = False
    risk_approved: bool = False


@dataclass(frozen=True)
class PortfolioAcceptanceCheckpoint:
    """Represents a verification checkpoint for a portfolio component."""
    checkpoint_id: str
    component_name: str
    expected_module: str
    expected_scripts: List[str] = field(default_factory=list)
    expected_tests: List[str] = field(default_factory=list)
    expected_manifest: str = ""
    expected_validation_report: str = ""
    expected_safety_boundary: str = ""
    expected_handoff: str = ""
    contract_only: bool = True
    non_production: bool = True
    manual_review_required: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_ready: bool = False
    signal_ready: bool = False
    strategy_approved: bool = False
    portfolio_approved: bool = False
    allocation_approved: bool = False
    risk_approved: bool = False


@dataclass(frozen=True)
class PortfolioPhaseAcceptanceItem:
    """Represents an acceptance evaluation item for an individual portfolio phase."""
    item_id: str
    phase_number: int
    phase_title: str
    criterion: str
    satisfied: bool
    status: str
    notes: str = ""
    contract_only: bool = True
    non_production: bool = True


@dataclass(frozen=True)
class PortfolioValidationEvidenceItem:
    """Represents validation evidence supporting portfolio block acceptance."""
    evidence_id: str
    phase_number: int
    evidence_type: str
    target_module: str
    status: str
    evidence_present: bool = True
    notes: str = ""


@dataclass(frozen=True)
class PortfolioAcceptanceBoundaryItem:
    """Represents a safety boundary or go/no-go rule for portfolio acceptance."""
    boundary_id: str
    boundary_type: str
    rule_name: str
    action_type: str
    is_allowed: bool
    reason: str


@dataclass(frozen=True)
class PortfolioAcceptanceFinding:
    """Represents an issue, blocker, gap, or warning discovered during acceptance."""
    finding_id: str
    finding_type: str
    phase_ref: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    is_blocking: bool = False


@dataclass(frozen=True)
class PortfolioAcceptanceReadinessScore:
    """Represents the calculated readiness score for portfolio acceptance."""
    overall_score: float
    classification: str
    meets_threshold: bool
    total_checks: int
    passed_checks: int
    warning_count: int
    blocker_count: int
    non_signal: bool = True
    dry_run: bool = True
    local_only: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False

    def __post_init__(self):
        if not (0.0 <= self.overall_score <= 1.0):
            raise ValueError(f"overall_score must be between 0.0 and 1.0, got {self.overall_score}")


@dataclass(frozen=True)
class PortfolioAcceptanceManifest:
    """Represents the complete master manifest for Phase 157 Portfolio Acceptance."""
    manifest_id: str
    current_phase: int = 157
    target_final_phase: int = 160
    next_phase: int = 158
    portfolio_block_completed: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    portfolio_constructed: bool = False
    position_sizing_generated: bool = False
    portfolio_optimized: bool = False
    capital_allocation_generated: bool = False
    portfolio_weights_generated: bool = False
    allocation_generated: bool = False
    rebalance_generated: bool = False
    orders_generated: bool = False
    risk_budget_generated: bool = False
    risk_report_generated: bool = False
    exposure_attribution_generated: bool = False
    limit_monitoring_executed: bool = False
    scenario_executed: bool = False
    drawdown_control_executed: bool = False
    portfolio_adjustment_generated: bool = False
    hedge_derisk_generated: bool = False
    alert_generated: bool = False
    dashboard_generated: bool = False
    metric_calculated: bool = False
    var_calculated: bool = False
    expected_shortfall_calculated: bool = False
    optimizer_executed: bool = False
    model_training_executed: bool = False
    prediction_generated: bool = False
    target_label_generated: bool = False
    broker_order_sent: bool = False
    live_order_sent: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    production_deployed: bool = False
    source_preserved: bool = True
    manual_review_required: bool = True
    phase_158_handoff_ready: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False


@dataclass(frozen=True)
class PortfolioAcceptanceManualReviewItem:
    """Represents an item queued for human review prior to final system integration."""
    item_id: str
    phase_ref: str
    title: str
    description: str
    action_required: str
    status: str = "PENDING_REVIEW"
