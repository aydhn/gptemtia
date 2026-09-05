"""Phase 125: Feature/Factor Acceptance Domain and Status Labels.

Provides canonical domain constants, evaluation status labels, and validation routines.
"""

from typing import List

ACCEPTANCE_DOMAIN_LABELS: List[str] = [
    "feature_factor_acceptance_profile_domain",
    "feature_factor_acceptance_domain",
    "inventory_domain",
    "dependency_domain",
    "acceptance_gate_domain",
    "acceptance_score_domain",
    "manual_review_domain",
    "safety_boundary_domain",
    "non_signal_compliance_domain",
    "no_lookahead_compliance_domain",
    "forbidden_column_compliance_domain",
    "news_metadata_only_compliance_domain",
    "source_preservation_compliance_domain",
    "feature_store_readiness_domain",
    "documentation_contract_domain",
    "script_contract_domain",
    "test_contract_domain",
    "manifest_domain",
    "phase_126_handoff_domain",
    "unknown_acceptance_domain",
]

ACCEPTANCE_STATUS_LABELS: List[str] = [
    "acceptance_pass",
    "acceptance_pass_with_warnings",
    "acceptance_manual_review_required",
    "acceptance_fail",
    "acceptance_blocked_by_safety",
    "acceptance_placeholder_only",
    "acceptance_unknown",
]


def list_acceptance_domain_labels() -> List[str]:
    """Return all valid acceptance domain labels."""
    return list(ACCEPTANCE_DOMAIN_LABELS)


def list_acceptance_status_labels() -> List[str]:
    """Return all valid acceptance status labels."""
    return list(ACCEPTANCE_STATUS_LABELS)


def validate_acceptance_domain_label(label: str) -> bool:
    """Check if domain label is recognized."""
    return label in ACCEPTANCE_DOMAIN_LABELS


def validate_acceptance_status_label(label: str) -> bool:
    """Check if status label is recognized."""
    return label in ACCEPTANCE_STATUS_LABELS
