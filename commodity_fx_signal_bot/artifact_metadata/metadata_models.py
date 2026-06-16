"""
Data models for Artifact Metadata.
"""

from dataclasses import dataclass, field
import hashlib

@dataclass
class ResearchArtifact:
    artifact_id: str
    relative_path: str
    artifact_type: str
    module_name: str
    title: str
    description: str
    created_or_modified_at_utc: str | None
    content_hash: str | None
    size_bytes: int | None
    use_label: str
    metadata_status: str
    warnings: list[str] = field(default_factory=list)

@dataclass
class ArtifactCard:
    card_id: str
    artifact_id: str
    card_type: str
    title: str
    summary: str
    intended_use: str
    non_use_policy: str
    limitations: list[str]
    inputs: list[str]
    outputs: list[str]
    metrics: dict
    lineage: list[str]
    reproducibility: str
    warnings: list[str] = field(default_factory=list)

@dataclass
class ReproducibilityChecklistItem:
    item_id: str
    artifact_id: str | None
    check_name: str
    status: str
    evidence_path: str | None
    recommendation: str
    warnings: list[str] = field(default_factory=list)

@dataclass
class MetadataExportRecord:
    export_id: str
    artifact_id: str
    card_id: str | None
    export_type: str
    export_path: str
    local_only: bool
    safe_to_share: bool
    warnings: list[str] = field(default_factory=list)

def build_research_artifact_id(relative_path: str) -> str:
    # Build a deterministic artifact ID from relative path
    hash_obj = hashlib.sha256(relative_path.encode('utf-8'))
    return f"art_{hash_obj.hexdigest()[:12]}"

def build_artifact_card_id(artifact_id: str, card_type: str) -> str:
    hash_obj = hashlib.sha256(f"{artifact_id}_{card_type}".encode('utf-8'))
    return f"crd_{hash_obj.hexdigest()[:12]}"

def build_reproducibility_check_id(artifact_id: str | None, check_name: str) -> str:
    art_part = artifact_id if artifact_id else "global"
    hash_obj = hashlib.sha256(f"{art_part}_{check_name}".encode('utf-8'))
    return f"rep_{hash_obj.hexdigest()[:12]}"

def build_metadata_export_id(artifact_id: str, export_type: str) -> str:
    hash_obj = hashlib.sha256(f"{artifact_id}_{export_type}".encode('utf-8'))
    return f"exp_{hash_obj.hexdigest()[:12]}"

def research_artifact_to_dict(item: ResearchArtifact) -> dict:
    return {
        "artifact_id": item.artifact_id,
        "relative_path": item.relative_path,
        "artifact_type": item.artifact_type,
        "module_name": item.module_name,
        "title": item.title,
        "description": item.description,
        "created_or_modified_at_utc": item.created_or_modified_at_utc,
        "content_hash": item.content_hash,
        "size_bytes": item.size_bytes,
        "use_label": item.use_label,
        "metadata_status": item.metadata_status,
        "warnings": ";".join(item.warnings)
    }

def artifact_card_to_dict(item: ArtifactCard) -> dict:
    return {
        "card_id": item.card_id,
        "artifact_id": item.artifact_id,
        "card_type": item.card_type,
        "title": item.title,
        "summary": item.summary,
        "intended_use": item.intended_use,
        "non_use_policy": item.non_use_policy,
        "limitations": ";".join(item.limitations),
        "inputs": ";".join(item.inputs),
        "outputs": ";".join(item.outputs),
        "metrics": str(item.metrics),
        "lineage": ";".join(item.lineage),
        "reproducibility": item.reproducibility,
        "warnings": ";".join(item.warnings)
    }

def reproducibility_checklist_item_to_dict(item: ReproducibilityChecklistItem) -> dict:
    return {
        "item_id": item.item_id,
        "artifact_id": item.artifact_id,
        "check_name": item.check_name,
        "status": item.status,
        "evidence_path": item.evidence_path,
        "recommendation": item.recommendation,
        "warnings": ";".join(item.warnings)
    }

def metadata_export_record_to_dict(item: MetadataExportRecord) -> dict:
    return {
        "export_id": item.export_id,
        "artifact_id": item.artifact_id,
        "card_id": item.card_id,
        "export_type": item.export_type,
        "export_path": item.export_path,
        "local_only": item.local_only,
        "safe_to_share": item.safe_to_share,
        "warnings": ";".join(item.warnings)
    }
