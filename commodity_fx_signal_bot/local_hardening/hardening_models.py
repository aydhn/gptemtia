
from dataclasses import dataclass, asdict

@dataclass
class HardeningDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_checks: list[str]
    warnings: list[str]

@dataclass
class DeadCodeCandidate:
    candidate_id: str
    relative_path: str
    symbol_name: str | None
    candidate_label: str
    evidence_hint: str
    confidence: str
    recommendation: str
    warnings: list[str]

@dataclass
class ContractSurfaceItem:
    contract_id: str
    contract_label: str
    surface_name: str
    source_path: str
    callable_or_key: str | None
    expected_inputs: list[str]
    expected_outputs: list[str]
    stability_note: str
    warnings: list[str]

@dataclass
class FreezeManifestItem:
    item_id: str
    item_name: str
    item_type: str
    source_path: str | None
    freeze_status: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class HardeningFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_hardening_domain_id(domain_label: str) -> str: return f"dom_{domain_label}"
def build_dead_code_candidate_id(relative_path: str, symbol_name: str | None, candidate_label: str) -> str: return f"dc_{relative_path}_{symbol_name}"
def build_contract_surface_id(contract_label: str, surface_name: str, callable_or_key: str | None = None) -> str: return f"cs_{contract_label}_{surface_name}"
def build_freeze_manifest_item_id(item_name: str, item_type: str) -> str: return f"fm_{item_type}_{item_name}"
def build_hardening_finding_id(title: str) -> str: return f"hf_{title}"

def hardening_domain_to_dict(item: HardeningDomain) -> dict: return asdict(item)
def dead_code_candidate_to_dict(item: DeadCodeCandidate) -> dict: return asdict(item)
def contract_surface_item_to_dict(item: ContractSurfaceItem) -> dict: return asdict(item)
def freeze_manifest_item_to_dict(item: FreezeManifestItem) -> dict: return asdict(item)
def hardening_finding_to_dict(item: HardeningFinding) -> dict: return asdict(item)
