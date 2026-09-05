from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class CalendarProviderProfileItem:
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

@dataclass
class CalendarProviderDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str]
    warnings: List[str]

@dataclass
class EconomicEvent:
    event_id: str
    canonical_event: str
    display_name: str
    category_label: str
    region: str
    currency: str
    mapped_macro_indicator: str
    default_importance: str
    release_frequency_note: str
    revision_note: str
    status_label: str
    warnings: List[str]

@dataclass
class EconomicEventCategory:
    category_id: str
    category_label: str
    category_name: str
    description: str
    example_events: List[str]
    warnings: List[str]

@dataclass
class EventImportanceRule:
    rule_id: str
    event_category: str
    region: str
    default_importance: str
    importance_reason: str
    manual_review_required: bool

@dataclass
class EventIndicatorMapping:
    mapping_id: str
    canonical_event: str
    macro_indicator: str
    region: str
    currency: str
    mapping_note: str
    manual_review_required: bool

@dataclass
class CalendarProviderCapability:
    capability_id: str
    provider_name: str
    provider_type: str
    event_categories: List[str]
    data_types: List[str]
    region_support: List[str]
    requires_network: bool
    requires_credentials: bool
    supports_local_cache: bool
    no_scraping_compliant: bool
    status_label: str
    warnings: List[str]

@dataclass
class CalendarProviderMetadata:
    provider_id: str
    provider_name: str
    provider_type: str
    description: str
    homepage_ref: str
    license_note: str
    credential_policy: str
    no_scraping_policy: str
    calendar_coverage_note: str
    status_label: str
    warnings: List[str]

@dataclass
class CalendarProviderRequest:
    request_id: str
    provider_name: str
    data_type: str
    events: List[str]
    region: Optional[str]
    start: Optional[str]
    end: Optional[str]
    dry_run: bool
    local_only: bool
    metadata: dict

@dataclass
class CalendarProviderResponse:
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

@dataclass
class CalendarProviderError:
    error_id: str
    provider_name: str
    error_type: str
    message: str
    retryable: bool
    blocked_by_safety: bool
    recommendation: str

@dataclass
class CalendarProviderContractItem:
    contract_id: str
    contract_area: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: List[str]
    manual_review_required: bool

@dataclass
class CalendarProviderFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_calendar_provider_profile_id(profile_name: str) -> str:
    return f"prof_{profile_name}"

def build_calendar_provider_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}"

def build_economic_event_id(canonical_event: str, region: str) -> str:
    return f"evt_{canonical_event}_{region}".lower()

def build_economic_event_category_id(category_label: str) -> str:
    return f"cat_{category_label}"

def build_event_importance_rule_id(event_category: str, region: str) -> str:
    return f"imp_{event_category}_{region}".lower()

def build_event_indicator_mapping_id(canonical_event: str, macro_indicator: str) -> str:
    return f"map_{canonical_event}_{macro_indicator}".lower()

def build_calendar_provider_capability_id(provider_name: str, data_type: str) -> str:
    return f"cap_{provider_name}_{data_type}".lower()

def build_calendar_provider_metadata_id(provider_name: str) -> str:
    return f"meta_{provider_name}".lower()

def build_calendar_provider_request_id(provider_name: str, data_type: str) -> str:
    return f"req_{provider_name}_{data_type}".lower()

def build_calendar_provider_response_id(request_id: str, provider_name: str) -> str:
    return f"res_{request_id}_{provider_name}".lower()

def build_calendar_provider_error_id(provider_name: str, error_type: str) -> str:
    return f"err_{provider_name}_{error_type}".lower()

def build_calendar_provider_contract_id(contract_area: str) -> str:
    return f"cont_{contract_area}".replace(" ", "_").lower()

def build_calendar_provider_finding_id(title: str) -> str:
    return f"find_{title}".replace(" ", "_").lower()

def to_dict(obj):
    return asdict(obj)
