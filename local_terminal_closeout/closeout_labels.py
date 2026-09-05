class LabelError(Exception):
    pass

_DOMAIN_LABELS = [
    "terminal_master_closeout_domain",
    "ultimate_project_ledger_domain",
    "governance_seal_rehearsal_domain",
    "final_archive_catalog_domain",
    "handover_constitution_domain",
    "terminal_closeout_evidence_domain",
    "terminal_closeout_issue_domain",
    "terminal_closeout_checklist_domain",
    "terminal_closeout_boundary_domain",
    "terminal_closeout_quality_domain",
    "quality_validation_domain",
    "unknown_terminal_closeout_domain"
]

_STATUS_LABELS = [
    "closeout_rehearsal_ready",
    "closeout_rehearsal_ready_with_warnings",
    "closeout_rehearsal_missing",
    "closeout_rehearsal_blocked_by_safety",
    "closeout_rehearsal_needs_manual_review",
    "closeout_rehearsal_unknown"
]

_SEAL_LABELS = [
    "governance_seal_rehearsal_documented_only",
    "governance_seal_not_official",
    "governance_seal_manual_review_required",
    "governance_seal_blocked_by_boundary",
    "governance_seal_unknown"
]

_HANDOVER_LABELS = [
    "handover_constitution_documented_only",
    "handover_constitution_not_official",
    "handover_constitution_manual_review_required",
    "handover_constitution_blocked_by_boundary",
    "handover_constitution_unknown"
]

_RISK_LABELS = [
    "terminal_closeout_critical_risk",
    "terminal_closeout_high_risk",
    "terminal_closeout_medium_risk",
    "terminal_closeout_low_risk",
    "terminal_closeout_info",
    "terminal_closeout_unknown_risk"
]

def list_terminal_closeout_domain_labels() -> list[str]:
    return _DOMAIN_LABELS.copy()

def list_terminal_closeout_status_labels() -> list[str]:
    return _STATUS_LABELS.copy()

def list_governance_seal_labels() -> list[str]:
    return _SEAL_LABELS.copy()

def list_handover_constitution_labels() -> list[str]:
    return _HANDOVER_LABELS.copy()

def list_terminal_closeout_risk_labels() -> list[str]:
    return _RISK_LABELS.copy()

def validate_terminal_closeout_domain_label(label: str) -> None:
    if label not in _DOMAIN_LABELS:
        raise LabelError(f"Invalid domain label: {label}")

def validate_terminal_closeout_status(label: str) -> None:
    if label not in _STATUS_LABELS:
        raise LabelError(f"Invalid status label: {label}")

def validate_governance_seal_label(label: str) -> None:
    if label not in _SEAL_LABELS:
        raise LabelError(f"Invalid seal label: {label}")

def validate_handover_constitution_label(label: str) -> None:
    if label not in _HANDOVER_LABELS:
        raise LabelError(f"Invalid handover label: {label}")

def validate_terminal_closeout_risk(label: str) -> None:
    if label not in _RISK_LABELS:
        raise LabelError(f"Invalid risk label: {label}")
