"""Phase 122 Factor Metadata Domain, Family, and Status Labels.

Provides canonical string constants and validation routines for factors,
factor families, contracts, and quality statuses.
"""

from typing import List

# Factor Metadata Domain Labels (32)
FACTOR_METADATA_PROFILE_DOMAIN = "factor_metadata_profile_domain"
FACTOR_METADATA_DOMAIN = "factor_metadata_domain"
FACTOR_FAMILY_DOMAIN = "factor_family_domain"
FACTOR_CONTRACT_DOMAIN = "factor_contract_domain"
FACTOR_INPUT_FEATURE_SET_DOMAIN = "factor_input_feature_set_domain"
FACTOR_NAMESPACE_DOMAIN = "factor_namespace_domain"
FACTOR_OUTPUT_SCHEMA_DOMAIN = "factor_output_schema_domain"
FACTOR_DEPENDENCY_DOMAIN = "factor_dependency_domain"
FACTOR_VALIDATION_DEPENDENCY_DOMAIN = "factor_validation_dependency_domain"
FACTOR_QUALITY_DEPENDENCY_DOMAIN = "factor_quality_dependency_domain"
TECHNICAL_FACTOR_DOMAIN = "technical_factor_domain"
TREND_FACTOR_DOMAIN = "trend_factor_domain"
MOMENTUM_FACTOR_DOMAIN = "momentum_factor_domain"
VOLATILITY_FACTOR_DOMAIN = "volatility_factor_domain"
MEAN_REVERSION_FACTOR_DOMAIN = "mean_reversion_factor_domain"
RETURN_FACTOR_DOMAIN = "return_factor_domain"
QUOTE_MICROSTRUCTURE_FACTOR_DOMAIN = "quote_microstructure_factor_domain"
MACRO_CONTEXT_FACTOR_DOMAIN = "macro_context_factor_domain"
CALENDAR_EVENT_FACTOR_DOMAIN = "calendar_event_factor_domain"
NEWS_ATTENTION_FACTOR_DOMAIN = "news_attention_factor_domain"
CROSS_ASSET_CONTEXT_FACTOR_DOMAIN = "cross_asset_context_factor_domain"
REGIME_PREP_FACTOR_DOMAIN = "regime_prep_factor_domain"
COMPOSITE_FACTOR_DOMAIN = "composite_factor_domain"
FACTOR_MANIFEST_DOMAIN = "factor_manifest_domain"
FACTOR_MANUAL_REVIEW_DOMAIN = "factor_manual_review_domain"
FACTOR_NON_SIGNAL_DOMAIN = "factor_non_signal_domain"
FACTOR_FORBIDDEN_CLAIM_DOMAIN = "factor_forbidden_claim_domain"
FACTOR_HEALTH_DOMAIN = "factor_health_domain"
FACTOR_VALIDATION_DOMAIN = "factor_validation_domain"
FACTOR_SAFETY_DOMAIN = "factor_safety_domain"
PHASE_123_HANDOFF_DOMAIN = "phase_123_handoff_domain"
UNKNOWN_FACTOR_DOMAIN = "unknown_factor_domain"

FACTOR_METADATA_DOMAINS: List[str] = [
    FACTOR_METADATA_PROFILE_DOMAIN,
    FACTOR_METADATA_DOMAIN,
    FACTOR_FAMILY_DOMAIN,
    FACTOR_CONTRACT_DOMAIN,
    FACTOR_INPUT_FEATURE_SET_DOMAIN,
    FACTOR_NAMESPACE_DOMAIN,
    FACTOR_OUTPUT_SCHEMA_DOMAIN,
    FACTOR_DEPENDENCY_DOMAIN,
    FACTOR_VALIDATION_DEPENDENCY_DOMAIN,
    FACTOR_QUALITY_DEPENDENCY_DOMAIN,
    TECHNICAL_FACTOR_DOMAIN,
    TREND_FACTOR_DOMAIN,
    MOMENTUM_FACTOR_DOMAIN,
    VOLATILITY_FACTOR_DOMAIN,
    MEAN_REVERSION_FACTOR_DOMAIN,
    RETURN_FACTOR_DOMAIN,
    QUOTE_MICROSTRUCTURE_FACTOR_DOMAIN,
    MACRO_CONTEXT_FACTOR_DOMAIN,
    CALENDAR_EVENT_FACTOR_DOMAIN,
    NEWS_ATTENTION_FACTOR_DOMAIN,
    CROSS_ASSET_CONTEXT_FACTOR_DOMAIN,
    REGIME_PREP_FACTOR_DOMAIN,
    COMPOSITE_FACTOR_DOMAIN,
    FACTOR_MANIFEST_DOMAIN,
    FACTOR_MANUAL_REVIEW_DOMAIN,
    FACTOR_NON_SIGNAL_DOMAIN,
    FACTOR_FORBIDDEN_CLAIM_DOMAIN,
    FACTOR_HEALTH_DOMAIN,
    FACTOR_VALIDATION_DOMAIN,
    FACTOR_SAFETY_DOMAIN,
    PHASE_123_HANDOFF_DOMAIN,
    UNKNOWN_FACTOR_DOMAIN,
]

# Factor Family Labels (13)
FACTOR_FAMILY_TREND = "factor_family_trend"
FACTOR_FAMILY_MOMENTUM = "factor_family_momentum"
FACTOR_FAMILY_VOLATILITY = "factor_family_volatility"
FACTOR_FAMILY_MEAN_REVERSION = "factor_family_mean_reversion"
FACTOR_FAMILY_RETURN = "factor_family_return"
FACTOR_FAMILY_QUOTE_MICROSTRUCTURE = "factor_family_quote_microstructure"
FACTOR_FAMILY_MACRO_CONTEXT = "factor_family_macro_context"
FACTOR_FAMILY_CALENDAR_EVENT = "factor_family_calendar_event"
FACTOR_FAMILY_NEWS_ATTENTION = "factor_family_news_attention"
FACTOR_FAMILY_CROSS_ASSET_CONTEXT = "factor_family_cross_asset_context"
FACTOR_FAMILY_REGIME_PREP = "factor_family_regime_prep"
FACTOR_FAMILY_COMPOSITE = "factor_family_composite"
FACTOR_FAMILY_UNKNOWN = "factor_family_unknown"

FACTOR_FAMILIES: List[str] = [
    FACTOR_FAMILY_TREND,
    FACTOR_FAMILY_MOMENTUM,
    FACTOR_FAMILY_VOLATILITY,
    FACTOR_FAMILY_MEAN_REVERSION,
    FACTOR_FAMILY_RETURN,
    FACTOR_FAMILY_QUOTE_MICROSTRUCTURE,
    FACTOR_FAMILY_MACRO_CONTEXT,
    FACTOR_FAMILY_CALENDAR_EVENT,
    FACTOR_FAMILY_NEWS_ATTENTION,
    FACTOR_FAMILY_CROSS_ASSET_CONTEXT,
    FACTOR_FAMILY_REGIME_PREP,
    FACTOR_FAMILY_COMPOSITE,
    FACTOR_FAMILY_UNKNOWN,
]

# Factor Status Labels (6)
FACTOR_READY = "factor_ready"
FACTOR_READY_WITH_WARNINGS = "factor_ready_with_warnings"
FACTOR_PLACEHOLDER_ONLY = "factor_placeholder_only"
FACTOR_MANUAL_REVIEW_REQUIRED = "factor_manual_review_required"
FACTOR_BLOCKED_BY_SAFETY = "factor_blocked_by_safety"
FACTOR_UNKNOWN = "factor_unknown"

FACTOR_STATUSES: List[str] = [
    FACTOR_READY,
    FACTOR_READY_WITH_WARNINGS,
    FACTOR_PLACEHOLDER_ONLY,
    FACTOR_MANUAL_REVIEW_REQUIRED,
    FACTOR_BLOCKED_BY_SAFETY,
    FACTOR_UNKNOWN,
]


def list_factor_metadata_domain_labels() -> List[str]:
    """Return all factor metadata domain label strings."""
    return list(FACTOR_METADATA_DOMAINS)


def list_factor_family_labels() -> List[str]:
    """Return all factor family label strings."""
    return list(FACTOR_FAMILIES)


def list_factor_status_labels() -> List[str]:
    """Return all factor status label strings."""
    return list(FACTOR_STATUSES)


def validate_factor_metadata_domain_label(label: str) -> bool:
    """Check whether a given label is a registered factor metadata domain."""
    return label in FACTOR_METADATA_DOMAINS


def validate_factor_family_label(label: str) -> bool:
    """Check whether a given label is a registered factor family."""
    return label in FACTOR_FAMILIES


def validate_factor_status_label(label: str) -> bool:
    """Check whether a given label is a registered factor status."""
    return label in FACTOR_STATUSES
