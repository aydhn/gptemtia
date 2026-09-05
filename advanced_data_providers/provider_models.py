from dataclasses import dataclass, asdict

@dataclass
class ProviderProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    no_scraping: bool
    status_label: str
    warnings: list[str]

@dataclass
class ProviderDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ProviderTypeItem:
    provider_type_id: str
    provider_type_label: str
    provider_type_name: str
    description: str
    allowed_network: bool
    requires_credentials: bool
    placeholder_only: bool
    warnings: list[str]

@dataclass
class ProviderCapability:
    capability_id: str
    provider_name: str
    provider_type: str
    asset_coverage: list[str]
    data_types: list[str]
    timeframe_support: list[str]
    requires_network: bool
    requires_credentials: bool
    supports_local_cache: bool
    no_scraping_compliant: bool
    status_label: str
    warnings: list[str]

@dataclass
class ProviderMetadata:
    provider_id: str
    provider_name: str
    provider_type: str
    description: str
    homepage_ref: str
    license_note: str
    credential_policy: str
    no_scraping_policy: str
    status_label: str
    warnings: list[str]

@dataclass
class ProviderRequest:
    request_id: str
    provider_name: str
    data_type: str
    symbols: list[str]
    timeframe: str
    start: str | None
    end: str | None
    dry_run: bool
    local_only: bool
    metadata: dict

@dataclass
class ProviderResponse:
    response_id: str
    request_id: str
    provider_name: str
    data_type: str
    status_label: str
    output_ref: str
    row_count: int
    schema_ref: str
    warnings: list[str]
    manual_review_required: bool

@dataclass
class ProviderError:
    error_id: str
    provider_name: str
    error_type: str
    message: str
    retryable: bool
    blocked_by_safety: bool
    recommendation: str

@dataclass
class ProviderContractItem:
    contract_id: str
    contract_area: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: list[str]
    manual_review_required: bool

@dataclass
class ProviderFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_provider_profile_id(profile_name: str) -> str: return f"profile_{profile_name}"
def build_provider_domain_id(domain_label: str) -> str: return f"domain_{domain_label}"
def build_provider_type_id(provider_type_label: str) -> str: return f"type_{provider_type_label}"
def build_provider_capability_id(provider_name: str, data_type: str) -> str: return f"cap_{provider_name}_{data_type}"
def build_provider_metadata_id(provider_name: str) -> str: return f"meta_{provider_name}"
def build_provider_request_id(provider_name: str, data_type: str, timeframe: str) -> str: return f"req_{provider_name}_{data_type}_{timeframe}"
def build_provider_response_id(request_id: str, provider_name: str) -> str: return f"resp_{request_id}_{provider_name}"
def build_provider_error_id(provider_name: str, error_type: str) -> str: return f"err_{provider_name}_{error_type}"
def build_provider_contract_id(contract_area: str) -> str: return f"contract_{contract_area}"
def build_provider_finding_id(title: str) -> str: return f"finding_{title}"
