import logging

logger = logging.getLogger(__name__)

_DELIVERY_DOMAIN_LABELS = [
    "bundle_manifest_domain", "handoff_index_domain", "reviewer_guide_domain",
    "transfer_checklist_domain", "evidence_map_domain", "delivery_rehearsal_domain",
    "recipient_orientation_domain", "safety_boundary_domain", "readiness_scoring_domain",
    "quality_validation_domain", "unknown_delivery_domain"
]

_DELIVERY_ITEM_LABELS = [
    "delivery_doc_item", "delivery_report_item", "delivery_datalake_item",
    "delivery_script_item", "delivery_test_item", "delivery_generated_doc_item",
    "delivery_safety_item", "delivery_acceptance_item", "delivery_unknown_item"
]

_DELIVERY_STATUS_LABELS = [
    "delivery_ready_for_rehearsal", "delivery_ready_with_warnings", "delivery_missing",
    "delivery_blocked_by_safety", "delivery_needs_manual_review", "delivery_unknown"
]

_TRANSFER_READINESS_LABELS = [
    "transfer_ready_for_manual_review", "transfer_ready_with_warnings",
    "transfer_missing_required_item", "transfer_blocked_by_no_go",
    "transfer_not_applicable", "transfer_unknown"
]

_DELIVERY_RISK_LABELS = [
    "delivery_critical_risk", "delivery_high_risk", "delivery_medium_risk",
    "delivery_low_risk", "delivery_info", "delivery_unknown_risk"
]

def list_delivery_domain_labels() -> list[str]:
    return _DELIVERY_DOMAIN_LABELS.copy()

def list_delivery_item_labels() -> list[str]:
    return _DELIVERY_ITEM_LABELS.copy()

def list_delivery_status_labels() -> list[str]:
    return _DELIVERY_STATUS_LABELS.copy()

def list_transfer_readiness_labels() -> list[str]:
    return _TRANSFER_READINESS_LABELS.copy()

def list_delivery_risk_labels() -> list[str]:
    return _DELIVERY_RISK_LABELS.copy()

def validate_delivery_domain_label(label: str) -> None:
    if label not in _DELIVERY_DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_delivery_item_label(label: str) -> None:
    if label not in _DELIVERY_ITEM_LABELS:
        raise ValueError(f"Invalid item label: {label}")

def validate_delivery_status(label: str) -> None:
    if label not in _DELIVERY_STATUS_LABELS:
        raise ValueError(f"Invalid status label: {label}")

def validate_transfer_readiness_label(label: str) -> None:
    if label not in _TRANSFER_READINESS_LABELS:
        raise ValueError(f"Invalid transfer readiness label: {label}")

def validate_delivery_risk(label: str) -> None:
    if label not in _DELIVERY_RISK_LABELS:
        raise ValueError(f"Invalid delivery risk label: {label}")
