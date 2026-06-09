from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class EvidenceArtifact:
    artifact_id: str
    relative_path: str
    artifact_label: str
    module_name: str
    evidence_title: str
    evidence_summary: str
    created_or_modified_at_utc: Optional[str]
    content_hash: Optional[str]
    size_bytes: Optional[int]
    freshness_label: str
    warnings: list[str]

@dataclass
class PolicyItem:
    policy_id: str
    policy_name: str
    policy_domain: str
    description: str
    local_only: bool
    official_compliance_claim: bool
    controls: list[str]
    warnings: list[str]

@dataclass
class ControlItem:
    control_id: str
    control_name: str
    control_domain: str
    description: str
    required_evidence_labels: list[str]
    optional_evidence_labels: list[str]
    status: str
    warnings: list[str]

@dataclass
class ControlEvidenceMapping:
    mapping_id: str
    control_id: str
    artifact_id: str
    mapping_strength: str
    status: str
    evidence_path: str
    warnings: list[str]

@dataclass
class EvidenceGap:
    gap_id: str
    control_id: str
    gap_type: str
    description: str
    severity: str
    recommended_safe_follow_up: str
    warnings: list[str]

def build_evidence_artifact_id(relative_path: str) -> str:
    import hashlib
    return f"art_{hashlib.md5(relative_path.encode()).hexdigest()[:10]}"

def build_policy_id(policy_name: str, policy_domain: str) -> str:
    import hashlib
    s = f"{policy_domain}_{policy_name}"
    return f"pol_{hashlib.md5(s.encode()).hexdigest()[:10]}"

def build_control_id(control_name: str, control_domain: str) -> str:
    import hashlib
    s = f"{control_domain}_{control_name}"
    return f"ctl_{hashlib.md5(s.encode()).hexdigest()[:10]}"

def build_control_evidence_mapping_id(control_id: str, artifact_id: str) -> str:
    import hashlib
    s = f"{control_id}_{artifact_id}"
    return f"map_{hashlib.md5(s.encode()).hexdigest()[:10]}"

def build_evidence_gap_id(control_id: str, gap_type: str) -> str:
    import hashlib
    s = f"{control_id}_{gap_type}"
    return f"gap_{hashlib.md5(s.encode()).hexdigest()[:10]}"

def evidence_artifact_to_dict(item: EvidenceArtifact) -> dict:
    return asdict(item)

def policy_item_to_dict(item: PolicyItem) -> dict:
    return asdict(item)

def control_item_to_dict(item: ControlItem) -> dict:
    return asdict(item)

def control_evidence_mapping_to_dict(item: ControlEvidenceMapping) -> dict:
    return asdict(item)

def evidence_gap_to_dict(item: EvidenceGap) -> dict:
    return asdict(item)
