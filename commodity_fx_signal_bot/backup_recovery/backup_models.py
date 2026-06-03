"""
Data models for backup recovery tracking.
"""

from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class ProjectStateArtifact:
    artifact_id: str
    relative_path: str
    artifact_type: str
    backup_scope: str
    criticality: str
    include_policy: str
    size_bytes: int | None
    content_hash: str | None
    modified_at_utc: str | None
    restore_priority: int
    warnings: list[str]


@dataclass
class BackupPolicy:
    policy_id: str
    scope_label: str
    description: str
    include: bool
    manifest_only: bool
    hash_required: bool
    restore_required: bool
    protected: bool
    warnings: list[str]


@dataclass
class BackupManifest:
    manifest_id: str
    profile_name: str
    created_at_utc: str
    dry_run: bool
    artifact_count: int
    included_count: int
    excluded_count: int
    manifest_only_count: int
    total_size_bytes: int
    artifact_ids: list[str]
    warnings: list[str]


@dataclass
class RestorePlanItem:
    restore_item_id: str
    artifact_id: str
    relative_path: str
    restore_action: str
    restore_priority: int
    dry_run: bool
    overwrite_allowed: bool
    source_available: bool
    target_expected: bool
    warnings: list[str]


@dataclass
class RestoreVerificationResult:
    check_id: str
    check_name: str
    artifact_id: str | None
    status: str
    passed: bool
    details: dict
    warnings: list[str]


def build_project_state_artifact_id(relative_path: str) -> str:
    import hashlib
    return hashlib.md5(relative_path.encode('utf-8')).hexdigest()[:12]


def build_backup_policy_id(scope_label: str) -> str:
    return f"pol_{scope_label}"


def build_backup_manifest_id(profile_name: str, created_at_utc: str) -> str:
    import hashlib
    base = f"{profile_name}_{created_at_utc}"
    return f"man_{hashlib.md5(base.encode('utf-8')).hexdigest()[:12]}"


def build_restore_item_id(artifact_id: str, restore_action: str) -> str:
    return f"res_{artifact_id}_{restore_action[:5]}"


def build_restore_verification_check_id(check_name: str, artifact_id: str | None = None) -> str:
    import hashlib
    base = f"{check_name}_{artifact_id or 'global'}"
    return f"chk_{hashlib.md5(base.encode('utf-8')).hexdigest()[:12]}"


def project_state_artifact_to_dict(artifact: ProjectStateArtifact) -> dict:
    return asdict(artifact)

def backup_policy_to_dict(policy: BackupPolicy) -> dict:
    return asdict(policy)

def backup_manifest_to_dict(manifest: BackupManifest) -> dict:
    return asdict(manifest)

def restore_plan_item_to_dict(item: RestorePlanItem) -> dict:
    return asdict(item)

def restore_verification_result_to_dict(result: RestoreVerificationResult) -> dict:
    return asdict(result)
