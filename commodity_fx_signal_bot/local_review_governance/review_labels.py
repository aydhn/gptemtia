
_REVIEW_DOMAIN_LABELS = [
    "human_review_cockpit_domain",
    "manual_approval_ledger_domain",
    "expert_review_workbook_domain",
    "reviewer_console_domain",
    "review_governance_binder_domain",
    "review_criteria_domain",
    "review_evidence_domain",
    "review_issue_domain",
    "review_escalation_domain",
    "review_boundary_domain",
    "quality_validation_domain",
    "unknown_review_domain"
]

_REVIEW_STATUS_LABELS = [
    "review_rehearsal_ready",
    "review_rehearsal_ready_with_warnings",
    "review_rehearsal_missing",
    "review_rehearsal_blocked_by_safety",
    "review_rehearsal_needs_manual_review",
    "review_rehearsal_unknown"
]

_APPROVAL_STATUS_LABELS = [
    "approval_rehearsal_not_requested",
    "approval_rehearsal_manual_review_required",
    "approval_rehearsal_blocked_by_boundary",
    "approval_rehearsal_documented_only",
    "approval_rehearsal_unknown"
]

_REVIEWER_ROLE_LABELS = [
    "reviewer_operator",
    "reviewer_analyst",
    "reviewer_maintainer",
    "reviewer_codex_agent",
    "reviewer_external_expert_rehearsal",
    "reviewer_unknown"
]

_REVIEW_RISK_LABELS = [
    "review_critical_risk",
    "review_high_risk",
    "review_medium_risk",
    "review_low_risk",
    "review_info",
    "review_unknown_risk"
]

def list_review_domain_labels() -> list[str]:
    return _REVIEW_DOMAIN_LABELS.copy()

def list_review_status_labels() -> list[str]:
    return _REVIEW_STATUS_LABELS.copy()

def list_approval_status_labels() -> list[str]:
    return _APPROVAL_STATUS_LABELS.copy()

def list_reviewer_role_labels() -> list[str]:
    return _REVIEWER_ROLE_LABELS.copy()

def list_review_risk_labels() -> list[str]:
    return _REVIEW_RISK_LABELS.copy()

def validate_review_domain_label(label: str) -> None:
    if label not in _REVIEW_DOMAIN_LABELS:
        raise ValueError(f"Invalid review domain label: {label}")

def validate_review_status(label: str) -> None:
    if label not in _REVIEW_STATUS_LABELS:
        raise ValueError(f"Invalid review status: {label}")

def validate_approval_status(label: str) -> None:
    if label not in _APPROVAL_STATUS_LABELS:
        raise ValueError(f"Invalid approval status: {label}")

def validate_reviewer_role(label: str) -> None:
    if label not in _REVIEWER_ROLE_LABELS:
        raise ValueError(f"Invalid reviewer role: {label}")

def validate_review_risk(label: str) -> None:
    if label not in _REVIEW_RISK_LABELS:
        raise ValueError(f"Invalid review risk label: {label}")
