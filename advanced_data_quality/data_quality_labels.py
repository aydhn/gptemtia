from typing import List

QUALITY_DOMAIN_LABELS = [
    "data_quality_profile_domain",
    "data_quality_domain",
    "quality_rule_domain",
    "quality_severity_domain",
    "schema_compliance_domain",
    "missing_data_domain",
    "stale_data_domain",
    "duplicate_data_domain",
    "outlier_placeholder_domain",
    "timestamp_integrity_domain",
    "frequency_unit_domain",
    "fx_quality_domain",
    "commodity_quality_domain",
    "macro_quality_domain",
    "calendar_quality_domain",
    "news_metadata_quality_domain",
    "provider_metadata_quality_domain",
    "ohlc_consistency_domain",
    "quote_consistency_domain",
    "event_release_consistency_domain",
    "news_copyright_quality_domain",
    "quality_finding_domain",
    "manual_review_domain",
    "provider_quality_score_domain",
    "dataset_quality_score_domain",
    "cross_provider_quality_domain",
    "data_quality_health_domain",
    "data_quality_validation_domain",
    "data_quality_safety_domain",
    "unknown_quality_domain",
]

QUALITY_SEVERITY_LABELS = [
    "quality_critical",
    "quality_high",
    "quality_medium",
    "quality_low",
    "quality_info",
    "quality_unknown",
]

QUALITY_STATUS_LABELS = [
    "quality_pass",
    "quality_pass_with_warnings",
    "quality_fail",
    "quality_not_applicable",
    "quality_manual_review_required",
    "quality_unknown",
]

DATASET_TYPE_LABELS = [
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

QUALITY_FINDING_TYPE_LABELS = [
    "finding_schema_mismatch",
    "finding_missing_required_field",
    "finding_missing_value",
    "finding_stale_data",
    "finding_duplicate_record",
    "finding_outlier_placeholder",
    "finding_timestamp_issue",
    "finding_frequency_unit_mismatch",
    "finding_ohlc_inconsistency",
    "finding_quote_inconsistency",
    "finding_event_release_inconsistency",
    "finding_news_copyright_boundary",
    "finding_provider_metadata_issue",
    "finding_manual_review_required",
]


def list_quality_domain_labels() -> List[str]:
    return list(QUALITY_DOMAIN_LABELS)


def list_quality_severity_labels() -> List[str]:
    return list(QUALITY_SEVERITY_LABELS)


def list_quality_status_labels() -> List[str]:
    return list(QUALITY_STATUS_LABELS)


def list_dataset_type_labels() -> List[str]:
    return list(DATASET_TYPE_LABELS)


def list_quality_finding_type_labels() -> List[str]:
    return list(QUALITY_FINDING_TYPE_LABELS)


def validate_quality_domain_label(label: str) -> bool:
    return label in QUALITY_DOMAIN_LABELS


def validate_quality_severity_label(label: str) -> bool:
    return label in QUALITY_SEVERITY_LABELS


def validate_quality_status_label(label: str) -> bool:
    return label in QUALITY_STATUS_LABELS


def validate_dataset_type_label(label: str) -> bool:
    return label in DATASET_TYPE_LABELS


def validate_quality_finding_type_label(label: str) -> bool:
    return label in QUALITY_FINDING_TYPE_LABELS
