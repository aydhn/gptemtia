# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Models.

Type-safe dataclass definitions representing backtest engine contracts,
order simulation contracts, cost/slippage models, bias guards, and manifests.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class RealisticBacktestProfileItem:
    """Dataclass representing an operational backtest profile."""

    profile_name: str
    description: str
    current_phase: int = 146
    target_final_phase: int = 160
    next_phase: int = 147
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
class BacktestEngineContract:
    """Contract specification for a backtest engine family."""

    contract_name: str
    engine_family: str
    description: str
    data_contract_ref: str
    feature_input_contract_ref: str
    signal_input_contract_ref: str
    order_simulation_ref: str
    transaction_cost_ref: str
    slippage_model_ref: str
    no_lookahead_guard_ref: str
    bias_guard_ref: str
    backtest_execution_allowed: bool = False
    optimizer_execution_allowed: bool = False
    walk_forward_allowed: bool = False
    benchmark_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    local_only: bool = True

    def __post_init__(self):
        if self.backtest_execution_allowed:
            raise ValueError("backtest_execution_allowed must be False in Phase 146")
        if self.live_trading_allowed:
            raise ValueError("live_trading_allowed must be False")
        if self.broker_execution_allowed:
            raise ValueError("broker_execution_allowed must be False")


@dataclass(frozen=True)
class OrderSimulationContract:
    """Specification for order simulation behavior."""

    simulation_type: str
    description: str
    order_type: str
    fill_model_ref: str
    latency_model_ref: str
    liquidity_constraint_ref: str
    broker_order_sent: bool = False
    live_order_sent: bool = False
    real_fill_occurred: bool = False
    manual_review_required: bool = True


@dataclass(frozen=True)
class TransactionCostModelContract:
    """Specification for transaction cost models and components."""

    model_name: str
    cost_type: str
    description: str
    formula_spec: str
    cost_components: List[str]
    real_cost_calculated: bool = False
    broker_cost_linked: bool = False
    non_signal: bool = True


@dataclass(frozen=True)
class SlippageModelContract:
    """Specification for slippage models."""

    model_name: str
    slippage_type: str
    description: str
    parameter_spec: Dict[str, Any]
    formula_spec: str
    real_slippage_calculated: bool = False
    performance_guaranteed: bool = False
    non_signal: bool = True


@dataclass(frozen=True)
class BacktestGuardItem:
    """Specification for bias, lookahead, and data leakage guards."""

    guard_name: str
    guard_type: str
    description: str
    enforcement_level: str = "STRICT"
    active: bool = True
    violating_columns: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class BacktestDisabledExecutionItem:
    """Record representing a strictly disabled execution path."""

    execution_name: str
    prohibited_reason: str
    blocked_actions: List[str]
    is_blocked: bool = True
    enforced: bool = True


@dataclass(frozen=True)
class BacktestFinding:
    """Finding or issue recorded during backtest contract validation."""

    finding_id: str
    finding_type: str
    domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True


@dataclass(frozen=True)
class BacktestManualReviewItem:
    """Item queued for human operator review."""

    review_id: str
    item_type: str
    item_name: str
    description: str
    review_status: str
    recommendation: str
    destructive_action_allowed: bool = False


@dataclass(frozen=True)
class BacktestReadinessScore:
    """Diagnostic readiness score for realistic backtest contract layer."""

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
class RealisticBacktestManifest:
    """Master manifest for Phase 146 realistic backtest contract layer."""

    manifest_id: str
    current_phase: int = 146
    target_final_phase: int = 160
    next_phase: int = 147
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    backtest_executed: bool = False
    optimizer_executed: bool = False
    walk_forward_executed: bool = False
    benchmark_executed: bool = False
    stress_test_executed: bool = False
    monte_carlo_executed: bool = False
    model_training_executed: bool = False
    prediction_generated: bool = False
    target_label_generated: bool = False
    transaction_cost_calculated: bool = False
    slippage_calculated: bool = False
    performance_claim_generated: bool = False
    broker_order_sent: bool = False
    live_order_sent: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    production_deployed: bool = False
    source_preserved: bool = True
    manual_review_required: bool = True
    phase_147_handoff_ready: bool = True
