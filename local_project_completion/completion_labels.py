def list_completion_domain_labels() -> list[str]:
    return [
        "system_closure_dossier_domain",
        "terminal_handoff_domain",
        "knowledge_freeze_domain",
        "last_mile_audit_domain",
        "completion_evidence_domain",
        "completion_criteria_domain",
        "final_inventory_domain",
        "final_command_output_map_domain",
        "final_recaps_domain",
        "final_handoff_checklist_domain",
        "terminal_maps_domain",
        "quality_validation_domain",
        "unknown_completion_domain"
    ]

def list_completion_status_labels() -> list[str]:
    return [
        "completion_rehearsal_ready",
        "completion_rehearsal_ready_with_warnings",
        "completion_rehearsal_missing",
        "completion_rehearsal_blocked_by_safety",
        "completion_rehearsal_needs_manual_review",
        "completion_rehearsal_unknown"
    ]

def list_knowledge_freeze_labels() -> list[str]:
    return [
        "knowledge_freeze_rehearsal_available",
        "knowledge_freeze_rehearsal_partial",
        "knowledge_freeze_rehearsal_missing",
        "knowledge_freeze_boundary_warning",
        "knowledge_freeze_unknown"
    ]

def list_audit_status_labels() -> list[str]:
    return [
        "last_mile_audit_pass_rehearsal",
        "last_mile_audit_warn_rehearsal",
        "last_mile_audit_fail_rehearsal",
        "last_mile_audit_blocked_by_safety",
        "last_mile_audit_manual_review",
        "last_mile_audit_unknown"
    ]

def list_completion_risk_labels() -> list[str]:
    return [
        "completion_critical_risk",
        "completion_high_risk",
        "completion_medium_risk",
        "completion_low_risk",
        "completion_info",
        "completion_unknown_risk"
    ]

def validate_completion_domain_label(label: str) -> None:
    if label not in list_completion_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_completion_status(label: str) -> None:
    if label not in list_completion_status_labels():
        raise ValueError(f"Invalid status label: {label}")

def validate_knowledge_freeze_label(label: str) -> None:
    if label not in list_knowledge_freeze_labels():
        raise ValueError(f"Invalid freeze label: {label}")

def validate_audit_status(label: str) -> None:
    if label not in list_audit_status_labels():
        raise ValueError(f"Invalid audit status label: {label}")

def validate_completion_risk(label: str) -> None:
    if label not in list_completion_risk_labels():
        raise ValueError(f"Invalid risk label: {label}")
