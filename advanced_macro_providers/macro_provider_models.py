
from dataclasses import dataclass, asdict

@dataclass
class MacroProviderProfileItem:
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
class MacroProviderDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class MacroIndicator:
    indicator_id: str
    canonical_indicator: str
    display_name: str
    category_label: str
    region: str
    currency: str
    default_frequency: str
    unit: str
    release_lag_note: str
    revision_note: str
    status_label: str
    warnings: list[str]

@dataclass
class MacroIndicatorCategory:
    category_id: str
    category_label: str
    category_name: str
    description: str
    example_indicators: list[str]
    warnings: list[str]

@dataclass
class MacroRegionMetadata:
    region_id: str
    region_code: str
    region_name: str
    currency_code: str
    central_bank_ref: str
    notes: str
    warnings: list[str]

@dataclass
class MacroSymbolNormalizationRule:
    rule_id: str
    canonical_indicator: str
    provider_name: str
    provider_symbol_pattern: str
    normalized_symbol: str
    notes: str
    manual_review_required: bool

@dataclass
class MacroProviderCapability:
    capability_id: str
    provider_name: str
    provider_type: str
    macro_categories: list[str]
    data_types: list[str]
    frequency_support: list[str]
    region_support: list[str]
    requires_network: bool
    requires_credentials: bool
    supports_local_cache: bool
    no_scraping_compliant: bool
    status_label: str
    warnings: list[str]

@dataclass
class MacroProviderMetadata:
    provider_id: str
    provider_name: str
    provider_type: str
    description: str
    homepage_ref: str
    license_note: str
    credential_policy: str
    no_scraping_policy: str
    macro_coverage_note: str
    status_label: str
    warnings: list[str]

@dataclass
class MacroProviderRequest:
    request_id: str
    provider_name: str
    data_type: str
    indicators: list[str]
    region: str | None
    frequency: str
    start: str | None
    end: str | None
    dry_run: bool
    local_only: bool
    metadata: dict

@dataclass
class MacroProviderResponse:
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
class MacroProviderError:
    error_id: str
    provider_name: str
    error_type: str
    message: str
    retryable: bool
    blocked_by_safety: bool
    recommendation: str

@dataclass
class MacroProviderContractItem:
    contract_id: str
    contract_area: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: list[str]
    manual_review_required: bool

@dataclass
class MacroProviderFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_macro_provider_profile_id(profile_name: str) -> str: return f"profile_{profile_name}"
def build_macro_provider_domain_id(domain_label: str) -> str: return f"domain_{domain_label}"
def build_macro_indicator_id(canonical_indicator: str, region: str) -> str: return f"ind_{canonical_indicator}_{region}"
def build_macro_category_id(category_label: str) -> str: return f"cat_{category_label}"
def build_macro_region_id(region_code: str) -> str: return f"reg_{region_code}"
def build_macro_symbol_normalization_rule_id(canonical_indicator: str, provider_name: str) -> str: return f"norm_{canonical_indicator}_{provider_name}"
def build_macro_provider_capability_id(provider_name: str, data_type: str) -> str: return f"cap_{provider_name}_{data_type}"
def build_macro_provider_metadata_id(provider_name: str) -> str: return f"meta_{provider_name}"
def build_macro_provider_request_id(provider_name: str, data_type: str, frequency: str) -> str: return f"req_{provider_name}_{data_type}_{frequency}"
def build_macro_provider_response_id(request_id: str, provider_name: str) -> str: return f"res_{request_id}_{provider_name}"
def build_macro_provider_error_id(provider_name: str, error_type: str) -> str: return f"err_{provider_name}_{error_type}"
def build_macro_provider_contract_id(contract_area: str) -> str: return f"contract_{contract_area}"
def build_macro_provider_finding_id(title: str) -> str: return f"find_{title}"
