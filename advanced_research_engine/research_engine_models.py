from dataclasses import dataclass, asdict

@dataclass
class ResearchEngineProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    status_label: str
    warnings: list[str]

@dataclass
class ResearchEngineDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ResearchContextItem:
    context_id: str
    context_area: str
    context_name: str
    source_ref: str
    research_role: str
    status_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ResearchRequest:
    request_id: str
    request_type: str
    universe: list[str]
    timeframe: str
    horizon: str
    requested_modules: list[str]
    dry_run: bool
    local_only: bool
    metadata: dict

@dataclass
class ResearchResult:
    result_id: str
    request_id: str
    result_type: str
    status_label: str
    output_ref: str
    summary: dict
    warnings: list[str]
    manual_review_required: bool

@dataclass
class ResearchInterfaceContract:
    contract_id: str
    interface_name: str
    input_contract: str
    output_contract: str
    future_phase_range: str
    forbidden_behavior: list[str]
    manual_review_required: bool

@dataclass
class ResearchGatewayItem:
    gateway_id: str
    gateway_area: str
    interface_ref: str
    target_module_ref: str
    future_phase_range: str
    gateway_status: str
    warnings: list[str]

@dataclass
class ResearchEngineFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_research_engine_profile_id(profile_name: str) -> str: return f"prof_{profile_name}"
def build_research_engine_domain_id(domain_label: str) -> str: return f"dom_{domain_label}"
def build_research_context_id(context_area: str, context_name: str) -> str: return f"ctx_{context_area}_{context_name}"
def build_research_request_id(request_type: str, timeframe: str, horizon: str) -> str: return f"req_{request_type}_{timeframe}_{horizon}"
def build_research_result_id(request_id: str, result_type: str) -> str: return f"res_{request_id}_{result_type}"
def build_research_interface_contract_id(interface_name: str) -> str: return f"int_{interface_name}"
def build_research_gateway_id(gateway_area: str, interface_ref: str) -> str: return f"gw_{gateway_area}_{interface_ref}"
def build_research_engine_finding_id(title: str) -> str: return f"find_{hash(title)}"
