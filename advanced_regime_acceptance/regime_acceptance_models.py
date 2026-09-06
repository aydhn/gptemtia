"""Phase 135: Regime Acceptance Data Models.

Provides strongly-typed dataclasses for inventory, dependencies, gates,
scoring, manual review, compliance, status, and block manifest.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class RegimeAcceptanceProfileItem:
    """Dataclass representing an active acceptance profile record."""
    profile_name: str
    description: str
    current_phase: int = 135
    target_final_phase: int = 160
    next_phase: int = 136
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    min_score: float = 0.45
    non_signal: bool = True
    status: str = "READY"


@dataclass(frozen=True)
class RegimeBlockInventoryItem:
    """Dataclass representing an inventory item of the regime block (Phases 126-135)."""
    phase_number: int
    module_name: str
    expected_scripts: int
    expected_tests: int
    expected_reports: int
    expected_datalake_outputs: int
    expected_docs: int
    status_label: str
    manual_review_required: bool = False
    non_signal: bool = True
    source_preserved: bool = True


@dataclass(frozen=True)
class RegimeBlockDependencyItem:
    """Dataclass representing a dependency node in the regime block execution DAG."""
    step_number: int
    source_phase: int
    target_phase: int
    source_module: str
    target_module: str
    dependency_type: str
    description: str
    non_signal: bool = True
    satisfied: bool = True


@dataclass(frozen=True)
class RegimeBlockAcceptanceGate:
    """Dataclass representing an acceptance gate evaluated across the regime block."""
    gate_id: str
    gate_name: str
    category: str
    description: str
    passed: bool
    status_label: str
    non_signal_verified: bool = True
    details: str = ""


@dataclass(frozen=True)
class RegimeBlockAcceptanceScore:
    """Dataclass representing the composite acceptance score across evaluated gates."""
    total_gates: int
    passed_gates: int
    score: float
    classification: str
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    model_training_ready: bool = False
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RegimeBlockManualReviewItem:
    """Dataclass representing an item in the manual review queue."""
    item_id: str
    phase_number: int
    module_name: str
    category: str
    issue_description: str
    manual_review_required: bool = True
    auto_destructive_action_allowed: bool = False
    recommendation: str = ""


@dataclass(frozen=True)
class RegimeBlockComplianceItem:
    """Dataclass representing a compliance check entry."""
    compliance_id: str
    domain: str
    title: str
    description: str
    compliant: bool
    non_signal: bool = True
    source_preserved: bool = True
    no_lookahead_verified: bool = True
    metadata_only_news: bool = True
    forbidden_column_clean: bool = True
    featurestore_ready: bool = True
    status_label: str = "acceptance_pass"


@dataclass(frozen=True)
class RegimeBlockStatusItem:
    """Dataclass representing status summary for an individual regime component."""
    component_name: str
    phase_number: int
    status_label: str
    gates_passed: int
    total_gates: int
    manual_review_required: bool = False
    non_signal: bool = True


@dataclass(frozen=True)
class Phase126135AcceptanceManifest:
    """Dataclass representing the final acceptance manifest for Phase 126-135 block."""
    block_name: str
    phase_start: int = 126
    phase_end: int = 135
    target_final_phase: int = 160
    next_phase: int = 136
    module_count: int = 10
    gate_count: int = 17
    manual_review_count: int = 0
    acceptance_score: float = 1.0
    manual_review_required: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    contains_article_body: bool = False
    contains_raw_content: bool = False
    contains_scraped_html: bool = False
    contains_embedding: bool = False
    contains_vector: bool = False
    sentiment_model_output: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
