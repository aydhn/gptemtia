from typing import List

_AUDIT_TYPE_LABELS = [
    "architecture_audit",
    "safety_audit",
    "integration_audit",
    "command_audit",
    "datalake_audit",
    "report_output_audit",
    "documentation_audit",
    "quality_gate_audit",
    "performance_audit",
    "maintenance_audit",
    "release_readiness_dry_run",
    "consolidation_audit",
    "unknown_audit"
]

_AUDIT_STATUS_LABELS = [
    "audit_passed",
    "audit_passed_with_warnings",
    "audit_failed",
    "audit_blocked",
    "audit_skipped",
    "audit_unknown"
]

_FINAL_READINESS_LABELS = [
    "offline_ready_for_research_use",
    "offline_ready_with_warnings",
    "offline_not_ready",
    "blocked_by_safety_issue",
    "insufficient_review_data",
    "unknown_readiness"
]

_RISK_SEVERITY_LABELS = [
    "critical_risk",
    "high_risk",
    "medium_risk",
    "low_risk",
    "informational_risk",
    "unknown_risk"
]

_GAP_CATEGORY_LABELS = [
    "architecture_gap",
    "safety_gap",
    "documentation_gap",
    "test_gap",
    "data_contract_gap",
    "reporting_gap",
    "performance_gap",
    "maintenance_gap",
    "integration_gap",
    "unknown_gap"
]

def list_audit_type_labels() -> List[str]:
    return _AUDIT_TYPE_LABELS.copy()

def list_audit_status_labels() -> List[str]:
    return _AUDIT_STATUS_LABELS.copy()

def list_final_readiness_labels() -> List[str]:
    return _FINAL_READINESS_LABELS.copy()

def list_risk_severity_labels() -> List[str]:
    return _RISK_SEVERITY_LABELS.copy()

def list_gap_category_labels() -> List[str]:
    return _GAP_CATEGORY_LABELS.copy()

def validate_audit_type(label: str) -> None:
    if label not in _AUDIT_TYPE_LABELS:
        raise ValueError(f"Invalid audit type label: {label}")

def validate_audit_status(label: str) -> None:
    if label not in _AUDIT_STATUS_LABELS:
        raise ValueError(f"Invalid audit status label: {label}")

def validate_final_readiness(label: str) -> None:
    if label not in _FINAL_READINESS_LABELS:
        raise ValueError(f"Invalid final readiness label: {label}")

def validate_risk_severity(label: str) -> None:
    if label not in _RISK_SEVERITY_LABELS:
        raise ValueError(f"Invalid risk severity label: {label}")

def validate_gap_category(label: str) -> None:
    if label not in _GAP_CATEGORY_LABELS:
        raise ValueError(f"Invalid gap category label: {label}")
