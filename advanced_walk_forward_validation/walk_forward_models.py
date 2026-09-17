# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Validation and Out-of-Sample Benchmarking Models.

Type-safe dataclass definitions representing walk-forward validation contracts,
split contracts, benchmark contracts, metric placeholders, bias guards, and manifests.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class WalkForwardProfileItem:
    """Dataclass representing an operational walk-forward profile."""

    profile_name: str
    description: str
    current_phase: int = 147
    target_final_phase: int = 160
    next_phase: int = 148
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
class WalkForwardValidationContract:
    """Contract specification for walk-forward validation strategies."""

    contract_name: str
    validation_family: str
    description: str
    data_contract_ref: str
    feature_input_contract_ref: str
    signal_input_contract_ref: str
    realistic_backtest_ref: str
    transaction_cost_ref: str
    slippage_model_ref: str
    split_policy_ref: str
    embargo_policy_ref: str
    no_lookahead_guard_ref: str
    bias_guard_ref: str
    walk_forward_execution_allowed: bool = False
    optimizer_execution_allowed: bool = False
    benchmark_execution_allowed: bool = False
    metric_calculation_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    local_only: bool = True

    def __post_init__(self):
        if self.walk_forward_execution_allowed:
            raise ValueError("walk_forward_execution_allowed must be False in Phase 147")
        if self.optimizer_execution_allowed:
            raise ValueError("optimizer_execution_allowed must be False in Phase 147")
        if self.live_trading_allowed:
            raise ValueError("live_trading_allowed must be False")
        if self.broker_execution_allowed:
            raise ValueError("broker_execution_allowed must be False")


@dataclass(frozen=True)
class SplitContract:
    """Specification for train/validation/test and OOS split boundaries."""

    split_name: str
    split_type: str
    description: str
    window_type: str
    train_ratio: float
    val_ratio: float
    test_ratio: float
    embargo_bars: int = 0
    purge_bars: int = 0
    anchored: bool = False
    non_signal: bool = True
    manual_review_required: bool = True
    contains_target_or_prediction: bool = False

    def __post_init__(self):
        if self.contains_target_or_prediction:
            raise ValueError("SplitContract must not contain targets or predictions")


@dataclass(frozen=True)
class BenchmarkContract:
    """Specification for baseline and out-of-sample benchmark contracts."""

    benchmark_name: str
    benchmark_type: str
    description: str
    universe_ref: str
    baseline_strategy_ref: str
    rebalance_policy: str
    transaction_cost_aware: bool = True
    slippage_aware: bool = True
    benchmark_executed: bool = False
    metric_calculated: bool = False
    investment_advice_allowed: bool = False
    non_signal: bool = True
    manual_review_required: bool = True

    def __post_init__(self):
        if self.benchmark_executed:
            raise ValueError("benchmark_executed must be False in Phase 147")
        if self.investment_advice_allowed:
            raise ValueError("investment_advice_allowed must be False")


@dataclass(frozen=True)
class BenchmarkPlaceholder:
    """Specification for benchmark baseline placeholder."""

    placeholder_name: str
    baseline_type: str
    description: str
    formula_spec: str
    parameters: Dict[str, Any] = field(default_factory=dict)
    real_execution_allowed: bool = False
    non_signal: bool = True


@dataclass(frozen=True)
class ValidationMetricPlaceholder:
    """Specification for validation and benchmark comparison metric placeholders."""

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
            raise ValueError("metric_calculated must be False in Phase 147")
        if self.performance_claim_generated:
            raise ValueError("performance_claim_generated must be False")


@dataclass(frozen=True)
class ValidationGuardItem:
    """Specification for bias, lookahead, purge, and embargo guards."""

    guard_name: str
    guard_type: str
    description: str
    enforcement_level: str = "STRICT"
    active: bool = True
    violating_columns: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class ValidationDisabledExecutionItem:
    """Record representing a strictly disabled execution path."""

    execution_name: str
    prohibited_reason: str
    blocked_actions: List[str]
    is_blocked: bool = True
    enforced: bool = True


@dataclass(frozen=True)
class WalkForwardFinding:
    """Finding or issue recorded during walk-forward contract validation."""

    finding_id: str
    finding_type: str
    domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True


@dataclass(frozen=True)
class WalkForwardReadinessScore:
    """Diagnostic readiness score for walk-forward contract layer."""

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
class WalkForwardValidationManifest:
    """Master manifest for Phase 147 walk-forward validation and OOS benchmarking layer."""

    manifest_id: str
    current_phase: int = 147
    target_final_phase: int = 160
    next_phase: int = 148
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    walk_forward_executed: bool = False
    oos_benchmark_executed: bool = False
    benchmark_metric_calculated: bool = False
    validation_metric_calculated: bool = False
    optimizer_executed: bool = False
    stress_test_executed: bool = False
    monte_carlo_executed: bool = False
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
    phase_148_handoff_ready: bool = True

    def __post_init__(self):
        if self.live_trading_ready:
            raise ValueError("live_trading_ready must be False in Phase 147")
        if self.broker_ready:
            raise ValueError("broker_ready must be False in Phase 147")
        if self.production_ready:
            raise ValueError("production_ready must be False in Phase 147")
        if self.walk_forward_executed:
            raise ValueError("walk_forward_executed must be False in Phase 147")
        if self.oos_benchmark_executed:
            raise ValueError("oos_benchmark_executed must be False in Phase 147")


@dataclass(frozen=True)
class WalkForwardManualReviewItem:
    """Item queued for human operator review."""

    review_id: str
    item_type: str
    item_name: str
    description: str
    review_status: str
    recommendation: str
    destructive_action_allowed: bool = False
