def list_export_type_labels() -> list[str]:
    return [
        "html_export",
        "pdf_export",
        "csv_bundle_export",
        "archive_export",
        "comparison_export",
        "tracking_export",
        "package_export",
        "unknown_export"
    ]

def list_export_status_labels() -> list[str]:
    return [
        "export_ready",
        "export_warning",
        "export_failed",
        "export_skipped",
        "export_dependency_missing",
        "export_unknown"
    ]

def list_report_archive_labels() -> list[str]:
    return [
        "archived_report",
        "archive_updated",
        "archive_duplicate",
        "archive_missing",
        "archive_unknown"
    ]

def list_comparison_labels() -> list[str]:
    return [
        "improved",
        "deteriorated",
        "unchanged",
        "mixed",
        "insufficient_history",
        "comparison_unknown"
    ]

def validate_export_type(label: str) -> None:
    if label not in list_export_type_labels():
        raise ValueError(f"Invalid export type label: {label}")

def validate_export_status(label: str) -> None:
    if label not in list_export_status_labels():
        raise ValueError(f"Invalid export status label: {label}")

def validate_report_archive_label(label: str) -> None:
    if label not in list_report_archive_labels():
        raise ValueError(f"Invalid report archive label: {label}")

def validate_comparison_label(label: str) -> None:
    if label not in list_comparison_labels():
        raise ValueError(f"Invalid comparison label: {label}")
