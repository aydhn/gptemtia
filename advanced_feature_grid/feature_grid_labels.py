from typing import List


FEATURE_GRID_DOMAINS = [
    "feature_grid_profile_domain",
    "feature_grid_domain",
    "window_grid_contract_domain",
    "parameter_grid_domain",
    "naming_domain",
    "output_schema_domain",
    "warmup_nan_policy_domain",
    "no_lookahead_guard_domain",
    "duplicate_detection_domain",
    "moving_average_grid_domain",
    "momentum_grid_domain",
    "volatility_grid_domain",
    "range_channel_grid_domain",
    "mean_reversion_grid_domain",
    "return_grid_domain",
    "quote_grid_placeholder_domain",
    "macro_grid_placeholder_domain",
    "calendar_grid_placeholder_domain",
    "news_grid_placeholder_domain",
    "computation_interface_domain",
    "computation_rehearsal_domain",
    "metadata_domain",
    "dependency_domain",
    "validation_domain",
    "quality_handoff_domain",
    "feature_grid_health_domain",
    "feature_grid_safety_domain",
    "phase_119_handoff_domain",
    "unknown_feature_grid_domain",
]

FEATURE_GRID_FAMILIES = [
    "grid_family_moving_average",
    "grid_family_momentum",
    "grid_family_volatility",
    "grid_family_range_channel",
    "grid_family_mean_reversion",
    "grid_family_return",
    "grid_family_quote_placeholder",
    "grid_family_macro_placeholder",
    "grid_family_calendar_placeholder",
    "grid_family_news_placeholder",
    "grid_family_unknown",
]

FEATURE_GRID_STATUSES = [
    "feature_grid_ready",
    "feature_grid_ready_with_warnings",
    "feature_grid_placeholder_only",
    "feature_grid_manual_review_required",
    "feature_grid_blocked_by_safety",
    "feature_grid_unknown",
]


def list_feature_grid_domain_labels() -> List[str]:
    return list(FEATURE_GRID_DOMAINS)


def list_feature_grid_family_labels() -> List[str]:
    return list(FEATURE_GRID_FAMILIES)


def list_feature_grid_status_labels() -> List[str]:
    return list(FEATURE_GRID_STATUSES)


def validate_feature_grid_domain_label(label: str) -> str:
    if label not in FEATURE_GRID_DOMAINS:
        return "unknown_feature_grid_domain"
    return label


def validate_feature_grid_family_label(label: str) -> str:
    if label not in FEATURE_GRID_FAMILIES:
        return "grid_family_unknown"
    return label


def validate_feature_grid_status_label(label: str) -> str:
    if label not in FEATURE_GRID_STATUSES:
        return "feature_grid_unknown"
    return label
