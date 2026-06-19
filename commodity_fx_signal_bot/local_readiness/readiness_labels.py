_READINESS_GATE_LABELS = [
    "gate_passed",
    "gate_passed_with_warnings",
    "gate_failed",
    "gate_blocked_by_no_go",
    "gate_skipped",
    "gate_unknown"
]

_READINESS_DOMAIN_LABELS = [
    "docs_readiness",
    "tests_readiness",
    "scripts_readiness",
    "reports_readiness",
    "datalake_readiness",
    "security_readiness",
    "backup_packaging_readiness",
    "metadata_evidence_graph_timeline_readiness",
    "consistency_readiness",
    "operator_readiness",
    "handoff_readiness",
    "unknown_readiness"
]

_GO_NO_GO_LABELS = [
    "safe_go_condition",
    "caution_go_condition",
    "no_go_condition",
    "manual_review_required",
    "unknown_go_condition"
]

_CHECKLIST_STATUS_LABELS = [
    "checklist_done",
    "checklist_warning",
    "checklist_missing",
    "checklist_blocked",
    "checklist_not_applicable",
    "checklist_unknown"
]

_RISK_LEVEL_LABELS = [
    "readiness_critical_risk",
    "readiness_high_risk",
    "readiness_medium_risk",
    "readiness_low_risk",
    "readiness_info",
    "readiness_unknown_risk"
]

def list_readiness_gate_labels() -> list[str]:
    return list(_READINESS_GATE_LABELS)

def list_readiness_domain_labels() -> list[str]:
    return list(_READINESS_DOMAIN_LABELS)

def list_go_no_go_labels() -> list[str]:
    return list(_GO_NO_GO_LABELS)

def list_checklist_status_labels() -> list[str]:
    return list(_CHECKLIST_STATUS_LABELS)

def list_risk_level_labels() -> list[str]:
    return list(_RISK_LEVEL_LABELS)

def validate_readiness_gate_label(label: str) -> None:
    if label not in _READINESS_GATE_LABELS:
        raise ValueError(f"Invalid readiness gate label: {label}")

def validate_readiness_domain_label(label: str) -> None:
    if label not in _READINESS_DOMAIN_LABELS:
        raise ValueError(f"Invalid readiness domain label: {label}")

def validate_go_no_go_label(label: str) -> None:
    if label not in _GO_NO_GO_LABELS:
        raise ValueError(f"Invalid go/no-go label: {label}")

def validate_checklist_status_label(label: str) -> None:
    if label not in _CHECKLIST_STATUS_LABELS:
        raise ValueError(f"Invalid checklist status label: {label}")

def validate_risk_level_label(label: str) -> None:
    if label not in _RISK_LEVEL_LABELS:
        raise ValueError(f"Invalid risk level label: {label}")
