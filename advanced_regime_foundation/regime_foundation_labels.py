"""Phase 126: Regime Classification and Market Behavior Foundation Labels.

Defines canonical taxonomy labels, family categories, and status enumerations.
"""

from typing import List

REGIME_FOUNDATION_DOMAIN_LABELS: List[str] = [
    "regime_foundation_profile_domain",
    "regime_foundation_domain",
    "market_behavior_taxonomy_domain",
    "regime_state_taxonomy_domain",
    "regime_family_domain",
    "volatility_regime_domain",
    "trend_regime_domain",
    "range_regime_domain",
    "liquidity_regime_domain",
    "macro_regime_context_domain",
    "event_regime_context_domain",
    "news_metadata_regime_context_domain",
    "cross_asset_regime_context_domain",
    "regime_input_contract_domain",
    "regime_factor_dependency_domain",
    "regime_validation_dependency_domain",
    "regime_quality_dependency_domain",
    "regime_output_schema_domain",
    "regime_namespace_domain",
    "regime_non_signal_domain",
    "regime_forbidden_claim_domain",
    "regime_manifest_domain",
    "regime_health_domain",
    "regime_validation_domain",
    "regime_safety_domain",
    "phase_127_handoff_domain",
    "unknown_regime_domain",
]

REGIME_FAMILY_LABELS: List[str] = [
    "regime_family_volatility",
    "regime_family_trend",
    "regime_family_range",
    "regime_family_liquidity_placeholder",
    "regime_family_macro_context",
    "regime_family_event_context",
    "regime_family_news_metadata_context",
    "regime_family_cross_asset_context",
    "regime_family_composite_placeholder",
    "regime_family_unknown",
]

REGIME_STATUS_LABELS: List[str] = [
    "regime_ready",
    "regime_ready_with_warnings",
    "regime_placeholder_only",
    "regime_manual_review_required",
    "regime_blocked_by_safety",
    "regime_unknown",
]


def list_regime_foundation_domain_labels() -> List[str]:
    """Return all canonical domain labels."""
    return list(REGIME_FOUNDATION_DOMAIN_LABELS)


def list_regime_family_labels() -> List[str]:
    """Return all canonical regime family labels."""
    return list(REGIME_FAMILY_LABELS)


def list_regime_status_labels() -> List[str]:
    """Return all canonical status labels."""
    return list(REGIME_STATUS_LABELS)


def validate_regime_foundation_domain_label(label: str) -> bool:
    """Validate whether label exists in canonical domain labels."""
    return label in REGIME_FOUNDATION_DOMAIN_LABELS


def validate_regime_family_label(label: str) -> bool:
    """Validate whether label exists in canonical family labels."""
    return label in REGIME_FAMILY_LABELS


def validate_regime_status_label(label: str) -> bool:
    """Validate whether label exists in canonical status labels."""
    return label in REGIME_STATUS_LABELS
