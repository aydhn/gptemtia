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
