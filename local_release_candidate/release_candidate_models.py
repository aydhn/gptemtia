from dataclasses import dataclass, asdict

@dataclass
class ReleaseCandidateDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class BaselineInventoryItem:
    item_id: str
    item_name: str
    item_path: str
    item_family: str
    item_kind: str
    size_bytes: int | None
    hash_value: str | None
    baseline_status: str
    warnings: list[str]

@dataclass
class AcceptanceCriterion:
    criterion_id: str
    criterion_name: str
    criterion_area: str
    acceptance_status: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class OperatorSignoffItem:
    signoff_id: str
    signoff_area: str
    signoff_status: str
    boundary_note: str
    evidence_refs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ReleaseCandidateFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_release_candidate_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}"

def build_baseline_inventory_item_id(item_path: str, item_kind: str) -> str:
    import hashlib
    return "inv_" + hashlib.md5(f"{item_path}_{item_kind}".encode()).hexdigest()

def build_acceptance_criterion_id(criterion_name: str, criterion_area: str) -> str:
    import hashlib
    return "acc_" + hashlib.md5(f"{criterion_name}_{criterion_area}".encode()).hexdigest()

def build_operator_signoff_item_id(signoff_area: str) -> str:
    import hashlib
    return "sig_" + hashlib.md5(signoff_area.encode()).hexdigest()

def build_release_candidate_finding_id(title: str) -> str:
    import hashlib
    return "fnd_" + hashlib.md5(title.encode()).hexdigest()

def release_candidate_domain_to_dict(item: ReleaseCandidateDomain) -> dict:
    return asdict(item)

def baseline_inventory_item_to_dict(item: BaselineInventoryItem) -> dict:
    return asdict(item)

def acceptance_criterion_to_dict(item: AcceptanceCriterion) -> dict:
    return asdict(item)

def operator_signoff_item_to_dict(item: OperatorSignoffItem) -> dict:
    return asdict(item)

def release_candidate_finding_to_dict(item: ReleaseCandidateFinding) -> dict:
    return asdict(item)
