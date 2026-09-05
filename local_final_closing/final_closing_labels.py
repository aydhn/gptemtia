def list_final_closing_domain_labels() -> list[str]:
    return [
        "final_master_terminal_lock_domain",
        "project_constitution_domain",
        "non_production_seal_domain",
        "terminal_archive_index_domain",
        "closing_governance_super_binder_domain",
        "closing_evidence_domain",
        "closing_issue_domain",
        "closing_checklist_domain",
        "closing_boundary_domain",
        "closing_quality_domain",
        "quality_validation_domain",
        "unknown_final_closing_domain"
    ]

def list_final_closing_status_labels() -> list[str]:
    return [
        "final_closing_rehearsal_ready",
        "final_closing_rehearsal_ready_with_warnings",
        "final_closing_rehearsal_missing",
        "final_closing_rehearsal_blocked_by_safety",
        "final_closing_rehearsal_needs_manual_review",
        "final_closing_rehearsal_unknown"
    ]

def list_project_constitution_labels() -> list[str]:
    return [
        "project_constitution_documented_only",
        "project_constitution_not_official",
        "project_constitution_manual_review_required",
        "project_constitution_blocked_by_boundary",
        "project_constitution_unknown"
    ]

def list_non_production_seal_labels() -> list[str]:
    return [
        "non_production_seal_documented_only",
        "non_production_seal_not_official",
        "non_production_seal_manual_review_required",
        "non_production_seal_blocked_by_boundary",
        "non_production_seal_unknown"
    ]

def list_final_closeout_risk_labels() -> list[str]:
    return [
        "final_closeout_critical_risk",
        "final_closeout_high_risk",
        "final_closeout_medium_risk",
        "final_closeout_low_risk",
        "final_closeout_info",
        "final_closeout_unknown_risk"
    ]

def validate_final_closing_domain_label(label: str) -> None:
    if label not in list_final_closing_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_final_closing_status(label: str) -> None:
    if label not in list_final_closing_status_labels():
        raise ValueError(f"Invalid status label: {label}")

def validate_project_constitution_label(label: str) -> None:
    if label not in list_project_constitution_labels():
        raise ValueError(f"Invalid constitution label: {label}")

def validate_non_production_seal_label(label: str) -> None:
    if label not in list_non_production_seal_labels():
        raise ValueError(f"Invalid seal label: {label}")

def validate_final_closeout_risk(label: str) -> None:
    if label not in list_final_closeout_risk_labels():
        raise ValueError(f"Invalid risk label: {label}")
