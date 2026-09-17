# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Validation and Out-of-Sample Benchmarking Labels.

Provides standardized domain labels, status labels, and execution labels
for walk-forward validation contracts and benchmark layers.
"""

# Domain Labels
WALK_FORWARD_PROFILE_DOMAIN = "walk_forward_profile_domain"
WALK_FORWARD_DOMAIN = "walk_forward_domain"
WALK_FORWARD_SCOPE_DOMAIN = "walk_forward_scope_domain"
SPLIT_CONTRACT_DOMAIN = "split_contract_domain"
ROLLING_WINDOW_CONTRACT_DOMAIN = "rolling_window_contract_domain"
EXPANDING_WINDOW_CONTRACT_DOMAIN = "expanding_window_contract_domain"
ANCHORED_WINDOW_CONTRACT_DOMAIN = "anchored_window_contract_domain"
PURGED_WALK_FORWARD_CONTRACT_DOMAIN = "purged_walk_forward_contract_domain"
EMBARGO_POLICY_DOMAIN = "embargo_policy_domain"
TRAIN_VALIDATION_TEST_SPLIT_DOMAIN = "train_validation_test_split_domain"
OUT_OF_SAMPLE_SPLIT_DOMAIN = "out_of_sample_split_domain"
HOLDOUT_PERIOD_DOMAIN = "holdout_period_domain"
TEMPORAL_SPLIT_BOUNDARY_DOMAIN = "temporal_split_boundary_domain"
REGIME_AWARE_SPLIT_DOMAIN = "regime_aware_split_domain"
CROSS_ASSET_OOS_SPLIT_DOMAIN = "cross_asset_oos_split_domain"
WALK_FORWARD_FOLD_DOMAIN = "walk_forward_fold_domain"
WALK_FORWARD_SCHEDULE_PLACEHOLDER_DOMAIN = "walk_forward_schedule_placeholder_domain"
BENCHMARK_CONTRACT_DOMAIN = "benchmark_contract_domain"
BENCHMARK_UNIVERSE_DOMAIN = "benchmark_universe_domain"
BENCHMARK_BASELINE_DOMAIN = "benchmark_baseline_domain"
BENCHMARK_COMPARISON_DOMAIN = "benchmark_comparison_domain"
BENCHMARK_PLACEHOLDER_DOMAIN = "benchmark_placeholder_domain"
BENCHMARK_METRIC_PLACEHOLDER_DOMAIN = "benchmark_metric_placeholder_domain"
VALIDATION_METRIC_PLACEHOLDER_DOMAIN = "validation_metric_placeholder_domain"
OUTPUT_CONTRACT_DOMAIN = "output_contract_domain"
VALIDATION_EVIDENCE_DOMAIN = "validation_evidence_domain"
DEPENDENCY_DOMAIN = "dependency_domain"
BIAS_GUARD_DOMAIN = "bias_guard_domain"
DISABLED_EXECUTION_DOMAIN = "disabled_execution_domain"
FINDING_DOMAIN = "finding_domain"
READINESS_SCORE_DOMAIN = "readiness_score_domain"
MANIFEST_DOMAIN = "manifest_domain"
HEALTH_DOMAIN = "health_domain"
VALIDATION_DOMAIN = "validation_domain"
SAFETY_DOMAIN = "safety_domain"
PHASE_148_HANDOFF_DOMAIN = "phase_148_handoff_domain"

# Status Labels
VALIDATION_CONTRACT_READY = "validation_contract_ready"
VALIDATION_CONTRACT_READY_WITH_WARNINGS = "validation_contract_ready_with_warnings"
VALIDATION_CONTRACT_MANUAL_REVIEW_REQUIRED = "validation_contract_manual_review_required"
VALIDATION_CONTRACT_BLOCKED_BY_SAFETY = "validation_contract_blocked_by_safety"
VALIDATION_CONTRACT_ONLY = "validation_contract_only"
VALIDATION_UNKNOWN = "validation_unknown"

# Execution Labels
EXECUTION_BLOCKED_NO_WALK_FORWARD = "execution_blocked_no_walk_forward"
EXECUTION_BLOCKED_NO_BENCHMARK = "execution_blocked_no_benchmark"
EXECUTION_BLOCKED_NO_METRIC_CALCULATION = "execution_blocked_no_metric_calculation"
EXECUTION_BLOCKED_NO_OPTIMIZER = "execution_blocked_no_optimizer"
EXECUTION_BLOCKED_NO_MODEL_TRAINING = "execution_blocked_no_model_training"
EXECUTION_BLOCKED_NO_PREDICTION = "execution_blocked_no_prediction"
EXECUTION_BLOCKED_NO_LIVE_TRADING = "execution_blocked_no_live_trading"
EXECUTION_BLOCKED_NO_BROKER = "execution_blocked_no_broker"
EXECUTION_CONTRACT_ONLY = "execution_contract_only"

DOMAIN_LABELS = [
    WALK_FORWARD_PROFILE_DOMAIN,
    WALK_FORWARD_DOMAIN,
    WALK_FORWARD_SCOPE_DOMAIN,
    SPLIT_CONTRACT_DOMAIN,
    ROLLING_WINDOW_CONTRACT_DOMAIN,
    EXPANDING_WINDOW_CONTRACT_DOMAIN,
    ANCHORED_WINDOW_CONTRACT_DOMAIN,
    PURGED_WALK_FORWARD_CONTRACT_DOMAIN,
    EMBARGO_POLICY_DOMAIN,
    TRAIN_VALIDATION_TEST_SPLIT_DOMAIN,
    OUT_OF_SAMPLE_SPLIT_DOMAIN,
    HOLDOUT_PERIOD_DOMAIN,
    TEMPORAL_SPLIT_BOUNDARY_DOMAIN,
    REGIME_AWARE_SPLIT_DOMAIN,
    CROSS_ASSET_OOS_SPLIT_DOMAIN,
    WALK_FORWARD_FOLD_DOMAIN,
    WALK_FORWARD_SCHEDULE_PLACEHOLDER_DOMAIN,
    BENCHMARK_CONTRACT_DOMAIN,
    BENCHMARK_UNIVERSE_DOMAIN,
    BENCHMARK_BASELINE_DOMAIN,
    BENCHMARK_COMPARISON_DOMAIN,
    BENCHMARK_PLACEHOLDER_DOMAIN,
    BENCHMARK_METRIC_PLACEHOLDER_DOMAIN,
    VALIDATION_METRIC_PLACEHOLDER_DOMAIN,
    OUTPUT_CONTRACT_DOMAIN,
    VALIDATION_EVIDENCE_DOMAIN,
    DEPENDENCY_DOMAIN,
    BIAS_GUARD_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_148_HANDOFF_DOMAIN,
]

STATUS_LABELS = [
    VALIDATION_CONTRACT_READY,
    VALIDATION_CONTRACT_READY_WITH_WARNINGS,
    VALIDATION_CONTRACT_MANUAL_REVIEW_REQUIRED,
    VALIDATION_CONTRACT_BLOCKED_BY_SAFETY,
    VALIDATION_CONTRACT_ONLY,
    VALIDATION_UNKNOWN,
]

EXECUTION_LABELS = [
    EXECUTION_BLOCKED_NO_WALK_FORWARD,
    EXECUTION_BLOCKED_NO_BENCHMARK,
    EXECUTION_BLOCKED_NO_METRIC_CALCULATION,
    EXECUTION_BLOCKED_NO_OPTIMIZER,
    EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    EXECUTION_BLOCKED_NO_PREDICTION,
    EXECUTION_BLOCKED_NO_LIVE_TRADING,
    EXECUTION_BLOCKED_NO_BROKER,
    EXECUTION_CONTRACT_ONLY,
]
