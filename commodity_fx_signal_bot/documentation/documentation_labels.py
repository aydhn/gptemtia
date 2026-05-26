DOCUMENT_TYPE_LABELS = [
    "user_guide_doc",
    "operator_manual_doc",
    "analyst_handbook_doc",
    "developer_guide_doc",
    "codex_agent_guide_doc",
    "safe_usage_guide_doc",
    "troubleshooting_doc",
    "faq_doc",
    "glossary_doc",
    "module_map_doc",
    "script_reference_doc",
    "output_reference_doc",
    "architecture_doc",
    "phase_log_doc",
    "generated_reference_doc",
    "unknown_doc"
]

DOCUMENTATION_STATUS_LABELS = [
    "doc_complete",
    "doc_incomplete",
    "doc_missing",
    "doc_outdated",
    "doc_warning",
    "doc_unknown"
]

DOCUMENTATION_SAFETY_LABELS = [
    "safety_language_ok",
    "missing_disclaimer",
    "live_trading_language_found",
    "investment_advice_language_found",
    "broker_language_found",
    "deployment_language_found",
    "unsafe_doc_language_unknown"
]

DOCUMENTATION_AUDIENCE_LABELS = [
    "user_audience",
    "operator_audience",
    "analyst_audience",
    "developer_audience",
    "codex_agent_audience",
    "maintainer_audience",
    "unknown_audience"
]

def list_document_type_labels() -> list[str]:
    return DOCUMENT_TYPE_LABELS

def list_documentation_status_labels() -> list[str]:
    return DOCUMENTATION_STATUS_LABELS

def list_documentation_safety_labels() -> list[str]:
    return DOCUMENTATION_SAFETY_LABELS

def list_documentation_audience_labels() -> list[str]:
    return DOCUMENTATION_AUDIENCE_LABELS

def validate_document_type(label: str) -> None:
    if label not in DOCUMENT_TYPE_LABELS:
        raise ValueError(f"Geçersiz document type label: {label}")

def validate_documentation_status(label: str) -> None:
    if label not in DOCUMENTATION_STATUS_LABELS:
        raise ValueError(f"Geçersiz documentation status label: {label}")

def validate_documentation_safety(label: str) -> None:
    if label not in DOCUMENTATION_SAFETY_LABELS:
        raise ValueError(f"Geçersiz documentation safety label: {label}")

def validate_documentation_audience(label: str) -> None:
    if label not in DOCUMENTATION_AUDIENCE_LABELS:
        raise ValueError(f"Geçersiz documentation audience label: {label}")
