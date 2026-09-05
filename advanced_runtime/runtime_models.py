from dataclasses import dataclass, asdict
from typing import List

@dataclass
class RuntimeProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    status_label: str
    warnings: List[str]
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeContextItem:
    context_id: str
    context_area: str
    context_name: str
    source_ref: str
    runtime_role: str
    status_label: str
    manual_review_required: bool
    warnings: List[str]
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeCapabilityItem:
    capability_id: str
    capability_label: str
    capability_name: str
    current_status: str
    future_phase_range: str
    required_by: List[str]
    warnings: List[str]
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeModuleItem:
    module_id: str
    module_area: str
    module_ref: str
    runtime_role: str
    contract_required: bool
    status_label: str
    warnings: List[str]
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeContractItem:
    contract_id: str
    contract_area: str
    contract_name: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: List[str]
    manual_review_required: bool
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeHealthFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    def to_dict(self): return asdict(self)

def build_runtime_profile_id(profile_name: str) -> str: return f"profile_{profile_name}"
def build_runtime_context_id(context_area: str, context_name: str) -> str: return f"ctx_{context_area}_{context_name}"
def build_runtime_capability_id(capability_label: str) -> str: return f"cap_{capability_label}"
def build_runtime_module_id(module_area: str, module_ref: str) -> str: return f"mod_{module_area}_{module_ref}"
def build_runtime_contract_id(contract_area: str, contract_name: str) -> str: return f"ctr_{contract_area}_{contract_name}"
def build_runtime_health_finding_id(title: str) -> str: return f"hlt_{title.replace(' ', '_').lower()}"
