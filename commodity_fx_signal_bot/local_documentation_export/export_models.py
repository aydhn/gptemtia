"""Export models."""
from dataclasses import dataclass, asdict
from typing import List
import hashlib

@dataclass
class DocumentationExportDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class DocumentationPageItem:
    page_id: str
    page_title: str
    source_ref: str
    output_ref: str
    format_label: str
    route_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class PrintableBinderItem:
    binder_id: str
    section_title: str
    section_area: str
    source_refs: list[str]
    reading_priority: int
    format_label: str
    warnings: list[str]

@dataclass
class DocumentationExportMapItem:
    map_id: str
    map_area: str
    source_ref: str
    output_ref: str
    relation_type: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class DocumentationExportFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_documentation_export_domain_id(domain_label: str) -> str:
    return hashlib.sha256(domain_label.encode()).hexdigest()[:12]

def build_documentation_page_item_id(page_title: str, output_ref: str) -> str:
    return hashlib.sha256(f"{page_title}_{output_ref}".encode()).hexdigest()[:12]

def build_printable_binder_item_id(section_title: str, section_area: str) -> str:
    return hashlib.sha256(f"{section_title}_{section_area}".encode()).hexdigest()[:12]

def build_documentation_export_map_item_id(map_area: str, source_ref: str, output_ref: str) -> str:
    return hashlib.sha256(f"{map_area}_{source_ref}_{output_ref}".encode()).hexdigest()[:12]

def build_documentation_export_finding_id(title: str) -> str:
    return hashlib.sha256(title.encode()).hexdigest()[:12]

def documentation_export_domain_to_dict(item: DocumentationExportDomain) -> dict:
    return asdict(item)

def documentation_page_item_to_dict(item: DocumentationPageItem) -> dict:
    return asdict(item)

def printable_binder_item_to_dict(item: PrintableBinderItem) -> dict:
    return asdict(item)

def documentation_export_map_item_to_dict(item: DocumentationExportMapItem) -> dict:
    return asdict(item)

def documentation_export_finding_to_dict(item: DocumentationExportFinding) -> dict:
    return asdict(item)
