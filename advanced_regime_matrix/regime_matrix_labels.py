"""Phase 127: Regime Feature Matrix and State Dataset Labels and Vocabulary.

Canonical domain, status, and entity labels for Phase 127.
"""

from typing import List

REGIME_MATRIX_DOMAIN_LABELS: List[str] = [
    "regime_matrix_profile_domain",
    "regime_matrix_domain",
    "regime_feature_matrix_contract_domain",
    "regime_state_dataset_contract_domain",
    "regime_matrix_entity_domain",
    "regime_matrix_namespace_domain",
    "regime_matrix_schema_domain",
    "regime_matrix_input_feature_domain",
    "regime_matrix_factor_input_domain",
    "regime_matrix_context_input_domain",
    "regime_matrix_quality_input_domain",
    "regime_matrix_timestamp_alignment_domain",
    "regime_matrix_asof_join_domain",
    "regime_matrix_no_lookahead_domain",
    "regime_state_dataset_schema_domain",
    "regime_state_dataset_metadata_domain",
    "regime_state_candidate_context_domain",
    "regime_matrix_integrity_domain",
    "regime_matrix_source_phase_domain",
    "regime_matrix_validation_dependency_domain",
    "regime_matrix_quality_dependency_domain",
    "regime_matrix_non_signal_domain",
    "regime_matrix_forbidden_column_domain",
    "regime_matrix_source_preservation_domain",
    "regime_matrix_manual_review_domain",
    "regime_matrix_health_domain",
    "regime_matrix_validation_domain",
    "regime_matrix_safety_domain",
    "phase_128_handoff_domain",
    "unknown_regime_matrix_domain",
]

REGIME_MATRIX_STATUS_LABELS: List[str] = [
    "matrix_ready",
    "matrix_ready_with_warnings",
    "matrix_placeholder_only",
    "matrix_manual_review_required",
    "matrix_blocked_by_safety",
    "matrix_unknown",
]

REGIME_MATRIX_ENTITY_LABELS: List[str] = [
    "matrix_entity_fx_pair",
    "matrix_entity_commodity_symbol",
    "matrix_entity_macro_indicator",
    "matrix_entity_calendar_event",
    "matrix_entity_news_metadata",
    "matrix_entity_cross_asset_context",
    "matrix_entity_regime_family",
    "matrix_entity_unknown",
]


def list_regime_matrix_domain_labels() -> List[str]:
    """Return all valid regime matrix domain labels."""
    return list(REGIME_MATRIX_DOMAIN_LABELS)


def list_regime_matrix_status_labels() -> List[str]:
    """Return all valid regime matrix status labels."""
    return list(REGIME_MATRIX_STATUS_LABELS)


def list_regime_matrix_entity_labels() -> List[str]:
    """Return all valid regime matrix entity labels."""
    return list(REGIME_MATRIX_ENTITY_LABELS)


def validate_regime_matrix_domain_label(label: str) -> bool:
    """Validate if domain label is recognized."""
    return label in REGIME_MATRIX_DOMAIN_LABELS


def validate_regime_matrix_status_label(label: str) -> bool:
    """Validate if status label is recognized."""
    return label in REGIME_MATRIX_STATUS_LABELS


def validate_regime_matrix_entity_label(label: str) -> bool:
    """Validate if entity label is recognized."""
    return label in REGIME_MATRIX_ENTITY_LABELS
