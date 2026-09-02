class LabelError(Exception):
    pass

AUDIENCE_LABELS = [
    "executive_audience", "business_stakeholder_audience", "analyst_audience",
    "operator_audience", "developer_audience", "compliance_reviewer_audience",
    "nontechnical_audience", "unknown_audience"
]

SECTION_LABELS = [
    "project_overview_section", "capability_section", "architecture_section",
    "milestone_section", "boundary_section", "risk_limitation_section",
    "decision_context_section", "operating_model_section", "next_steps_section",
    "faq_section", "unknown_section"
]

STATUS_LABELS = [
    "communication_ready", "communication_ready_with_warnings", "communication_missing",
    "communication_blocked_by_safety", "communication_needs_manual_review", "communication_unknown"
]

DECISION_LABELS = [
    "decision_context_informational", "decision_context_manual_review",
    "decision_context_no_go_related", "decision_context_safe_next_step", "decision_context_unknown"
]

RISK_LABELS = [
    "communication_critical_risk", "communication_high_risk", "communication_medium_risk",
    "communication_low_risk", "communication_info", "communication_unknown_risk"
]

def list_audience_labels() -> list[str]: return AUDIENCE_LABELS
def list_briefing_section_labels() -> list[str]: return SECTION_LABELS
def list_communication_status_labels() -> list[str]: return STATUS_LABELS
def list_decision_context_labels() -> list[str]: return DECISION_LABELS
def list_communication_risk_labels() -> list[str]: return RISK_LABELS

def validate_audience_label(label: str) -> None:
    if label not in AUDIENCE_LABELS:
        raise LabelError(f"Invalid audience label: {label}")
def validate_briefing_section_label(label: str) -> None:
    if label not in SECTION_LABELS:
        raise LabelError(f"Invalid section label: {label}")
def validate_communication_status(label: str) -> None:
    if label not in STATUS_LABELS:
        raise LabelError(f"Invalid status label: {label}")
def validate_decision_context_label(label: str) -> None:
    if label not in DECISION_LABELS:
        raise LabelError(f"Invalid decision label: {label}")
def validate_communication_risk(label: str) -> None:
    if label not in RISK_LABELS:
        raise LabelError(f"Invalid risk label: {label}")
