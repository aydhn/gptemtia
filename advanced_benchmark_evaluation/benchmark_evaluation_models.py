# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Models Module.

Type-safe data models representing contracts, placeholders, guards, findings,
readiness scores, and manifests with strict negative invariant validation.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class BenchmarkEvaluationProfileItem:
    """Represents an active benchmark evaluation profile entry."""

    profile_name: str
    description: str
    current_phase: int = 151
    target_final_phase: int = 160
    next_phase: int = 152
    dry_run: bool = True
    local_only: bool = True
    non_production: bool = True
    non_signal: bool = True
    allow_live_trading: bool = False
    allow_broker: bool = False


@dataclass(frozen=True)
class BenchmarkComparisonReportContract:
    """Represents a benchmark comparison report contract."""

    contract_name: str
    report_family: str
    phase_146_ref: str
    phase_147_ref: str
    phase_148_ref: str
    phase_149_ref: str
    phase_150_ref: str
    benchmark_universe_ref: str
    benchmark_baseline_ref: str
    metric_placeholder_ref: str
    result_claim_guard_ref: str
    performance_claim_guard_ref: str
    benchmark_execution_allowed: bool = False
    metric_calculation_allowed: bool = False
    result_claim_allowed: bool = False
    performance_claim_allowed: bool = False
    strategy_approval_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    status: str = "evaluation_contract_ready"


@dataclass(frozen=True)
class StrategyEvaluationReportContract:
    """Represents a strategy evaluation report contract."""

    contract_name: str
    report_family: str
    phase_146_ref: str
    phase_147_ref: str
    phase_148_ref: str
    phase_149_ref: str
    phase_150_ref: str
    evaluation_scope_ref: str
    metric_placeholder_ref: str
    claim_guard_ref: str
    strategy_approval_allowed: bool = False
    capital_allocation_allowed: bool = False
    portfolio_construction_allowed: bool = False
    position_sizing_allowed: bool = False
    investment_advice_allowed: bool = False
    signal_generation_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    status: str = "evaluation_contract_ready"


@dataclass(frozen=True)
class EvaluationSummaryPlaceholder:
    """Represents an uncalculated summary placeholder in reports."""

    placeholder_id: str
    title: str
    domain: str
    description: str
    is_calculated: bool = False
    performance_claim_allowed: bool = False
    strategy_approval_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass(frozen=True)
class EvaluationMetricPlaceholder:
    """Represents an uncalculated metric placeholder."""

    metric_name: str
    category: str
    formula_spec: str
    target_role: str
    is_calculated: bool = False
    actual_value: Optional[float] = None
    performance_claim_allowed: bool = False
    non_signal: bool = True


@dataclass(frozen=True)
class EvaluationGuardItem:
    """Represents a boundary guard preventing unauthorized execution or claims."""

    guard_id: str
    domain: str
    description: str
    action_blocked: str
    is_active: bool = True
    violates_contract: bool = False


@dataclass(frozen=True)
class EvaluationDisabledExecutionItem:
    """Documents disabled operational features."""

    feature_name: str
    description: str
    disabled_reason: str
    policy_reference: str
    is_disabled: bool = True
    attempted_execution_blocked: bool = True


@dataclass(frozen=True)
class BenchmarkEvaluationFinding:
    """Represents a finding or gap identified during evaluation checks."""

    finding_id: str
    finding_type: str
    domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    is_blocker: bool = False


@dataclass(frozen=True)
class BenchmarkEvaluationReadinessScore:
    """Score representing contract completeness and safety compliance."""

    score: float
    classification: str
    meets_threshold: bool
    current_phase: int = 151
    target_final_phase: int = 160
    next_phase: int = 152
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    backtest_executed: bool = False
    benchmark_executed: bool = False
    metric_calculated: bool = False
    result_claim_generated: bool = False
    performance_claim_generated: bool = False
    strategy_approved: bool = False
    capital_allocation_generated: bool = False
    portfolio_constructed: bool = False
    position_sizing_generated: bool = False
    optimizer_executed: bool = False
    model_training_executed: bool = False
    model_predict_executed: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    broker_order_sent: bool = False
    live_order_sent: bool = False

    def __post_init__(self):
        if not (0.0 <= self.score <= 1.0):
            raise ValueError(f"Readiness score must be between 0.0 and 1.0, got {self.score}")
        if (
            self.broker_ready
            or self.production_ready
            or self.live_trading_ready
            or self.official_approval
            or self.contains_target_or_prediction
            or self.contains_trading_recommendation
            or self.backtest_executed
            or self.benchmark_executed
            or self.metric_calculated
            or self.result_claim_generated
            or self.performance_claim_generated
            or self.strategy_approved
            or self.capital_allocation_generated
            or self.portfolio_constructed
            or self.position_sizing_generated
            or self.optimizer_executed
            or self.model_training_executed
            or self.model_predict_executed
            or self.artifact_persisted
            or self.model_registry_written
            or self.broker_order_sent
            or self.live_order_sent
        ):
            raise ValueError("All execution, approval, and claim invariants must remain False.")


@dataclass(frozen=True)
class BenchmarkEvaluationManifest:
    """Master manifest capturing the integrity state of Phase 151."""

    manifest_id: str
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    current_phase: int = 151
    target_final_phase: int = 160
    next_phase: int = 152
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    benchmark_report_executed: bool = False
    strategy_evaluation_executed: bool = False
    benchmark_executed: bool = False
    backtest_executed: bool = False
    metric_calculated: bool = False
    result_claim_generated: bool = False
    performance_claim_generated: bool = False
    strategy_approved: bool = False
    capital_allocation_generated: bool = False
    portfolio_constructed: bool = False
    position_sizing_generated: bool = False
    optimizer_executed: bool = False
    model_training_executed: bool = False
    prediction_generated: bool = False
    target_label_generated: bool = False
    broker_order_sent: bool = False
    live_order_sent: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    production_deployed: bool = False
    source_preserved: bool = True
    manual_review_required: bool = True
    phase_152_handoff_ready: bool = True


@dataclass(frozen=True)
class BenchmarkEvaluationManualReviewItem:
    """Represents a human verification requirement."""

    review_id: str
    topic: str
    inspection_focus: str
    status: str = "PENDING_OPERATOR_REVIEW"
    mandatory: bool = True
