from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib

@dataclass
class DocumentationRecord:
    doc_id: str
    title: str
    document_type: str
    audience: str
    path: str
    relative_path: str
    status: str
    word_count: int | None
    heading_count: int | None
    has_disclaimer: bool
    safety_label: str
    warnings: list[str]

@dataclass
class DocumentationCoverageItem:
    coverage_id: str
    module_name: str
    expected_doc: str
    doc_exists: bool
    section_exists: bool
    status: str
    warnings: list[str]

@dataclass
class DocumentationLinkCheck:
    link_id: str
    source_doc: str
    target: str
    link_type: str
    exists: bool
    status: str
    warnings: list[str]

@dataclass
class DocumentationPackManifest:
    manifest_id: str
    profile_name: str
    created_at_utc: str
    document_count: int
    required_document_count: int
    generated_documents: list[str]
    missing_documents: list[str]
    quality_score: float
    warnings: list[str]

def build_doc_id(relative_path: str) -> str:
    hash_object = hashlib.md5(relative_path.encode())
    return f"doc_{hash_object.hexdigest()[:12]}"

def build_coverage_id(module_name: str, expected_doc: str) -> str:
    hash_str = f"{module_name}_{expected_doc}"
    hash_object = hashlib.md5(hash_str.encode())
    return f"cov_{hash_object.hexdigest()[:12]}"

def build_link_check_id(source_doc: str, target: str) -> str:
    hash_str = f"{source_doc}_{target}"
    hash_object = hashlib.md5(hash_str.encode())
    return f"lnk_{hash_object.hexdigest()[:12]}"

def build_documentation_manifest_id(profile_name: str, created_at_utc: str) -> str:
    hash_str = f"{profile_name}_{created_at_utc}"
    hash_object = hashlib.md5(hash_str.encode())
    return f"dman_{hash_object.hexdigest()[:12]}"

def documentation_record_to_dict(record: DocumentationRecord) -> dict:
    return asdict(record)

def documentation_coverage_item_to_dict(item: DocumentationCoverageItem) -> dict:
    return asdict(item)

def documentation_link_check_to_dict(check: DocumentationLinkCheck) -> dict:
    return asdict(check)

def documentation_pack_manifest_to_dict(manifest: DocumentationPackManifest) -> dict:
    return asdict(manifest)

def estimate_word_count(text: str) -> int:
    if not text:
        return 0
    return len(text.split())

def count_markdown_headings(text: str) -> int:
    if not text:
        return 0
    return sum(1 for line in text.split('\n') if line.strip().startswith('#'))
