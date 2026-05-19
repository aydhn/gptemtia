"""
Controlled vocabulary and labels for security audits.
"""

_SECURITY_STATUS_LABELS = [
    "security_passed",
    "security_warning",
    "security_failed",
    "security_critical",
    "security_unknown"
]

_SECURITY_FINDING_SEVERITY_LABELS = [
    "info",
    "low",
    "medium",
    "high",
    "critical",
    "unknown"
]

_SECURITY_CATEGORY_LABELS = [
    "secret_hygiene",
    "config_hardening",
    "safe_defaults",
    "permission_boundary",
    "path_safety",
    "log_redaction",
    "dependency_security",
    "file_permission",
    "token_leakage",
    "readiness",
    "unknown_security_category"
]

_READINESS_LABELS = [
    "ready_for_local_research",
    "ready_for_paper_simulation",
    "ready_for_reporting",
    "not_ready",
    "readiness_warning",
    "unknown_readiness"
]

def list_security_status_labels() -> list[str]:
    return _SECURITY_STATUS_LABELS.copy()

def list_security_finding_severity_labels() -> list[str]:
    return _SECURITY_FINDING_SEVERITY_LABELS.copy()

def list_security_category_labels() -> list[str]:
    return _SECURITY_CATEGORY_LABELS.copy()

def list_readiness_labels() -> list[str]:
    return _READINESS_LABELS.copy()

def validate_security_status(label: str) -> None:
    if label not in _SECURITY_STATUS_LABELS:
        raise ValueError(f"Invalid security status label: {label}")

def validate_security_finding_severity(label: str) -> None:
    if label not in _SECURITY_FINDING_SEVERITY_LABELS:
        raise ValueError(f"Invalid security finding severity label: {label}")

def validate_security_category(label: str) -> None:
    if label not in _SECURITY_CATEGORY_LABELS:
        raise ValueError(f"Invalid security category label: {label}")

def validate_readiness_label(label: str) -> None:
    if label not in _READINESS_LABELS:
        raise ValueError(f"Invalid readiness label: {label}")

def is_blocking_security_status(label: str) -> bool:
    validate_security_status(label)
    return label in ("security_failed", "security_critical")

def is_critical_security_severity(label: str) -> bool:
    validate_security_finding_severity(label)
    return label == "critical"
