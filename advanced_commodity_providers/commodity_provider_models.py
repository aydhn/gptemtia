
from dataclasses import dataclass, asdict

@dataclass
class CommodityProviderProfileItem:
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
class CommodityProviderDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class CommodityItem:
    commodity_id: str
    commodity_name: str
    canonical_symbol: str
    category_label: str
    common_symbol_variants: list[str]
    quote_currency: str
    unit_note: str
    spot_or_futures_note: str
    status_label: str
    warnings: list[str]

@dataclass
class CommodityCategory:
    category_id: str
    category_label: str
    category_name: str
    description: str
    example_symbols: list[str]
    warnings: list[str]

@dataclass
class CommodityMetadata:
    commodity_id: str
    canonical_symbol: str
    commodity_name: str
    category_label: str
    unit_note: str
    contract_note: str
    liquidity_note: str
    data_availability_note: str
    warnings: list[str]

@dataclass
class CommoditySymbolNormalizationRule:
    rule_id: str
    canonical_symbol: str
    provider_name: str
    provider_symbol_pattern: str
    normalized_symbol: str
    notes: str
    manual_review_required: bool

@dataclass
class CommodityProviderCapability:
    capability_id: str
    provider_name: str
    provider_type: str
    commodity_categories: list[str]
    data_types: list[str]
    timeframe_support: list[str]
    requires_network: bool
    requires_credentials: bool
    supports_local_cache: bool
    no_scraping_compliant: bool
    status_label: str
    warnings: list[str]

@dataclass
class CommodityProviderMetadata:
    provider_id: str
    provider_name: str
    provider_type: str
    description: str
    homepage_ref: str
    license_note: str
    credential_policy: str
    no_scraping_policy: str
    commodity_coverage_note: str
    status_label: str
    warnings: list[str]

@dataclass
class CommodityProviderRequest:
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
class CommodityProviderResponse:
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
class CommodityProviderError:
    error_id: str
    provider_name: str
    error_type: str
    message: str
    retryable: bool
    blocked_by_safety: bool
    recommendation: str

@dataclass
class CommodityProviderContractItem:
    contract_id: str
    contract_area: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: list[str]
    manual_review_required: bool

@dataclass
class CommodityProviderFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_commodity_provider_profile_id(profile_name: str) -> str: return f"prf_{profile_name}"
def build_commodity_provider_domain_id(domain_label: str) -> str: return f"dom_{domain_label}"
def build_commodity_id(canonical_symbol: str) -> str: return f"com_{canonical_symbol}"
def build_commodity_category_id(category_label: str) -> str: return f"cat_{category_label}"
def build_commodity_metadata_id(canonical_symbol: str) -> str: return f"meta_{canonical_symbol}"
def build_commodity_symbol_normalization_rule_id(canonical_symbol: str, provider_name: str) -> str: return f"snorm_{canonical_symbol}_{provider_name}"
def build_commodity_provider_capability_id(provider_name: str, data_type: str) -> str: return f"cap_{provider_name}_{data_type}"
def build_commodity_provider_metadata_id(provider_name: str) -> str: return f"pmet_{provider_name}"
def build_commodity_provider_request_id(provider_name: str, data_type: str, timeframe: str) -> str: return f"req_{provider_name}_{data_type}_{timeframe}"
def build_commodity_provider_response_id(request_id: str, provider_name: str) -> str: return f"res_{request_id}_{provider_name}"
def build_commodity_provider_error_id(provider_name: str, error_type: str) -> str: return f"err_{provider_name}_{error_type}"
def build_commodity_provider_contract_id(contract_area: str) -> str: return f"ctr_{contract_area}"
def build_commodity_provider_finding_id(title: str) -> str: return f"fnd_{title.replace(' ', '_').lower()}"

def commodity_provider_request_to_dict(request: CommodityProviderRequest) -> dict: return asdict(request)
def commodity_provider_response_to_dict(response: CommodityProviderResponse) -> dict: return asdict(response)
def commodity_provider_error_to_dict(error: CommodityProviderError) -> dict: return asdict(error)
