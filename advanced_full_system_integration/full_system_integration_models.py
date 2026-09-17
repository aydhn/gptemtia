# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Data Models.

Provides dataclass definitions enforcing strict non-production invariants,
system-wide boundary policies, and governance constraints for Phase 158.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class FullSystemIntegrationProfileItem:
    """Represents a full system integration profile registration."""
    profile_name: str
    description: str
    current_phase: int = 158
    target_final_phase: int = 160
    next_phase: int = 159
    min_readiness_score: float = 0.50
    non_signal: bool = True
    dry_run: bool = True
    local_only: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False


@dataclass(frozen=True)
class SystemComponentItem:
    """Represents a component registered within the full-system architecture."""
    component_id: str
    component_name: str
    layer_name: str
    module_name: str
    status: str
    contract_only: bool = True
    non_production: bool = True
    dry_run: bool = True
    local_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_ready: bool = False
    signal_ready: bool = False
    system_executed: bool = False


@dataclass(frozen=True)
class SystemComponentCheckpoint:
    """Represents a verification checkpoint for a system component."""
    checkpoint_id: str
    component_name: str
    expected_module: str
    expected_config: str = ""
    expected_scripts: List[str] = field(default_factory=list)
    expected_tests: List[str] = field(default_factory=list)
    expected_manifest: str = ""
    expected_validation_report: str = ""
    expected_safety_boundary: str = ""
    contract_only: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    manual_review_required: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_ready: bool = False
    signal_ready: bool = False


@dataclass(frozen=True)
class SystemIntegrationContract:
    """Represents a subsystem integration contract within the unified map."""
    contract_id: str
    subsystem_name: str
    contract_type: str
    version: str
    status: str
    contract_only: bool = True
    non_production: bool = True
    manual_review_required: bool = True
    zero_execution_guaranteed: bool = True
    notes: str = ""


@dataclass(frozen=True)
class AdvancedAcceptanceRehearsalItem:
    """Represents an item in the advanced acceptance rehearsal checklist."""
    rehearsal_id: str
    rehearsal_name: str
    target_layer: str
    verification_type: str
    status: str
    is_satisfied: bool
    notes: str = ""
    contract_only: bool = True
    non_production: bool = True
    zero_execution_verified: bool = True


@dataclass(frozen=True)
class SystemBoundaryItem:
    """Represents a system safety, non-production, or dry-run boundary rule."""
    boundary_id: str
    boundary_type: str
    rule_name: str
    action_type: str
    is_allowed: bool
    reason: str


@dataclass(frozen=True)
class SystemDisabledExecutionItem:
    """Represents a disabled execution guarantee or policy report."""
    item_id: str
    execution_type: str
    is_disabled: bool
    blocking_reason: str
    enforcement_layer: str = "contract"
    status: str = "DISABLED"


@dataclass(frozen=True)
class SystemIntegrationFinding:
    """Represents an issue, blocker, gap, or warning discovered during integration."""
    finding_id: str
    finding_type: str
    domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    is_blocking: bool = False


@dataclass(frozen=True)
class SystemIntegrationReadinessScore:
    """Represents the calculated readiness score for full system integration."""
    overall_score: float
    classification: str
    meets_threshold: bool
    total_checks: int
    passed_checks: int
    warning_count: int
    blocker_count: int
    non_signal: bool = True
    dry_run: bool = True
    local_only: bool = True
    non_production: bool = True
    broker_ready: bool = False
    production_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False

    def __post_init__(self):
        if not (0.0 <= self.overall_score <= 1.0):
            raise ValueError(f"overall_score must be between 0.0 and 1.0, got {self.overall_score}")


@dataclass(frozen=True)
class FullSystemIntegrationManifest:
    """Represents the complete master manifest for Phase 158 Full-System Integration."""
    manifest_id: str
    current_phase: int = 158
    target_final_phase: int = 160
    next_phase: int = 159
    full_system_integration_completed: bool = True
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    system_executed: bool = False
    end_to_end_run_executed: bool = False
    live_trading_executed: bool = False
    broker_execution_executed: bool = False
    order_generation_executed: bool = False
    signal_generation_executed: bool = False
    model_training_executed: bool = False
    model_predict_executed: bool = False
    prediction_generated: bool = False
    target_label_generated: bool = False
    backtest_executed: bool = False
    benchmark_executed: bool = False
    portfolio_executed: bool = False
    risk_executed: bool = False
    scenario_executed: bool = False
    metric_calculated: bool = False
    optimizer_executed: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    production_deployed: bool = False
    source_preserved: bool = True
    manual_review_required: bool = True
    phase_159_handoff_ready: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False


@dataclass(frozen=True)
class SystemManualReviewItem:
    """Represents an item queued for human review prior to final release candidate."""
    item_id: str
    gate_name: str
    title: str
    description: str
    action_required: str
    status: str = "PENDING_REVIEW"
