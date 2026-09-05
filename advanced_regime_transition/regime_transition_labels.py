"""Phase 130: Regime Transition and Stability Analysis Labels.

Defines standardized domain, status, and severity labels for Phase 130
Regime Transition and Stability Analysis.
"""

from typing import List

REGIME_TRANSITION_DOMAIN_LABELS: List[str] = [
    "regime_transition_profile_domain",
    "regime_transition_domain",
    "state_sequence_contract_domain",
    "candidate_sequence_schema_domain",
    "pseudo_sequence_schema_domain",
    "transition_metric_domain",
    "stability_metric_domain",
    "transition_threshold_domain",
    "timestamp_policy_domain",
    "no_lookahead_guard_domain",
    "source_phase_domain",
    "persistence_diagnostics_domain",
    "transition_frequency_domain",
    "transition_matrix_placeholder_domain",
    "transition_ambiguity_domain",
    "transition_continuity_domain",
    "transition_stability_domain",
    "volatility_transition_domain",
    "trend_transition_domain",
    "range_transition_domain",
    "macro_event_transition_domain",
    "news_metadata_transition_domain",
    "cross_asset_transition_prep_domain",
    "quality_dependency_domain",
    "validation_dependency_domain",
    "transition_finding_domain",
    "manual_review_domain",
    "transition_score_domain",
    "transition_manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_131_handoff_domain",
    "unknown_transition_domain",
]

REGIME_TRANSITION_STATUS_LABELS: List[str] = [
    "transition_ready",
    "transition_ready_with_warnings",
    "transition_placeholder_only",
    "transition_manual_review_required",
    "transition_blocked_by_safety",
    "transition_unknown",
]

REGIME_TRANSITION_SEVERITY_LABELS: List[str] = [
    "transition_critical",
    "transition_high",
    "transition_medium",
    "transition_low",
    "transition_info",
]


def list_regime_transition_domain_labels() -> List[str]:
    """Return all valid domain labels."""
    return list(REGIME_TRANSITION_DOMAIN_LABELS)


def list_regime_transition_status_labels() -> List[str]:
    """Return all valid status labels."""
    return list(REGIME_TRANSITION_STATUS_LABELS)


def list_regime_transition_severity_labels() -> List[str]:
    """Return all valid severity labels."""
    return list(REGIME_TRANSITION_SEVERITY_LABELS)


def validate_regime_transition_domain_label(label: str) -> bool:
    """Check if domain label is valid."""
    if label not in REGIME_TRANSITION_DOMAIN_LABELS:
        raise ValueError(
            f"Invalid regime transition domain label: {label}. "
            f"Valid labels: {REGIME_TRANSITION_DOMAIN_LABELS}"
        )
    return True


def validate_regime_transition_status_label(label: str) -> bool:
    """Check if status label is valid."""
    if label not in REGIME_TRANSITION_STATUS_LABELS:
        raise ValueError(
            f"Invalid regime transition status label: {label}. "
            f"Valid labels: {REGIME_TRANSITION_STATUS_LABELS}"
        )
    return True


def validate_regime_transition_severity_label(label: str) -> bool:
    """Check if severity label is valid."""
    if label not in REGIME_TRANSITION_SEVERITY_LABELS:
        raise ValueError(
            f"Invalid regime transition severity label: {label}. "
            f"Valid labels: {REGIME_TRANSITION_SEVERITY_LABELS}"
        )
    return True
