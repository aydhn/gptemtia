"""Phase 135: Regime Acceptance Labels and Domain Definitions.

Defines standardized domain identifiers and acceptance status labels for Phase 135.
"""

from typing import List

# Domain labels
REGIME_ACCEPTANCE_PROFILE_DOMAIN = "regime_acceptance_profile_domain"
REGIME_ACCEPTANCE_DOMAIN = "regime_acceptance_domain"
REGIME_BLOCK_INVENTORY_DOMAIN = "regime_block_inventory_domain"
REGIME_BLOCK_DEPENDENCY_DOMAIN = "regime_block_dependency_domain"
REGIME_BLOCK_ACCEPTANCE_GATE_DOMAIN = "regime_block_acceptance_gate_domain"
REGIME_BLOCK_ACCEPTANCE_SCORE_DOMAIN = "regime_block_acceptance_score_domain"
REGIME_BLOCK_MANUAL_REVIEW_DOMAIN = "regime_block_manual_review_domain"
REGIME_BLOCK_SAFETY_BOUNDARY_DOMAIN = "regime_block_safety_boundary_domain"
REGIME_BLOCK_NON_SIGNAL_COMPLIANCE_DOMAIN = "regime_block_non_signal_compliance_domain"
REGIME_BLOCK_NO_LOOKAHEAD_COMPLIANCE_DOMAIN = "regime_block_no_lookahead_compliance_domain"
REGIME_BLOCK_METADATA_ONLY_NEWS_COMPLIANCE_DOMAIN = "regime_block_metadata_only_news_compliance_domain"
REGIME_BLOCK_FORBIDDEN_COLUMN_COMPLIANCE_DOMAIN = "regime_block_forbidden_column_compliance_domain"
REGIME_BLOCK_SOURCE_PRESERVATION_DOMAIN = "regime_block_source_preservation_domain"
REGIME_BLOCK_FEATURESTORE_READINESS_DOMAIN = "regime_block_featurestore_readiness_domain"
REGIME_BLOCK_COMPONENT_ACCEPTANCE_DOMAIN = "regime_block_component_acceptance_domain"
REGIME_BLOCK_DOCUMENTATION_DOMAIN = "regime_block_documentation_domain"
REGIME_BLOCK_SCRIPT_CONTRACT_DOMAIN = "regime_block_script_contract_domain"
REGIME_BLOCK_TEST_CONTRACT_DOMAIN = "regime_block_test_contract_domain"
REGIME_BLOCK_STATUS_DOMAIN = "regime_block_status_domain"
PHASE_126_135_MANIFEST_DOMAIN = "phase_126_135_manifest_domain"
PHASE_136_HANDOFF_DOMAIN = "phase_136_handoff_domain"
UNKNOWN_REGIME_ACCEPTANCE_DOMAIN = "unknown_regime_acceptance_domain"

ALL_REGIME_ACCEPTANCE_DOMAINS: List[str] = [
    REGIME_ACCEPTANCE_PROFILE_DOMAIN,
    REGIME_ACCEPTANCE_DOMAIN,
    REGIME_BLOCK_INVENTORY_DOMAIN,
    REGIME_BLOCK_DEPENDENCY_DOMAIN,
    REGIME_BLOCK_ACCEPTANCE_GATE_DOMAIN,
    REGIME_BLOCK_ACCEPTANCE_SCORE_DOMAIN,
    REGIME_BLOCK_MANUAL_REVIEW_DOMAIN,
    REGIME_BLOCK_SAFETY_BOUNDARY_DOMAIN,
    REGIME_BLOCK_NON_SIGNAL_COMPLIANCE_DOMAIN,
    REGIME_BLOCK_NO_LOOKAHEAD_COMPLIANCE_DOMAIN,
    REGIME_BLOCK_METADATA_ONLY_NEWS_COMPLIANCE_DOMAIN,
    REGIME_BLOCK_FORBIDDEN_COLUMN_COMPLIANCE_DOMAIN,
    REGIME_BLOCK_SOURCE_PRESERVATION_DOMAIN,
    REGIME_BLOCK_FEATURESTORE_READINESS_DOMAIN,
    REGIME_BLOCK_COMPONENT_ACCEPTANCE_DOMAIN,
    REGIME_BLOCK_DOCUMENTATION_DOMAIN,
    REGIME_BLOCK_SCRIPT_CONTRACT_DOMAIN,
    REGIME_BLOCK_TEST_CONTRACT_DOMAIN,
    REGIME_BLOCK_STATUS_DOMAIN,
    PHASE_126_135_MANIFEST_DOMAIN,
    PHASE_136_HANDOFF_DOMAIN,
    UNKNOWN_REGIME_ACCEPTANCE_DOMAIN,
]

# Status labels
ACCEPTANCE_PASS = "acceptance_pass"
ACCEPTANCE_PASS_WITH_WARNINGS = "acceptance_pass_with_warnings"
ACCEPTANCE_MANUAL_REVIEW_REQUIRED = "acceptance_manual_review_required"
ACCEPTANCE_FAIL = "acceptance_fail"
ACCEPTANCE_BLOCKED_BY_SAFETY = "acceptance_blocked_by_safety"
ACCEPTANCE_PLACEHOLDER_ONLY = "acceptance_placeholder_only"
ACCEPTANCE_UNKNOWN = "acceptance_unknown"

ALL_REGIME_ACCEPTANCE_STATUS_LABELS: List[str] = [
    ACCEPTANCE_PASS,
    ACCEPTANCE_PASS_WITH_WARNINGS,
    ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
    ACCEPTANCE_FAIL,
    ACCEPTANCE_BLOCKED_BY_SAFETY,
    ACCEPTANCE_PLACEHOLDER_ONLY,
    ACCEPTANCE_UNKNOWN,
]


def list_regime_acceptance_domain_labels() -> List[str]:
    """List all registered regime acceptance domain labels."""
    return list(ALL_REGIME_ACCEPTANCE_DOMAINS)


def list_regime_acceptance_status_labels() -> List[str]:
    """List all registered regime acceptance status labels."""
    return list(ALL_REGIME_ACCEPTANCE_STATUS_LABELS)


def validate_regime_acceptance_domain_label(label: str) -> bool:
    """Check whether a given domain label is recognized."""
    return label in ALL_REGIME_ACCEPTANCE_DOMAINS


def validate_regime_acceptance_status_label(label: str) -> bool:
    """Check whether a given status label is recognized."""
    return label in ALL_REGIME_ACCEPTANCE_STATUS_LABELS
