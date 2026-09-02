USABILITY_DOMAIN_LABELS = [
    "usability_review_domain", "friction_map_domain", "task_journey_domain",
    "command_discoverability_domain", "script_index_domain", "reading_order_domain",
    "navigation_assistant_domain", "operator_path_domain", "human_loop_domain",
    "troubleshooting_domain", "quick_reference_domain", "quality_validation_domain",
    "unknown_usability_domain"
]

FRICTION_LABELS = [
    "friction_low", "friction_medium", "friction_high", "friction_very_high", "friction_unknown"
]

OPERATOR_PATH_LABELS = [
    "first_hour_path", "first_day_path", "weekly_review_path",
    "emergency_review_path", "docs_only_path", "quality_only_path",
    "status_only_path", "unknown_operator_path"
]

USABILITY_STATUS_LABELS = [
    "usability_ready_for_rehearsal", "usability_ready_with_warnings",
    "usability_missing", "usability_blocked_by_safety",
    "usability_needs_manual_review", "usability_unknown"
]

USABILITY_RISK_LABELS = [
    "usability_critical_risk", "usability_high_risk", "usability_medium_risk",
    "usability_low_risk", "usability_info", "usability_unknown_risk"
]

def list_usability_domain_labels() -> list[str]:
    return USABILITY_DOMAIN_LABELS

def list_friction_labels() -> list[str]:
    return FRICTION_LABELS

def list_operator_path_labels() -> list[str]:
    return OPERATOR_PATH_LABELS

def list_usability_status_labels() -> list[str]:
    return USABILITY_STATUS_LABELS

def list_usability_risk_labels() -> list[str]:
    return USABILITY_RISK_LABELS

def validate_usability_domain_label(label: str) -> None:
    if label not in USABILITY_DOMAIN_LABELS:
        raise ValueError(f"Invalid usability domain label: {label}")

def validate_friction_label(label: str) -> None:
    if label not in FRICTION_LABELS:
        raise ValueError(f"Invalid friction label: {label}")

def validate_operator_path_label(label: str) -> None:
    if label not in OPERATOR_PATH_LABELS:
        raise ValueError(f"Invalid operator path label: {label}")

def validate_usability_status(label: str) -> None:
    if label not in USABILITY_STATUS_LABELS:
        raise ValueError(f"Invalid usability status: {label}")

def validate_usability_risk(label: str) -> None:
    if label not in USABILITY_RISK_LABELS:
        raise ValueError(f"Invalid usability risk: {label}")
