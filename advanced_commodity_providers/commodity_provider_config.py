
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
