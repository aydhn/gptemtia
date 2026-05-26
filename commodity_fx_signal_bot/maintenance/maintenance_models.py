"""Data models for the maintenance subsystem."""
from dataclasses import dataclass, asdict
from typing import Optional, List
import hashlib

@dataclass
class StorageArtifactRecord:
    artifact_id: str
    path: str
    relative_path: str
    artifact_type: str
    retention_category: str
    size_bytes: Optional[int]
    modified_at_utc: Optional[str]
    age_days: Optional[float]
    extension: str
    protected: bool
    lifecycle_label: str
    warnings: List[str]

@dataclass
class RetentionPolicy:
    policy_id: str
    retention_category: str
    description: str
    keep_days: Optional[int]
    keep_latest_n: Optional[int]
    protected: bool
    archive_before_cleanup: bool
    dry_run_only: bool
    warnings: List[str]

@dataclass
class MaintenanceCandidate:
    candidate_id: str
    artifact_id: str
    path: str
    action_label: str
    reason: str
    size_bytes: Optional[int]
    age_days: Optional[float]
    policy_id: Optional[str]
    dry_run: bool
    protected: bool
    warnings: List[str]

@dataclass
class ArchiveManifest:
    archive_id: str
    archive_name: str
    created_at_utc: str
    archive_format: str
    candidate_count: int
    total_size_bytes: int
    candidate_artifact_ids: List[str]
    manifest_path: Optional[str]
    dry_run: bool
    warnings: List[str]

@dataclass
class MaintenancePlan:
    plan_id: str
    plan_name: str
    created_at_utc: str
    dry_run: bool
    cleanup_candidate_count: int
    archive_candidate_count: int
    protected_count: int
    estimated_reclaimable_bytes: int
    warnings: List[str]


def build_storage_artifact_id(relative_path: str, size_bytes: Optional[int] = None, modified_at_utc: Optional[str] = None) -> str:
    base = f"{relative_path}_{size_bytes}_{modified_at_utc}"
    return hashlib.sha256(base.encode()).hexdigest()[:16]

def build_retention_policy_id(retention_category: str) -> str:
    return f"policy_{retention_category}"

def build_maintenance_candidate_id(artifact_id: str, action_label: str) -> str:
    return f"cand_{artifact_id}_{action_label}"

def build_archive_id(archive_name: str, created_at_utc: str) -> str:
    base = f"{archive_name}_{created_at_utc}"
    return f"arch_{hashlib.sha256(base.encode()).hexdigest()[:16]}"

def build_maintenance_plan_id(plan_name: str, created_at_utc: str) -> str:
    base = f"{plan_name}_{created_at_utc}"
    return f"plan_{hashlib.sha256(base.encode()).hexdigest()[:16]}"

def storage_artifact_record_to_dict(record: StorageArtifactRecord) -> dict:
    return asdict(record)

def retention_policy_to_dict(policy: RetentionPolicy) -> dict:
    return asdict(policy)

def maintenance_candidate_to_dict(candidate: MaintenanceCandidate) -> dict:
    return asdict(candidate)

def archive_manifest_to_dict(manifest: ArchiveManifest) -> dict:
    return asdict(manifest)

def maintenance_plan_to_dict(plan: MaintenancePlan) -> dict:
    return asdict(plan)
