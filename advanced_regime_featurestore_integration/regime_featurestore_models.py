"""Phase 134: Regime FeatureStore Integration Models.

Defines immutable dataclass structures representing FeatureStore contracts,
catalog items, accepted references, lineage, blockers, and metadata manifests.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class RegimeFeatureStoreProfileItem:
    """Represents an active FeatureStore integration profile item."""

    profile_name: str
    description: str
    current_phase: int = 134
    target_final_phase: int = 160
    next_phase: int = 135
    min_readiness_score: float = 0.45
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class RegimeFeatureStoreContract:
    """Represents a formal read/write contract for a FeatureStore regime entity."""

    contract_name: str
    store_entity_type: str
    entity_keys: List[str]
    timestamp_field: str
    namespace_policy_ref: str
    schema_policy_ref: str
    validation_acceptance_required: bool = True
    no_lookahead_acceptance_required: bool = True
    metadata_only_news_acceptance_required: bool = True
    source_preservation_required: bool = True
    non_signal_required: bool = True
    quality_dependency_required: bool = True
    lineage_required: bool = True
    manual_review_required: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class RegimeFeatureStoreEntity:
    """Represents an entity type registered within the Regime FeatureStore."""

    entity_name: str
    store_entity_type: str
    primary_key: str
    description: str
    source_phase: int
    source_component: str
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class RegimeFeatureStoreSchemaItem:
    """Represents a column/field specification in the FeatureStore schema."""

    field_name: str
    field_type: str
    required: bool
    description: str
    is_forbidden_candidate: bool = False
    is_acceptance_ref: bool = False
    is_lineage_ref: bool = False


@dataclass
class RegimeStoreCatalogItem:
    """Represents an entry in a component store catalog."""

    store_catalog_name: str
    store_entity_type: str
    source_phase: int
    source_component: str
    source_report_ref: str
    validation_acceptance_ref: str
    no_lookahead_accepted: bool = True
    metadata_only_news_accepted: bool = True
    source_preserved: bool = True
    non_signal: bool = True
    manual_review_required: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class RegimeAcceptedReferenceItem:
    """Represents an accepted reference binding an upstream verified component."""

    reference_id: str
    reference_type: str
    source_phase: int
    source_gate_ref: str
    acceptance_status: str
    accepted_timestamp_utc: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    non_signal: bool = True
    source_preserved: bool = True


@dataclass
class RegimeLineageReference:
    """Represents an end-to-end lineage path element from Phase 126 through Phase 134."""

    lineage_id: str
    source_phase: int
    source_component: str
    target_component: str
    dependency_chain: List[str]
    traceability_status: str = "VERIFIED"
    non_signal: bool = True


@dataclass
class RegimeManualReviewBlockerStoreItem:
    """Represents an audit blocker preventing unverified promotions."""

    blocker_id: str
    blocker_type: str
    severity: str
    description: str
    affected_component: str
    remediation_guidance: str
    auto_fix_allowed: bool = False
    destructive_action_allowed: bool = False


@dataclass
class RegimeFeatureStoreMetadataManifest:
    """Master metadata manifest for the Phase 134 Regime FeatureStore integration."""

    manifest_name: str
    generated_at_utc: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    current_phase: int = 134
    target_final_phase: int = 160
    next_phase: int = 135
    contract_count: int = 0
    catalog_count: int = 0
    accepted_reference_count: int = 0
    dependency_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 1.0
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
    metadata: Dict[str, Any] = field(default_factory=dict)
