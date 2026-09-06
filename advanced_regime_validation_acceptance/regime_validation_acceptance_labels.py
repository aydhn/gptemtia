"""Phase 133: Regime Validation Acceptance Labels and Domains.

Defines standard domains, statuses, severities, and validation functions.
"""

from typing import List, Set

REGIME_VALIDATION_ACCEPTANCE_DOMAINS: Set[str] = {
    "regime_validation_acceptance_profile_domain",
    "regime_validation_acceptance_domain",
    "validation_gate_domain",
    "no_lookahead_acceptance_domain",
    "timestamp_order_acceptance_domain",
    "backward_asof_acceptance_domain",
    "forbidden_column_acceptance_domain",
    "metadata_only_news_acceptance_domain",
    "source_preservation_acceptance_domain",
    "non_signal_acceptance_domain",
    "target_label_prediction_absence_domain",
    "model_execution_absence_domain",
    "matrix_validation_acceptance_domain",
    "candidate_state_validation_acceptance_domain",
    "pseudo_state_validation_acceptance_domain",
    "transition_validation_acceptance_domain",
    "cross_asset_validation_acceptance_domain",
    "macro_event_news_validation_acceptance_domain",
    "validation_dependency_acceptance_domain",
    "quality_dependency_acceptance_domain",
    "validation_finding_domain",
    "manual_review_domain",
    "acceptance_score_domain",
    "acceptance_manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_134_handoff_domain",
    "unknown_regime_validation_acceptance_domain",
}

REGIME_VALIDATION_ACCEPTANCE_STATUSES: Set[str] = {
    "acceptance_pass",
    "acceptance_pass_with_warnings",
    "acceptance_manual_review_required",
    "acceptance_fail",
    "acceptance_blocked_by_safety",
    "acceptance_placeholder_only",
    "acceptance_unknown",
}

REGIME_VALIDATION_ACCEPTANCE_SEVERITIES: Set[str] = {
    "acceptance_critical",
    "acceptance_high",
    "acceptance_medium",
    "acceptance_low",
    "acceptance_info",
}


def list_regime_validation_acceptance_domain_labels() -> List[str]:
    """List all registered validation acceptance domain labels in sorted order."""
    return sorted(list(REGIME_VALIDATION_ACCEPTANCE_DOMAINS))


def list_regime_validation_acceptance_status_labels() -> List[str]:
    """List all registered validation acceptance status labels in sorted order."""
    return sorted(list(REGIME_VALIDATION_ACCEPTANCE_STATUSES))


def list_regime_validation_acceptance_severity_labels() -> List[str]:
    """List all registered validation acceptance severity labels in sorted order."""
    return sorted(list(REGIME_VALIDATION_ACCEPTANCE_SEVERITIES))


def validate_regime_validation_acceptance_domain_label(label: str) -> bool:
    """Check whether domain label is valid."""
    return label in REGIME_VALIDATION_ACCEPTANCE_DOMAINS


def validate_regime_validation_acceptance_status_label(label: str) -> bool:
    """Check whether status label is valid."""
    return label in REGIME_VALIDATION_ACCEPTANCE_STATUSES


def validate_regime_validation_acceptance_severity_label(label: str) -> bool:
    """Check whether severity label is valid."""
    return label in REGIME_VALIDATION_ACCEPTANCE_SEVERITIES
