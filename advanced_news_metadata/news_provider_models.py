from dataclasses import dataclass, asdict, field
from typing import List, Optional, Dict, Any

@dataclass
class NewsProviderProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    no_scraping: bool
    metadata_only: bool
    status_label: str
    warnings: List[str] = field(default_factory=list)

@dataclass
class NewsDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

@dataclass
class NewsSource:
    source_id: str
    source_name: str
    source_category: str
    region: str
    coverage_note: str
    license_note: str
    metadata_only_policy: str
    no_scraping_policy: str
    status_label: str
    warnings: List[str]

@dataclass
class NewsSourceCategory:
    category_id: str
    category_label: str
    category_name: str
    description: str
    example_sources: List[str]
    warnings: List[str]

@dataclass
class NewsMetadataSchemaField:
    field_id: str
    field_name: str
    field_type: str
    description: str
    required: bool
    privacy_copyright_note: str
    manual_review_required: bool

@dataclass
class NewsItemReferenceField:
    field_id: str
    field_name: str
    field_type: str
    description: str
    required: bool
    no_full_text_policy: str
    manual_review_required: bool

@dataclass
class NewsTag:
    tag_id: str
    tag_label: str
    tag_domain: str
    mapped_entity: str
    description: str
    manual_review_required: bool

@dataclass
class NewsEventLinkage:
    linkage_id: str
    news_topic: str
    linked_calendar_event: str
    linked_macro_indicator: str
    linked_asset_or_commodity: str
    linkage_note: str
    manual_review_required: bool

@dataclass
class NewsProviderCapability:
    capability_id: str
    provider_name: str
    provider_type: str
    source_categories: List[str]
    data_types: List[str]
    topic_support: List[str]
    region_support: List[str]
    requires_network: bool
    requires_credentials: bool
    supports_local_cache: bool
    metadata_only: bool
    no_scraping_compliant: bool
    copyright_safe: bool
    status_label: str
    warnings: List[str]

@dataclass
class NewsProviderMetadata:
    provider_id: str
    provider_name: str
    provider_type: str
    description: str
    homepage_ref: str
    license_note: str
    credential_policy: str
    no_scraping_policy: str
    metadata_only_policy: str
    copyright_policy: str
    news_coverage_note: str
    status_label: str
    warnings: List[str]

@dataclass
class NewsProviderRequest:
    request_id: str
    provider_name: str
    data_type: str
    topics: List[str] = field(default_factory=list)
    asset_tags: List[str] = field(default_factory=list)
    region: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    dry_run: bool = True
    local_only: bool = True
    metadata_only: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class NewsProviderResponse:
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
class NewsProviderError:
    error_id: str
    provider_name: str
    error_type: str
    message: str
    retryable: bool
    blocked_by_safety: bool
    recommendation: str

@dataclass
class NewsProviderContractItem:
    contract_id: str
    contract_area: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: List[str]
    manual_review_required: bool

@dataclass
class NewsProviderFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_news_provider_profile_id(profile_name: str) -> str:
    return f"prof_{profile_name}".lower()

def build_news_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}".lower()

def build_news_source_id(source_name: str) -> str:
    return f"src_{source_name}".lower()

def build_news_source_category_id(category_label: str) -> str:
    return f"cat_{category_label}".lower()

def build_news_schema_field_id(field_name: str) -> str:
    return f"fld_{field_name}".lower()

def build_news_item_reference_field_id(field_name: str) -> str:
    return f"ref_fld_{field_name}".lower()

def build_news_tag_id(tag_label: str, tag_domain: str) -> str:
    return f"tag_{tag_domain}_{tag_label}".lower()

def build_news_event_linkage_id(news_topic: str, linked_calendar_event: str) -> str:
    return f"link_{news_topic}_{linked_calendar_event}".lower()

def build_news_provider_capability_id(provider_name: str, data_type: str) -> str:
    return f"cap_{provider_name}_{data_type}".lower()

def build_news_provider_metadata_id(provider_name: str) -> str:
    return f"meta_{provider_name}".lower()

def build_news_provider_request_id(provider_name: str, data_type: str) -> str:
    return f"req_{provider_name}_{data_type}".lower()

def build_news_provider_response_id(request_id: str, provider_name: str) -> str:
    return f"res_{request_id}_{provider_name}".lower()

def build_news_provider_error_id(provider_name: str, error_type: str) -> str:
    return f"err_{provider_name}_{error_type}".lower()

def build_news_provider_contract_id(contract_area: str) -> str:
    return f"cont_{contract_area}".replace(" ", "_").lower()

def build_news_provider_finding_id(title: str) -> str:
    return f"find_{title}".replace(" ", "_").lower()

def to_dict(obj: Any) -> Dict[str, Any]:
    return asdict(obj)
