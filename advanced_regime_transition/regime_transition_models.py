"""Phase 130: Regime Transition and Stability Analysis Models.

Data models and contracts for state sequence contracts, transition diagnostics,
stability metrics, quality findings, review queues, and manifests.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RegimeTransitionProfileItem:
    """Represents a registered regime transition operational profile."""

    profile_name: str
    description: str
    current_phase: int = 130
    target_final_phase: int = 160
    next_phase: int = 131
    min_stability_score: float = 0.45
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass
class StateSequenceContract:
    """Defines contract requirements for a state sequence dataset."""

    contract_name: str
    sequence_family: str
    entity_keys: List[str]
    timestamp_field: str
    state_context_field: str
    source_phase_refs: List[str]
    required_validation_refs: List[str]
    required_quality_refs: List[str]
    no_lookahead_required: bool = True
    metadata_only_news_required: bool = True
    non_signal_required: bool = True
    model_training_allowed: bool = False
    clustering_allowed: bool = False
    manual_review_required: bool = False
    extra_metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class StateSequenceSchemaItem:
    """Represents a column schema definition for sequence tables."""

    column_name: str
    data_type: str
    is_required: bool
    is_entity_key: bool = False
    is_timestamp: bool = False
    is_forbidden_signal: bool = False
    description: str = ""
    source_reference: str = ""


@dataclass
class TransitionMetric:
    """Specification of a regime transition metric."""

    metric_name: str
    metric_family: str
    description: str
    formula_placeholder: str
    expected_range: str
    non_signal: bool = True
    source_preserved: bool = True
    requires_no_lookahead: bool = True


@dataclass
class StabilityMetric:
    """Specification of a regime stability metric."""

    metric_name: str
    metric_family: str
    description: str
    formula_placeholder: str
    expected_range: str
    non_signal: bool = True
    source_preserved: bool = True
    requires_no_lookahead: bool = True


@dataclass
class TransitionQualityFinding:
    """A single diagnostic finding or defect observation."""

    finding_id: str
    finding_type: str
    transition_family: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    non_signal: bool = True


@dataclass
class TransitionStabilityScore:
    """Aggregated transition stability score."""

    profile_name: str
    stability_score: float
    classification: str
    finding_count: int
    manual_review_count: int
    current_phase: int = 130
    target_final_phase: int = 160
    next_phase: int = 131
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    model_training_executed: bool = False
    clustering_executed: bool = False

    def __post_init__(self):
        if not (0.0 <= self.stability_score <= 1.0):
            raise ValueError(
                f"stability_score must be between 0.0 and 1.0, got {self.stability_score}"
            )


@dataclass
class TransitionDiagnosticsManifest:
    """Master manifest certifying Phase 130 transition diagnostics integrity."""

    manifest_name: str
    current_phase: int = 130
    target_final_phase: int = 160
    next_phase: int = 131
    sequence_contract_count: int = 0
    transition_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    stability_score: float = 0.0
    manual_review_required: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    dimensionality_reduction_executed: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass
class TransitionManualReviewItem:
    """Item placed into the manual inspection review queue."""

    review_id: str
    target_component: str
    issue_description: str
    recommended_inspection: str
    blocking_status: str = "review_pending"
    manual_review_required: bool = True
    auto_fix_forbidden: bool = True
