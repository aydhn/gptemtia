import os
from pathlib import Path

def generate_modules():
    base_dir = Path("advanced_commodity_providers")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    (base_dir / "__init__.py").write_text("", encoding="utf-8")
    
    config_code = """
from dataclasses import dataclass, field

@dataclass(frozen=True)
class CommodityProviderProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 108
    target_final_phase: int = 160
    next_phase: int = 109
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_futures_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_futures_advice: bool = False
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
    enable_precious_metals: bool = True
    enable_energy: bool = True
    enable_industrial_metals: bool = True
    enable_agriculture: bool = True
    enable_spot_schema: bool = True
    enable_futures_contract_metadata: bool = True
    enable_continuous_contract_requirements: bool = True
    enable_roll_adjustment_requirements: bool = True
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

def get_commodity_provider_profile(name: str) -> CommodityProviderProfile:
    profiles = {
        "balanced_no_scraping_commodity_provider": CommodityProviderProfile(
            name="balanced_no_scraping_commodity_provider",
            description="Phase 108 no-scraping commodities provider layer için dengeli profil.",
            notes="Phase 108 no-scraping commodities provider layer için dengeli profil."
        ),
        "strict_commodity_provider_safety": CommodityProviderProfile(
            name="strict_commodity_provider_safety",
            description="Scraping, credential output, futures broker, live/broker, deployment, external API zorunluluğu ve yatırım tavsiyesi sınırlarını sıkı denetleyen commodity provider profili.",
            min_readiness_score=0.65,
            min_quality_score=0.65,
            notes="Scraping, credential output, futures broker, live/broker, deployment, external API zorunluluğu ve yatırım tavsiyesi sınırlarını sıkı denetleyen commodity provider profili."
        ),
        "commodity_dry_run_fixture_focus": CommodityProviderProfile(
            name="commodity_dry_run_fixture_focus",
            description="Gerçek commodity API çağrısı yapmadan commodities provider contract ve dry-run fixture testlerine odaklı profil.",
            enable_dry_run_fixture_provider=True,
            enable_manual_file_provider=True,
            enable_local_cache_provider=True,
            notes="Gerçek commodity API çağrısı yapmadan commodities provider contract ve dry-run fixture testlerine odaklı profil."
        )
    }
    if name not in profiles:
        raise ValueError(f"ConfigError: Bilinmeyen profile {name}")
    return profiles[name]

def list_commodity_provider_profiles(enabled_only: bool = True) -> list[CommodityProviderProfile]:
    profiles = [
        get_commodity_provider_profile("balanced_no_scraping_commodity_provider"),
        get_commodity_provider_profile("strict_commodity_provider_safety"),
        get_commodity_provider_profile("commodity_dry_run_fixture_focus")
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_commodity_provider_profiles() -> None:
    for p in list_commodity_provider_profiles(enabled_only=False):
        if p.current_phase != 108: raise ValueError("current_phase 108 olmalı")
        if p.target_final_phase != 160: raise ValueError("target_final_phase 160 olmalı")
        if p.next_phase != 109: raise ValueError("next_phase 109 olmalı")
        if not p.dry_run_default: raise ValueError("dry_run_default True olmalı")
        if not p.local_only: raise ValueError("local_only True olmalı")
        if not p.non_production: raise ValueError("non_production True olmalı")
        if not p.research_only: raise ValueError("research_only True olmalı")
        if p.allow_live_trading or p.allow_web_scraping: raise ValueError("riskli allow flagleri False olmalı")
        if not (0.0 <= p.min_readiness_score <= 1.0): raise ValueError("score 0-1 aralığında olmalı")

def get_default_commodity_provider_profile() -> CommodityProviderProfile:
    return get_commodity_provider_profile("balanced_no_scraping_commodity_provider")
"""
    (base_dir / "commodity_provider_config.py").write_text(config_code, encoding="utf-8")

    labels_code = """
def list_commodity_domain_labels() -> list[str]:
    return [
        "commodity_provider_profile_domain", "commodity_provider_domain", "commodity_universe_domain",
        "commodity_category_domain", "commodity_metadata_domain", "commodity_symbol_normalization_domain",
        "commodity_spot_schema_domain", "commodity_ohlcv_schema_domain", "commodity_futures_contract_domain",
        "commodity_continuous_contract_domain", "commodity_roll_adjustment_domain", "commodity_provider_capability_domain",
        "commodity_provider_metadata_domain", "commodity_provider_request_domain", "commodity_provider_response_domain",
        "commodity_provider_error_domain", "commodity_provider_interface_domain", "commodity_adapter_contract_domain",
        "commodity_provider_registry_domain", "commodity_provider_resolver_domain", "commodity_provider_preference_domain",
        "commodity_provider_matcher_domain", "commodity_fixture_domain", "commodity_placeholder_domain",
        "commodity_output_validation_domain", "commodity_safety_domain", "commodity_health_domain",
        "commodity_quality_domain", "unknown_commodity_domain"
    ]

def list_commodity_category_labels() -> list[str]:
    return [
        "commodity_precious_metals", "commodity_energy", "commodity_industrial_metals",
        "commodity_agriculture", "commodity_livestock_placeholder", "commodity_softs", "commodity_unknown_category"
    ]

def list_commodity_data_type_labels() -> list[str]:
    return [
        "commodity_data_spot", "commodity_data_ohlcv", "commodity_data_futures_contract_metadata",
        "commodity_data_continuous_contract_placeholder", "commodity_data_symbol_metadata",
        "commodity_data_provider_metadata", "commodity_data_unknown"
    ]

def list_commodity_provider_status_labels() -> list[str]:
    return [
        "commodity_provider_ready", "commodity_provider_ready_with_warnings", "commodity_provider_placeholder_only",
        "commodity_provider_missing", "commodity_provider_blocked_by_no_scraping_boundary",
        "commodity_provider_needs_manual_review", "commodity_provider_unknown"
    ]

def list_commodity_risk_labels() -> list[str]:
    return [
        "commodity_provider_critical_risk", "commodity_provider_high_risk", "commodity_provider_medium_risk",
        "commodity_provider_low_risk", "commodity_provider_info", "commodity_provider_unknown_risk"
    ]

def validate_commodity_domain_label(label: str) -> bool: return label in list_commodity_domain_labels()
def validate_commodity_category_label(label: str) -> bool: return label in list_commodity_category_labels()
def validate_commodity_data_type_label(label: str) -> bool: return label in list_commodity_data_type_labels()
def validate_commodity_provider_status(label: str) -> bool: return label in list_commodity_provider_status_labels()
def validate_commodity_risk_label(label: str) -> bool: return label in list_commodity_risk_labels()
"""
    (base_dir / "commodity_provider_labels.py").write_text(labels_code, encoding="utf-8")

    models_code = """
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
"""
    (base_dir / "commodity_provider_models.py").write_text(models_code, encoding="utf-8")

if __name__ == "__main__":
    generate_modules()
    print("Core modules generated.")
