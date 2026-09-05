"""Phase 124 Feature Store Integration Domain and Status Labels."""

from typing import List

FEATURE_STORE_INTEGRATION_DOMAIN_LABELS: List[str] = [
    "feature_store_integration_profile_domain",
    "feature_store_integration_domain",
    "feature_store_contract_domain",
    "feature_store_entity_domain",
    "feature_store_feature_domain",
    "feature_store_factor_domain",
    "feature_store_namespace_domain",
    "feature_store_schema_domain",
    "feature_store_version_policy_domain",
    "feature_store_partition_policy_domain",
    "feature_store_lineage_domain",
    "feature_store_validation_status_domain",
    "feature_store_quality_score_domain",
    "feature_store_drift_score_domain",
    "feature_store_manual_review_domain",
    "feature_store_manifest_domain",
    "feature_store_read_contract_domain",
    "feature_store_write_contract_domain",
    "feature_store_query_contract_domain",
    "feature_store_non_signal_domain",
    "feature_store_forbidden_column_domain",
    "feature_store_source_preservation_domain",
    "feature_store_catalog_domain",
    "feature_store_health_domain",
    "feature_store_validation_domain",
    "feature_store_safety_domain",
    "phase_125_handoff_domain",
    "unknown_feature_store_integration_domain",
]

FEATURE_STORE_STATUS_LABELS: List[str] = [
    "store_ready",
    "store_ready_with_warnings",
    "store_placeholder_only",
    "store_manual_review_required",
    "store_blocked_by_safety",
    "store_unknown",
]

FEATURE_STORE_ENTITY_TYPE_LABELS: List[str] = [
    "entity_fx_pair",
    "entity_commodity_symbol",
    "entity_macro_indicator",
    "entity_calendar_event",
    "entity_news_metadata",
    "entity_cross_asset_context",
    "entity_factor_family",
    "entity_unknown",
]


def list_feature_store_integration_domain_labels() -> List[str]:
    """Return all valid domain labels."""
    return list(FEATURE_STORE_INTEGRATION_DOMAIN_LABELS)


def list_feature_store_status_labels() -> List[str]:
    """Return all valid store status labels."""
    return list(FEATURE_STORE_STATUS_LABELS)


def list_feature_store_entity_type_labels() -> List[str]:
    """Return all valid entity type labels."""
    return list(FEATURE_STORE_ENTITY_TYPE_LABELS)


def validate_feature_store_integration_domain_label(label: str) -> str:
    """Validate domain label or return unknown."""
    if label in FEATURE_STORE_INTEGRATION_DOMAIN_LABELS:
        return label
    return "unknown_feature_store_integration_domain"


def validate_feature_store_status_label(label: str) -> str:
    """Validate store status label or return unknown."""
    if label in FEATURE_STORE_STATUS_LABELS:
        return label
    return "store_unknown"


def validate_feature_store_entity_type_label(label: str) -> str:
    """Validate entity type label or return unknown."""
    if label in FEATURE_STORE_ENTITY_TYPE_LABELS:
        return label
    return "entity_unknown"
