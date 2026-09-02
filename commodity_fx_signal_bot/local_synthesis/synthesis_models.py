from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class PhaseFamily:
    family_id: str
    family_label: str
    family_name: str
    phase_range_hint: str
    description: str
    key_outputs: List[str]
    warnings: List[str]

@dataclass
class MasterIndexItem:
    item_id: str
    item_label: str
    relative_path: str
    family_label: str
    source_layer: str
    file_type: Optional[str]
    size_bytes: Optional[int]
    modified_at_utc: Optional[str]
    status: str
    warnings: List[str]

@dataclass
class FinalMapNode:
    node_id: str
    node_name: str
    family_label: str
    layer_name: str
    description: str
    related_outputs: List[str]
    warnings: List[str]

@dataclass
class FinalBinderSection:
    section_id: str
    section_title: str
    section_label: str
    summary: str
    references: List[str]
    warnings: List[str]

@dataclass
class SynthesisFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: List[str]

def build_phase_family_id(family_label: str) -> str: return f"fam_{family_label}"
def build_master_index_item_id(relative_path: str, item_label: str) -> str: return f"idx_{hash(relative_path)}_{item_label}"
def build_final_map_node_id(node_name: str, family_label: str) -> str: return f"node_{hash(node_name)}_{family_label}"
def build_final_binder_section_id(section_title: str) -> str: return f"sec_{hash(section_title)}"
def build_synthesis_finding_id(title: str) -> str: return f"fnd_{hash(title)}"

def phase_family_to_dict(item: PhaseFamily) -> dict: return asdict(item)
def master_index_item_to_dict(item: MasterIndexItem) -> dict: return asdict(item)
def final_map_node_to_dict(item: FinalMapNode) -> dict: return asdict(item)
def final_binder_section_to_dict(item: FinalBinderSection) -> dict: return asdict(item)
def synthesis_finding_to_dict(item: SynthesisFinding) -> dict: return asdict(item)
