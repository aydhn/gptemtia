# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Models and Data Structures."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class PortfolioConstructionProfileItem:
    """Model representing a portfolio construction profile item."""
    profile_name: str
    description: str
    current_phase: int = 153
    target_final_phase: int = 160
    next_phase: int = 154
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    min_readiness_score: float = 0.50
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False


@dataclass
class PortfolioConstructionContract:
    """Model representing a portfolio construction contract."""
    contract_name: str
    portfolio_family: str
    backtest_acceptance_ref: str
    benchmark_evaluation_ref: str
    model_governance_ref: str
    regime_context_ref: str
    featurestore_ref: str
    risk_budget_ref: str
    position_sizing_ref: str
    limit_contract_ref: str
    no_lookahead_guard_ref: str
    investment_advice_guard_ref: str
    description: str = ""
    status: str = "PORTFOLIO_CONTRACT_READY"
    portfolio_construction_allowed: bool = False
    position_sizing_allowed: bool = False
    capital_allocation_allowed: bool = False
    weight_generation_allowed: bool = False
    order_generation_allowed: bool = False
    optimizer_execution_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    manual_review_required: bool = True
    contract_only: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False


@dataclass
class PositionSizingContract:
    """Model representing a position sizing contract."""
    sizing_name: str
    sizing_family: str
    risk_budget_ref: str
    exposure_limit_ref: str
    concentration_limit_ref: str
    volatility_budget_ref: str
    drawdown_budget_ref: str
    liquidity_limit_ref: str
    transaction_cost_ref: str
    slippage_model_ref: str
    description: str = ""
    status: str = "POSITION_SIZING_CONTRACT_READY"
    position_sizing_allowed: bool = False
    capital_allocation_allowed: bool = False
    order_generation_allowed: bool = False
    broker_execution_allowed: bool = False
    investment_advice_allowed: bool = False
    manual_review_required: bool = True
    contract_only: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False


@dataclass
class RiskBudgetContract:
    """Model representing a risk budget contract."""
    budget_name: str
    risk_budget_family: str
    asset_scope: str
    strategy_scope: str
    regime_scope: str
    limit_ref: str
    output_ref: str
    description: str = ""
    status: str = "RISK_BUDGET_CONTRACT_READY"
    risk_budget_generation_allowed: bool = False
    capital_allocation_allowed: bool = False
    position_sizing_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    manual_review_required: bool = True
    contract_only: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False


@dataclass
class PortfolioLimitContract:
    """Model representing an exposure or concentration limit contract/placeholder."""
    limit_name: str
    limit_family: str
    scope: str
    threshold_value: float
    unit: str
    description: str = ""
    status: str = "LIMIT_CONTRACT_READY"
    actual_limits_assigned: bool = False
    broker_margin_recommended: bool = False
    manual_review_required: bool = True
    contract_only: bool = True
    non_production: bool = True


@dataclass
class PortfolioMetricPlaceholder:
    """Model representing a placeholder metric metadata."""
    metric_name: str
    metric_family: str
    formula_reference: str
    computation_status: str = "METRIC_CALCULATION_DISABLED"
    real_calculation_executed: bool = False
    performance_claim_generated: bool = False
    non_signal: bool = True
    description: str = ""


@dataclass
class PortfolioGuardItem:
    """Model representing a safety guard or policy enforcement."""
    guard_name: str
    guard_domain: str
    policy_rule: str
    enforced: bool = True
    status: str = "GUARD_ACTIVE"
    violations_caught: int = 0
    non_signal: bool = True


LimitContract = PortfolioLimitContract
PortfolioGuardContract = PortfolioGuardItem


@dataclass
class PortfolioDisabledExecutionItem:
    """Model representing a disabled execution check."""
    report_name: str
    action_type: str
    execution_prohibited: bool = True
    reason: str = "Strict offline/local contract boundaries prevent execution."
    status: str = "EXECUTION_DISABLED"
    blocked_requests_count: int = 0


@dataclass
class PortfolioFinding:
    """Model representing a portfolio construction finding."""
    finding_id: str
    finding_type: str
    domain: str
    severity: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass
class PortfolioReadinessScore:
    """Model representing readiness score assessment."""
    overall_score: float
    classification: str
    meets_threshold: bool
    findings_count: int
    critical_count: int
    current_phase: int = 153
    target_final_phase: int = 160
    next_phase: int = 154
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

    def __post_init__(self):
        if not (0.0 <= self.overall_score <= 1.0):
            raise ValueError(f"Score must be between 0.0 and 1.0, got {self.overall_score}")


@dataclass
class PortfolioConstructionManifest:
    """Model representing the master manifest for Phase 153."""
    manifest_id: str
    manifest_name: str = "portfolio_construction_manifest"
    current_phase: int = 153
    target_final_phase: int = 160
    next_phase: int = 154
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
    capital_allocation_generated: bool = False
    portfolio_weights_generated: bool = False
    orders_generated: bool = False
    risk_budget_generated: bool = False
    exposure_limits_generated: bool = False
    leverage_recommendation_generated: bool = False
    optimizer_executed: bool = False
    metric_calculated: bool = False
    result_claim_generated: bool = False
    performance_claim_generated: bool = False
    strategy_approved: bool = False
    backtest_executed: bool = False
    benchmark_executed: bool = False
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
    phase_154_handoff_ready: bool = True


@dataclass
class PortfolioManualReviewItem:
    """Model representing an item in the manual review queue."""
    review_id: str
    component_name: str
    review_scope: str
    trigger_reason: str
    action_required: str
    resolution_status: str = "PENDING_OPERATOR_REVIEW"
    auto_remediation_allowed: bool = False
    non_signal: bool = True
