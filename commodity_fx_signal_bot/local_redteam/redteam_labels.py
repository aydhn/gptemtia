class LabelError(Exception):
    pass

_REDTEAM_DOMAIN_LABELS = [
    "redteam_rehearsal_domain",
    "misuse_scenario_domain",
    "abuse_case_simulation_domain",
    "adversarial_prompt_safety_domain",
    "prompt_injection_risk_domain",
    "unsafe_output_domain",
    "forbidden_capability_domain",
    "boundary_violation_domain",
    "safety_response_domain",
    "manual_escalation_domain",
    "safety_assurance_domain",
    "safety_coverage_domain",
    "quality_validation_domain",
    "unknown_redteam_domain"
]

_MISUSE_CATEGORY_LABELS = [
    "misuse_live_trading",
    "misuse_broker_execution",
    "misuse_investment_advice",
    "misuse_model_deployment",
    "misuse_secret_exposure",
    "misuse_file_action",
    "misuse_cloud_publish",
    "misuse_external_llm_api",
    "misuse_prompt_injection",
    "misuse_jailbreak_request",
    "misuse_performance_overclaim",
    "misuse_compliance_overclaim",
    "misuse_unknown"
]

_SAFETY_RESPONSE_LABELS = [
    "response_refuse",
    "response_refuse_and_redirect",
    "response_boundary_reminder",
    "response_manual_review",
    "response_no_go",
    "response_safe_summary",
    "response_unknown"
]

_REDTEAM_STATUS_LABELS = [
    "redteam_ready_for_rehearsal",
    "redteam_ready_with_warnings",
    "redteam_missing",
    "redteam_blocked_by_safety",
    "redteam_needs_manual_review",
    "redteam_unknown"
]

_REDTEAM_RISK_LABELS = [
    "redteam_critical_risk",
    "redteam_high_risk",
    "redteam_medium_risk",
    "redteam_low_risk",
    "redteam_info",
    "redteam_unknown_risk"
]

def list_redteam_domain_labels() -> list[str]:
    return _REDTEAM_DOMAIN_LABELS.copy()

def list_misuse_category_labels() -> list[str]:
    return _MISUSE_CATEGORY_LABELS.copy()

def list_safety_response_labels() -> list[str]:
    return _SAFETY_RESPONSE_LABELS.copy()

def list_redteam_status_labels() -> list[str]:
    return _REDTEAM_STATUS_LABELS.copy()

def list_redteam_risk_labels() -> list[str]:
    return _REDTEAM_RISK_LABELS.copy()

def validate_redteam_domain_label(label: str) -> None:
    if label not in _REDTEAM_DOMAIN_LABELS:
        raise LabelError(f"Invalid redteam domain label: {label}")

def validate_misuse_category_label(label: str) -> None:
    if label not in _MISUSE_CATEGORY_LABELS:
        raise LabelError(f"Invalid misuse category label: {label}")

def validate_safety_response_label(label: str) -> None:
    if label not in _SAFETY_RESPONSE_LABELS:
        raise LabelError(f"Invalid safety response label: {label}")

def validate_redteam_status(label: str) -> None:
    if label not in _REDTEAM_STATUS_LABELS:
        raise LabelError(f"Invalid redteam status label: {label}")

def validate_redteam_risk(label: str) -> None:
    if label not in _REDTEAM_RISK_LABELS:
        raise LabelError(f"Invalid redteam risk label: {label}")
