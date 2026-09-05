from dataclasses import dataclass

@dataclass(frozen=True)
class DataProviderAbstractionProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 106
    target_final_phase: int = 160
    next_phase: int = 107
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

def get_data_provider_abstraction_profile(name: str) -> DataProviderAbstractionProfile:
    if name == "balanced_no_scraping_provider_abstraction":
        return DataProviderAbstractionProfile(
            name=name,
            description="Phase 106 no-scraping multi-provider abstraction için dengeli profil.",
            notes="Phase 106 no-scraping multi-provider abstraction için dengeli profil."
        )
    elif name == "strict_no_scraping_provider_safety":
        return DataProviderAbstractionProfile(
            name=name,
            description="Scraping, credential output, live/broker, deployment, external API zorunluluğu ve yatırım tavsiyesi sınırlarını sıkı denetleyen provider profili.",
            min_readiness_score=0.65,
            min_quality_score=0.65,
            notes="Scraping, credential output, live/broker, deployment, external API zorunluluğu ve yatırım tavsiyesi sınırlarını sıkı denetleyen provider profili."
        )
    elif name == "dry_run_fixture_focus":
        return DataProviderAbstractionProfile(
            name=name,
            description="Gerçek API çağrısı yapmadan provider contract ve dry-run fixture testlerine odaklı profil.",
            enable_dry_run_fixture_provider=True,
            enable_manual_file_provider=True,
            enable_local_cache_provider=True,
            notes="Gerçek API çağrısı yapmadan provider contract ve dry-run fixture testlerine odaklı profil."
        )
    raise ValueError(f"ConfigError: Unknown profile {name}")

def list_data_provider_abstraction_profiles(enabled_only: bool = True) -> list[DataProviderAbstractionProfile]:
    return [
        get_data_provider_abstraction_profile("balanced_no_scraping_provider_abstraction"),
        get_data_provider_abstraction_profile("strict_no_scraping_provider_safety"),
        get_data_provider_abstraction_profile("dry_run_fixture_focus"),
    ]

def validate_data_provider_abstraction_profiles() -> None:
    pass

def get_default_data_provider_abstraction_profile() -> DataProviderAbstractionProfile:
    return get_data_provider_abstraction_profile("balanced_no_scraping_provider_abstraction")
