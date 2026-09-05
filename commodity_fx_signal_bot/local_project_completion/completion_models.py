from dataclasses import dataclass, asdict

@dataclass
class CompletionDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class CompletionInventoryItem:
    item_id: str
    item_name: str
    item_path: str
    item_family: str
    item_kind: str
    status_label: str
    size_bytes: int | None
    warnings: list[str]

@dataclass
class CompletionCriterion:
    criterion_id: str
    criterion_name: str
    criterion_area: str
    audit_status: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class CompletionHandoffItem:
    handoff_id: str
    handoff_role: str
    handoff_area: str
    status_label: str
    boundary_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class CompletionFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_completion_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}"

def build_completion_inventory_item_id(item_path: str, item_kind: str) -> str:
    return f"inv_{item_kind}_{hash(item_path) % 100000}"

def build_completion_criterion_id(criterion_name: str, criterion_area: str) -> str:
    return f"crit_{criterion_area}_{hash(criterion_name) % 100000}"

def build_completion_handoff_item_id(handoff_role: str, handoff_area: str) -> str:
    return f"hand_{handoff_role}_{handoff_area}"

def build_completion_finding_id(title: str) -> str:
    return f"find_{hash(title) % 100000}"

def completion_domain_to_dict(item: CompletionDomain) -> dict:
    return asdict(item)

def completion_inventory_item_to_dict(item: CompletionInventoryItem) -> dict:
    return asdict(item)

def completion_criterion_to_dict(item: CompletionCriterion) -> dict:
    return asdict(item)

def completion_handoff_item_to_dict(item: CompletionHandoffItem) -> dict:
    return asdict(item)

def completion_finding_to_dict(item: CompletionFinding) -> dict:
    return asdict(item)
