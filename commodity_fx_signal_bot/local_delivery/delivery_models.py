import hashlib
from dataclasses import dataclass

@dataclass
class DeliveryDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_items: list[str]
    warnings: list[str]

@dataclass
class DeliveryItem:
    item_id: str
    item_label: str
    relative_path: str
    source_layer: str
    item_status: str
    size_bytes: int | None
    modified_at_utc: str | None
    delivery_notes: list[str]
    warnings: list[str]

@dataclass
class DeliveryTraceItem:
    trace_id: str
    source_item_id: str
    source_path: str
    target_bundle_section: str
    trace_status: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class DeliveryChecklistItem:
    checklist_id: str
    checklist_name: str
    description: str
    readiness_label: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class DeliveryFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_delivery_domain_id(domain_label: str) -> str:
    return hashlib.md5(f"domain_{domain_label}".encode()).hexdigest()[:12]

def build_delivery_item_id(relative_path: str, item_label: str) -> str:
    return hashlib.md5(f"item_{relative_path}_{item_label}".encode()).hexdigest()[:12]

def build_delivery_trace_id(source_item_id: str, target_bundle_section: str) -> str:
    return hashlib.md5(f"trace_{source_item_id}_{target_bundle_section}".encode()).hexdigest()[:12]

def build_delivery_checklist_id(checklist_name: str) -> str:
    return hashlib.md5(f"check_{checklist_name}".encode()).hexdigest()[:12]

def build_delivery_finding_id(title: str) -> str:
    return hashlib.md5(f"find_{title}".encode()).hexdigest()[:12]

def delivery_domain_to_dict(item: DeliveryDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_items": item.required_items,
        "warnings": item.warnings
    }

def delivery_item_to_dict(item: DeliveryItem) -> dict:
    return {
        "item_id": item.item_id,
        "item_label": item.item_label,
        "relative_path": item.relative_path,
        "source_layer": item.source_layer,
        "item_status": item.item_status,
        "size_bytes": item.size_bytes,
        "modified_at_utc": item.modified_at_utc,
        "delivery_notes": item.delivery_notes,
        "warnings": item.warnings
    }

def delivery_trace_item_to_dict(item: DeliveryTraceItem) -> dict:
    return {
        "trace_id": item.trace_id,
        "source_item_id": item.source_item_id,
        "source_path": item.source_path,
        "target_bundle_section": item.target_bundle_section,
        "trace_status": item.trace_status,
        "manual_review_required": item.manual_review_required,
        "warnings": item.warnings
    }

def delivery_checklist_item_to_dict(item: DeliveryChecklistItem) -> dict:
    return {
        "checklist_id": item.checklist_id,
        "checklist_name": item.checklist_name,
        "description": item.description,
        "readiness_label": item.readiness_label,
        "evidence_refs": item.evidence_refs,
        "manual_review_required": item.manual_review_required,
        "warnings": item.warnings
    }

def delivery_finding_to_dict(item: DeliveryFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": item.warnings
    }
