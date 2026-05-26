"""Controlled labels for maintenance artifact lifecycles, retention, actions, and storage health."""

ARTIFACT_LIFECYCLE_LABELS = [
    "active_artifact",
    "stale_artifact",
    "archive_candidate",
    "cleanup_candidate",
    "keep_required",
    "protected_artifact",
    "unknown_lifecycle"
]

RETENTION_CATEGORY_LABELS = [
    "raw_data_retention",
    "processed_data_retention",
    "report_retention",
    "quality_report_retention",
    "governance_retention",
    "experiment_retention",
    "knowledge_base_retention",
    "cache_retention",
    "checkpoint_retention",
    "log_retention",
    "unknown_retention"
]

MAINTENANCE_ACTION_LABELS = [
    "keep_action",
    "archive_dry_run_action",
    "cleanup_dry_run_action",
    "rotate_dry_run_action",
    "review_required_action",
    "blocked_delete_action",
    "blocked_move_action",
    "unknown_action"
]

STORAGE_HEALTH_LABELS = [
    "healthy_storage",
    "moderate_storage_pressure",
    "high_storage_pressure",
    "critical_storage_pressure",
    "unknown_storage_health"
]

def list_artifact_lifecycle_labels() -> list[str]:
    return ARTIFACT_LIFECYCLE_LABELS

def list_retention_category_labels() -> list[str]:
    return RETENTION_CATEGORY_LABELS

def list_maintenance_action_labels() -> list[str]:
    return MAINTENANCE_ACTION_LABELS

def list_storage_health_labels() -> list[str]:
    return STORAGE_HEALTH_LABELS

def validate_artifact_lifecycle(label: str) -> None:
    if label not in ARTIFACT_LIFECYCLE_LABELS:
        raise ValueError(f"Invalid artifact lifecycle label: {label}")

def validate_retention_category(label: str) -> None:
    if label not in RETENTION_CATEGORY_LABELS:
        raise ValueError(f"Invalid retention category label: {label}")

def validate_maintenance_action(label: str) -> None:
    if label not in MAINTENANCE_ACTION_LABELS:
        raise ValueError(f"Invalid maintenance action label: {label}")

def validate_storage_health(label: str) -> None:
    if label not in STORAGE_HEALTH_LABELS:
        raise ValueError(f"Invalid storage health label: {label}")
