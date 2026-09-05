from typing import List

TECHNICAL_INDICATOR_DOMAIN_LABELS = [
    "technical_indicator_profile_domain",
    "technical_indicator_domain",
    "indicator_catalog_domain",
    "price_action_domain",
    "return_indicator_domain",
    "moving_average_domain",
    "trend_indicator_domain",
    "momentum_indicator_domain",
    "oscillator_indicator_domain",
    "volatility_indicator_domain",
    "range_indicator_domain",
    "channel_indicator_domain",
    "candle_anatomy_domain",
    "quote_microstructure_domain",
    "mean_reversion_domain",
    "indicator_parameter_domain",
    "indicator_output_schema_domain",
    "warmup_nan_policy_domain",
    "no_lookahead_guard_domain",
    "computation_interface_domain",
    "computation_rehearsal_domain",
    "validation_rule_domain",
    "dependency_domain",
    "quality_handoff_domain",
    "technical_indicator_health_domain",
    "technical_indicator_validation_domain",
    "technical_indicator_safety_domain",
    "phase_118_handoff_domain",
    "unknown_technical_indicator_domain",
]

INDICATOR_FAMILY_LABELS = [
    "family_price_action",
    "family_returns",
    "family_moving_average",
    "family_trend",
    "family_momentum",
    "family_oscillator",
    "family_volatility",
    "family_range",
    "family_channel",
    "family_candle_anatomy",
    "family_quote_microstructure",
    "family_mean_reversion",
    "family_unknown",
]

INDICATOR_STATUS_LABELS = [
    "indicator_ready",
    "indicator_ready_with_warnings",
    "indicator_placeholder_only",
    "indicator_manual_review_required",
    "indicator_blocked_by_safety",
    "indicator_unknown",
]


def list_technical_indicator_domain_labels() -> List[str]:
    return list(TECHNICAL_INDICATOR_DOMAIN_LABELS)


def list_indicator_family_labels() -> List[str]:
    return list(INDICATOR_FAMILY_LABELS)


def list_indicator_status_labels() -> List[str]:
    return list(INDICATOR_STATUS_LABELS)


def validate_technical_indicator_domain_label(label: str) -> bool:
    return label in TECHNICAL_INDICATOR_DOMAIN_LABELS


def validate_indicator_family_label(label: str) -> bool:
    return label in INDICATOR_FAMILY_LABELS


def validate_indicator_status_label(label: str) -> bool:
    return label in INDICATOR_STATUS_LABELS
