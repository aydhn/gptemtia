ACCEPTANCE_DOMAIN_LABELS = [
    "final_acceptance_domain",
    "reviewer_pack_domain",
    "evidence_trail_domain",
    "signoff_rehearsal_domain",
    "verification_rehearsal_domain",
    "criteria_domain",
    "exception_domain",
    "no_go_safe_go_domain",
    "quality_validation_domain",
    "unknown_acceptance_domain"
]

ACCEPTANCE_STATUS_LABELS = [
    "acceptance_ready_for_rehearsal",
    "acceptance_ready_with_warnings",
    "acceptance_missing",
    "acceptance_blocked_by_safety",
    "acceptance_needs_manual_review",
    "acceptance_unknown"
]

EVIDENCE_TRACE_LABELS = [
    "evidence_trace_available",
    "evidence_trace_partial",
    "evidence_trace_missing",
    "evidence_trace_not_applicable",
    "evidence_trace_blocked_by_safety",
    "evidence_trace_unknown"
]

REVIEWER_RESPONSE_LABELS = [
    "reviewer_response_ready",
    "reviewer_response_needs_evidence",
    "reviewer_response_needs_manual_review",
    "reviewer_response_blocked_by_safety",
    "reviewer_response_unknown"
]

ACCEPTANCE_RISK_LABELS = [
    "acceptance_critical_risk",
    "acceptance_high_risk",
    "acceptance_medium_risk",
    "acceptance_low_risk",
    "acceptance_info",
    "acceptance_unknown_risk"
]

def list_acceptance_domain_labels() -> list[str]:
    return ACCEPTANCE_DOMAIN_LABELS

def list_acceptance_status_labels() -> list[str]:
    return ACCEPTANCE_STATUS_LABELS

def list_evidence_trace_labels() -> list[str]:
    return EVIDENCE_TRACE_LABELS

def list_reviewer_response_labels() -> list[str]:
    return REVIEWER_RESPONSE_LABELS

def list_acceptance_risk_labels() -> list[str]:
    return ACCEPTANCE_RISK_LABELS

def validate_acceptance_domain_label(label: str) -> None:
    if label not in ACCEPTANCE_DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_acceptance_status(label: str) -> None:
    if label not in ACCEPTANCE_STATUS_LABELS:
        raise ValueError(f"Invalid status label: {label}")

def validate_evidence_trace_label(label: str) -> None:
    if label not in EVIDENCE_TRACE_LABELS:
        raise ValueError(f"Invalid evidence trace label: {label}")

def validate_reviewer_response_label(label: str) -> None:
    if label not in REVIEWER_RESPONSE_LABELS:
        raise ValueError(f"Invalid reviewer response label: {label}")

def validate_acceptance_risk(label: str) -> None:
    if label not in ACCEPTANCE_RISK_LABELS:
        raise ValueError(f"Invalid risk label: {label}")
