def list_evidence_artifact_labels() -> list[str]:
    return [
        "report_evidence",
        "datalake_evidence",
        "documentation_evidence",
        "quality_evidence",
        "safety_evidence",
        "secrets_hygiene_evidence",
        "backup_recovery_evidence",
        "packaging_evidence",
        "scenario_regression_evidence",
        "final_review_evidence",
        "master_orchestration_evidence",
        "governance_evidence",
        "unknown_evidence"
    ]

def list_control_domain_labels() -> list[str]:
    return [
        "safety_controls",
        "secrets_controls",
        "backup_recovery_controls",
        "packaging_controls",
        "quality_controls",
        "documentation_controls",
        "scenario_regression_controls",
        "final_review_controls",
        "master_orchestration_controls",
        "governance_controls",
        "data_integrity_controls",
        "operational_controls",
        "unknown_controls"
    ]

def list_control_status_labels() -> list[str]:
    return [
        "control_evidenced",
        "control_partially_evidenced",
        "control_missing_evidence",
        "control_stale_evidence",
        "control_not_applicable",
        "control_unknown"
    ]

def list_evidence_freshness_labels() -> list[str]:
    return [
        "evidence_fresh",
        "evidence_warning_stale",
        "evidence_stale",
        "evidence_missing_timestamp",
        "evidence_unknown_freshness"
    ]

def list_evidence_export_labels() -> list[str]:
    return [
        "export_ready_local",
        "export_ready_with_warnings",
        "export_blocked_by_safety",
        "export_incomplete",
        "export_unknown"
    ]

def validate_evidence_artifact_label(label: str) -> None:
    if label not in list_evidence_artifact_labels():
        raise ValueError(f"Invalid evidence artifact label: {label}")

def validate_control_domain(label: str) -> None:
    if label not in list_control_domain_labels():
        raise ValueError(f"Invalid control domain label: {label}")

def validate_control_status(label: str) -> None:
    if label not in list_control_status_labels():
        raise ValueError(f"Invalid control status label: {label}")
    if label == "control_evidenced":
        pass # Not an official compliance claim

def validate_evidence_freshness(label: str) -> None:
    if label not in list_evidence_freshness_labels():
        raise ValueError(f"Invalid evidence freshness label: {label}")

def validate_evidence_export_label(label: str) -> None:
    if label not in list_evidence_export_labels():
        raise ValueError(f"Invalid evidence export label: {label}")
