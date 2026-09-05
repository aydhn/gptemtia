"""Phase 124 Feature Store Integration Data Models.

Provides dataclass representations of contracts, entities, features, factors,
schemas, lineage references, validation statuses, scores, and manifests.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class FeatureStoreIntegrationProfileItem:
    profile_name: str
    description: str
    min_readiness_score: float = 0.45
    non_signal: bool = True
    source_preserved: bool = True
    current_phase: int = 124
    target_final_phase: int = 160
    next_phase: int = 125


@dataclass(frozen=True)
class FeatureStoreContract:
    store_name: str
    entity_keys: List[str]
    timestamp_field: str
    symbol_field: str
    feature_namespace_policy: str
    schema_policy: str
    validation_status_required: bool = True
    quality_score_required: bool = True
    drift_score_required: bool = True
    lineage_reference_required: bool = True
    manual_review_blocker_policy: str = "block_on_unresolved"
    non_signal_required: bool = True
    source_preserved_required: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass(frozen=True)
class FeatureStoreEntity:
    entity_type: str
    entity_id: str
    description: str
    identifier_field: str
    source_phase: int
    namespace_prefix: str
    non_signal: bool = True
    source_preserved: bool = True


@dataclass(frozen=True)
class FeatureStoreFeatureRecord:
    store_key: str
    feature_name: str
    feature_family: str
    entity_type: str
    source_phase: int
    data_type: str
    namespace: str
    validation_status: str
    quality_score_ref: float
    drift_score_ref: float
    lineage_ref: str
    manual_review_required: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False


@dataclass(frozen=True)
class FeatureStoreFactorRecord:
    factor_name: str
    factor_family: str
    entity_type: str
    source_phase: int
    input_feature_set_ref: str
    validation_dependency_ref: str
    quality_dependency_ref: str
    manifest_ref: str
    manual_review_required: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass(frozen=True)
class FeatureStoreSchemaRecord:
    schema_id: str
    store_name: str
    required_columns: List[str]
    column_types: Dict[str, str]
    timestamp_field: str
    entity_field: str
    version_tag: str
    non_signal: bool = True
    source_preserved: bool = True


@dataclass(frozen=True)
class FeatureStoreLineageReference:
    reference_id: str
    feature_or_factor_name: str
    source_phase: int
    source_dataset: str
    lineage_hash: str
    transformation_record: str
    non_signal: bool = True
    source_preserved: bool = True


@dataclass(frozen=True)
class FeatureStoreValidationStatus:
    status_id: str
    entity_id: str
    feature_name: str
    status_label: str  # validation_pass, validation_pass_with_warnings, validation_manual_review_required, validation_fail
    severity: str
    issues_detected: int = 0
    non_signal: bool = True
    source_preserved: bool = True


@dataclass(frozen=True)
class FeatureStoreQualityScoreRecord:
    score_id: str
    feature_name: str
    entity_id: str
    quality_score: float
    completeness_score: float
    variance_score: float
    stability_score: float
    passed: bool = True
    non_signal: bool = True


@dataclass(frozen=True)
class FeatureStoreDriftScoreRecord:
    score_id: str
    feature_name: str
    entity_id: str
    drift_score: float
    ks_statistic: float
    psi_score: float
    drift_detected: bool = False
    non_signal: bool = True


@dataclass(frozen=True)
class FeatureStoreManualReviewBlocker:
    blocker_id: str
    target_item: str
    blocker_type: str
    reason: str
    blocking_status: bool = True
    non_signal: bool = True
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass(frozen=True)
class FeatureStoreMetadataManifest:
    store_name: str
    entity_count: int
    feature_count: int
    factor_count: int
    validation_status_count: int
    quality_score_count: int
    drift_score_count: int
    manual_review_blocker_count: int
    source_phase_refs: List[int]
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    manual_review_required: bool = True
