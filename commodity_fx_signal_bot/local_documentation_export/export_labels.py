"""Export labels."""

_DOMAINS = [
    "static_site_export_domain", "offline_html_pack_domain", "printable_binder_domain",
    "pdf_ready_docs_domain", "presentation_freeze_domain", "documentation_export_map_domain",
    "documentation_route_domain", "documentation_evidence_domain", "documentation_quality_domain",
    "documentation_boundary_domain", "quality_validation_domain", "unknown_documentation_export_domain"
]

_STATUS = [
    "documentation_export_rehearsal_ready", "documentation_export_rehearsal_ready_with_warnings",
    "documentation_export_rehearsal_missing", "documentation_export_rehearsal_blocked_by_safety",
    "documentation_export_rehearsal_needs_manual_review", "documentation_export_rehearsal_unknown"
]

_FORMAT = [
    "format_markdown", "format_html_rehearsal", "format_txt", "format_csv", "format_json",
    "format_pdf_ready_not_pdf", "format_printable", "format_unknown"
]

_ROUTE = [
    "docs_route_operator", "docs_route_analyst", "docs_route_maintainer",
    "docs_route_codex_agent", "docs_route_reviewer", "docs_route_future_reader", "docs_route_unknown"
]

_RISK = [
    "documentation_export_critical_risk", "documentation_export_high_risk",
    "documentation_export_medium_risk", "documentation_export_low_risk",
    "documentation_export_info", "documentation_export_unknown_risk"
]

def list_documentation_export_domain_labels() -> list[str]:
    return _DOMAINS.copy()

def list_documentation_export_status_labels() -> list[str]:
    return _STATUS.copy()

def list_documentation_format_labels() -> list[str]:
    return _FORMAT.copy()

def list_documentation_route_labels() -> list[str]:
    return _ROUTE.copy()

def list_documentation_export_risk_labels() -> list[str]:
    return _RISK.copy()

def validate_documentation_export_domain_label(label: str) -> None:
    if label not in _DOMAINS:
        raise ValueError("Invalid domain")

def validate_documentation_export_status(label: str) -> None:
    if label not in _STATUS:
        raise ValueError("Invalid status")

def validate_documentation_format(label: str) -> None:
    if label not in _FORMAT:
        raise ValueError("Invalid format")

def validate_documentation_route(label: str) -> None:
    if label not in _ROUTE:
        raise ValueError("Invalid route")

def validate_documentation_export_risk(label: str) -> None:
    if label not in _RISK:
        raise ValueError("Invalid risk")
