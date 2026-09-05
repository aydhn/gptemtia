def list_completion_domain_labels() -> list[str]:
    return [
        "closure_synthesis_domain", "end_state_certification_domain",
        "project_freeze_domain", "acceptance_evidence_domain",
        "completion_governance_domain", "completion_criteria_domain",
        "completion_evidence_domain", "completion_handoff_domain",
        "completion_boundary_domain", "completion_quality_domain",
        "quality_validation_domain", "unknown_completion_domain"
    ]

def list_completion_status_labels() -> list[str]:
    return [
        "completion_rehearsal_ready", "completion_rehearsal_ready_with_warnings",
        "completion_rehearsal_missing", "completion_rehearsal_blocked_by_safety",
        "completion_rehearsal_needs_manual_review", "completion_rehearsal_unknown"
    ]

def list_certification_rehearsal_labels() -> list[str]:
    return [
        "certification_rehearsal_documented_only", "certification_rehearsal_not_certified",
        "certification_rehearsal_manual_review_required", "certification_rehearsal_blocked_by_boundary",
        "certification_rehearsal_unknown"
    ]

def list_acceptance_rehearsal_labels() -> list[str]:
    return [
        "acceptance_rehearsal_documented_only", "acceptance_rehearsal_not_approved",
        "acceptance_rehearsal_manual_review_required", "acceptance_rehearsal_blocked_by_boundary",
        "acceptance_rehearsal_unknown"
    ]

def list_completion_risk_labels() -> list[str]:
    return [
        "completion_critical_risk", "completion_high_risk",
        "completion_medium_risk", "completion_low_risk",
        "completion_info", "completion_unknown_risk"
    ]

def validate_completion_domain_label(label: str) -> None:
    if label not in list_completion_domain_labels():
        raise ValueError(f"Invalid completion domain label: {label}")

def validate_completion_status(label: str) -> None:
    if label not in list_completion_status_labels():
        raise ValueError(f"Invalid completion status label: {label}")

def validate_certification_rehearsal_label(label: str) -> None:
    if label not in list_certification_rehearsal_labels():
        raise ValueError(f"Invalid certification rehearsal label: {label}")

def validate_acceptance_rehearsal_label(label: str) -> None:
    if label not in list_acceptance_rehearsal_labels():
        raise ValueError(f"Invalid acceptance rehearsal label: {label}")

def validate_completion_risk(label: str) -> None:
    if label not in list_completion_risk_labels():
        raise ValueError(f"Invalid completion risk label: {label}")
