def list_governance_domain_labels() -> list[str]:
    return [
        "governance_control_room_domain",
        "executive_oversight_domain",
        "manual_approval_domain",
        "risk_committee_rehearsal_domain",
        "operator_supervision_domain",
        "escalation_domain",
        "governance_roles_domain",
        "decision_authority_domain",
        "approval_boundary_domain",
        "oversight_evidence_domain",
        "governance_metrics_domain",
        "governance_template_domain",
        "quality_validation_domain",
        "unknown_governance_domain"
    ]

def list_approval_status_labels() -> list[str]:
    return [
        "approval_rehearsal_pending",
        "approval_rehearsal_reviewed",
        "approval_rehearsal_rejected",
        "approval_rehearsal_blocked_by_safety",
        "approval_rehearsal_not_applicable",
        "approval_rehearsal_unknown"
    ]

def list_governance_status_labels() -> list[str]:
    return [
        "governance_ready_for_rehearsal",
        "governance_ready_with_warnings",
        "governance_missing",
        "governance_blocked_by_safety",
        "governance_needs_manual_review",
        "governance_unknown"
    ]

def list_escalation_labels() -> list[str]:
    return [
        "escalation_info",
        "escalation_manual_review",
        "escalation_risk_committee_rehearsal",
        "escalation_blocked_by_no_go",
        "escalation_external_approval_not_allowed",
        "escalation_unknown"
    ]

def list_governance_risk_labels() -> list[str]:
    return [
        "governance_critical_risk",
        "governance_high_risk",
        "governance_medium_risk",
        "governance_low_risk",
        "governance_info",
        "governance_unknown_risk"
    ]

def validate_governance_domain_label(label: str) -> None:
    if label not in list_governance_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_approval_status(label: str) -> None:
    if label not in list_approval_status_labels():
        raise ValueError(f"Invalid approval status: {label}")

def validate_governance_status(label: str) -> None:
    if label not in list_governance_status_labels():
        raise ValueError(f"Invalid governance status: {label}")

def validate_escalation_label(label: str) -> None:
    if label not in list_escalation_labels():
        raise ValueError(f"Invalid escalation label: {label}")

def validate_governance_risk(label: str) -> None:
    if label not in list_governance_risk_labels():
        raise ValueError(f"Invalid risk label: {label}")
