from typing import List


DOMAIN_LABELS: List[str] = [
    "cross_asset_alignment_profile_domain",
    "cross_asset_alignment_domain",
    "asset_universe_domain",
    "symbol_mapping_domain",
    "feature_namespace_domain",
    "timestamp_alignment_domain",
    "session_calendar_alignment_domain",
    "feature_matrix_contract_domain",
    "join_policy_domain",
    "asof_join_policy_domain",
    "no_lookahead_alignment_domain",
    "cross_asset_metadata_domain",
    "fx_commodity_alignment_domain",
    "fx_macro_alignment_domain",
    "fx_calendar_alignment_domain",
    "fx_news_alignment_domain",
    "commodity_macro_alignment_domain",
    "commodity_calendar_alignment_domain",
    "commodity_news_alignment_domain",
    "macro_calendar_alignment_domain",
    "calendar_news_alignment_domain",
    "cross_domain_feature_matrix_domain",
    "aligned_feature_matrix_manifest_domain",
    "alignment_validation_domain",
    "alignment_quality_handoff_domain",
    "cross_asset_health_domain",
    "cross_asset_safety_domain",
    "phase_120_handoff_domain",
    "unknown_cross_asset_alignment_domain",
]

ALIGNMENT_FAMILY_LABELS: List[str] = [
    "alignment_family_fx_commodity",
    "alignment_family_fx_macro",
    "alignment_family_fx_calendar",
    "alignment_family_fx_news",
    "alignment_family_commodity_macro",
    "alignment_family_commodity_calendar",
    "alignment_family_commodity_news",
    "alignment_family_macro_calendar",
    "alignment_family_calendar_news",
    "alignment_family_cross_domain",
    "alignment_family_unknown",
]

ALIGNMENT_STATUS_LABELS: List[str] = [
    "alignment_ready",
    "alignment_pending",
    "alignment_ready_with_warnings",
    "alignment_placeholder_only",
    "alignment_manual_review_required",
    "alignment_blocked_by_safety",
    "alignment_unknown",
]

JOIN_POLICY_LABELS: List[str] = [
    "join_policy_exact_timestamp",
    "join_policy_asof_backward",
    "join_policy_asof_nearest_disabled",
    "join_policy_session_bucket",
    "join_policy_event_window_placeholder",
    "join_policy_metadata_tag_link",
    "join_policy_manual_review_only",
]


ALIGNMENT_DOMAINS: List[str] = [
    "fx",
    "commodity",
    "macro",
    "calendar",
    "news",
]

ALIGNMENT_FAMILIES: List[str] = [
    "price_technical",
    "macro_interest_rate",
    "calendar_scheduled_event",
    "news_metadata_sentiment",
]

JOIN_POLICIES: List[str] = JOIN_POLICY_LABELS


def list_cross_asset_alignment_domain_labels() -> List[str]:
    return list(DOMAIN_LABELS)


def list_alignment_family_labels() -> List[str]:
    return list(ALIGNMENT_FAMILY_LABELS)


def list_alignment_status_labels() -> List[str]:
    return list(ALIGNMENT_STATUS_LABELS)


def list_join_policy_labels() -> List[str]:
    return list(JOIN_POLICY_LABELS)


def validate_alignment_domain(domain: str) -> bool:
    d = domain.lower()
    return d in ALIGNMENT_DOMAINS or d in DOMAIN_LABELS


def validate_alignment_family(family: str) -> bool:
    f = family.lower()
    return f in ALIGNMENT_FAMILIES or f in ALIGNMENT_FAMILY_LABELS


def validate_join_policy(policy: str) -> bool:
    p = policy.lower()
    if "forward" in p or "nearest" in p:
        return False
    return policy in JOIN_POLICY_LABELS or policy in JOIN_POLICIES


def validate_cross_asset_alignment_domain_label(label: str) -> bool:
    return validate_alignment_domain(label)


def validate_alignment_family_label(label: str) -> bool:
    return validate_alignment_family(label)


def validate_alignment_status_label(label: str) -> bool:
    return label in ALIGNMENT_STATUS_LABELS


def validate_join_policy_label(label: str) -> bool:
    return validate_join_policy(label)

