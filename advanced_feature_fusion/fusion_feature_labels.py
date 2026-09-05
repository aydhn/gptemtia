from typing import List

# Domain labels
DOMAIN_LABELS: List[str] = [
    "fusion_feature_profile_domain",
    "fusion_feature_domain",
    "macro_fusion_contract_domain",
    "calendar_event_fusion_contract_domain",
    "release_event_fusion_contract_domain",
    "news_metadata_fusion_contract_domain",
    "macro_release_lag_policy_domain",
    "calendar_event_window_policy_domain",
    "news_metadata_only_policy_domain",
    "fusion_timestamp_alignment_domain",
    "fusion_asof_join_domain",
    "no_lookahead_fusion_guard_domain",
    "macro_feature_fusion_domain",
    "macro_surprise_placeholder_domain",
    "macro_revision_placeholder_domain",
    "calendar_event_window_feature_domain",
    "release_event_feature_domain",
    "event_importance_placeholder_domain",
    "news_topic_fusion_domain",
    "news_asset_tag_fusion_domain",
    "news_event_linkage_domain",
    "news_freshness_placeholder_domain",
    "macro_calendar_fusion_domain",
    "macro_news_fusion_domain",
    "calendar_news_fusion_domain",
    "cross_domain_context_fusion_domain",
    "fusion_feature_matrix_contract_domain",
    "fusion_feature_matrix_domain",
    "fusion_feature_metadata_domain",
    "fusion_feature_dependency_domain",
    "fusion_feature_validation_domain",
    "fusion_quality_handoff_domain",
    "fusion_feature_health_domain",
    "fusion_feature_safety_domain",
    "phase_121_handoff_domain",
    "unknown_fusion_feature_domain",
]

# Family labels
FAMILY_LABELS: List[str] = [
    "fusion_family_macro",
    "fusion_family_calendar",
    "fusion_family_release_event",
    "fusion_family_news_metadata",
    "fusion_family_macro_calendar",
    "fusion_family_macro_news",
    "fusion_family_calendar_news",
    "fusion_family_cross_domain_context",
    "fusion_family_unknown",
]

# Status labels
STATUS_LABELS: List[str] = [
    "fusion_ready",
    "fusion_ready_with_warnings",
    "fusion_placeholder_only",
    "fusion_manual_review_required",
    "fusion_blocked_by_safety",
    "fusion_unknown",
]

# Join policy labels
JOIN_POLICY_LABELS: List[str] = [
    "fusion_join_policy_backward_asof",
    "fusion_join_policy_release_time_only",
    "fusion_join_policy_event_window_placeholder",
    "fusion_join_policy_metadata_tag_link",
    "fusion_join_policy_manual_review_only",
]


def list_fusion_feature_domain_labels() -> List[str]:
    return list(DOMAIN_LABELS)


def list_fusion_family_labels() -> List[str]:
    return list(FAMILY_LABELS)


def list_fusion_status_labels() -> List[str]:
    return list(STATUS_LABELS)


def list_fusion_join_policy_labels() -> List[str]:
    return list(JOIN_POLICY_LABELS)


def validate_fusion_feature_domain_label(label: str) -> bool:
    if label not in DOMAIN_LABELS:
        raise ValueError(f"Geçersiz fusion feature domain etiketi: {label}")
    return True


def validate_fusion_family_label(label: str) -> bool:
    if label not in FAMILY_LABELS:
        raise ValueError(f"Geçersiz fusion family etiketi: {label}")
    return True


def validate_fusion_status_label(label: str) -> bool:
    if label not in STATUS_LABELS:
        raise ValueError(f"Geçersiz fusion status etiketi: {label}")
    return True


def validate_fusion_join_policy_label(label: str) -> bool:
    if label not in JOIN_POLICY_LABELS:
        raise ValueError(f"Geçersiz fusion join policy etiketi: {label}")
    return True
