# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Robustness and Parameter Stability Data Models.

Defines structured dataclasses with strict safety invariants and zero live execution guarantees.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class MonteCarloProfileItem:
    """Represents a registered Monte Carlo profile entry."""

    profile_name: str
    description: str
    current_phase: int = 149
    target_final_phase: int = 160
    next_phase: int = 150
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False


@dataclass
class MonteCarloRobustnessContract:
    """Core contract defining a Monte Carlo robustness evaluation dimension."""

    contract_name: str
    robustness_family: str
    realistic_backtest_ref: str
    walk_forward_ref: str
    stress_testing_ref: str
    transaction_cost_ref: str
    slippage_model_ref: str
    regime_context_ref: str
    no_lookahead_guard_ref: str
    resampling_leakage_guard_ref: str
    description: str = ""
    monte_carlo_execution_allowed: bool = False
    bootstrap_execution_allowed: bool = False
    resampling_execution_allowed: bool = False
    metric_calculation_allowed: bool = False
    optimizer_execution_allowed: bool = False
    parameter_optimization_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    manual_review_required: bool = True
    status: str = "monte_carlo_contract_ready"

    def __post_init__(self):
        if self.live_trading_allowed:
            raise ValueError("Live trading is strictly prohibited in Phase 149 Monte Carlo contracts.")
        if self.broker_execution_allowed:
            raise ValueError("Broker execution is strictly prohibited in Phase 149 Monte Carlo contracts.")


@dataclass
class BootstrapSimulationContract:
    """Defines contract specifications for a bootstrap simulation method."""

    method_name: str
    resampling_type: str
    preserves_autocorrelation: bool
    resampling_block_size_formula: str
    requires_iid_assumption: bool
    description: str = ""
    simulation_executed: bool = False
    sample_generated: bool = False
    contract_status: str = "contract_ready"


@dataclass
class ParameterStabilityContract:
    """Defines parameter stability contract specifications."""

    parameter_name: str
    strategy_ref: str
    perturbation_range: str
    sensitivity_metric: str
    plateau_detection_rule: str
    description: str = ""
    optimization_allowed: bool = False
    sweep_allowed: bool = False
    contract_status: str = "contract_ready"


# Model Aliases
MonteCarloContractModel = MonteCarloRobustnessContract
BootstrapContractModel = BootstrapSimulationContract
ParameterStabilityContractModel = ParameterStabilityContract


@dataclass
class ParameterSensitivityContract:

    """Defines parameter sensitivity gradient and boundary contracts."""

    parameter_name: str
    sensitivity_type: str
    perturbation_pct: float
    fragility_threshold: float
    optimization_executed: bool = False
    contract_status: str = "contract_ready"


@dataclass
class RobustnessPlaceholderItem:
    """Defines placeholder metadata for uncalculated robustness components."""

    placeholder_id: str
    placeholder_type: str
    envelope_bound: str
    formula_reference: str
    calculated: bool = False
    value: Optional[float] = None
    status: str = "uncalculated_placeholder"


@dataclass
class MonteCarloMetricPlaceholder:
    """Metadata-only definition for a Monte Carlo robustness metric."""

    metric_name: str
    metric_category: str
    target_distribution: str
    formula_definition: str
    calculated: bool = False
    value: Optional[float] = None
    performance_claim: bool = False


@dataclass
class MonteCarloGuardItem:
    """Guards enforcing temporal integrity, bias avoidance, and leakage prevention."""

    guard_id: str
    guard_type: str
    target_bias: str
    enforcement_action: str
    status: str = "ACTIVE"
    violations_found: int = 0


@dataclass
class MonteCarloDisabledExecutionItem:
    """Audit item confirming execution prohibition for a specific capability."""

    capability_name: str
    disabled: bool = True
    policy_reference: str = "PHASE_149_ZERO_EXECUTION_POLICY"
    block_reason: str = "Execution prohibited under offline/local research contract."
    execution_blocked: bool = True


@dataclass
class MonteCarloFinding:
    """Diagnostic finding discovered during Phase 149 contract inspection."""

    finding_id: str
    finding_type: str
    domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    status: str = "OPEN"


@dataclass
class MonteCarloReadinessScore:
    """Aggregate readiness score indicating contract layer completeness."""

    score: float
    classification: str
    total_checks: int
    passed_checks: int
    critical_findings_count: int
    manual_review_required: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False

    def __post_init__(self):
        if not (0.0 <= self.score <= 1.0):
            raise ValueError(f"Readiness score must be between 0.0 and 1.0, got {self.score}")


@dataclass
class MonteCarloManualReviewItem:
    """Action item requiring human operator verification."""

    item_id: str
    title: str
    category: str
    inspection_focus: str
    status: str = "PENDING_REVIEW"
    safe_resolution: str = "Review contracts, formulas, and boundaries without executing simulations."


@dataclass
class MonteCarloManifest:
    """Master integrity manifest validating all Phase 149 negative invariants."""

    manifest_id: str
    current_phase: int = 149
    target_final_phase: int = 160
    next_phase: int = 150
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    monte_carlo_executed: bool = False
    bootstrap_executed: bool = False
    resampling_executed: bool = False
    parameter_optimization_executed: bool = False
    parameter_sweep_executed: bool = False
    robustness_metric_calculated: bool = False
    parameter_stability_metric_calculated: bool = False
    distribution_calculated: bool = False
    var_calculated: bool = False
    expected_shortfall_calculated: bool = False
    optimizer_executed: bool = False
    model_training_executed: bool = False
    model_predict_executed: bool = False
    prediction_generated: bool = False
    target_label_generated: bool = False
    performance_claim_generated: bool = False
    broker_order_sent: bool = False
    live_order_sent: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    production_deployed: bool = False
    source_preserved: bool = True
    manual_review_required: bool = True
    phase_150_handoff_ready: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
