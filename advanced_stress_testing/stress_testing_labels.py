# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing and Scenario Simulation Labels.

Provides standardized domain labels, status labels, and execution labels
for stress testing and scenario simulation contracts.
"""

# Domain Labels
STRESS_TESTING_PROFILE_DOMAIN = "stress_testing_profile_domain"
STRESS_TESTING_DOMAIN = "stress_testing_domain"
STRESS_TESTING_SCOPE_DOMAIN = "stress_testing_scope_domain"
STRESS_SCENARIO_CONTRACT_DOMAIN = "stress_scenario_contract_domain"
HISTORICAL_SCENARIO_CONTRACT_DOMAIN = "historical_scenario_contract_domain"
HYPOTHETICAL_SCENARIO_CONTRACT_DOMAIN = "hypothetical_scenario_contract_domain"
REGIME_SHOCK_DOMAIN = "regime_shock_domain"
VOLATILITY_SHOCK_DOMAIN = "volatility_shock_domain"
LIQUIDITY_SHOCK_DOMAIN = "liquidity_shock_domain"
SPREAD_WIDENING_DOMAIN = "spread_widening_domain"
GAP_RISK_PLACEHOLDER_DOMAIN = "gap_risk_placeholder_domain"
CORRELATION_BREAKDOWN_PLACEHOLDER_DOMAIN = "correlation_breakdown_placeholder_domain"
MACRO_SHOCK_PLACEHOLDER_DOMAIN = "macro_shock_placeholder_domain"
CROSS_ASSET_CONTAGION_PLACEHOLDER_DOMAIN = "cross_asset_contagion_placeholder_domain"
EXECUTION_DISRUPTION_PLACEHOLDER_DOMAIN = "execution_disruption_placeholder_domain"
TRANSACTION_COST_SHOCK_DOMAIN = "transaction_cost_shock_domain"
SLIPPAGE_SHOCK_DOMAIN = "slippage_shock_domain"
STRESS_METRIC_PLACEHOLDER_DOMAIN = "stress_metric_placeholder_domain"
SCENARIO_METRIC_PLACEHOLDER_DOMAIN = "scenario_metric_placeholder_domain"
ROBUSTNESS_METRIC_PLACEHOLDER_DOMAIN = "robustness_metric_placeholder_domain"
OUTPUT_CONTRACT_DOMAIN = "output_contract_domain"
DEPENDENCY_DOMAIN = "dependency_domain"
BIAS_GUARD_DOMAIN = "bias_guard_domain"
DISABLED_EXECUTION_DOMAIN = "disabled_execution_domain"
FINDING_DOMAIN = "finding_domain"
READINESS_SCORE_DOMAIN = "readiness_score_domain"
MANIFEST_DOMAIN = "manifest_domain"
HEALTH_DOMAIN = "health_domain"
VALIDATION_DOMAIN = "validation_domain"
SAFETY_DOMAIN = "safety_domain"
PHASE_149_HANDOFF_DOMAIN = "phase_149_handoff_domain"

# Status Labels
STRESS_CONTRACT_READY = "stress_contract_ready"
STRESS_CONTRACT_READY_WITH_WARNINGS = "stress_contract_ready_with_warnings"
STRESS_CONTRACT_MANUAL_REVIEW_REQUIRED = "stress_contract_manual_review_required"
STRESS_CONTRACT_BLOCKED_BY_SAFETY = "stress_contract_blocked_by_safety"
STRESS_CONTRACT_ONLY = "stress_contract_only"
STRESS_UNKNOWN = "stress_unknown"

# Execution Labels
EXECUTION_BLOCKED_NO_STRESS_TEST = "execution_blocked_no_stress_test"
EXECUTION_BLOCKED_NO_SCENARIO_SIMULATION = "execution_blocked_no_scenario_simulation"
EXECUTION_BLOCKED_NO_METRIC_CALCULATION = "execution_blocked_no_metric_calculation"
EXECUTION_BLOCKED_NO_OPTIMIZER = "execution_blocked_no_optimizer"
EXECUTION_BLOCKED_NO_MODEL_TRAINING = "execution_blocked_no_model_training"
EXECUTION_BLOCKED_NO_PREDICTION = "execution_blocked_no_prediction"
EXECUTION_BLOCKED_NO_LIVE_TRADING = "execution_blocked_no_live_trading"
EXECUTION_BLOCKED_NO_BROKER = "execution_blocked_no_broker"
EXECUTION_CONTRACT_ONLY = "execution_contract_only"

DOMAIN_LABELS = [
    STRESS_TESTING_PROFILE_DOMAIN,
    STRESS_TESTING_DOMAIN,
    STRESS_TESTING_SCOPE_DOMAIN,
    STRESS_SCENARIO_CONTRACT_DOMAIN,
    HISTORICAL_SCENARIO_CONTRACT_DOMAIN,
    HYPOTHETICAL_SCENARIO_CONTRACT_DOMAIN,
    REGIME_SHOCK_DOMAIN,
    VOLATILITY_SHOCK_DOMAIN,
    LIQUIDITY_SHOCK_DOMAIN,
    SPREAD_WIDENING_DOMAIN,
    GAP_RISK_PLACEHOLDER_DOMAIN,
    CORRELATION_BREAKDOWN_PLACEHOLDER_DOMAIN,
    MACRO_SHOCK_PLACEHOLDER_DOMAIN,
    CROSS_ASSET_CONTAGION_PLACEHOLDER_DOMAIN,
    EXECUTION_DISRUPTION_PLACEHOLDER_DOMAIN,
    TRANSACTION_COST_SHOCK_DOMAIN,
    SLIPPAGE_SHOCK_DOMAIN,
    STRESS_METRIC_PLACEHOLDER_DOMAIN,
    SCENARIO_METRIC_PLACEHOLDER_DOMAIN,
    ROBUSTNESS_METRIC_PLACEHOLDER_DOMAIN,
    OUTPUT_CONTRACT_DOMAIN,
    DEPENDENCY_DOMAIN,
    BIAS_GUARD_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_149_HANDOFF_DOMAIN,
]

STATUS_LABELS = [
    STRESS_CONTRACT_READY,
    STRESS_CONTRACT_READY_WITH_WARNINGS,
    STRESS_CONTRACT_MANUAL_REVIEW_REQUIRED,
    STRESS_CONTRACT_BLOCKED_BY_SAFETY,
    STRESS_CONTRACT_ONLY,
    STRESS_UNKNOWN,
]

EXECUTION_LABELS = [
    EXECUTION_BLOCKED_NO_STRESS_TEST,
    EXECUTION_BLOCKED_NO_SCENARIO_SIMULATION,
    EXECUTION_BLOCKED_NO_METRIC_CALCULATION,
    EXECUTION_BLOCKED_NO_OPTIMIZER,
    EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    EXECUTION_BLOCKED_NO_PREDICTION,
    EXECUTION_BLOCKED_NO_LIVE_TRADING,
    EXECUTION_BLOCKED_NO_BROKER,
    EXECUTION_CONTRACT_ONLY,
]
