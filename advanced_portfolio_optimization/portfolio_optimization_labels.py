# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization and Allocation Constraints Domain & Status Labels.

Defines standardized, safe, non-commercial domain and status labels.
"""

# Functional Domain Labels
PORTFOLIO_OPTIMIZATION_PROFILE_DOMAIN = "portfolio_optimization_profile_domain"
PORTFOLIO_OPTIMIZATION_DOMAIN = "portfolio_optimization_domain"
PORTFOLIO_OPTIMIZATION_SCOPE_DOMAIN = "portfolio_optimization_scope_domain"
OPTIMIZATION_CONTRACT_DOMAIN = "optimization_contract_domain"
OBJECTIVE_CONTRACT_DOMAIN = "objective_contract_domain"
OBJECTIVE_PLACEHOLDER_DOMAIN = "objective_placeholder_domain"
ALLOCATION_CONSTRAINT_DOMAIN = "allocation_constraint_domain"
EXPOSURE_CONSTRAINT_DOMAIN = "exposure_constraint_domain"
TURNOVER_CONSTRAINT_DOMAIN = "turnover_constraint_domain"
RISK_BUDGET_CONSTRAINT_DOMAIN = "risk_budget_constraint_domain"
VOLATILITY_CONSTRAINT_DOMAIN = "volatility_constraint_domain"
DRAWDOWN_CONSTRAINT_DOMAIN = "drawdown_constraint_domain"
LEVERAGE_MARGIN_CONSTRAINT_DOMAIN = "leverage_margin_constraint_domain"
SOLVER_CONTRACT_DOMAIN = "solver_contract_domain"
SOLVER_PLACEHOLDER_DOMAIN = "solver_placeholder_domain"
EFFICIENT_FRONTIER_PLACEHOLDER_DOMAIN = "efficient_frontier_placeholder_domain"
OUTPUT_CONTRACT_DOMAIN = "output_contract_domain"
METRIC_PLACEHOLDER_DOMAIN = "metric_placeholder_domain"
DEPENDENCY_DOMAIN = "dependency_domain"
CLAIM_GUARD_DOMAIN = "claim_guard_domain"
DISABLED_EXECUTION_DOMAIN = "disabled_execution_domain"
FINDING_DOMAIN = "finding_domain"
READINESS_SCORE_DOMAIN = "readiness_score_domain"
MANIFEST_DOMAIN = "manifest_domain"
HEALTH_DOMAIN = "health_domain"
VALIDATION_DOMAIN = "validation_domain"
SAFETY_DOMAIN = "safety_domain"
PHASE_155_HANDOFF_DOMAIN = "phase_155_handoff_domain"

ALL_DOMAINS = [
    PORTFOLIO_OPTIMIZATION_PROFILE_DOMAIN,
    PORTFOLIO_OPTIMIZATION_DOMAIN,
    PORTFOLIO_OPTIMIZATION_SCOPE_DOMAIN,
    OPTIMIZATION_CONTRACT_DOMAIN,
    OBJECTIVE_CONTRACT_DOMAIN,
    OBJECTIVE_PLACEHOLDER_DOMAIN,
    ALLOCATION_CONSTRAINT_DOMAIN,
    EXPOSURE_CONSTRAINT_DOMAIN,
    TURNOVER_CONSTRAINT_DOMAIN,
    RISK_BUDGET_CONSTRAINT_DOMAIN,
    VOLATILITY_CONSTRAINT_DOMAIN,
    DRAWDOWN_CONSTRAINT_DOMAIN,
    LEVERAGE_MARGIN_CONSTRAINT_DOMAIN,
    SOLVER_CONTRACT_DOMAIN,
    SOLVER_PLACEHOLDER_DOMAIN,
    EFFICIENT_FRONTIER_PLACEHOLDER_DOMAIN,
    OUTPUT_CONTRACT_DOMAIN,
    METRIC_PLACEHOLDER_DOMAIN,
    DEPENDENCY_DOMAIN,
    CLAIM_GUARD_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_155_HANDOFF_DOMAIN,
]

# Status Labels
OPTIMIZATION_CONTRACT_READY = "optimization_contract_ready"
OPTIMIZATION_CONTRACT_READY_WITH_WARNINGS = "optimization_contract_ready_with_warnings"
OPTIMIZATION_CONTRACT_MANUAL_REVIEW_REQUIRED = "optimization_contract_manual_review_required"
OPTIMIZATION_CONTRACT_BLOCKED_BY_SAFETY = "optimization_contract_blocked_by_safety"
OPTIMIZATION_CONTRACT_ONLY = "optimization_contract_only"
OPTIMIZATION_UNKNOWN = "optimization_unknown"
PORTFOLIO_OPTIMIZATION_CONTRACT_READY = "portfolio_optimization_contract_ready"
HANDOFF_READY = "HANDOFF_READY"
HANDOFF_BLOCKED = "HANDOFF_BLOCKED"

# Execution Labels (Blocked Invariants)
EXECUTION_BLOCKED_NO_PORTFOLIO_OPTIMIZATION = "execution_blocked_no_portfolio_optimization"
EXECUTION_BLOCKED_NO_SOLVER = "execution_blocked_no_solver"
EXECUTION_BLOCKED_NO_WEIGHT_GENERATION = "execution_blocked_no_weight_generation"
EXECUTION_BLOCKED_NO_ALLOCATION_GENERATION = "execution_blocked_no_allocation_generation"
EXECUTION_BLOCKED_NO_REBALANCE_GENERATION = "execution_blocked_no_rebalance_generation"
EXECUTION_BLOCKED_NO_ORDER_GENERATION = "execution_blocked_no_order_generation"
EXECUTION_BLOCKED_NO_METRIC_CALCULATION = "execution_blocked_no_metric_calculation"
EXECUTION_BLOCKED_NO_MODEL_TRAINING = "execution_blocked_no_model_training"
EXECUTION_BLOCKED_NO_PREDICTION = "execution_blocked_no_prediction"
EXECUTION_BLOCKED_NO_LIVE_TRADING = "execution_blocked_no_live_trading"
EXECUTION_BLOCKED_NO_BROKER = "execution_blocked_no_broker"
EXECUTION_CONTRACT_ONLY = "execution_contract_only"

from enum import Enum

class OptimizationProfileType(str, Enum):
    BALANCED = "balanced"
    STRICT_SAFETY = "strict_safety"
    DRY_RUN = "dry_run"

class OptimizationDomainType(str, Enum):
    PORTFOLIO_OPTIMIZATION = "portfolio_optimization"
    OBJECTIVE = "objective"
    CONSTRAINT = "constraint"
    SOLVER = "solver"
    OUTPUT = "output"
    METRIC = "metric"
    SAFETY = "safety"
    HANDOFF = "handoff"

class OptimizationScopeType(str, Enum):
    ASSET = "asset"
    STRATEGY = "strategy"
    PORTFOLIO = "portfolio"
    CROSS_ASSET = "cross_asset"

class OptimizationObjectiveType(str, Enum):
    MEAN_VARIANCE = "mean_variance"
    MINIMUM_VARIANCE = "minimum_variance"
    MAXIMUM_SHARPE = "maximum_sharpe"
    RISK_PARITY = "risk_parity"
    CVAR = "cvar"
    DRAWDOWN_MINIMIZATION = "drawdown_minimization"
    TURNOVER_MINIMIZATION = "turnover_minimization"
    COST_AWARE = "cost_aware"
    SLIPPAGE_AWARE = "slippage_aware"
    REGIME_AWARE = "regime_aware"
    ROBUST_OPTIMIZATION = "robust_optimization"

class AllocationConstraintType(str, Enum):
    LONG_ONLY = "long_only"
    MAX_WEIGHT = "max_weight"
    MIN_WEIGHT = "min_weight"
    GROUP_WEIGHT = "group_weight"
    ASSET_COUNT = "asset_count"
    CONCENTRATION = "concentration"
    EXPOSURE = "exposure"
    GROSS_EXPOSURE = "gross_exposure"
    NET_EXPOSURE = "net_exposure"
    CURRENCY_EXPOSURE = "currency_exposure"
    CROSS_ASSET_EXPOSURE = "cross_asset_exposure"
    CORRELATION = "correlation"
    LIQUIDITY = "liquidity"
    TURNOVER = "turnover"
    TRANSACTION_COST = "transaction_cost"
    SLIPPAGE = "slippage"
    RISK_BUDGET = "risk_budget"
    VOLATILITY = "volatility"
    DRAWDOWN = "drawdown"
    LEVERAGE = "leverage"
    MARGIN = "margin"
    REBALANCE = "rebalance"

class OptimizationSolverType(str, Enum):
    CONVEX = "convex"
    HEURISTIC = "heuristic"
    GRID_SEARCH_DISABLED = "grid_search_disabled"
    OPTIMIZER_DISABLED = "optimizer_disabled"

class OptimizationExecutionStatus(str, Enum):
    CONTRACT_ONLY = "contract_only"
    EXECUTION_DISABLED = "execution_disabled"
    BLOCKED = "blocked"

