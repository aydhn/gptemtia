# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing and Scenario Simulation Models.

Type-safe dataclass definitions representing stress testing contracts,
scenario placeholders, metric placeholders, bias guards, and manifests.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class StressTestingProfileItem:
    """Dataclass representing an operational stress testing profile."""

    profile_name: str
    description: str
    current_phase: int = 148
    target_final_phase: int = 160
    next_phase: int = 149
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    non_signal: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    min_readiness_score: float = 0.50

    def __post_init__(self):
        if not (0.0 <= self.min_readiness_score <= 1.0):
            raise ValueError(f"min_readiness_score must be in [0, 1], got {self.min_readiness_score}")


@dataclass(frozen=True)
class StressScenarioContract:
    """Contract specification for stress testing and scenario simulations."""

    contract_name: str
    scenario_family: str
    description: str
    realistic_backtest_ref: str
    walk_forward_ref: str
    transaction_cost_ref: str
    slippage_model_ref: str
    regime_context_ref: str
    no_lookahead_guard_ref: str
    scenario_leakage_guard_ref: str
    stress_execution_allowed: bool = False
    scenario_simulation_allowed: bool = False
    metric_calculation_allowed: bool = False
    optimizer_execution_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    local_only: bool = True

    def __post_init__(self):
        if self.stress_execution_allowed:
            raise ValueError("stress_execution_allowed must be False in Phase 148")
        if self.scenario_simulation_allowed:
            raise ValueError("scenario_simulation_allowed must be False in Phase 148")
        if self.metric_calculation_allowed:
            raise ValueError("metric_calculation_allowed must be False in Phase 148")
        if self.optimizer_execution_allowed:
            raise ValueError("optimizer_execution_allowed must be False in Phase 148")
        if self.live_trading_allowed:
            raise ValueError("live_trading_allowed must be False")
        if self.broker_execution_allowed:
            raise ValueError("broker_execution_allowed must be False")
        if self.signal_generation_allowed:
            raise ValueError("signal_generation_allowed must be False")


@dataclass(frozen=True)
class ShockScenarioPlaceholder:
    """Specification for shock scenario placeholders."""

    placeholder_name: str
    shock_type: str
    description: str
    magnitude_spec: str
    parameters: Dict[str, Any] = field(default_factory=dict)
    real_execution_allowed: bool = False
    non_signal: bool = True
    contains_trading_recommendation: bool = False

    def __post_init__(self):
        if self.real_execution_allowed:
            raise ValueError("real_execution_allowed must be False in Phase 148")
        if self.contains_trading_recommendation:
            raise ValueError("contains_trading_recommendation must be False")


@dataclass(frozen=True)
class StressMetricPlaceholder:
    """Specification for stress and scenario metric placeholders."""

    metric_name: str
    metric_category: str
    description: str
    formula_spec: str
    benchmark_relative: bool = False
    metric_calculated: bool = False
    performance_claim_generated: bool = False
    non_signal: bool = True

    def __post_init__(self):
        if self.metric_calculated:
            raise ValueError("metric_calculated must be False in Phase 148")
        if self.performance_claim_generated:
            raise ValueError("performance_claim_generated must be False")


@dataclass(frozen=True)
class StressGuardItem:
    """Specification for bias, lookahead, and leakage guards."""

    guard_name: str
    guard_type: str
    description: str
    enforcement_level: str = "STRICT"
    active: bool = True
    violating_columns: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class StressDisabledExecutionItem:
    """Record representing a strictly disabled execution path."""

    execution_name: str
    prohibited_reason: str
    blocked_actions: List[str]
    is_blocked: bool = True
    enforced: bool = True


@dataclass(frozen=True)
class StressFinding:
    """Finding or issue recorded during stress testing contract validation."""

    finding_id: str
    finding_type: str
    domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True


@dataclass(frozen=True)
class StressReadinessScore:
    """Diagnostic readiness score for stress testing contract layer."""

    score: float
    classification: str
    total_findings: int
    critical_blockers: int
    meets_threshold: bool
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False

    def __post_init__(self):
        if not (0.0 <= self.score <= 1.0):
            raise ValueError(f"Readiness score must be in [0, 1], got {self.score}")


@dataclass(frozen=True)
class StressTestingManifest:
    """Master manifest for Phase 148 stress testing and scenario simulation layer."""

    manifest_id: str
    current_phase: int = 148
    target_final_phase: int = 160
    next_phase: int = 149
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    stress_test_executed: bool = False
    scenario_simulation_executed: bool = False
    stress_metric_calculated: bool = False
    scenario_metric_calculated: bool = False
    stressed_pnl_calculated: bool = False
    stressed_drawdown_calculated: bool = False
    var_calculated: bool = False
    expected_shortfall_calculated: bool = False
    monte_carlo_executed: bool = False
    optimizer_executed: bool = False
    model_training_executed: bool = False
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
    phase_149_handoff_ready: bool = True

    def __post_init__(self):
        if self.live_trading_ready:
            raise ValueError("live_trading_ready must be False in Phase 148")
        if self.broker_ready:
            raise ValueError("broker_ready must be False in Phase 148")
        if self.production_ready:
            raise ValueError("production_ready must be False in Phase 148")
        if self.stress_test_executed:
            raise ValueError("stress_test_executed must be False in Phase 148")
        if self.scenario_simulation_executed:
            raise ValueError("scenario_simulation_executed must be False in Phase 148")
        if self.stress_metric_calculated:
            raise ValueError("stress_metric_calculated must be False in Phase 148")
        if self.scenario_metric_calculated:
            raise ValueError("scenario_metric_calculated must be False in Phase 148")
        if self.stressed_pnl_calculated:
            raise ValueError("stressed_pnl_calculated must be False in Phase 148")
        if self.stressed_drawdown_calculated:
            raise ValueError("stressed_drawdown_calculated must be False in Phase 148")
        if self.var_calculated:
            raise ValueError("var_calculated must be False in Phase 148")
        if self.expected_shortfall_calculated:
            raise ValueError("expected_shortfall_calculated must be False in Phase 148")
        if self.monte_carlo_executed:
            raise ValueError("monte_carlo_executed must be False in Phase 148")
        if self.optimizer_executed:
            raise ValueError("optimizer_executed must be False in Phase 148")
        if self.model_training_executed:
            raise ValueError("model_training_executed must be False in Phase 148")
        if self.prediction_generated:
            raise ValueError("prediction_generated must be False in Phase 148")
        if self.target_label_generated:
            raise ValueError("target_label_generated must be False in Phase 148")
        if self.performance_claim_generated:
            raise ValueError("performance_claim_generated must be False in Phase 148")
        if self.broker_order_sent:
            raise ValueError("broker_order_sent must be False in Phase 148")
        if self.live_order_sent:
            raise ValueError("live_order_sent must be False in Phase 148")
        if self.artifact_persisted:
            raise ValueError("artifact_persisted must be False in Phase 148")
        if self.model_registry_written:
            raise ValueError("model_registry_written must be False in Phase 148")
        if self.model_deployed:
            raise ValueError("model_deployed must be False in Phase 148")
        if self.production_deployed:
            raise ValueError("production_deployed must be False in Phase 148")


@dataclass(frozen=True)
class StressManualReviewItem:
    """Item queued for human operator review in stress testing layer."""

    review_id: str
    item_type: str
    item_name: str
    description: str
    review_status: str
    recommendation: str
    destructive_action_allowed: bool = False
