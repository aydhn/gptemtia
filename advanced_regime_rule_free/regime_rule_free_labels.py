"""Phase 128: Regime Rule-Free Labeling Contracts and Unsupervised Prep Labels.

Defines canonical domain, status, and candidate state taxonomy labels for Phase 128.
"""

from typing import List

REGIME_RULE_FREE_DOMAIN_LABELS = [
    "regime_rule_free_profile_domain",
    "regime_rule_free_domain",
    "rule_free_labeling_contract_domain",
    "candidate_state_assignment_policy_domain",
    "candidate_state_schema_domain",
    "pseudo_state_schema_domain",
    "unsupervised_prep_contract_domain",
    "clustering_input_contract_domain",
    "clustering_algorithm_placeholder_domain",
    "distance_metric_placeholder_domain",
    "normalization_prep_contract_domain",
    "scaling_prep_contract_domain",
    "dimensionality_reduction_placeholder_domain",
    "candidate_feature_set_domain",
    "candidate_state_context_domain",
    "candidate_state_metadata_domain",
    "candidate_state_namespace_domain",
    "candidate_state_integrity_domain",
    "no_lookahead_guard_domain",
    "timestamp_policy_domain",
    "quality_dependency_domain",
    "validation_dependency_domain",
    "manual_review_domain",
    "non_signal_policy_domain",
    "forbidden_claim_domain",
    "source_preservation_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_129_handoff_domain",
    "unknown_rule_free_domain",
]

REGIME_RULE_FREE_STATUS_LABELS = [
    "rule_free_ready",
    "rule_free_ready_with_warnings",
    "rule_free_placeholder_only",
    "rule_free_manual_review_required",
    "rule_free_blocked_by_safety",
    "rule_free_unknown",
]

CANDIDATE_STATE_LABELS = [
    "candidate_state_volatility_context",
    "candidate_state_trend_context",
    "candidate_state_range_context",
    "candidate_state_macro_event_context",
    "candidate_state_news_attention_context",
    "candidate_state_cross_asset_context",
    "candidate_state_transition_context",
    "candidate_state_uncertain_context",
    "candidate_state_unknown",
]


def list_regime_rule_free_domain_labels() -> List[str]:
    """Return all valid Phase 128 domain labels."""
    return list(REGIME_RULE_FREE_DOMAIN_LABELS)


def list_regime_rule_free_status_labels() -> List[str]:
    """Return all valid Phase 128 status labels."""
    return list(REGIME_RULE_FREE_STATUS_LABELS)


def list_candidate_state_labels() -> List[str]:
    """Return all valid candidate state context labels."""
    return list(CANDIDATE_STATE_LABELS)


def validate_regime_rule_free_domain_label(label: str) -> bool:
    """Validate if a string is a recognized domain label."""
    return label in REGIME_RULE_FREE_DOMAIN_LABELS


def validate_regime_rule_free_status_label(label: str) -> bool:
    """Validate if a string is a recognized status label."""
    return label in REGIME_RULE_FREE_STATUS_LABELS


def validate_candidate_state_label(label: str) -> bool:
    """Validate if a string is a recognized candidate state label."""
    return label in CANDIDATE_STATE_LABELS
