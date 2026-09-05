from dataclasses import dataclass, asdict

@dataclass
class PreservationDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class PreservationInventoryItem:
    item_id: str
    item_name: str
    item_path: str
    item_family: str
    item_kind: str
    status_label: str
    size_bytes: int | None
    fingerprint: str | None
    warnings: list[str]

@dataclass
class EvidenceVaultItem:
    evidence_id: str
    evidence_name: str
    evidence_area: str
    source_path: str
    vault_status: str
    reading_priority: int
    manual_review_required: bool
    warnings: list[str]

@dataclass
class KnowledgeCapsuleItem:
    capsule_id: str
    topic: str
    summary: str
    source_refs: list[str]
    boundary_note: str
    warnings: list[str]

@dataclass
class PreservationFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_preservation_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}"
def build_preservation_inventory_item_id(item_path: str, item_kind: str) -> str:
    return f"inv_{hash(item_path)}_{item_kind}"
def build_evidence_vault_item_id(evidence_name: str, evidence_area: str) -> str:
    return f"ev_{hash(evidence_name)}_{hash(evidence_area)}"
def build_knowledge_capsule_item_id(topic: str) -> str:
    return f"cap_{hash(topic)}"
def build_preservation_finding_id(title: str) -> str:
    return f"find_{hash(title)}"

def preservation_domain_to_dict(item: PreservationDomain) -> dict: return asdict(item)
def preservation_inventory_item_to_dict(item: PreservationInventoryItem) -> dict: return asdict(item)
def evidence_vault_item_to_dict(item: EvidenceVaultItem) -> dict: return asdict(item)
def knowledge_capsule_item_to_dict(item: KnowledgeCapsuleItem) -> dict: return asdict(item)
def preservation_finding_to_dict(item: PreservationFinding) -> dict: return asdict(item)
