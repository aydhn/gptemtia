from typing import List


FEATURE_DOMAIN_LABELS = [
    "feature_engine_profile_domain",
    "feature_engine_domain",
    "feature_input_contract_domain",
    "feature_schema_domain",
    "factor_schema_domain",
    "indicator_catalog_domain",
    "price_indicator_domain",
    "trend_indicator_domain",
    "momentum_indicator_domain",
    "volatility_indicator_domain",
    "mean_reversion_indicator_domain",
    "quote_feature_domain",
    "volume_liquidity_feature_domain",
    "macro_feature_domain",
    "calendar_feature_domain",
    "news_metadata_feature_domain",
    "feature_metadata_domain",
    "factor_metadata_domain",
    "rolling_window_domain",
    "feature_computation_domain",
    "feature_dependency_domain",
    "feature_validation_domain",
    "feature_quality_handoff_domain",
    "feature_safety_domain",
    "phase_117_handoff_domain",
    "unknown_feature_domain",
]

FEATURE_TYPE_LABELS = [
    "feature_type_price",
    "feature_type_trend",
    "feature_type_momentum",
    "feature_type_volatility",
    "feature_type_mean_reversion",
    "feature_type_quote",
    "feature_type_volume_liquidity_placeholder",
    "feature_type_macro",
    "feature_type_calendar",
    "feature_type_news_metadata",
    "feature_type_cross_domain",
    "feature_type_unknown",
]

FEATURE_STATUS_LABELS = [
    "feature_ready",
    "feature_ready_with_warnings",
    "feature_placeholder_only",
    "feature_manual_review_required",
    "feature_blocked_by_safety",
    "feature_unknown",
]

FEATURE_DATASET_LABELS = [
    "dataset_fx_ohlcv",
    "dataset_fx_quote",
    "dataset_commodity_ohlcv",
    "dataset_commodity_spot",
    "dataset_macro_timeseries",
    "dataset_calendar_event",
    "dataset_release_event",
    "dataset_news_metadata",
    "dataset_unknown",
]


def list_feature_domain_labels() -> List[str]:
    return list(FEATURE_DOMAIN_LABELS)


def list_feature_type_labels() -> List[str]:
    return list(FEATURE_TYPE_LABELS)


def list_feature_status_labels() -> List[str]:
    return list(FEATURE_STATUS_LABELS)


def list_feature_dataset_labels() -> List[str]:
    return list(FEATURE_DATASET_LABELS)


def validate_feature_domain_label(label: str) -> bool:
    return label in FEATURE_DOMAIN_LABELS


def validate_feature_type_label(label: str) -> bool:
    return label in FEATURE_TYPE_LABELS


def validate_feature_status_label(label: str) -> bool:
    return label in FEATURE_STATUS_LABELS


def validate_feature_dataset_label(label: str) -> bool:
    return label in FEATURE_DATASET_LABELS
