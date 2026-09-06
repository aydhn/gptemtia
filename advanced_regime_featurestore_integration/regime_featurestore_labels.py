"""Phase 134: Regime FeatureStore Integration Labels, Domains, and Enums.

Defines standardized domain, status, and entity labels along with validation helpers.
"""

from typing import List, Set

# Canonical Domain Labels
REGIME_FEATURESTORE_PROFILE_DOMAIN = "regime_featurestore_profile_domain"
REGIME_FEATURESTORE_DOMAIN = "regime_featurestore_domain"
REGIME_FEATURESTORE_CONTRACT_DOMAIN = "regime_featurestore_contract_domain"
REGIME_FEATURESTORE_ENTITY_DOMAIN = "regime_featurestore_entity_domain"
REGIME_FEATURESTORE_NAMESPACE_DOMAIN = "regime_featurestore_namespace_domain"
REGIME_FEATURESTORE_SCHEMA_DOMAIN = "regime_featurestore_schema_domain"
REGIME_FEATURESTORE_VERSION_POLICY_DOMAIN = "regime_featurestore_version_policy_domain"
REGIME_FEATURESTORE_PARTITION_POLICY_DOMAIN = "regime_featurestore_partition_policy_domain"
TAXONOMY_STORE_CATALOG_DOMAIN = "taxonomy_store_catalog_domain"
MATRIX_STORE_CATALOG_DOMAIN = "matrix_store_catalog_domain"
CANDIDATE_STATE_STORE_CATALOG_DOMAIN = "candidate_state_store_catalog_domain"
PSEUDO_STATE_STORE_CATALOG_DOMAIN = "pseudo_state_store_catalog_domain"
TRANSITION_STORE_CATALOG_DOMAIN = "transition_store_catalog_domain"
CROSS_ASSET_STORE_CATALOG_DOMAIN = "cross_asset_store_catalog_domain"
MACRO_EVENT_NEWS_STORE_CATALOG_DOMAIN = "macro_event_news_store_catalog_domain"
VALIDATION_ACCEPTANCE_STORE_CATALOG_DOMAIN = "validation_acceptance_store_catalog_domain"
ACCEPTED_REFERENCE_DOMAIN = "accepted_reference_domain"
QUALITY_DEPENDENCY_STORE_DOMAIN = "quality_dependency_store_domain"
VALIDATION_DEPENDENCY_STORE_DOMAIN = "validation_dependency_store_domain"
LINEAGE_REFERENCE_DOMAIN = "lineage_reference_domain"
MANUAL_REVIEW_BLOCKER_DOMAIN = "manual_review_blocker_domain"
METADATA_MANIFEST_DOMAIN = "metadata_manifest_domain"
READ_CONTRACT_DOMAIN = "read_contract_domain"
WRITE_CONTRACT_DOMAIN = "write_contract_domain"
QUERY_CONTRACT_DOMAIN = "query_contract_domain"
FORBIDDEN_COLUMN_POLICY_DOMAIN = "forbidden_column_policy_domain"
NON_SIGNAL_POLICY_DOMAIN = "non_signal_policy_domain"
SOURCE_PRESERVATION_POLICY_DOMAIN = "source_preservation_policy_domain"
HEALTH_DOMAIN = "health_domain"
VALIDATION_DOMAIN = "validation_domain"
SAFETY_DOMAIN = "safety_domain"
PHASE_135_HANDOFF_DOMAIN = "phase_135_handoff_domain"
UNKNOWN_REGIME_FEATURESTORE_DOMAIN = "unknown_regime_featurestore_domain"

ALL_DOMAINS: Set[str] = {
    REGIME_FEATURESTORE_PROFILE_DOMAIN,
    REGIME_FEATURESTORE_DOMAIN,
    REGIME_FEATURESTORE_CONTRACT_DOMAIN,
    REGIME_FEATURESTORE_ENTITY_DOMAIN,
    REGIME_FEATURESTORE_NAMESPACE_DOMAIN,
    REGIME_FEATURESTORE_SCHEMA_DOMAIN,
    REGIME_FEATURESTORE_VERSION_POLICY_DOMAIN,
    REGIME_FEATURESTORE_PARTITION_POLICY_DOMAIN,
    TAXONOMY_STORE_CATALOG_DOMAIN,
    MATRIX_STORE_CATALOG_DOMAIN,
    CANDIDATE_STATE_STORE_CATALOG_DOMAIN,
    PSEUDO_STATE_STORE_CATALOG_DOMAIN,
    TRANSITION_STORE_CATALOG_DOMAIN,
    CROSS_ASSET_STORE_CATALOG_DOMAIN,
    MACRO_EVENT_NEWS_STORE_CATALOG_DOMAIN,
    VALIDATION_ACCEPTANCE_STORE_CATALOG_DOMAIN,
    ACCEPTED_REFERENCE_DOMAIN,
    QUALITY_DEPENDENCY_STORE_DOMAIN,
    VALIDATION_DEPENDENCY_STORE_DOMAIN,
    LINEAGE_REFERENCE_DOMAIN,
    MANUAL_REVIEW_BLOCKER_DOMAIN,
    METADATA_MANIFEST_DOMAIN,
    READ_CONTRACT_DOMAIN,
    WRITE_CONTRACT_DOMAIN,
    QUERY_CONTRACT_DOMAIN,
    FORBIDDEN_COLUMN_POLICY_DOMAIN,
    NON_SIGNAL_POLICY_DOMAIN,
    SOURCE_PRESERVATION_POLICY_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_135_HANDOFF_DOMAIN,
    UNKNOWN_REGIME_FEATURESTORE_DOMAIN,
}

# Canonical Status Labels
REGIME_STORE_READY = "regime_store_ready"
REGIME_STORE_READY_WITH_WARNINGS = "regime_store_ready_with_warnings"
REGIME_STORE_PLACEHOLDER_ONLY = "regime_store_placeholder_only"
REGIME_STORE_MANUAL_REVIEW_REQUIRED = "regime_store_manual_review_required"
REGIME_STORE_BLOCKED_BY_SAFETY = "regime_store_blocked_by_safety"
REGIME_STORE_UNKNOWN = "regime_store_unknown"

ALL_STATUSES: Set[str] = {
    REGIME_STORE_READY,
    REGIME_STORE_READY_WITH_WARNINGS,
    REGIME_STORE_PLACEHOLDER_ONLY,
    REGIME_STORE_MANUAL_REVIEW_REQUIRED,
    REGIME_STORE_BLOCKED_BY_SAFETY,
    REGIME_STORE_UNKNOWN,
}

# Canonical Entity Labels
STORE_ENTITY_REGIME_TAXONOMY = "store_entity_regime_taxonomy"
STORE_ENTITY_REGIME_MATRIX = "store_entity_regime_matrix"
STORE_ENTITY_CANDIDATE_STATE = "store_entity_candidate_state"
STORE_ENTITY_PSEUDO_STATE = "store_entity_pseudo_state"
STORE_ENTITY_TRANSITION = "store_entity_transition"
STORE_ENTITY_CROSS_ASSET_CONTEXT = "store_entity_cross_asset_context"
STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT = "store_entity_macro_event_news_context"
STORE_ENTITY_VALIDATION_ACCEPTANCE = "store_entity_validation_acceptance"
STORE_ENTITY_UNKNOWN = "store_entity_unknown"

ALL_ENTITIES: Set[str] = {
    STORE_ENTITY_REGIME_TAXONOMY,
    STORE_ENTITY_REGIME_MATRIX,
    STORE_ENTITY_CANDIDATE_STATE,
    STORE_ENTITY_PSEUDO_STATE,
    STORE_ENTITY_TRANSITION,
    STORE_ENTITY_CROSS_ASSET_CONTEXT,
    STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
    STORE_ENTITY_VALIDATION_ACCEPTANCE,
    STORE_ENTITY_UNKNOWN,
}


def list_regime_featurestore_domain_labels() -> List[str]:
    """Return sorted list of all valid domain labels."""
    return sorted(list(ALL_DOMAINS))


def list_regime_featurestore_status_labels() -> List[str]:
    """Return sorted list of all valid status labels."""
    return sorted(list(ALL_STATUSES))


def list_regime_featurestore_entity_labels() -> List[str]:
    """Return sorted list of all valid entity labels."""
    return sorted(list(ALL_ENTITIES))


def validate_regime_featurestore_domain_label(label: str) -> bool:
    """Validate whether domain label is canonical."""
    return label in ALL_DOMAINS


def validate_regime_featurestore_status_label(label: str) -> bool:
    """Validate whether status label is canonical."""
    return label in ALL_STATUSES


def validate_regime_featurestore_entity_label(label: str) -> bool:
    """Validate whether entity label is canonical."""
    return label in ALL_ENTITIES
