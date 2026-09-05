from typing import List

# Normalization Domain Labels
NORMALIZATION_DOMAINS: List[str] = [
    "data_normalization_profile_domain",
    "data_normalization_domain",
    "normalization_rule_domain",
    "normalization_status_domain",
    "canonical_schema_domain",
    "canonical_field_domain",
    "schema_version_normalization_domain",
    "provider_name_normalization_domain",
    "fx_symbol_normalization_domain",
    "commodity_symbol_normalization_domain",
    "macro_indicator_normalization_domain",
    "calendar_event_normalization_domain",
    "news_topic_tag_normalization_domain",
    "region_currency_normalization_domain",
    "timestamp_timezone_normalization_domain",
    "session_alignment_domain",
    "frequency_normalization_domain",
    "unit_normalization_domain",
    "numeric_type_normalization_domain",
    "string_case_slug_normalization_domain",
    "duplicate_key_normalization_domain",
    "normalized_view_domain",
    "normalization_finding_domain",
    "normalization_decision_domain",
    "manual_review_normalization_domain",
    "normalization_scoring_domain",
    "cross_domain_mapping_domain",
    "data_normalization_health_domain",
    "data_normalization_validation_domain",
    "data_normalization_safety_domain",
    "phase_114_handoff_domain",
    "unknown_normalization_domain",
]

# Normalization Status Labels
NORMALIZATION_STATUSES: List[str] = [
    "normalization_applied",
    "normalization_not_applicable",
    "normalization_manual_review_required",
    "normalization_blocked_by_safety",
    "normalization_placeholder_only",
    "normalization_failed",
    "normalization_unknown",
]

# Normalization Severity Labels
NORMALIZATION_SEVERITIES: List[str] = [
    "normalization_critical",
    "normalization_high",
    "normalization_medium",
    "normalization_low",
    "normalization_info",
    "normalization_unknown_severity",
]

# Normalization Action Labels
NORMALIZATION_ACTIONS: List[str] = [
    "action_canonicalize_symbol",
    "action_canonicalize_timestamp",
    "action_canonicalize_timezone",
    "action_canonicalize_frequency",
    "action_canonicalize_unit",
    "action_canonicalize_region",
    "action_canonicalize_provider",
    "action_canonicalize_tag",
    "action_canonicalize_schema_version",
    "action_create_normalized_view",
    "action_manual_review_only",
    "action_unknown",
]

# Dataset Type Labels
NORMALIZATION_DATASET_TYPES: List[str] = [
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


def list_normalization_domain_labels() -> List[str]:
    return list(NORMALIZATION_DOMAINS)


def list_normalization_status_labels() -> List[str]:
    return list(NORMALIZATION_STATUSES)


def list_normalization_severity_labels() -> List[str]:
    return list(NORMALIZATION_SEVERITIES)


def list_normalization_action_labels() -> List[str]:
    return list(NORMALIZATION_ACTIONS)


def list_normalization_dataset_type_labels() -> List[str]:
    return list(NORMALIZATION_DATASET_TYPES)


def validate_normalization_domain_label(label: str) -> bool:
    return label in NORMALIZATION_DOMAINS


def validate_normalization_status_label(label: str) -> bool:
    return label in NORMALIZATION_STATUSES


def validate_normalization_severity_label(label: str) -> bool:
    return label in NORMALIZATION_SEVERITIES


def validate_normalization_action_label(label: str) -> bool:
    return label in NORMALIZATION_ACTIONS


def validate_normalization_dataset_type_label(label: str) -> bool:
    return label in NORMALIZATION_DATASET_TYPES
