"""Phase 132: Macro/Event/News Regime Context Expansion Labels and Taxonomy Sets."""

from typing import List, Set

MACRO_EVENT_NEWS_REGIME_DOMAIN_LABELS: List[str] = [
    "macro_event_news_regime_profile_domain",
    "macro_event_news_regime_domain",
    "macro_entity_domain",
    "event_entity_domain",
    "news_metadata_entity_domain",
    "macro_context_taxonomy_domain",
    "event_context_taxonomy_domain",
    "news_metadata_context_taxonomy_domain",
    "macro_indicator_context_domain",
    "macro_release_context_domain",
    "macro_revision_context_domain",
    "macro_surprise_placeholder_domain",
    "calendar_event_context_domain",
    "event_window_context_domain",
    "pre_event_context_domain",
    "post_event_context_domain",
    "event_importance_context_domain",
    "release_lag_context_domain",
    "release_alignment_domain",
    "news_topic_context_domain",
    "news_asset_tag_context_domain",
    "news_macro_tag_context_domain",
    "news_event_linkage_context_domain",
    "news_freshness_placeholder_domain",
    "metadata_only_news_boundary_domain",
    "cross_asset_context_domain",
    "transition_context_domain",
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
    "phase_133_handoff_domain",
    "unknown_macro_event_news_regime_domain",
]

MACRO_EVENT_NEWS_STATUS_LABELS: List[str] = [
    "macro_event_news_context_ready",
    "macro_event_news_context_ready_with_warnings",
    "macro_event_news_context_placeholder_only",
    "macro_event_news_context_manual_review_required",
    "macro_event_news_context_blocked_by_safety",
    "macro_event_news_context_unknown",
]

MACRO_EVENT_NEWS_CONTEXT_LABELS: List[str] = [
    "macro_inflation_context",
    "macro_rate_context",
    "macro_growth_context",
    "macro_revision_context",
    "macro_surprise_placeholder_context",
    "calendar_event_context",
    "pre_event_context",
    "post_event_context",
    "release_lag_context",
    "news_topic_context",
    "news_asset_tag_context",
    "news_macro_tag_context",
    "news_event_linkage_context",
    "news_freshness_placeholder_context",
    "unknown_context",
]

_DOMAIN_LABELS_SET: Set[str] = set(MACRO_EVENT_NEWS_REGIME_DOMAIN_LABELS)
_STATUS_LABELS_SET: Set[str] = set(MACRO_EVENT_NEWS_STATUS_LABELS)
_CONTEXT_LABELS_SET: Set[str] = set(MACRO_EVENT_NEWS_CONTEXT_LABELS)


def list_macro_event_news_regime_domain_labels() -> List[str]:
    """Return all valid regime domain labels for Phase 132."""
    return list(MACRO_EVENT_NEWS_REGIME_DOMAIN_LABELS)


def list_macro_event_news_status_labels() -> List[str]:
    """Return all valid status labels for Phase 132."""
    return list(MACRO_EVENT_NEWS_STATUS_LABELS)


def list_macro_event_news_context_labels() -> List[str]:
    """Return all valid context labels for Phase 132."""
    return list(MACRO_EVENT_NEWS_CONTEXT_LABELS)


def validate_macro_event_news_regime_domain_label(label: str) -> bool:
    """Validate whether label is registered as a domain label."""
    return label in _DOMAIN_LABELS_SET


def validate_macro_event_news_status_label(label: str) -> bool:
    """Validate whether label is registered as a status label."""
    return label in _STATUS_LABELS_SET


def validate_macro_event_news_context_label(label: str) -> bool:
    """Validate whether label is registered as a context label."""
    return label in _CONTEXT_LABELS_SET
