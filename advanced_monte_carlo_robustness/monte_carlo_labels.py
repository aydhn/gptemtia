# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Robustness and Parameter Stability Labels.

Defines standardized string constants for domains, validation statuses,
execution blocks, and invariant classifications.
"""

# Domain Labels
MONTE_CARLO_PROFILE_DOMAIN = "monte_carlo_profile_domain"
MONTE_CARLO_DOMAIN = "monte_carlo_domain"
MONTE_CARLO_SCOPE_DOMAIN = "monte_carlo_scope_domain"
ROBUSTNESS_CONTRACT_DOMAIN = "robustness_contract_domain"
BOOTSTRAP_CONTRACT_DOMAIN = "bootstrap_contract_domain"
BLOCK_BOOTSTRAP_CONTRACT_DOMAIN = "block_bootstrap_contract_domain"
STATIONARY_BOOTSTRAP_CONTRACT_DOMAIN = "stationary_bootstrap_contract_domain"
RETURN_PATH_RESAMPLING_DOMAIN = "return_path_resampling_domain"
TRADE_SEQUENCE_RESHUFFLING_DOMAIN = "trade_sequence_reshuffling_domain"
RESIDUAL_RESAMPLING_PLACEHOLDER_DOMAIN = "residual_resampling_placeholder_domain"
NOISE_INJECTION_PLACEHOLDER_DOMAIN = "noise_injection_placeholder_domain"
PATH_PERTURBATION_PLACEHOLDER_DOMAIN = "path_perturbation_placeholder_domain"
PARAMETER_STABILITY_CONTRACT_DOMAIN = "parameter_stability_contract_domain"
PARAMETER_SENSITIVITY_CONTRACT_DOMAIN = "parameter_sensitivity_contract_domain"
PARAMETER_PERTURBATION_CONTRACT_DOMAIN = "parameter_perturbation_contract_domain"
PARAMETER_GRID_STABILITY_PLACEHOLDER_DOMAIN = "parameter_grid_stability_placeholder_domain"
PARAMETER_SURFACE_PLACEHOLDER_DOMAIN = "parameter_surface_placeholder_domain"
PARAMETER_FRAGILITY_PLACEHOLDER_DOMAIN = "parameter_fragility_placeholder_domain"
ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN = "robustness_envelope_placeholder_domain"
STABILITY_BAND_PLACEHOLDER_DOMAIN = "stability_band_placeholder_domain"
CONFIDENCE_INTERVAL_PLACEHOLDER_DOMAIN = "confidence_interval_placeholder_domain"
DISTRIBUTION_PLACEHOLDER_DOMAIN = "distribution_placeholder_domain"
LINKAGE_DOMAIN = "linkage_domain"
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
PHASE_150_HANDOFF_DOMAIN = "phase_150_handoff_domain"

# Domain Aliases
RESAMPLING_PLACEHOLDER_DOMAIN = RETURN_PATH_RESAMPLING_DOMAIN
ROBUSTNESS_ENVELOPE_DOMAIN = ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN
METRIC_PLACEHOLDER_DOMAIN = "metric_placeholders"
GUARD_DOMAIN = BIAS_GUARD_DOMAIN
HANDOFF_DOMAIN = PHASE_150_HANDOFF_DOMAIN
STATUS_DOMAIN = "monte_carlo_status"

# Status Labels
MONTE_CARLO_CONTRACT_READY = "monte_carlo_contract_ready"
MONTE_CARLO_CONTRACT_READY_WITH_WARNINGS = "monte_carlo_contract_ready_with_warnings"
MONTE_CARLO_CONTRACT_MANUAL_REVIEW_REQUIRED = "monte_carlo_contract_manual_review_required"
MONTE_CARLO_CONTRACT_BLOCKED_BY_SAFETY = "monte_carlo_contract_blocked_by_safety"
MONTE_CARLO_CONTRACT_ONLY = "monte_carlo_contract_only"
MONTE_CARLO_UNKNOWN = "monte_carlo_unknown"

# Execution Labels
EXECUTION_BLOCKED_NO_MONTE_CARLO = "execution_blocked_no_monte_carlo"
EXECUTION_BLOCKED_NO_BOOTSTRAP = "execution_blocked_no_bootstrap"
EXECUTION_BLOCKED_NO_RESAMPLING = "execution_blocked_no_resampling"
EXECUTION_BLOCKED_NO_PARAMETER_OPTIMIZATION = "execution_blocked_no_parameter_optimization"
EXECUTION_BLOCKED_NO_PARAMETER_SWEEP = "execution_blocked_no_parameter_sweep"
EXECUTION_BLOCKED_NO_METRIC_CALCULATION = "execution_blocked_no_metric_calculation"
EXECUTION_BLOCKED_NO_MODEL_TRAINING = "execution_blocked_no_model_training"
EXECUTION_BLOCKED_NO_PREDICTION = "execution_blocked_no_prediction"
EXECUTION_BLOCKED_NO_LIVE_TRADING = "execution_blocked_no_live_trading"
EXECUTION_BLOCKED_NO_BROKER = "execution_blocked_no_broker"
EXECUTION_CONTRACT_ONLY = "execution_contract_only"
