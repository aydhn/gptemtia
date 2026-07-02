"""
Archive Labels Module
Defines the controlled vocabularies for local archive registries.
"""

def list_archive_domain_labels() -> list[str]:
    return [
        "documentation_archive",
        "report_archive",
        "datalake_archive",
        "config_archive",
        "script_archive",
        "test_archive",
        "security_archive",
        "backup_packaging_archive",
        "cross_layer_archive",
        "dependency_archive",
        "operator_archive",
        "unknown_archive"
    ]

def list_archive_item_status_labels() -> list[str]:
    return [
        "archive_candidate",
        "archive_excluded",
        "archive_manifested",
        "archive_hash_recorded",
        "archive_integrity_warning",
        "archive_missing",
        "archive_unknown"
    ]

def list_retention_labels() -> list[str]:
    return [
        "retain_long_term_manual",
        "retain_medium_term_manual",
        "retain_short_term_manual",
        "retain_until_next_review_manual",
        "exclude_from_archive",
        "retention_unknown"
    ]

def list_archive_risk_labels() -> list[str]:
    return [
        "archive_critical_risk",
        "archive_high_risk",
        "archive_medium_risk",
        "archive_low_risk",
        "archive_info",
        "archive_unknown_risk"
    ]

def list_integrity_status_labels() -> list[str]:
    return [
        "integrity_hash_available",
        "integrity_hash_skipped_large_file",
        "integrity_missing_hash",
        "integrity_path_missing",
        "integrity_manual_review_required",
        "integrity_unknown"
    ]

def validate_archive_domain_label(label: str) -> None:
    if label not in list_archive_domain_labels():
        raise ValueError(f"Invalid archive domain label: {label}")

def validate_archive_item_status(label: str) -> None:
    if label not in list_archive_item_status_labels():
        raise ValueError(f"Invalid archive item status label: {label}")

def validate_retention_label(label: str) -> None:
    if label not in list_retention_labels():
        raise ValueError(f"Invalid retention label: {label}")

def validate_archive_risk(label: str) -> None:
    if label not in list_archive_risk_labels():
        raise ValueError(f"Invalid archive risk label: {label}")

def validate_integrity_status(label: str) -> None:
    if label not in list_integrity_status_labels():
        raise ValueError(f"Invalid integrity status label: {label}")
