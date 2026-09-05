class LabelError(Exception):
    pass

DOMAIN_LABELS = [
    "distribution_bundle_domain",
    "portable_docs_domain",
    "release_folder_manifest_domain",
    "handover_zip_map_domain",
    "packaging_governance_domain",
    "packaging_criteria_domain",
    "packaging_evidence_domain",
    "packaging_handoff_domain",
    "packaging_boundary_domain",
    "packaging_quality_domain",
    "quality_validation_domain",
    "unknown_packaging_domain"
]

STATUS_LABELS = [
    "packaging_rehearsal_ready",
    "packaging_rehearsal_ready_with_warnings",
    "packaging_rehearsal_missing",
    "packaging_rehearsal_blocked_by_safety",
    "packaging_rehearsal_needs_manual_review",
    "packaging_rehearsal_unknown"
]

ARTIFACT_LABELS = [
    "artifact_manifest_only",
    "artifact_documentation_only",
    "artifact_csv_registry",
    "artifact_markdown_packet",
    "artifact_txt_packet",
    "artifact_json_report",
    "artifact_html_rehearsal",
    "artifact_zip_map_not_zip",
    "artifact_unknown"
]

ROUTE_LABELS = [
    "package_route_operator",
    "package_route_analyst",
    "package_route_maintainer",
    "package_route_reviewer",
    "package_route_codex_agent",
    "package_route_future_reader",
    "package_route_unknown"
]

RISK_LABELS = [
    "packaging_critical_risk",
    "packaging_high_risk",
    "packaging_medium_risk",
    "packaging_low_risk",
    "packaging_info",
    "packaging_unknown_risk"
]

def list_packaging_domain_labels() -> list[str]:
    return list(DOMAIN_LABELS)

def list_packaging_status_labels() -> list[str]:
    return list(STATUS_LABELS)

def list_packaging_artifact_labels() -> list[str]:
    return list(ARTIFACT_LABELS)

def list_packaging_route_labels() -> list[str]:
    return list(ROUTE_LABELS)

def list_packaging_risk_labels() -> list[str]:
    return list(RISK_LABELS)

def validate_packaging_domain_label(label: str) -> None:
    if label not in DOMAIN_LABELS:
        raise LabelError(f"Invalid domain label: {label}")

def validate_packaging_status(label: str) -> None:
    if label not in STATUS_LABELS:
        raise LabelError(f"Invalid status label: {label}")

def validate_packaging_artifact_label(label: str) -> None:
    if label not in ARTIFACT_LABELS:
        raise LabelError(f"Invalid artifact label: {label}")

def validate_packaging_route(label: str) -> None:
    if label not in ROUTE_LABELS:
        raise LabelError(f"Invalid route label: {label}")

def validate_packaging_risk(label: str) -> None:
    if label not in RISK_LABELS:
        raise LabelError(f"Invalid risk label: {label}")
