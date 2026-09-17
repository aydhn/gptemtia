# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Labels.

Provides standardized domain labels, status labels, and execution labels
for backtest contract specifications and realistic modeling layers.
"""

# Domain Labels
REALISTIC_BACKTEST_PROFILE_DOMAIN = "realistic_backtest_profile_domain"
REALISTIC_BACKTEST_DOMAIN = "realistic_backtest_domain"
BACKTEST_SCOPE_DOMAIN = "backtest_scope_domain"
ENGINE_CONTRACT_DOMAIN = "engine_contract_domain"
EVENT_DRIVEN_CONTRACT_DOMAIN = "event_driven_contract_domain"
VECTORIZED_CONTRACT_DOMAIN = "vectorized_contract_domain"
PORTFOLIO_CONTRACT_DOMAIN = "portfolio_contract_domain"
ORDER_SIMULATION_DOMAIN = "order_simulation_domain"
FILL_MODEL_DOMAIN = "fill_model_domain"
EXECUTION_PRICE_MODEL_DOMAIN = "execution_price_model_domain"
COMMISSION_MODEL_DOMAIN = "commission_model_domain"
FEE_MODEL_DOMAIN = "fee_model_domain"
SPREAD_MODEL_DOMAIN = "spread_model_domain"
SLIPPAGE_MODEL_DOMAIN = "slippage_model_domain"
MARKET_IMPACT_PLACEHOLDER_DOMAIN = "market_impact_placeholder_domain"
LATENCY_PLACEHOLDER_DOMAIN = "latency_placeholder_domain"
LIQUIDITY_CONSTRAINT_PLACEHOLDER_DOMAIN = "liquidity_constraint_placeholder_domain"
TRANSACTION_COST_DOMAIN = "transaction_cost_domain"
ACCOUNTING_CONTRACT_DOMAIN = "accounting_contract_domain"
LIFECYCLE_CONTRACT_DOMAIN = "lifecycle_contract_domain"
BIAS_GUARD_DOMAIN = "bias_guard_domain"
DISABLED_EXECUTION_DOMAIN = "disabled_execution_domain"
DEPENDENCY_DOMAIN = "dependency_domain"
VALIDATION_EVIDENCE_DOMAIN = "validation_evidence_domain"
FINDING_DOMAIN = "finding_domain"
READINESS_SCORE_DOMAIN = "readiness_score_domain"
MANIFEST_DOMAIN = "manifest_domain"
HEALTH_DOMAIN = "health_domain"
VALIDATION_DOMAIN = "validation_domain"
SAFETY_DOMAIN = "safety_domain"
PHASE_147_HANDOFF_DOMAIN = "phase_147_handoff_domain"

# Status Labels
BACKTEST_CONTRACT_READY = "backtest_contract_ready"
BACKTEST_CONTRACT_READY_WITH_WARNINGS = "backtest_contract_ready_with_warnings"
BACKTEST_CONTRACT_MANUAL_REVIEW_REQUIRED = "backtest_contract_manual_review_required"
BACKTEST_CONTRACT_BLOCKED_BY_SAFETY = "backtest_contract_blocked_by_safety"
BACKTEST_CONTRACT_ONLY = "backtest_contract_only"
BACKTEST_UNKNOWN = "backtest_unknown"

# Execution Labels
EXECUTION_BLOCKED_NO_LIVE_TRADING = "execution_blocked_no_live_trading"
EXECUTION_BLOCKED_NO_BROKER = "execution_blocked_no_broker"
EXECUTION_BLOCKED_NO_OPTIMIZER = "execution_blocked_no_optimizer"
EXECUTION_BLOCKED_NO_WALK_FORWARD = "execution_blocked_no_walk_forward"
EXECUTION_BLOCKED_NO_BENCHMARK = "execution_blocked_no_benchmark"
EXECUTION_BLOCKED_NO_MODEL_TRAINING = "execution_blocked_no_model_training"
EXECUTION_BLOCKED_NO_PREDICTION = "execution_blocked_no_prediction"
EXECUTION_CONTRACT_ONLY = "execution_contract_only"

DOMAIN_LABELS = [
    REALISTIC_BACKTEST_PROFILE_DOMAIN,
    REALISTIC_BACKTEST_DOMAIN,
    BACKTEST_SCOPE_DOMAIN,
    ENGINE_CONTRACT_DOMAIN,
    EVENT_DRIVEN_CONTRACT_DOMAIN,
    VECTORIZED_CONTRACT_DOMAIN,
    PORTFOLIO_CONTRACT_DOMAIN,
    ORDER_SIMULATION_DOMAIN,
    FILL_MODEL_DOMAIN,
    EXECUTION_PRICE_MODEL_DOMAIN,
    COMMISSION_MODEL_DOMAIN,
    FEE_MODEL_DOMAIN,
    SPREAD_MODEL_DOMAIN,
    SLIPPAGE_MODEL_DOMAIN,
    MARKET_IMPACT_PLACEHOLDER_DOMAIN,
    LATENCY_PLACEHOLDER_DOMAIN,
    LIQUIDITY_CONSTRAINT_PLACEHOLDER_DOMAIN,
    TRANSACTION_COST_DOMAIN,
    ACCOUNTING_CONTRACT_DOMAIN,
    LIFECYCLE_CONTRACT_DOMAIN,
    BIAS_GUARD_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    DEPENDENCY_DOMAIN,
    VALIDATION_EVIDENCE_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_147_HANDOFF_DOMAIN,
]

STATUS_LABELS = [
    BACKTEST_CONTRACT_READY,
    BACKTEST_CONTRACT_READY_WITH_WARNINGS,
    BACKTEST_CONTRACT_MANUAL_REVIEW_REQUIRED,
    BACKTEST_CONTRACT_BLOCKED_BY_SAFETY,
    BACKTEST_CONTRACT_ONLY,
    BACKTEST_UNKNOWN,
]

EXECUTION_LABELS = [
    EXECUTION_BLOCKED_NO_LIVE_TRADING,
    EXECUTION_BLOCKED_NO_BROKER,
    EXECUTION_BLOCKED_NO_OPTIMIZER,
    EXECUTION_BLOCKED_NO_WALK_FORWARD,
    EXECUTION_BLOCKED_NO_BENCHMARK,
    EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    EXECUTION_BLOCKED_NO_PREDICTION,
    EXECUTION_CONTRACT_ONLY,
]


def get_domain_label_description(label: str) -> str:
    return f"Domain specification for {label}"


def get_status_label_description(label: str) -> str:
    return f"Status evaluation for {label}"


def get_execution_label_description(label: str) -> str:
    return f"Execution constraint for {label}"

