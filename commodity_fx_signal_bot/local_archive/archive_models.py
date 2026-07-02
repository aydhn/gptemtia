"""
Archive Models Module
Defines the data structures used in local archive processes.
"""

from dataclasses import dataclass, asdict
from typing import Optional, List
import hashlib

@dataclass
class ArchiveDomain:
    domain_id: str
    domain_name: str
    domain_label: str
    description: str
    retention_label: str
    required_artifacts: List[str]
    warnings: List[str]

@dataclass
class ArchiveItem:
    item_id: str
    relative_path: str
    domain_label: str
    item_status: str
    retention_label: str
    size_bytes: Optional[int]
    modified_at_utc: Optional[str]
    content_hash: Optional[str]
    integrity_status: str
    warnings: List[str]

@dataclass
class SnapshotCatalogItem:
    snapshot_id: str
    snapshot_name: str
    created_at_utc: str
    snapshot_scope: str
    item_count: int
    local_only: bool
    manifest_path: Optional[str]
    warnings: List[str]

@dataclass
class RetentionPolicyItem:
    policy_id: str
    domain_label: str
    retention_label: str
    review_interval_days: int
    rationale: str
    manual_review_required: bool
    warnings: List[str]

@dataclass
class ArchiveFinding:
    finding_id: str
    domain_label: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: List[str]

def build_archive_domain_id(domain_name: str) -> str:
    hash_object = hashlib.md5(domain_name.encode('utf-8'))
    return f"dom_{hash_object.hexdigest()[:8]}"

def build_archive_item_id(relative_path: str) -> str:
    hash_object = hashlib.sha1(relative_path.encode('utf-8'))
    return f"itm_{hash_object.hexdigest()[:12]}"

def build_snapshot_id(snapshot_name: str, created_at_utc: str) -> str:
    combined = f"{snapshot_name}_{created_at_utc}"
    hash_object = hashlib.md5(combined.encode('utf-8'))
    return f"snp_{hash_object.hexdigest()[:10]}"

def build_retention_policy_id(domain_label: str, retention_label: str) -> str:
    combined = f"{domain_label}_{retention_label}"
    hash_object = hashlib.md5(combined.encode('utf-8'))
    return f"ret_{hash_object.hexdigest()[:8]}"

def build_archive_finding_id(domain_label: str, title: str) -> str:
    combined = f"{domain_label}_{title}"
    hash_object = hashlib.sha1(combined.encode('utf-8'))
    return f"fnd_{hash_object.hexdigest()[:10]}"

def archive_domain_to_dict(item: ArchiveDomain) -> dict:
    return asdict(item)

def archive_item_to_dict(item: ArchiveItem) -> dict:
    return asdict(item)

def snapshot_catalog_item_to_dict(item: SnapshotCatalogItem) -> dict:
    return asdict(item)

def retention_policy_item_to_dict(item: RetentionPolicyItem) -> dict:
    return asdict(item)

def archive_finding_to_dict(item: ArchiveFinding) -> dict:
    return asdict(item)
