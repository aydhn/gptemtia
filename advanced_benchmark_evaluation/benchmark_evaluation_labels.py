# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Labels Module.

Standardized domain labels, status codes, and execution blockers for Phase 151.
"""

from typing import List

# ---------------------------------------------------------------------------
# Domain Labels
# ---------------------------------------------------------------------------
LABEL_BENCHMARK_EVALUATION_PROFILE_DOMAIN = "benchmark_evaluation_profile_domain"
LABEL_BENCHMARK_EVALUATION_DOMAIN = "benchmark_evaluation_domain"
LABEL_BENCHMARK_EVALUATION_SCOPE_DOMAIN = "benchmark_evaluation_scope_domain"
LABEL_BENCHMARK_REPORT_CONTRACT_DOMAIN = "benchmark_report_contract_domain"
LABEL_STRATEGY_EVALUATION_REPORT_CONTRACT_DOMAIN = "strategy_evaluation_report_contract_domain"
LABEL_BENCHMARK_UNIVERSE_REPORT_DOMAIN = "benchmark_universe_report_domain"
LABEL_BENCHMARK_BASELINE_REPORT_DOMAIN = "benchmark_baseline_report_domain"
LABEL_STRATEGY_VS_BENCHMARK_REPORT_DOMAIN = "strategy_vs_benchmark_report_domain"
LABEL_COST_ADJUSTED_EVALUATION_DOMAIN = "cost_adjusted_evaluation_domain"
LABEL_SLIPPAGE_ADJUSTED_EVALUATION_DOMAIN = "slippage_adjusted_evaluation_domain"
LABEL_REGIME_AWARE_EVALUATION_DOMAIN = "regime_aware_evaluation_domain"
LABEL_WALK_FORWARD_EVALUATION_DOMAIN = "walk_forward_evaluation_domain"
LABEL_OOS_EVALUATION_DOMAIN = "oos_evaluation_domain"
LABEL_STRESS_AWARE_EVALUATION_DOMAIN = "stress_aware_evaluation_domain"
LABEL_MONTE_CARLO_ROBUSTNESS_EVALUATION_DOMAIN = "monte_carlo_robustness_evaluation_domain"
LABEL_PARAMETER_STABILITY_EVALUATION_DOMAIN = "parameter_stability_evaluation_domain"
LABEL_GOVERNANCE_AWARE_EVALUATION_DOMAIN = "governance_aware_evaluation_domain"
LABEL_RESULT_DISCLOSURE_DOMAIN = "result_disclosure_domain"
LABEL_SUMMARY_PLACEHOLDER_DOMAIN = "summary_placeholder_domain"
LABEL_METRIC_PLACEHOLDER_DOMAIN = "metric_placeholder_domain"
LABEL_RISK_SUMMARY_DOMAIN = "risk_summary_domain"
LABEL_COST_IMPACT_SUMMARY_DOMAIN = "cost_impact_summary_domain"
LABEL_SLIPPAGE_IMPACT_SUMMARY_DOMAIN = "slippage_impact_summary_domain"
LABEL_REPORT_DISCLAIMER_DOMAIN = "report_disclaimer_domain"
LABEL_CLAIM_GUARD_DOMAIN = "claim_guard_domain"
LABEL_STRATEGY_APPROVAL_GUARD_DOMAIN = "strategy_approval_guard_domain"
LABEL_BENCHMARK_SELECTION_BIAS_GUARD_DOMAIN = "benchmark_selection_bias_guard_domain"
LABEL_DISABLED_EXECUTION_DOMAIN = "disabled_execution_domain"
LABEL_DEPENDENCY_DOMAIN = "dependency_domain"
LABEL_FINDING_DOMAIN = "finding_domain"
LABEL_READINESS_SCORE_DOMAIN = "readiness_score_domain"
LABEL_MANIFEST_DOMAIN = "manifest_domain"
LABEL_HEALTH_DOMAIN = "health_domain"
LABEL_VALIDATION_DOMAIN = "validation_domain"
LABEL_SAFETY_DOMAIN = "safety_domain"
LABEL_PHASE_152_HANDOFF_DOMAIN = "phase_152_handoff_domain"

ALL_DOMAINS: List[str] = [
    LABEL_BENCHMARK_EVALUATION_PROFILE_DOMAIN,
    LABEL_BENCHMARK_EVALUATION_DOMAIN,
    LABEL_BENCHMARK_EVALUATION_SCOPE_DOMAIN,
    LABEL_BENCHMARK_REPORT_CONTRACT_DOMAIN,
    LABEL_STRATEGY_EVALUATION_REPORT_CONTRACT_DOMAIN,
    LABEL_BENCHMARK_UNIVERSE_REPORT_DOMAIN,
    LABEL_BENCHMARK_BASELINE_REPORT_DOMAIN,
    LABEL_STRATEGY_VS_BENCHMARK_REPORT_DOMAIN,
    LABEL_COST_ADJUSTED_EVALUATION_DOMAIN,
    LABEL_SLIPPAGE_ADJUSTED_EVALUATION_DOMAIN,
    LABEL_REGIME_AWARE_EVALUATION_DOMAIN,
    LABEL_WALK_FORWARD_EVALUATION_DOMAIN,
    LABEL_OOS_EVALUATION_DOMAIN,
    LABEL_STRESS_AWARE_EVALUATION_DOMAIN,
    LABEL_MONTE_CARLO_ROBUSTNESS_EVALUATION_DOMAIN,
    LABEL_PARAMETER_STABILITY_EVALUATION_DOMAIN,
    LABEL_GOVERNANCE_AWARE_EVALUATION_DOMAIN,
    LABEL_RESULT_DISCLOSURE_DOMAIN,
    LABEL_SUMMARY_PLACEHOLDER_DOMAIN,
    LABEL_METRIC_PLACEHOLDER_DOMAIN,
    LABEL_RISK_SUMMARY_DOMAIN,
    LABEL_COST_IMPACT_SUMMARY_DOMAIN,
    LABEL_SLIPPAGE_IMPACT_SUMMARY_DOMAIN,
    LABEL_REPORT_DISCLAIMER_DOMAIN,
    LABEL_CLAIM_GUARD_DOMAIN,
    LABEL_STRATEGY_APPROVAL_GUARD_DOMAIN,
    LABEL_BENCHMARK_SELECTION_BIAS_GUARD_DOMAIN,
    LABEL_DISABLED_EXECUTION_DOMAIN,
    LABEL_DEPENDENCY_DOMAIN,
    LABEL_FINDING_DOMAIN,
    LABEL_READINESS_SCORE_DOMAIN,
    LABEL_MANIFEST_DOMAIN,
    LABEL_HEALTH_DOMAIN,
    LABEL_VALIDATION_DOMAIN,
    LABEL_SAFETY_DOMAIN,
    LABEL_PHASE_152_HANDOFF_DOMAIN,
]

# ---------------------------------------------------------------------------
# Status Labels
# ---------------------------------------------------------------------------
STATUS_EVALUATION_CONTRACT_READY = "evaluation_contract_ready"
STATUS_EVALUATION_CONTRACT_READY_WITH_WARNINGS = "evaluation_contract_ready_with_warnings"
STATUS_EVALUATION_CONTRACT_MANUAL_REVIEW_REQUIRED = "evaluation_contract_manual_review_required"
STATUS_EVALUATION_CONTRACT_BLOCKED_BY_SAFETY = "evaluation_contract_blocked_by_safety"
STATUS_EVALUATION_CONTRACT_ONLY = "evaluation_contract_only"
STATUS_EVALUATION_UNKNOWN = "evaluation_unknown"

# ---------------------------------------------------------------------------
# Execution Labels
# ---------------------------------------------------------------------------
EXEC_BLOCKED_NO_BENCHMARK_REPORT = "execution_blocked_no_benchmark_report"
EXEC_BLOCKED_NO_STRATEGY_EVALUATION = "execution_blocked_no_strategy_evaluation"
EXEC_BLOCKED_NO_METRIC_CALCULATION = "execution_blocked_no_metric_calculation"
EXEC_BLOCKED_NO_RESULT_CLAIM = "execution_blocked_no_result_claim"
EXEC_BLOCKED_NO_STRATEGY_APPROVAL = "execution_blocked_no_strategy_approval"
EXEC_BLOCKED_NO_OPTIMIZER = "execution_blocked_no_optimizer"
EXEC_BLOCKED_NO_MODEL_TRAINING = "execution_blocked_no_model_training"
EXEC_BLOCKED_NO_PREDICTION = "execution_blocked_no_prediction"
EXEC_BLOCKED_NO_LIVE_TRADING = "execution_blocked_no_live_trading"
EXEC_BLOCKED_NO_BROKER = "execution_blocked_no_broker"
EXEC_CONTRACT_ONLY = "execution_contract_only"
