
from dataclasses import dataclass

@dataclass(frozen=True)
class MacroProviderProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 109
    target_final_phase: int = 160
    next_phase: int = 110
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_directional_macro_claim: bool = False
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
    enable_rates_and_yields: bool = True
    enable_inflation: bool = True
    enable_growth: bool = True
    enable_labor: bool = True
    enable_trade_balance: bool = True
    enable_central_bank_policy: bool = True
    enable_liquidity_indicators: bool = True
    enable_risk_sentiment: bool = True
    enable_yield_curve: bool = True
    enable_dxy_placeholder: bool = True
    enable_release_metadata: bool = True
    enable_revision_policy_requirements: bool = True
    enable_frequency_unit_normalization: bool = True
    enable_manual_file_provider: bool = True
    enable_local_cache_provider: bool = True
    enable_official_api_placeholder: bool = True
    enable_licensed_provider_placeholder: bool = True
    enable_public_dataset_placeholder: bool = True
    enable_dry_run_fixture_provider: bool = True
    enable_capability_matching: bool = True
    enable_preference_resolution: bool = True
    enable_health_check: bool = True
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

def get_default_macro_provider_profile() -> MacroProviderProfile:
    return MacroProviderProfile(
        name="balanced_no_scraping_macro_provider",
        description="Phase 109 no-scraping macro provider layer için dengeli profil.",
        notes="Phase 109 no-scraping macro provider layer için dengeli profil."
    )

def get_macro_provider_profile(name: str) -> MacroProviderProfile:
    if name == "balanced_no_scraping_macro_provider":
        return get_default_macro_provider_profile()
    elif name == "strict_macro_provider_safety":
        return MacroProviderProfile(
            name="strict_macro_provider_safety",
            description="Strict safety profile",
            min_readiness_score=0.65,
            min_quality_score=0.65,
            notes="Scraping, credential output, live/broker, deployment, external API zorunluluğu, yönlü makro iddia ve yatırım tavsiyesi sınırlarını sıkı denetleyen macro provider profili."
        )
    elif name == "macro_dry_run_fixture_focus":
        return MacroProviderProfile(
            name="macro_dry_run_fixture_focus",
            description="Dry run focus",
            notes="Gerçek macro API çağrısı yapmadan macro provider contract ve dry-run fixture testlerine odaklı profil."
        )
    raise ValueError(f"Unknown profile {name}")

def list_macro_provider_profiles(enabled_only: bool = True) -> list[MacroProviderProfile]:
    return [
        get_default_macro_provider_profile(),
        get_macro_provider_profile("strict_macro_provider_safety"),
        get_macro_provider_profile("macro_dry_run_fixture_focus")
    ]

def validate_macro_provider_profiles() -> None:
    pass
