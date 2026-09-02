"""
Archival Models.
"""
import hashlib
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class ArchivalDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_artifacts: list[str]
    warnings: list[str]

@dataclass
class ArchivalItem:
    item_id: str
    item_label: str
    relative_path: str
    source_layer: str
    hash_algorithm: Optional[str]
    hash_value: Optional[str]
    hash_status: str
    size_bytes: Optional[int]
    modified_at_utc: Optional[str]
    warnings: list[str]

@dataclass
class ProvenanceLockEntry:
    entry_id: str
    relative_path: str
    source_layer: str
    provenance_note: str
    hash_ref: Optional[str]
    exclusion_reason: Optional[str]
    warnings: list[str]

@dataclass
class CustodyRehearsalItem:
    custody_id: str
    custody_step: str
    custody_status: str
    responsible_role_hint: str
    evidence_refs: list[str]
    warnings: list[str]

@dataclass
class ArchivalFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_archival_domain_id(domain_label: str) -> str:
    return hashlib.sha256(f"domain:{domain_label}".encode('utf-8')).hexdigest()[:16]

def build_archival_item_id(relative_path: str, item_label: str) -> str:
    return hashlib.sha256(f"item:{relative_path}:{item_label}".encode('utf-8')).hexdigest()[:16]

def build_provenance_lock_entry_id(relative_path: str) -> str:
    return hashlib.sha256(f"lock:{relative_path}".encode('utf-8')).hexdigest()[:16]

def build_custody_rehearsal_item_id(custody_step: str) -> str:
    return hashlib.sha256(f"custody:{custody_step}".encode('utf-8')).hexdigest()[:16]

def build_archival_finding_id(title: str) -> str:
    return hashlib.sha256(f"finding:{title}".encode('utf-8')).hexdigest()[:16]

def archival_domain_to_dict(item: ArchivalDomain) -> dict: return asdict(item)
def archival_item_to_dict(item: ArchivalItem) -> dict: return asdict(item)
def provenance_lock_entry_to_dict(item: ProvenanceLockEntry) -> dict: return asdict(item)
def custody_rehearsal_item_to_dict(item: CustodyRehearsalItem) -> dict: return asdict(item)
def archival_finding_to_dict(item: ArchivalFinding) -> dict: return asdict(item)
