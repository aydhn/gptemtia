"""
Backup recovery labels and status tracking.
"""

def list_backup_scope_labels() -> list[str]:
    return [
        "critical_source_scope",
        "config_template_scope",
        "docs_scope",
        "tests_scope",
        "generated_manifest_scope",
        "reports_manifest_only_scope",
        "data_manifest_only_scope",
        "environment_snapshot_scope",
        "setup_guide_scope",
        "excluded_secret_scope",
        "excluded_cache_scope",
        "excluded_large_artifact_scope",
        "review_required_scope",
        "unknown_scope"
    ]


def list_backup_status_labels() -> list[str]:
    return [
        "backup_plan_ready",
        "backup_plan_ready_with_warnings",
        "backup_plan_blocked",
        "backup_plan_incomplete",
        "backup_plan_unknown"
    ]


def list_restore_status_labels() -> list[str]:
    return [
        "restore_plan_ready_dry_run",
        "restore_plan_ready_with_warnings",
        "restore_plan_blocked",
        "restore_plan_incomplete",
        "restore_plan_unknown"
    ]


def list_recovery_readiness_labels() -> list[str]:
    return [
        "recovery_ready_for_local_dry_run",
        "recovery_ready_with_warnings",
        "recovery_not_ready",
        "recovery_blocked_by_safety",
        "recovery_insufficient_data",
        "recovery_unknown"
    ]


def list_artifact_criticality_labels() -> list[str]:
    return [
        "critical_artifact",
        "important_artifact",
        "optional_artifact",
        "generated_artifact",
        "excluded_artifact",
        "unknown_criticality"
    ]


def validate_backup_scope(label: str) -> None:
    if label not in list_backup_scope_labels():
        raise ValueError(f"Invalid backup scope label: {label}")


def validate_backup_status(label: str) -> None:
    if label not in list_backup_status_labels():
        raise ValueError(f"Invalid backup status label: {label}")


def validate_restore_status(label: str) -> None:
    if label not in list_restore_status_labels():
        raise ValueError(f"Invalid restore status label: {label}")


def validate_recovery_readiness(label: str) -> None:
    if label not in list_recovery_readiness_labels():
        raise ValueError(f"Invalid recovery readiness label: {label}")


def validate_artifact_criticality(label: str) -> None:
    if label not in list_artifact_criticality_labels():
        raise ValueError(f"Invalid artifact criticality label: {label}")
