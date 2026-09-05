from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any

@dataclass
class FXProviderProfileItem:
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
    warnings: List[str]
    
    def to_dict(self): return asdict(self)

@dataclass
class FXProviderDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str]
    warnings: List[str]
    
    def to_dict(self): return asdict(self)

@dataclass
class FXPair:
    pair_id: str
    pair: str
    base_currency: str
    quote_currency: str
    pair_group: str
    default_symbol_variants: List[str]
    pip_convention_note: str
    status_label: str
    warnings: List[str]
    
    def to_dict(self): return asdict(self)

@dataclass
class FXCurrencyMetadata:
    currency_id: str
    currency_code: str
    currency_name: str
    region: str
    is_major_currency: bool
    notes: str
    warnings: List[str]
    
    def to_dict(self): return asdict(self)

@dataclass
class FXSymbolNormalizationRule:
    rule_id: str
    canonical_pair: str
    provider_name: str
    provider_symbol_pattern: str
    normalized_symbol: str
    notes: str
    manual_review_required: bool
    
    def to_dict(self): return asdict(self)

@dataclass
class FXProviderCapability:
    capability_id: str
    provider_name: str
    provider_type: str
    pair_groups: List[str]
    data_types: List[str]
    timeframe_support: List[str]
    requires_network: bool
    requires_credentials: bool
    supports_local_cache: bool
    no_scraping_compliant: bool
    status_label: str
    warnings: List[str]
    
    def to_dict(self): return asdict(self)

@dataclass
class FXProviderMetadata:
    provider_id: str
    provider_name: str
    provider_type: str
    description: str
    homepage_ref: str
    license_note: str
    credential_policy: str
    no_scraping_policy: str
    fx_coverage_note: str
    status_label: str
    warnings: List[str]
    
    def to_dict(self): return asdict(self)

@dataclass
class FXProviderRequest:
    request_id: str
    provider_name: str
    data_type: str
    pairs: List[str]
    timeframe: str
    start: Optional[str]
    end: Optional[str]
    dry_run: bool
    local_only: bool
    metadata: Dict[str, Any]
    
    def to_dict(self): return asdict(self)

@dataclass
class FXProviderResponse:
    response_id: str
    request_id: str
    provider_name: str
    data_type: str
    status_label: str
    output_ref: str
    row_count: int
    schema_ref: str
    warnings: List[str]
    manual_review_required: bool
    
    def to_dict(self): return asdict(self)

@dataclass
class FXProviderError:
    error_id: str
    provider_name: str
    error_type: str
    message: str
    retryable: bool
    blocked_by_safety: bool
    recommendation: str
    
    def to_dict(self): return asdict(self)

@dataclass
class FXProviderContractItem:
    contract_id: str
    contract_area: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: List[str]
    manual_review_required: bool
    
    def to_dict(self): return asdict(self)

@dataclass
class FXProviderFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    
    def to_dict(self): return asdict(self)

def build_fx_provider_profile_id(profile_name: str) -> str: return f"profile_{profile_name}"
def build_fx_provider_domain_id(domain_label: str) -> str: return f"domain_{domain_label}"
def build_fx_pair_id(pair: str) -> str: return f"pair_{pair.replace('/', '_')}"
def build_fx_currency_id(currency_code: str) -> str: return f"curr_{currency_code}"
def build_fx_symbol_normalization_rule_id(canonical_pair: str, provider_name: str) -> str: return f"rule_{canonical_pair.replace('/', '_')}_{provider_name}"
def build_fx_provider_capability_id(provider_name: str, data_type: str) -> str: return f"cap_{provider_name}_{data_type}"
def build_fx_provider_metadata_id(provider_name: str) -> str: return f"meta_{provider_name}"
def build_fx_provider_request_id(provider_name: str, data_type: str, timeframe: str) -> str: return f"req_{provider_name}_{data_type}_{timeframe}"
def build_fx_provider_response_id(request_id: str, provider_name: str) -> str: return f"resp_{request_id}_{provider_name}"
def build_fx_provider_error_id(provider_name: str, error_type: str) -> str: return f"err_{provider_name}_{error_type}"
def build_fx_provider_contract_id(contract_area: str) -> str: return f"contract_{contract_area}"
def build_fx_provider_finding_id(title: str) -> str: return f"finding_{title.replace(' ', '_')}"
