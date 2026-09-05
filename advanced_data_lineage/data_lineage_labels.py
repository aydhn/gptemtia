from typing import List


LINEAGE_DOMAIN_LABELS: List[str] = [
    "data_lineage_profile_domain",
    "data_lineage_domain",
    "provenance_source_domain",
    "source_reference_domain",
    "provider_provenance_domain",
    "dataset_provenance_domain",
    "schema_provenance_domain",
    "transformation_provenance_domain",
    "normalization_lineage_domain",
    "quality_finding_lineage_domain",
    "manual_review_lineage_domain",
    "normalized_output_lineage_domain",
    "fx_lineage_domain",
    "commodity_lineage_domain",
    "macro_lineage_domain",
    "calendar_lineage_domain",
    "news_metadata_lineage_domain",
    "license_provenance_domain",
    "copyright_boundary_domain",
    "metadata_only_provenance_domain",
    "data_usage_boundary_domain",
    "audit_trail_domain",
    "transformation_audit_domain",
    "lineage_finding_domain",
    "provenance_scoring_domain",
    "traceability_scoring_domain",
    "lineage_graph_domain",
    "cross_domain_provenance_domain",
    "data_lineage_health_domain",
    "data_lineage_validation_domain",
    "data_lineage_safety_domain",
    "phase_115_handoff_domain",
    "unknown_lineage_domain",
]

LINEAGE_STATUS_LABELS: List[str] = [
    "lineage_complete",
    "lineage_partial",
    "lineage_missing",
    "lineage_manual_review_required",
    "lineage_blocked_by_safety",
    "lineage_placeholder_only",
    "lineage_unknown",
]

PROVENANCE_CONFIDENCE_LABELS: List[str] = [
    "provenance_high_confidence",
    "provenance_medium_confidence",
    "provenance_low_confidence",
    "provenance_unknown_confidence",
]

AUDIT_EVENT_LABELS: List[str] = [
    "audit_source_registered",
    "audit_provider_registered",
    "audit_schema_linked",
    "audit_quality_finding_linked",
    "audit_normalization_applied",
    "audit_normalized_view_created",
    "audit_manual_review_required",
    "audit_license_boundary_recorded",
    "audit_copyright_boundary_recorded",
    "audit_metadata_only_boundary_recorded",
    "audit_phase_115_handoff_created",
]

LINEAGE_DATASET_TYPE_LABELS: List[str] = [
    "dataset_fx_ohlcv",
    "dataset_fx_quote",
    "dataset_commodity_spot",
    "dataset_commodity_ohlcv",
    "dataset_macro_timeseries",
    "dataset_calendar_event",
    "dataset_release_event",
    "dataset_news_metadata",
    "dataset_provider_metadata",
    "dataset_unknown",
]


def list_lineage_domain_labels() -> List[str]:
    return list(LINEAGE_DOMAIN_LABELS)


def list_lineage_status_labels() -> List[str]:
    return list(LINEAGE_STATUS_LABELS)


def list_provenance_confidence_labels() -> List[str]:
    return list(PROVENANCE_CONFIDENCE_LABELS)


def list_audit_event_labels() -> List[str]:
    return list(AUDIT_EVENT_LABELS)


def list_lineage_dataset_type_labels() -> List[str]:
    return list(LINEAGE_DATASET_TYPE_LABELS)


def validate_lineage_domain_label(label: str) -> bool:
    if label not in LINEAGE_DOMAIN_LABELS:
        raise ValueError(f"Invalid lineage domain label: '{label}'. Allowed: {LINEAGE_DOMAIN_LABELS}")
    return True


def validate_lineage_status_label(label: str) -> bool:
    if label not in LINEAGE_STATUS_LABELS:
        raise ValueError(f"Invalid lineage status label: '{label}'. Allowed: {LINEAGE_STATUS_LABELS}")
    return True


def validate_provenance_confidence_label(label: str) -> bool:
    if label not in PROVENANCE_CONFIDENCE_LABELS:
        raise ValueError(f"Invalid provenance confidence label: '{label}'. Allowed: {PROVENANCE_CONFIDENCE_LABELS}")
    return True


def validate_audit_event_label(label: str) -> bool:
    if label not in AUDIT_EVENT_LABELS:
        raise ValueError(f"Invalid audit event label: '{label}'. Allowed: {AUDIT_EVENT_LABELS}")
    return True


def validate_lineage_dataset_type_label(label: str) -> bool:
    if label not in LINEAGE_DATASET_TYPE_LABELS:
        raise ValueError(f"Invalid lineage dataset type label: '{label}'. Allowed: {LINEAGE_DATASET_TYPE_LABELS}")
    return True
