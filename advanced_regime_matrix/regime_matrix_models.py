"""Phase 127: Regime Feature Matrix and State Dataset Data Models.

Defines immutable dataclass structures enforcing Phase 127 contracts and non-signal invariants.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RegimeMatrixProfileItem:
    """Represents an active operational profile for regime feature matrix contracts."""

    profile_name: str
    description: str
    current_phase: int = 127
    target_final_phase: int = 160
    next_phase: int = 128
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    min_readiness_score: float = 0.45
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    model_training_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass
class RegimeFeatureMatrixContract:
    """Formal contract specification for a regime feature matrix family."""

    contract_name: str
    matrix_family: str
    required_entity_keys: List[str]
    timestamp_field: str
    symbol_field: str
    required_feature_families: List[str]
    required_factor_families: List[str]
    required_context_inputs: List[str]
    required_quality_inputs: List[str]
    validation_required: bool = True
    no_lookahead_required: bool = True
    metadata_only_news_required: bool = True
    non_signal_required: bool = True
    manual_review_required: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    model_training_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass
class RegimeStateDatasetContract:
    """Formal contract specification for a regime state research dataset."""

    dataset_name: str
    dataset_purpose: str
    entity_keys: List[str]
    timestamp_field: str
    regime_state_namespace: str
    candidate_context_fields: List[str]
    forbidden_fields: List[str]
    no_target_label_prediction: bool = True
    model_training_allowed: bool = False
    clustering_allowed: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    manual_review_required: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    model_training_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass
class RegimeMatrixEntity:
    """Entity representation participating in regime matrix construction."""

    entity_type: str
    entity_id: str
    description: str
    canonical_prefix: str
    source_phases: List[int]
    status: str = "matrix_ready"
    non_signal: bool = True
    source_preserved: bool = True


@dataclass
class RegimeMatrixSchemaItem:
    """Schema definition item for regime feature matrix columns."""

    column_name: str
    data_type: str
    entity_type: str
    feature_family: str
    factor_family: str
    regime_family: str
    source_phase: int
    validation_status: str
    quality_score_ref: str
    drift_score_ref: str
    lineage_ref: str
    is_nullable: bool = True
    manual_review_required: bool = True
    non_signal: bool = True
    source_preserved: bool = True


@dataclass
class RegimeMatrixInputFeature:
    """Input feature mapped from upstream phases into the regime matrix."""

    feature_key: str
    feature_name: str
    source_phase: int
    source_module: str
    feature_family: str
    entity_type: str
    validation_dependency_ref: str
    quality_dependency_ref: str
    status: str = "matrix_ready"
    non_signal: bool = True
    source_preserved: bool = True


@dataclass
class RegimeStateDatasetSchemaItem:
    """Schema item for non-signal regime state candidate dataset."""

    field_name: str
    data_type: str
    field_role: str
    is_candidate_context: bool = False
    is_target_or_label: bool = False
    forbidden_status: str = "allowed"
    manual_review_required: bool = True
    non_signal: bool = True
    source_preserved: bool = True


@dataclass
class RegimeStateCandidateContext:
    """Candidate context flag used for research state dataset preparation."""

    candidate_name: str
    regime_family: str
    underlying_features: List[str]
    underlying_factors: List[str]
    context_type: str
    description: str
    is_target_or_label: bool = False
    is_prediction: bool = False
    is_trade_signal: bool = False
    status: str = "matrix_ready"
    non_signal: bool = True
    source_preserved: bool = True


@dataclass
class RegimeMatrixIntegrityManifest:
    """Central integrity manifest record for Phase 127."""

    manifest_name: str
    current_phase: int = 127
    target_final_phase: int = 160
    next_phase: int = 128
    feature_contract_count: int = 0
    dataset_contract_count: int = 0
    input_feature_count: int = 0
    dependency_count: int = 0
    manifest_status: str = "MANIFEST_VALID"
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    model_training_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    manual_review_required: bool = True
    extra_metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RegimeMatrixManualReviewItem:
    """Audit item in the non-destructive regime matrix manual review queue."""

    item_id: str
    finding_type: str
    affected_entity: str
    severity: str
    description: str
    recommended_action: str
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    status: str = "PENDING_REVIEW"
