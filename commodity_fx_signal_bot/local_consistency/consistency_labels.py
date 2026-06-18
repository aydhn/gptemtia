def list_consistency_check_type_labels() -> list[str]:
    return [
        "config_env_check",
        "settings_docs_check",
        "paths_datalake_check",
        "script_report_check",
        "report_datalake_check",
        "docs_phase_log_check",
        "evidence_control_check",
        "metadata_artifact_check",
        "graph_metadata_check",
        "timeline_artifact_check",
        "backup_packaging_secrets_check",
        "non_use_policy_check",
        "disclaimer_check",
        "safety_boundary_check",
        "contradiction_check",
        "reference_check",
        "stale_reconciliation_check",
        "unknown_check"
    ]

def list_consistency_status_labels() -> list[str]:
    return [
        "consistency_passed",
        "consistency_warning",
        "consistency_failed",
        "consistency_blocked_by_safety",
        "consistency_skipped",
        "consistency_unknown"
    ]

def list_contradiction_severity_labels() -> list[str]:
    return [
        "critical_contradiction",
        "high_contradiction",
        "medium_contradiction",
        "low_contradiction",
        "informational_inconsistency",
        "unknown_contradiction"
    ]

def list_reference_status_labels() -> list[str]:
    return [
        "reference_valid",
        "reference_missing",
        "reference_broken",
        "reference_stale",
        "reference_ambiguous",
        "reference_unknown"
    ]

def list_reconciliation_status_labels() -> list[str]:
    return [
        "reconciliation_not_needed",
        "reconciliation_recommended",
        "reconciliation_requires_manual_review",
        "reconciliation_blocked_by_safety",
        "reconciliation_unknown"
    ]

def validate_consistency_check_type(label: str) -> None:
    if label not in list_consistency_check_type_labels():
        raise ValueError(f"Invalid consistency check type: {label}")

def validate_consistency_status(label: str) -> None:
    if label not in list_consistency_status_labels():
        raise ValueError(f"Invalid consistency status: {label}")

def validate_contradiction_severity(label: str) -> None:
    if label not in list_contradiction_severity_labels():
        raise ValueError(f"Invalid contradiction severity: {label}")

def validate_reference_status(label: str) -> None:
    if label not in list_reference_status_labels():
        raise ValueError(f"Invalid reference status: {label}")

def validate_reconciliation_status(label: str) -> None:
    if label not in list_reconciliation_status_labels():
        raise ValueError(f"Invalid reconciliation status: {label}")
