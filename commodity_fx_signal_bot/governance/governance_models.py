import hashlib
from dataclasses import asdict, dataclass


@dataclass
class ArtifactRecord:
    artifact_id: str
    artifact_type: str
    path: str
    relative_path: str
    file_name: str
    extension: str
    size_bytes: int | None
    modified_at_utc: str | None
    created_at_utc: str | None
    row_count: int | None
    column_count: int | None
    schema_fingerprint: str | None
    content_fingerprint: str | None
    warnings: list[str]

@dataclass
class ProvenanceRecord:
    provenance_id: str
    artifact_id: str
    artifact_type: str
    source_system: str
    producer_module: str | None
    producer_script: str | None
    run_id: str | None
    experiment_id: str | None
    timeframe: str | None
    symbols: list[str]
    parameters_hash: str | None
    input_artifact_ids: list[str]
    created_at_utc: str
    warnings: list[str]

@dataclass
class LineageNode:
    node_id: str
    artifact_id: str
    artifact_type: str
    label: str
    path: str | None
    metadata: dict
    warnings: list[str]

@dataclass
class LineageEdge:
    edge_id: str
    source_node_id: str
    target_node_id: str
    relation: str
    confidence_score: float
    metadata: dict
    warnings: list[str]

@dataclass
class AuditTrailRecord:
    audit_id: str
    event_label: str
    artifact_id: str | None
    actor: str
    event_timestamp_utc: str
    description: str
    metadata: dict
    warnings: list[str]

def _hash_str(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def build_artifact_id(relative_path: str, size_bytes: int | None = None, modified_at_utc: str | None = None) -> str:
    components = [relative_path]
    if size_bytes is not None:
        components.append(str(size_bytes))
    if modified_at_utc is not None:
        components.append(modified_at_utc)
    return _hash_str("_".join(components))

def build_provenance_id(artifact_id: str, producer_module: str | None = None) -> str:
    components = [artifact_id]
    if producer_module:
        components.append(producer_module)
    return _hash_str("_".join(components))

def build_lineage_node_id(artifact_id: str) -> str:
    return f"node_{artifact_id}"

def build_lineage_edge_id(source_node_id: str, target_node_id: str, relation: str) -> str:
    return _hash_str(f"{source_node_id}_{relation}_{target_node_id}")

def build_audit_id(event_label: str, artifact_id: str | None, timestamp_utc: str) -> str:
    components = [event_label]
    if artifact_id:
        components.append(artifact_id)
    components.append(timestamp_utc)
    return _hash_str("_".join(components))

def artifact_record_to_dict(record: ArtifactRecord) -> dict:
    return asdict(record)

def provenance_record_to_dict(record: ProvenanceRecord) -> dict:
    return asdict(record)

def lineage_node_to_dict(node: LineageNode) -> dict:
    return asdict(node)

def lineage_edge_to_dict(edge: LineageEdge) -> dict:
    return asdict(edge)

def audit_trail_record_to_dict(record: AuditTrailRecord) -> dict:
    return asdict(record)
