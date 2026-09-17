# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization and Allocation Constraints Data Models.

Defines Pydantic / dataclass models for profiles, contracts, objectives,
constraints, solvers, guards, findings, readiness score, and manifest.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_validator


class PortfolioOptimizationProfileItem(BaseModel):
    """Pydantic model for a registered optimization profile."""
    profile_name: str
    description: str
    current_phase: int = 154
    target_final_phase: int = 160
    next_phase: int = 155
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_signal_generation: bool = False
    allow_portfolio_optimization: bool = False
    allow_portfolio_construction: bool = False
    allow_position_sizing: bool = False
    allow_capital_allocation: bool = False
    allow_weight_generation: bool = False
    allow_allocation_generation: bool = False
    allow_rebalance_generation: bool = False
    allow_order_generation: bool = False
    allow_optimizer_execution: bool = False
    allow_solver_execution: bool = False
    allow_grid_search_execution: bool = False
    allow_efficient_frontier_generation: bool = False
    allow_metric_calculation: bool = False
    min_readiness_score: float = Field(default=0.50, ge=0.0, le=1.0)


class PortfolioOptimizationContract(BaseModel):
    """Model representing an offline/local portfolio optimization contract."""
    contract_name: str
    optimization_family: str
    portfolio_construction_ref: str
    risk_budget_ref: str
    allocation_constraint_ref: str
    objective_ref: str
    solver_ref: str
    backtest_acceptance_ref: str
    benchmark_evaluation_ref: str
    model_governance_ref: str
    regime_context_ref: str
    featurestore_ref: str
    no_lookahead_guard_ref: str
    investment_advice_guard_ref: str
    portfolio_optimization_allowed: bool = False
    solver_execution_allowed: bool = False
    weight_generation_allowed: bool = False
    allocation_generation_allowed: bool = False
    rebalance_generation_allowed: bool = False
    order_generation_allowed: bool = False
    optimizer_execution_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    manual_review_required: bool = True


class OptimizationObjectiveContract(BaseModel):
    """Model representing an optimization objective specification."""
    objective_name: str
    objective_type: str  # e.g., "mean_variance", "min_variance", "max_sharpe", "risk_parity", "cvar", "drawdown", "turnover"
    description: str
    mathematical_formulation: str
    target_variable: str
    risk_metric_ref: str
    is_placeholder: bool = True
    actual_objective_calculated: Optional[float] = None
    is_calculated: bool = False
    allows_execution: bool = False


class AllocationConstraintContract(BaseModel):
    """Model representing an allocation constraint specification."""
    constraint_name: str
    constraint_family: str  # e.g., "long_only", "weight", "exposure", "turnover", "risk_budget", "leverage"
    description: str
    mathematical_formulation: str
    bound_type: str  # "equality", "upper_bound", "lower_bound", "box"
    is_placeholder: bool = True
    is_enforced_live: bool = False
    allows_weight_generation: bool = False
    allows_allocation_generation: bool = False


class SolverContract(BaseModel):
    """Model representing an optimization solver contract specification."""
    solver_name: str
    solver_type: str  # "convex", "heuristic", "grid_search_disabled"
    description: str
    supported_objectives: List[str]
    is_placeholder: bool = True
    solver_executed: bool = False
    allows_execution: bool = False


class OptimizationMetricPlaceholder(BaseModel):
    """Model representing a metric placeholder with formula metadata."""
    metric_name: str
    metric_domain: str
    formula_description: str
    unit: str
    is_placeholder: bool = True
    actual_value: Optional[float] = None
    is_calculated: bool = False


class OptimizationGuardItem(BaseModel):
    """Model for an optimization safety guard policy."""
    guard_name: str
    domain: str
    guard_rule: str
    is_active: bool = True
    action_on_violation: str = "BLOCK"


class OptimizationDisabledExecutionItem(BaseModel):
    """Model documenting a strictly disabled execution component."""
    component_name: str
    prohibited_actions: List[str]
    enforcement_mechanism: str
    is_disabled: bool = True
    status: str = "execution_contract_only"


class PortfolioOptimizationFinding(BaseModel):
    """Diagnostic finding item."""
    finding_id: str
    finding_type: str
    domain: str
    severity_label: str  # "INFO", "WARNING", "BLOCKER"
    message: str
    recommendation: str
    manual_review_required: bool = True

    @field_validator("recommendation")
    @classmethod
    def validate_no_prohibited_actions(cls, v: str) -> str:
        prohibited = [
            "auto-optimize portfolio",
            "auto-generate weights",
            "auto-generate allocation",
            "auto-rebalance portfolio",
            "auto-generate orders",
            "auto-solve optimizer",
            "auto-calculate efficient frontier",
            "auto-calculate Sharpe/CVaR",
            "auto-send broker order",
            "auto-generate signal",
            "auto-run prediction",
            "approve production",
            "approve broker readiness",
            "auto-deploy",
            "auto-write model registry",
            "auto-overwrite",
            "auto-delete",
            "auto-impute",
            "enable scraping",
        ]
        for p in prohibited:
            if p.lower() in v.lower():
                raise ValueError(f"Prohibited automatic remediation phrase detected: '{p}'")
        return v


class PortfolioOptimizationReadinessScore(BaseModel):
    """Readiness scoring model for Phase 154."""
    readiness_score: float = Field(..., ge=0.0, le=1.0)
    classification: str
    is_contract_ready: bool
    summary_text: str
    current_phase: int = 154
    target_final_phase: int = 160
    next_phase: int = 155
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False


class PortfolioOptimizationManifest(BaseModel):
    """Master Phase 154 portfolio optimization manifest."""
    manifest_name: str = "Phase 154 Portfolio Optimization and Allocation Constraints Manifest"
    current_phase: int = 154
    target_final_phase: int = 160
    next_phase: int = 155
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    portfolio_optimized: bool = False
    portfolio_constructed: bool = False
    position_sizing_generated: bool = False
    capital_allocation_generated: bool = False
    portfolio_weights_generated: bool = False
    allocation_generated: bool = False
    rebalance_generated: bool = False
    orders_generated: bool = False
    risk_budget_generated: bool = False
    exposure_limits_generated: bool = False
    efficient_frontier_generated: bool = False
    optimizer_executed: bool = False
    solver_executed: bool = False
    grid_search_executed: bool = False
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
    phase_155_handoff_ready: bool = True


class PortfolioOptimizationManualReviewItem(BaseModel):
    """Manual review queue checkpoint."""
    checkpoint_id: str
    domain: str
    review_target: str
    description: str
    status: str = "PENDING_OPERATOR_REVIEW"
    recommendation: str
