import os

def w(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

w("advanced_fx_providers/__init__.py", '"""Advanced FX Providers Module."""')

w("advanced_fx_providers/fx_provider_config.py", '''
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class FXProviderProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 107
    target_final_phase: int = 160
    next_phase: int = 108
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_server: bool = False
    allow_dashboard: bool = False
    allow_gui_tui: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_web_scraping: bool = False
    allow_html_scraping: bool = False
    allow_browser_automation_scraping: bool = False
    allow_hidden_api_reverse_engineering: bool = False
    allow_paywall_bypass: bool = False
    allow_rate_limit_abuse: bool = False
    allow_required_network_call: bool = False
    allow_required_paid_api: bool = False
    allow_credential_output: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    enable_major_pairs: bool = True
    enable_minor_pairs: bool = True
    enable_exotic_pairs: bool = True
    enable_cross_rate_requirements: bool = True
    enable_symbol_normalization: bool = True
    enable_manual_file_provider: bool = True
    enable_local_cache_provider: bool = True
    enable_official_api_placeholder: bool = True
    enable_licensed_provider_placeholder: bool = True
    enable_dry_run_fixture_provider: bool = True
    enable_capability_matching: bool = True
    enable_preference_resolution: bool = True
    enable_health_check: bool = True
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

PROFILES = [
    FXProviderProfile(
        name="balanced_no_scraping_fx_provider",
        description="Phase 107 balanced profile for offline no-scraping FX provider testing.",
        notes="Phase 107 no-scraping FX provider layer için dengeli profil."
    ),
    FXProviderProfile(
        name="strict_fx_provider_safety",
        description="Strict safety profile for FX providers.",
        min_readiness_score=0.65,
        min_quality_score=0.65,
        notes="Scraping, credential output, live/broker, deployment, external API zorunluluğu ve yatırım tavsiyesi sınırlarını sıkı denetleyen FX provider profili."
    ),
    FXProviderProfile(
        name="fx_dry_run_fixture_focus",
        description="Dry-run fixture focus profile.",
        notes="Gerçek FX API çağrısı yapmadan FX provider contract ve dry-run fixture testlerine odaklı profil."
    )
]

def get_fx_provider_profile(name: str) -> FXProviderProfile:
    for p in PROFILES:
        if p.name == name:
            return p
    raise ValueError(f"ConfigError: Unknown FX provider profile: {name}")

def list_fx_provider_profiles(enabled_only: bool = True) -> List[FXProviderProfile]:
    if enabled_only:
        return [p for p in PROFILES if p.enabled]
    return PROFILES

def validate_fx_provider_profiles() -> None:
    for p in PROFILES:
        assert p.current_phase == 107
        assert p.target_final_phase == 160
        assert p.next_phase == 108
        assert p.dry_run_default is True
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert not any([
            p.allow_live_trading, p.allow_broker_integration, p.allow_real_order,
            p.allow_investment_advice, p.allow_model_deployment, p.allow_production_deployment,
            p.allow_web_server, p.allow_dashboard, p.allow_gui_tui, p.allow_external_llm,
            p.allow_vector_db, p.allow_embedding_api, p.allow_web_scraping, p.allow_html_scraping,
            p.allow_browser_automation_scraping, p.allow_hidden_api_reverse_engineering,
            p.allow_paywall_bypass, p.allow_rate_limit_abuse, p.allow_required_network_call,
            p.allow_required_paid_api, p.allow_credential_output, p.allow_cloud_publish,
            p.allow_docker_push, p.allow_git_tag, p.allow_archive_creation, p.allow_file_deletion,
            p.allow_file_move, p.allow_overwrite
        ])
        assert 0.0 <= p.min_readiness_score <= 1.0
        assert 0.0 <= p.min_quality_score <= 1.0

def get_default_fx_provider_profile() -> FXProviderProfile:
    return get_fx_provider_profile("balanced_no_scraping_fx_provider")
''')

w("advanced_fx_providers/fx_provider_labels.py", '''
def list_fx_domain_labels() -> list[str]:
    return [
        "fx_provider_profile_domain", "fx_provider_domain", "fx_pair_universe_domain",
        "fx_currency_metadata_domain", "fx_symbol_normalization_domain", "fx_quote_schema_domain",
        "fx_ohlcv_schema_domain", "fx_cross_rate_domain", "fx_provider_capability_domain",
        "fx_provider_metadata_domain", "fx_provider_request_domain", "fx_provider_response_domain",
        "fx_provider_error_domain", "fx_provider_interface_domain", "fx_adapter_contract_domain",
        "fx_provider_registry_domain", "fx_provider_resolver_domain", "fx_provider_preference_domain",
        "fx_provider_matcher_domain", "fx_fixture_domain", "fx_placeholder_domain",
        "fx_output_validation_domain", "fx_safety_domain", "fx_health_domain",
        "fx_quality_domain", "unknown_fx_domain"
    ]

def list_fx_pair_group_labels() -> list[str]:
    return ["fx_major_pair", "fx_minor_pair", "fx_exotic_pair", "fx_cross_pair", "fx_custom_pair", "fx_unknown_pair_group"]

def list_fx_data_type_labels() -> list[str]:
    return ["fx_data_ohlcv", "fx_data_quote", "fx_data_spot_rate", "fx_data_forward_placeholder", "fx_data_symbol_metadata", "fx_data_provider_metadata", "fx_data_unknown"]

def list_fx_provider_status_labels() -> list[str]:
    return ["fx_provider_ready", "fx_provider_ready_with_warnings", "fx_provider_placeholder_only", "fx_provider_missing", "fx_provider_blocked_by_no_scraping_boundary", "fx_provider_needs_manual_review", "fx_provider_unknown"]

def list_fx_risk_labels() -> list[str]:
    return ["fx_provider_critical_risk", "fx_provider_high_risk", "fx_provider_medium_risk", "fx_provider_low_risk", "fx_provider_info", "fx_provider_unknown_risk"]

def validate_fx_domain_label(label: str) -> bool:
    return label in list_fx_domain_labels()

def validate_fx_pair_group_label(label: str) -> bool:
    return label in list_fx_pair_group_labels()

def validate_fx_data_type_label(label: str) -> bool:
    return label in list_fx_data_type_labels()

def validate_fx_provider_status(label: str) -> bool:
    return label in list_fx_provider_status_labels()

def validate_fx_risk_label(label: str) -> bool:
    return label in list_fx_risk_labels()
''')

w("advanced_fx_providers/fx_provider_models.py", '''
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
''')

w("advanced_fx_providers/fx_provider_profile_registry.py", '''
import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderProfileItem, build_fx_provider_profile_id

def build_default_fx_provider_profile_items(profile: FXProviderProfile) -> List[FXProviderProfileItem]:
    return [
        FXProviderProfileItem(
            profile_id=build_fx_provider_profile_id(profile.name),
            profile_name=profile.name,
            current_phase=profile.current_phase,
            target_final_phase=profile.target_final_phase,
            next_phase=profile.next_phase,
            local_only=profile.local_only,
            non_production=profile.non_production,
            research_only=profile.research_only,
            no_scraping=not profile.allow_web_scraping,
            status_label="fx_provider_ready",
            warnings=[]
        )
    ]

def build_fx_provider_profile_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_provider_profile_items(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_provider_profile_registry(df)

def summarize_fx_provider_profile_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if not df.empty else []
    }
''')

w("advanced_fx_providers/fx_provider_domain_registry.py", '''
import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderDomain, build_fx_provider_domain_id
from .fx_provider_labels import list_fx_domain_labels

def build_default_fx_provider_domains(profile: FXProviderProfile) -> List[FXProviderDomain]:
    return [
        FXProviderDomain(
            domain_id=build_fx_provider_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Domain for {lbl}",
            required_outputs=["schema", "registry"],
            warnings=[]
        ) for lbl in list_fx_domain_labels() if lbl != "unknown_fx_domain"
    ]

def build_fx_provider_domain_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_provider_domains(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_provider_domains(df)

def summarize_fx_provider_domains(df: pd.DataFrame) -> Dict:
    return {
        "total_domains": len(df),
        "domains": df["domain_label"].tolist() if not df.empty else []
    }
''')

w("advanced_fx_providers/fx_pair_universe.py", '''
import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXPair, build_fx_pair_id

def build_major_fx_pairs(profile: FXProviderProfile) -> List[FXPair]:
    pairs = [("EUR/USD", "EUR", "USD"), ("GBP/USD", "GBP", "USD"), ("USD/JPY", "USD", "JPY"), 
             ("USD/CHF", "USD", "CHF"), ("USD/CAD", "USD", "CAD"), ("AUD/USD", "AUD", "USD"), 
             ("NZD/USD", "NZD", "USD")]
    return [
        FXPair(
            pair_id=build_fx_pair_id(p[0]), pair=p[0], base_currency=p[1], quote_currency=p[2],
            pair_group="fx_major_pair", default_symbol_variants=[p[0], p[0].replace("/", ""), p[0].replace("/", "_")],
            pip_convention_note="Standard pip mapping", status_label="fx_provider_ready", warnings=[]
        ) for p in pairs
    ]

def build_minor_fx_pairs(profile: FXProviderProfile) -> List[FXPair]:
    pairs = [("EUR/GBP", "EUR", "GBP"), ("EUR/JPY", "EUR", "JPY"), ("GBP/JPY", "GBP", "JPY"), 
             ("EUR/CHF", "EUR", "CHF"), ("AUD/JPY", "AUD", "JPY"), ("CAD/JPY", "CAD", "JPY"), 
             ("AUD/NZD", "AUD", "NZD")]
    return [
        FXPair(
            pair_id=build_fx_pair_id(p[0]), pair=p[0], base_currency=p[1], quote_currency=p[2],
            pair_group="fx_minor_pair", default_symbol_variants=[p[0], p[0].replace("/", ""), p[0].replace("/", "_")],
            pip_convention_note="Standard pip mapping", status_label="fx_provider_ready", warnings=[]
        ) for p in pairs
    ]

def build_exotic_fx_pairs(profile: FXProviderProfile) -> List[FXPair]:
    pairs = [("USD/TRY", "USD", "TRY"), ("EUR/TRY", "EUR", "TRY"), ("USD/MXN", "USD", "MXN"), 
             ("USD/ZAR", "USD", "ZAR"), ("USD/BRL", "USD", "BRL"), ("USD/CNH", "USD", "CNH"), 
             ("USD/SGD", "USD", "SGD")]
    return [
        FXPair(
            pair_id=build_fx_pair_id(p[0]), pair=p[0], base_currency=p[1], quote_currency=p[2],
            pair_group="fx_exotic_pair", default_symbol_variants=[p[0], p[0].replace("/", ""), p[0].replace("/", "_")],
            pip_convention_note="Non-standard pip mapping", status_label="fx_provider_ready", warnings=["Exotic pair - not investment advice"]
        ) for p in pairs
    ]

def build_default_fx_pairs(profile: FXProviderProfile) -> List[FXPair]:
    pairs = []
    if profile.enable_major_pairs: pairs.extend(build_major_fx_pairs(profile))
    if profile.enable_minor_pairs: pairs.extend(build_minor_fx_pairs(profile))
    if profile.enable_exotic_pairs: pairs.extend(build_exotic_fx_pairs(profile))
    return pairs

def build_fx_pair_universe_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_pairs(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_pair_universe(df)

def summarize_fx_pair_universe(df: pd.DataFrame) -> Dict:
    return {
        "total_pairs": len(df),
        "by_group": df["pair_group"].value_counts().to_dict() if not df.empty else {}
    }
''')

w("advanced_fx_providers/fx_currency_metadata.py", '''
import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXCurrencyMetadata, build_fx_currency_id

def build_default_fx_currency_metadata(profile: FXProviderProfile) -> List[FXCurrencyMetadata]:
    currencies = [
        ("USD", "US Dollar", "North America", True),
        ("EUR", "Euro", "Europe", True),
        ("GBP", "British Pound", "Europe", True),
        ("JPY", "Japanese Yen", "Asia", True),
        ("CHF", "Swiss Franc", "Europe", True),
        ("CAD", "Canadian Dollar", "North America", True),
        ("AUD", "Australian Dollar", "Oceania", True),
        ("NZD", "New Zealand Dollar", "Oceania", True),
        ("TRY", "Turkish Lira", "Europe/Asia", False),
        ("MXN", "Mexican Peso", "North America", False),
        ("ZAR", "South African Rand", "Africa", False),
        ("BRL", "Brazilian Real", "South America", False),
        ("CNH", "Offshore Chinese Yuan", "Asia", False),
        ("SGD", "Singapore Dollar", "Asia", False)
    ]
    meta = [
        FXCurrencyMetadata(
            currency_id=build_fx_currency_id(c[0]), currency_code=c[0], currency_name=c[1],
            region=c[2], is_major_currency=c[3], notes="", warnings=[]
        ) for c in currencies
    ]
    meta.append(FXCurrencyMetadata(
        currency_id=build_fx_currency_id("XAU"), currency_code="XAU", currency_name="Gold",
        region="Global", is_major_currency=False, notes="Precious metals handled by commodities provider",
        warnings=["XAU is deferred to Phase 108 commodities provider"]
    ))
    return meta

def build_fx_currency_metadata_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_currency_metadata(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_currency_metadata(df)

def summarize_fx_currency_metadata(df: pd.DataFrame) -> Dict:
    return {
        "total_currencies": len(df),
        "major_count": int(df["is_major_currency"].sum()) if not df.empty else 0
    }
''')
