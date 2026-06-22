from typing import List

_MAINTENANCE_DOMAIN_LABELS = [
    "documentation_maintenance",
    "tests_maintenance",
    "scripts_maintenance",
    "reports_maintenance",
    "datalake_maintenance",
    "security_maintenance",
    "backup_packaging_maintenance",
    "evidence_metadata_graph_timeline_maintenance",
    "consistency_readiness_maintenance",
    "dependency_maintenance",
    "operator_maintenance",
    "unknown_maintenance"
]

_MAINTENANCE_TASK_STATUS_LABELS = [
    "maintenance_current",
    "maintenance_due_soon",
    "maintenance_overdue",
    "maintenance_missing",
    "maintenance_blocked",
    "maintenance_not_applicable",
    "maintenance_unknown"
]

_REFRESH_CADENCE_LABELS = [
    "refresh_daily_manual",
    "refresh_weekly_manual",
    "refresh_monthly_manual",
    "refresh_quarterly_manual",
    "refresh_on_change_manual",
    "refresh_before_handoff_manual",
    "refresh_not_applicable",
    "refresh_unknown"
]

_DEPENDENCY_STATUS_LABELS = [
    "dependency_current",
    "dependency_review_due",
    "dependency_aging_warning",
    "dependency_missing_metadata",
    "dependency_unknown"
]

_SUSTAINABILITY_RISK_LABELS = [
    "sustainability_critical_risk",
    "sustainability_high_risk",
    "sustainability_medium_risk",
    "sustainability_low_risk",
    "sustainability_info",
    "sustainability_unknown_risk"
]

def list_maintenance_domain_labels() -> List[str]:
    return _MAINTENANCE_DOMAIN_LABELS.copy()

def list_maintenance_task_status_labels() -> List[str]:
    return _MAINTENANCE_TASK_STATUS_LABELS.copy()

def list_refresh_cadence_labels() -> List[str]:
    return _REFRESH_CADENCE_LABELS.copy()

def list_dependency_status_labels() -> List[str]:
    return _DEPENDENCY_STATUS_LABELS.copy()

def list_sustainability_risk_labels() -> List[str]:
    return _SUSTAINABILITY_RISK_LABELS.copy()

def validate_maintenance_domain_label(label: str) -> None:
    if label not in _MAINTENANCE_DOMAIN_LABELS:
        raise ValueError(f"Invalid maintenance domain label: {label}")

def validate_maintenance_task_status(label: str) -> None:
    if label not in _MAINTENANCE_TASK_STATUS_LABELS:
        raise ValueError(f"Invalid maintenance task status label: {label}")

def validate_refresh_cadence_label(label: str) -> None:
    if label not in _REFRESH_CADENCE_LABELS:
        raise ValueError(f"Invalid refresh cadence label: {label}")

def validate_dependency_status(label: str) -> None:
    if label not in _DEPENDENCY_STATUS_LABELS:
        raise ValueError(f"Invalid dependency status label: {label}")

def validate_sustainability_risk(label: str) -> None:
    if label not in _SUSTAINABILITY_RISK_LABELS:
        raise ValueError(f"Invalid sustainability risk label: {label}")
