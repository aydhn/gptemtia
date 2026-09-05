"""Labels and taxonomies for Phase 121 Feature Validation Layer.

Defines standard labels for validation domains, severity, status, and families.
Strictly non-signal and research-only.
"""

from typing import List

FEATURE_VALIDATION_DOMAIN_LABELS: List[str] = [
    "feature_validation_profile_domain",
    "feature_validation_domain",
    "validation_rule_domain",
    "forbidden_column_domain",
    "no_lookahead_domain",
    "timestamp_order_domain",
    "asof_join_domain",
    "macro_release_lag_domain",
    "event_window_domain",
    "news_metadata_only_domain",
    "warmup_nan_domain",
    "duplicate_feature_domain",
    "namespace_collision_domain",
    "numeric_sanity_domain",
    "missingness_domain",
    "infinite_value_domain",
    "matrix_integrity_domain",
    "validation_finding_domain",
    "manual_review_domain",
    "validation_scoring_domain",
    "indicator_output_validation_domain",
    "feature_grid_validation_domain",
    "cross_asset_alignment_validation_domain",
    "fusion_feature_validation_domain",
    "no_leakage_guard_domain",
    "non_signal_validation_domain",
    "feature_validation_health_domain",
    "feature_validation_safety_domain",
    "phase_122_handoff_domain",
    "unknown_feature_validation_domain",
]

VALIDATION_SEVERITY_LABELS: List[str] = [
    "validation_critical",
    "validation_high",
    "validation_medium",
    "validation_low",
    "validation_info",
    "validation_unknown_severity",
]

VALIDATION_STATUS_LABELS: List[str] = [
    "validation_pass",
    "validation_pass_with_warnings",
    "validation_fail",
    "validation_manual_review_required",
    "validation_blocked_by_safety",
    "validation_placeholder_only",
    "validation_unknown",
]

VALIDATION_FAMILY_LABELS: List[str] = [
    "validation_family_no_lookahead",
    "validation_family_forbidden_columns",
    "validation_family_timestamp_order",
    "validation_family_news_metadata_only",
    "validation_family_matrix_integrity",
    "validation_family_numeric_sanity",
    "validation_family_missingness",
    "validation_family_namespace",
    "validation_family_non_signal",
    "validation_family_unknown",
]


def list_feature_validation_domain_labels() -> List[str]:
    """Return all valid feature validation domain labels."""
    return list(FEATURE_VALIDATION_DOMAIN_LABELS)


def list_validation_severity_labels() -> List[str]:
    """Return all valid severity labels."""
    return list(VALIDATION_SEVERITY_LABELS)


def list_validation_status_labels() -> List[str]:
    """Return all valid validation status labels."""
    return list(VALIDATION_STATUS_LABELS)


def list_validation_family_labels() -> List[str]:
    """Return all valid validation family labels."""
    return list(VALIDATION_FAMILY_LABELS)


def validate_feature_validation_domain_label(label: str) -> bool:
    """Validate that label is in FEATURE_VALIDATION_DOMAIN_LABELS."""
    if label not in FEATURE_VALIDATION_DOMAIN_LABELS:
        raise ValueError(
            f"Invalid feature validation domain label '{label}'. "
            f"Allowed: {FEATURE_VALIDATION_DOMAIN_LABELS}"
        )
    return True


def validate_validation_severity_label(label: str) -> bool:
    """Validate that label is in VALIDATION_SEVERITY_LABELS."""
    if label not in VALIDATION_SEVERITY_LABELS:
        raise ValueError(
            f"Invalid validation severity label '{label}'. "
            f"Allowed: {VALIDATION_SEVERITY_LABELS}"
        )
    return True


def validate_validation_status_label(label: str) -> bool:
    """Validate that label is in VALIDATION_STATUS_LABELS."""
    if label not in VALIDATION_STATUS_LABELS:
        raise ValueError(
            f"Invalid validation status label '{label}'. "
            f"Allowed: {VALIDATION_STATUS_LABELS}"
        )
    return True


def validate_validation_family_label(label: str) -> bool:
    """Validate that label is in VALIDATION_FAMILY_LABELS."""
    if label not in VALIDATION_FAMILY_LABELS:
        raise ValueError(
            f"Invalid validation family label '{label}'. "
            f"Allowed: {VALIDATION_FAMILY_LABELS}"
        )
    return True


FEATURE_VALIDATION_LABELS = {
    "phase_name": "Feature Validation and No-Lookahead Guard",
    "current_phase": 121,
    "target_final_phase": 160,
    "next_phase": 122,
    "non_signal": True,
    "dry_run": True,
    "destructive_action_allowed": False,
}


def get_feature_validation_label(key: str, default=None):
    return FEATURE_VALIDATION_LABELS.get(key, default)

