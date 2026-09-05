def list_preservation_domain_labels() -> list[str]:
    return [
        "archive_seal_rehearsal_domain", "immutable_readme_domain", "evidence_vault_domain",
        "knowledge_capsule_domain", "preservation_binder_domain", "preservation_inventory_domain",
        "preservation_fingerprint_domain", "restore_notes_domain", "preservation_access_domain",
        "preservation_handoff_domain", "quality_validation_domain", "unknown_preservation_domain"
    ]

def list_preservation_status_labels() -> list[str]:
    return [
        "preservation_rehearsal_ready", "preservation_rehearsal_ready_with_warnings",
        "preservation_rehearsal_missing", "preservation_rehearsal_blocked_by_safety",
        "preservation_rehearsal_needs_manual_review", "preservation_rehearsal_unknown"
    ]

def list_archive_seal_status_labels() -> list[str]:
    return [
        "archive_seal_rehearsal_available", "archive_seal_rehearsal_partial",
        "archive_seal_rehearsal_missing", "archive_seal_boundary_warning", "archive_seal_unknown"
    ]

def list_evidence_vault_status_labels() -> list[str]:
    return [
        "evidence_vault_indexed_rehearsal", "evidence_vault_partial_rehearsal",
        "evidence_vault_missing_rehearsal", "evidence_vault_manual_review", "evidence_vault_unknown"
    ]

def list_preservation_risk_labels() -> list[str]:
    return [
        "preservation_critical_risk", "preservation_high_risk", "preservation_medium_risk",
        "preservation_low_risk", "preservation_info", "preservation_unknown_risk"
    ]

def validate_preservation_domain_label(label: str) -> None:
    if label not in list_preservation_domain_labels(): raise ValueError()
def validate_preservation_status(label: str) -> None:
    if label not in list_preservation_status_labels(): raise ValueError()
def validate_archive_seal_status(label: str) -> None:
    if label not in list_archive_seal_status_labels(): raise ValueError()
def validate_evidence_vault_status(label: str) -> None:
    if label not in list_evidence_vault_status_labels(): raise ValueError()
def validate_preservation_risk(label: str) -> None:
    if label not in list_preservation_risk_labels(): raise ValueError()
