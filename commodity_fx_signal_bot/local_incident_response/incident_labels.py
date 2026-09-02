from typing import List

INCIDENT_DOMAIN_LABELS = [
    "incident_rehearsal_domain", "safety_event_domain", "incident_taxonomy_domain",
    "incident_triage_domain", "incident_classification_domain", "rollback_rehearsal_domain",
    "containment_rehearsal_domain", "degraded_mode_domain", "recovery_rehearsal_domain",
    "resilience_supervision_domain", "post_incident_review_domain", "corrective_action_domain",
    "escalation_domain", "quality_validation_domain", "unknown_incident_domain"
]

SAFETY_EVENT_CATEGORY_LABELS = [
    "event_boundary_breach", "event_unsafe_output", "event_forbidden_capability_request",
    "event_secret_exposure", "event_file_action_request", "event_cloud_publish_request",
    "event_live_trading_broker_request", "event_investment_advice_request",
    "event_model_deployment_request", "event_external_llm_api_request",
    "event_quality_warning", "event_unknown"
]

SEVERITY_LABELS = [
    "severity_info", "severity_low", "severity_medium", "severity_high", "severity_critical", "severity_unknown"
]

INCIDENT_STATUS_LABELS = [
    "incident_ready_for_rehearsal", "incident_ready_with_warnings", "incident_missing",
    "incident_blocked_by_safety", "incident_needs_manual_review", "incident_unknown"
]

INCIDENT_RISK_LABELS = [
    "incident_critical_risk", "incident_high_risk", "incident_medium_risk",
    "incident_low_risk", "incident_info", "incident_unknown_risk"
]

def list_incident_domain_labels() -> List[str]:
    return INCIDENT_DOMAIN_LABELS

def list_safety_event_category_labels() -> List[str]:
    return SAFETY_EVENT_CATEGORY_LABELS

def list_severity_labels() -> List[str]:
    return SEVERITY_LABELS

def list_incident_status_labels() -> List[str]:
    return INCIDENT_STATUS_LABELS

def list_incident_risk_labels() -> List[str]:
    return INCIDENT_RISK_LABELS

def validate_incident_domain_label(label: str) -> None:
    if label not in INCIDENT_DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_safety_event_category(label: str) -> None:
    if label not in SAFETY_EVENT_CATEGORY_LABELS:
        raise ValueError(f"Invalid safety event category label: {label}")

def validate_severity_label(label: str) -> None:
    if label not in SEVERITY_LABELS:
        raise ValueError(f"Invalid severity label: {label}")

def validate_incident_status(label: str) -> None:
    if label not in INCIDENT_STATUS_LABELS:
        raise ValueError(f"Invalid incident status label: {label}")

def validate_incident_risk(label: str) -> None:
    if label not in INCIDENT_RISK_LABELS:
        raise ValueError(f"Invalid incident risk label: {label}")
