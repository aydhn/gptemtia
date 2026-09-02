"""
Archival Labels.
"""

_ARCHIVAL_DOMAIN_LABELS = [
    "seal_rehearsal_domain",
    "immutable_manifest_domain",
    "provenance_lockfile_domain",
    "hash_catalog_domain",
    "hash_policy_domain",
    "exclusion_policy_domain",
    "custody_rehearsal_domain",
    "retention_domain",
    "tamper_evidence_domain",
    "reproducibility_domain",
    "provenance_trace_domain",
    "quality_validation_domain",
    "unknown_archival_domain"
]

_ARCHIVAL_ITEM_LABELS = [
    "archival_doc_item",
    "archival_report_item",
    "archival_datalake_item",
    "archival_script_item",
    "archival_test_item",
    "archival_generated_doc_item",
    "archival_safety_item",
    "archival_delivery_item",
    "archival_acceptance_item",
    "archival_excluded_sensitive_item",
    "archival_unknown_item"
]

_HASH_STATUS_LABELS = [
    "hash_rehearsal_ready",
    "hash_rehearsal_skipped_sensitive",
    "hash_rehearsal_skipped_large_file",
    "hash_rehearsal_missing",
    "hash_rehearsal_error",
    "hash_rehearsal_unknown"
]

_CUSTODY_STATUS_LABELS = [
    "custody_rehearsal_ready",
    "custody_rehearsal_ready_with_warnings",
    "custody_rehearsal_missing",
    "custody_rehearsal_blocked_by_safety",
    "custody_rehearsal_needs_manual_review",
    "custody_rehearsal_unknown"
]

_ARCHIVAL_RISK_LABELS = [
    "archival_critical_risk",
    "archival_high_risk",
    "archival_medium_risk",
    "archival_low_risk",
    "archival_info",
    "archival_unknown_risk"
]

def list_archival_domain_labels() -> list[str]: return _ARCHIVAL_DOMAIN_LABELS.copy()
def list_archival_item_labels() -> list[str]: return _ARCHIVAL_ITEM_LABELS.copy()
def list_hash_status_labels() -> list[str]: return _HASH_STATUS_LABELS.copy()
def list_custody_status_labels() -> list[str]: return _CUSTODY_STATUS_LABELS.copy()
def list_archival_risk_labels() -> list[str]: return _ARCHIVAL_RISK_LABELS.copy()

def validate_archival_domain_label(label: str) -> None:
    if label not in _ARCHIVAL_DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_archival_item_label(label: str) -> None:
    if label not in _ARCHIVAL_ITEM_LABELS:
        raise ValueError(f"Invalid item label: {label}")

def validate_hash_status(label: str) -> None:
    if label not in _HASH_STATUS_LABELS:
        raise ValueError(f"Invalid hash status: {label}")

def validate_custody_status(label: str) -> None:
    if label not in _CUSTODY_STATUS_LABELS:
        raise ValueError(f"Invalid custody status: {label}")

def validate_archival_risk(label: str) -> None:
    if label not in _ARCHIVAL_RISK_LABELS:
        raise ValueError(f"Invalid risk label: {label}")
