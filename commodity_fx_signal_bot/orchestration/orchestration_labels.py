"""
Controlled label sets for orchestration.
"""

_JOB_STATUS_LABELS = [
    "job_pending",
    "job_running",
    "job_success",
    "job_failed",
    "job_skipped",
    "job_blocked",
    "job_retry_candidate",
    "job_dry_run",
    "job_unknown"
]

_WORKFLOW_STATUS_LABELS = [
    "workflow_pending",
    "workflow_running",
    "workflow_success",
    "workflow_partial_success",
    "workflow_failed",
    "workflow_dry_run",
    "workflow_blocked",
    "workflow_unknown"
]

_DEPENDENCY_STATUS_LABELS = [
    "dependency_available",
    "dependency_missing",
    "dependency_stale",
    "dependency_optional_missing",
    "dependency_not_required",
    "dependency_unknown"
]

_JOB_TYPE_LABELS = [
    "data_job",
    "feature_job",
    "candidate_job",
    "risk_job",
    "sizing_job",
    "level_job",
    "backtest_job",
    "performance_job",
    "validation_job",
    "ml_dataset_job",
    "ml_training_job",
    "ml_prediction_job",
    "ml_integration_job",
    "paper_job",
    "notification_job",
    "healthcheck_job",
    "unknown_job"
]

def list_job_status_labels() -> list[str]:
    return list(_JOB_STATUS_LABELS)

def list_workflow_status_labels() -> list[str]:
    return list(_WORKFLOW_STATUS_LABELS)

def list_dependency_status_labels() -> list[str]:
    return list(_DEPENDENCY_STATUS_LABELS)

def list_job_type_labels() -> list[str]:
    return list(_JOB_TYPE_LABELS)

def validate_job_status(label: str) -> None:
    if label not in _JOB_STATUS_LABELS:
        raise ValueError(f"Invalid job status label: {label}")

def validate_workflow_status(label: str) -> None:
    if label not in _WORKFLOW_STATUS_LABELS:
        raise ValueError(f"Invalid workflow status label: {label}")

def validate_dependency_status(label: str) -> None:
    if label not in _DEPENDENCY_STATUS_LABELS:
        raise ValueError(f"Invalid dependency status label: {label}")

def validate_job_type(label: str) -> None:
    if label not in _JOB_TYPE_LABELS:
        raise ValueError(f"Invalid job type label: {label}")

def is_terminal_job_status(label: str) -> bool:
    validate_job_status(label)
    return label in ["job_success", "job_failed", "job_skipped", "job_blocked", "job_dry_run", "job_unknown"]

def is_failed_job_status(label: str) -> bool:
    validate_job_status(label)
    return label in ["job_failed", "job_blocked", "job_unknown"]
