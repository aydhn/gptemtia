"""Phase 128: Regime Rule-Free Labeling Contracts and Unsupervised Prep Models.

Defines canonical dataclass models with strict non-signal, non-execution, and source preservation invariants.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class RegimeRuleFreeProfileItem:
    """Model representing a Phase 128 operational profile definition."""

    profile_name: str
    description: str
    current_phase: int = 128
    target_final_phase: int = 160
    next_phase: int = 129
    is_active: bool = True
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    clustering_allowed: bool = False
    model_training_allowed: bool = False
    min_readiness_score: float = 0.45


@dataclass
class RuleFreeLabelingContract:
    """Contract defining rule-free candidate state annotation preparation.

    Note: Not a supervised target label or trading label.
    """

    contract_name: str
    candidate_state_family: str
    source_matrix_contract_ref: str
    required_feature_families: List[str] = field(default_factory=list)
    required_factor_families: List[str] = field(default_factory=list)
    required_context_inputs: List[str] = field(default_factory=list)
    required_quality_inputs: List[str] = field(default_factory=list)
    validation_required: bool = True
    no_lookahead_required: bool = True
    metadata_only_news_required: bool = True
    non_signal_required: bool = True
    target_label_forbidden: bool = True
    prediction_forbidden: bool = True
    model_training_allowed: bool = False
    clustering_allowed: bool = False
    manual_review_required: bool = True
    status: str = "rule_free_ready"


@dataclass
class CandidateStateAssignmentPolicy:
    """Policy definition for candidate state contextual assignment placeholder.

    Note: Pure policy definition, not an execution algorithm.
    """

    policy_name: str
    policy_type: str
    description: str
    candidate_state_family: str
    execution_allowed: bool = False
    generates_trade_signal: bool = False
    non_signal: bool = True
    requires_validation: bool = True
    manual_review_required: bool = True
    status: str = "rule_free_placeholder_only"


@dataclass
class CandidateStateSchemaItem:
    """Field specification for candidate state dataset schema."""

    column_name: str
    data_type: str
    description: str
    is_mandatory: bool = True
    forbidden_terms_checked: bool = True
    is_target_or_prediction: bool = False
    is_signal: bool = False
    non_signal: bool = True


@dataclass
class PseudoStateSchemaItem:
    """Schema specification for non-signal pseudo-state preparation."""

    pseudo_state_key: str
    pseudo_state_family: str
    pseudo_state_context: str
    source_candidate_state_ref: str
    future_phase_usage_note: str
    model_training_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    status: str = "rule_free_placeholder_only"


@dataclass
class UnsupervisedPrepContract:
    """Preparation contract for future unsupervised regime discovery."""

    contract_name: str
    prep_category: str
    description: str
    fit_transform_allowed: bool = False
    model_training_allowed: bool = False
    clustering_allowed: bool = False
    dimensionality_reduction_allowed: bool = False
    no_lookahead_required: bool = True
    non_signal: bool = True
    status: str = "rule_free_ready"


@dataclass
class ClusteringInputContract:
    """Input contract specification for clustering readiness without execution."""

    input_contract_name: str
    required_matrix_schema: str
    required_feature_families: List[str] = field(default_factory=list)
    required_quality_score_refs: List[str] = field(default_factory=list)
    required_validation_status_refs: List[str] = field(default_factory=list)
    forbidden_columns: List[str] = field(default_factory=list)
    no_lookahead_required: bool = True
    scaling_required_future_phase: bool = True
    model_training_allowed: bool = False
    clustering_allowed: bool = False
    non_signal: bool = True
    status: str = "rule_free_ready"


@dataclass
class AlgorithmPlaceholder:
    """Non-executable placeholder for unsupervised clustering / distance algorithms."""

    algorithm_id: str
    family: str  # clustering, distance_metric, dimensionality_reduction
    description: str
    is_placeholder_only: bool = True
    execution_permitted: bool = False
    model_fit_permitted: bool = False
    non_signal: bool = True


@dataclass
class CandidateStateMetadataItem:
    """Metadata record for a registered candidate state context."""

    candidate_state_family: str
    source_matrix_ref: str
    source_feature_refs: List[str]
    assignment_policy_ref: str
    quality_dependency_ref: str
    validation_dependency_ref: str
    no_lookahead_policy_ref: str
    phase_129_ready: bool = True
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass
class CandidateStateIntegrityManifest:
    """Master governance manifest certifying Phase 128 safety invariants."""

    manifest_name: str
    current_phase: int = 128
    target_final_phase: int = 160
    next_phase: int = 129
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
    total_contracts: int = 0
    total_schemas: int = 0
    total_prep_contracts: int = 0
    total_dependencies: int = 0
    manual_review_required: bool = True
    manifest_status: str = "MANIFEST_VALID"


@dataclass
class CandidateStateManualReviewItem:
    """Item queued for non-destructive offline manual review."""

    review_id: str
    review_domain: str
    reason: str
    source_ref: str
    requires_human_signoff: bool = True
    destructive_action_permitted: bool = False
    auto_fix_permitted: bool = False
    status: str = "QUEUED_FOR_MANUAL_REVIEW"
