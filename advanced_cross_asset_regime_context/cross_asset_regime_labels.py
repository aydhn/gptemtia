"""Phase 131: Cross-Asset Regime Context Domain and Status Labels.

Defines standardized domain taxonomy, operational status labels, and relationship labels.
"""

from typing import List

CROSS_ASSET_REGIME_DOMAIN_LABELS: List[str] = [
    "cross_asset_regime_profile_domain",
    "cross_asset_regime_domain",
    "entity_domain",
    "pair_domain",
    "relationship_taxonomy_domain",
    "fx_commodity_context_domain",
    "fx_macro_context_domain",
    "commodity_macro_context_domain",
    "macro_calendar_context_domain",
    "calendar_news_context_domain",
    "transition_alignment_domain",
    "volatility_linkage_domain",
    "trend_linkage_domain",
    "range_linkage_domain",
    "divergence_context_domain",
    "convergence_context_domain",
    "correlation_placeholder_domain",
    "lead_lag_placeholder_domain",
    "context_contract_domain",
    "timestamp_policy_domain",
    "asof_join_policy_domain",
    "no_lookahead_guard_domain",
    "validation_dependency_domain",
    "quality_dependency_domain",
    "source_phase_domain",
    "manual_review_domain",
    "finding_domain",
    "scoring_domain",
    "manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_132_handoff_domain",
    "unknown_cross_asset_regime_domain",
]

CROSS_ASSET_REGIME_STATUS_LABELS: List[str] = [
    "cross_asset_context_ready",
    "cross_asset_context_ready_with_warnings",
    "cross_asset_context_placeholder_only",
    "cross_asset_context_manual_review_required",
    "cross_asset_context_blocked_by_safety",
    "cross_asset_context_unknown",
]

CROSS_ASSET_RELATIONSHIP_LABELS: List[str] = [
    "relationship_comovement_context",
    "relationship_divergence_context",
    "relationship_convergence_context",
    "relationship_volatility_linkage_context",
    "relationship_trend_linkage_context",
    "relationship_range_linkage_context",
    "relationship_macro_sensitivity_context",
    "relationship_event_sensitivity_context",
    "relationship_news_metadata_context",
    "relationship_lead_lag_placeholder",
    "relationship_unknown",
]


def list_cross_asset_regime_domain_labels() -> List[str]:
    """Return all valid domain labels."""
    return list(CROSS_ASSET_REGIME_DOMAIN_LABELS)


def list_cross_asset_regime_status_labels() -> List[str]:
    """Return all valid status labels."""
    return list(CROSS_ASSET_REGIME_STATUS_LABELS)


def list_cross_asset_relationship_labels() -> List[str]:
    """Return all valid relationship taxonomy labels."""
    return list(CROSS_ASSET_RELATIONSHIP_LABELS)


def validate_cross_asset_regime_domain_label(label: str) -> bool:
    """Validate whether label is recognized in domain taxonomy."""
    return label in CROSS_ASSET_REGIME_DOMAIN_LABELS


def validate_cross_asset_regime_status_label(label: str) -> bool:
    """Validate whether label is recognized in status taxonomy."""
    return label in CROSS_ASSET_REGIME_STATUS_LABELS


def validate_cross_asset_relationship_label(label: str) -> bool:
    """Validate whether label is recognized in relationship taxonomy."""
    return label in CROSS_ASSET_RELATIONSHIP_LABELS
