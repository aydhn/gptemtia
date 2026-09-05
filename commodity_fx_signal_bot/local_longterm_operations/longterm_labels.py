"""Long-term labels definition."""

_DOMAIN_LABELS = [
    "longterm_operations_binder_domain",
    "review_calendar_domain",
    "lifecycle_maintenance_domain",
    "maintenance_cadence_domain",
    "retention_review_domain",
    "quality_safety_review_domain",
    "incident_redteam_governance_review_domain",
    "deprecation_rehearsal_domain",
    "migration_readiness_domain",
    "roadmap_governance_domain",
    "feature_intake_domain",
    "change_control_domain",
    "quality_validation_domain",
    "unknown_longterm_domain"
]

_CALENDAR_LABELS = [
    "calendar_rehearsal_available",
    "calendar_rehearsal_partial",
    "calendar_rehearsal_missing",
    "calendar_rehearsal_manual_review",
    "calendar_rehearsal_unknown"
]

_LIFECYCLE_LABELS = [
    "lifecycle_rehearsal_ready",
    "lifecycle_rehearsal_ready_with_warnings",
    "lifecycle_rehearsal_missing",
    "lifecycle_rehearsal_blocked_by_safety",
    "lifecycle_rehearsal_needs_manual_review",
    "lifecycle_rehearsal_unknown"
]

_DEPRECATION_LABELS = [
    "deprecation_rehearsal_candidate",
    "deprecation_rehearsal_not_candidate",
    "deprecation_rehearsal_blocked",
    "deprecation_rehearsal_manual_review",
    "deprecation_rehearsal_unknown"
]

_RISK_LABELS = [
    "lifecycle_critical_risk",
    "lifecycle_high_risk",
    "lifecycle_medium_risk",
    "lifecycle_low_risk",
    "lifecycle_info",
    "lifecycle_unknown_risk"
]

def list_longterm_domain_labels() -> list[str]:
    return _DOMAIN_LABELS

def list_calendar_status_labels() -> list[str]:
    return _CALENDAR_LABELS

def list_lifecycle_status_labels() -> list[str]:
    return _LIFECYCLE_LABELS

def list_deprecation_status_labels() -> list[str]:
    return _DEPRECATION_LABELS

def list_lifecycle_risk_labels() -> list[str]:
    return _RISK_LABELS

def validate_longterm_domain_label(label: str) -> None:
    if label not in _DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_calendar_status(label: str) -> None:
    if label not in _CALENDAR_LABELS:
        raise ValueError(f"Invalid calendar status label: {label}")

def validate_lifecycle_status(label: str) -> None:
    if label not in _LIFECYCLE_LABELS:
        raise ValueError(f"Invalid lifecycle status label: {label}")

def validate_deprecation_status(label: str) -> None:
    if label not in _DEPRECATION_LABELS:
        raise ValueError(f"Invalid deprecation status label: {label}")

def validate_lifecycle_risk(label: str) -> None:
    if label not in _RISK_LABELS:
        raise ValueError(f"Invalid lifecycle risk label: {label}")
