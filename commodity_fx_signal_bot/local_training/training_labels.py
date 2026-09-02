
TRAINING_DOMAIN_LABELS = [
    "operator_training",
    "analyst_training",
    "developer_training",
    "safe_usage_training",
    "non_use_policy_training",
    "command_training",
    "report_training",
    "datalake_training",
    "cross_layer_training",
    "troubleshooting_training",
    "handover_training",
    "unknown_training"
]

TRAINING_LESSON_STATUS_LABELS = [
    "lesson_ready",
    "lesson_ready_with_warnings",
    "lesson_missing",
    "lesson_blocked_by_safety",
    "lesson_needs_manual_review",
    "lesson_unknown"
]

ONBOARDING_ROLE_LABELS = [
    "operator_role",
    "analyst_role",
    "developer_role",
    "maintainer_role",
    "reviewer_role",
    "unknown_role"
]

ASSESSMENT_STATUS_LABELS = [
    "assessment_dry_run_ready",
    "assessment_needs_manual_review",
    "assessment_blocked_by_safety",
    "assessment_not_applicable",
    "assessment_unknown"
]

TRAINING_RISK_LABELS = [
    "training_critical_risk",
    "training_high_risk",
    "training_medium_risk",
    "training_low_risk",
    "training_info",
    "training_unknown_risk"
]

def list_training_domain_labels() -> list[str]: return TRAINING_DOMAIN_LABELS
def list_training_lesson_status_labels() -> list[str]: return TRAINING_LESSON_STATUS_LABELS
def list_onboarding_role_labels() -> list[str]: return ONBOARDING_ROLE_LABELS
def list_assessment_status_labels() -> list[str]: return ASSESSMENT_STATUS_LABELS
def list_training_risk_labels() -> list[str]: return TRAINING_RISK_LABELS

def validate_training_domain_label(label: str) -> None:
    if label not in TRAINING_DOMAIN_LABELS: raise ValueError(f"Invalid domain label: {label}")
def validate_training_lesson_status(label: str) -> None:
    if label not in TRAINING_LESSON_STATUS_LABELS: raise ValueError(f"Invalid lesson status: {label}")
def validate_onboarding_role(label: str) -> None:
    if label not in ONBOARDING_ROLE_LABELS: raise ValueError(f"Invalid role label: {label}")
def validate_assessment_status(label: str) -> None:
    if label not in ASSESSMENT_STATUS_LABELS: raise ValueError(f"Invalid assessment status: {label}")
def validate_training_risk(label: str) -> None:
    if label not in TRAINING_RISK_LABELS: raise ValueError(f"Invalid risk label: {label}")
