from dataclasses import dataclass, asdict

@dataclass
class GapClosureProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    status_label: str
    warnings: list[str]

@dataclass
class ReadinessReconciliationItem:
    reconciliation_id: str
    foundation_area: str
    source_phase_range: str
    current_state: str
    target_state: str
    reconciliation_status: str
    warnings: list[str]
    manual_review_required: bool

@dataclass
class ClosureMatrixItem:
    closure_id: str
    mvp_area: str
    advanced_target_area: str
    current_phase_support: str
    required_future_phase: str
    closure_status: str
    gap_note: str
    manual_review_required: bool

@dataclass
class MissingFunctionalityItem:
    missing_id: str
    functionality_area: str
    current_gap: str
    required_for_phase: int
    priority_label: str
    risk_label: str
    recommendation: str
    manual_review_required: bool

@dataclass
class DataFoundationRequirement:
    requirement_id: str
    requirement_area: str
    required_for_phase: int
    provider_relevance: str
    no_scraping_constraint: str
    expected_contract: str
    readiness_label: str
    warnings: list[str]

@dataclass
class ContractHandoffItem:
    handoff_id: str
    source_layer: str
    target_layer: str
    contract_area: str
    handoff_summary: str
    handoff_status: str
    manual_review_required: bool

@dataclass
class FunctionalGapFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_gap_closure_profile_id(profile_name: str) -> str: return f"profile_{profile_name}"
def build_readiness_reconciliation_id(foundation_area: str, source_phase_range: str) -> str: return f"recon_{foundation_area}_{source_phase_range}"
def build_closure_matrix_id(mvp_area: str, advanced_target_area: str) -> str: return f"closure_{mvp_area}_{advanced_target_area}"
def build_missing_functionality_id(functionality_area: str, required_for_phase: int) -> str: return f"miss_{functionality_area}_{required_for_phase}"
def build_data_foundation_requirement_id(requirement_area: str, required_for_phase: int) -> str: return f"req_{requirement_area}_{required_for_phase}"
def build_contract_handoff_id(source_layer: str, target_layer: str, contract_area: str) -> str: return f"handoff_{source_layer}_{target_layer}_{contract_area}"
def build_functional_gap_finding_id(title: str) -> str: return f"finding_{title.replace(' ', '_').lower()}"

def to_dict(obj):
    return asdict(obj)
