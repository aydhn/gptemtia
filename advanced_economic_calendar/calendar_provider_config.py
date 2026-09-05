from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class CalendarProviderProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 110
    target_final_phase: int = 160
    next_phase: int = 111
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_event_directional_claim: bool = False
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
    enable_release_events: bool = True
    enable_central_bank_events: bool = True
    enable_inflation_events: bool = True
    enable_labor_events: bool = True
    enable_growth_events: bool = True
    enable_pmi_sentiment_events: bool = True
    enable_energy_inventory_events: bool = True
    enable_event_importance: bool = True
    enable_event_indicator_mapping: bool = True
    enable_surprise_requirements: bool = True
    enable_time_normalization_requirements: bool = True
    enable_revision_handling_requirements: bool = True
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

def get_calendar_provider_profile(name: str) -> CalendarProviderProfile:
    profiles = {p.name: p for p in list_calendar_provider_profiles(enabled_only=False)}
    if name not in profiles:
        raise ValueError(f"Unknown profile: {name}")
    return profiles[name]

def list_calendar_provider_profiles(enabled_only: bool = True) -> List[CalendarProviderProfile]:
    profiles = [
        CalendarProviderProfile(
            name="balanced_no_scraping_calendar_provider",
            description="Phase 110 no-scraping economic calendar provider layer dengeli profil.",
            notes="Phase 110 no-scraping economic calendar provider layer için dengeli profil."
        ),
        CalendarProviderProfile(
            name="strict_calendar_provider_safety",
            description="Strict safety calendar provider profile.",
            min_readiness_score=0.65,
            min_quality_score=0.65,
            notes="Scraping, credential output, live/broker, deployment, external API zorunluluğu, event directional claim ve yatırım tavsiyesi sınırlarını sıkı denetleyen calendar provider profili."
        ),
        CalendarProviderProfile(
            name="calendar_dry_run_fixture_focus",
            description="Dry run fixture focused calendar provider profile.",
            enable_dry_run_fixture_provider=True,
            enable_manual_file_provider=True,
            enable_local_cache_provider=True,
            notes="Gerçek economic calendar API çağrısı yapmadan calendar provider contract ve dry-run fixture testlerine odaklı profil."
        )
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_calendar_provider_profiles() -> None:
    for profile in list_calendar_provider_profiles(enabled_only=False):
        if profile.current_phase != 110:
            raise ValueError(f"current_phase must be 110, got {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"target_final_phase must be 160, got {profile.target_final_phase}")
        if profile.next_phase != 111:
            raise ValueError(f"next_phase must be 111, got {profile.next_phase}")
        if not profile.dry_run_default:
            raise ValueError("dry_run_default must be True")
        if not (profile.local_only and profile.non_production and profile.research_only):
            raise ValueError("local_only, non_production, research_only must be True")
        if any([
            profile.allow_live_trading, profile.allow_broker_integration, profile.allow_real_order,
            profile.allow_investment_advice, profile.allow_event_directional_claim, profile.allow_model_deployment,
            profile.allow_production_deployment, profile.allow_web_server, profile.allow_dashboard,
            profile.allow_gui_tui, profile.allow_external_llm, profile.allow_vector_db, profile.allow_embedding_api,
            profile.allow_web_scraping, profile.allow_html_scraping, profile.allow_browser_automation_scraping,
            profile.allow_hidden_api_reverse_engineering, profile.allow_paywall_bypass, profile.allow_rate_limit_abuse,
            profile.allow_required_network_call, profile.allow_required_paid_api, profile.allow_credential_output,
            profile.allow_cloud_publish, profile.allow_docker_push, profile.allow_git_tag, profile.allow_archive_creation,
            profile.allow_file_deletion, profile.allow_file_move, profile.allow_overwrite
        ]):
            raise ValueError("All risk allow flags must be False")
        if not (0.0 <= profile.min_readiness_score <= 1.0) or not (0.0 <= profile.min_quality_score <= 1.0):
            raise ValueError("Scores must be between 0 and 1")

def get_default_calendar_provider_profile() -> CalendarProviderProfile:
    return get_calendar_provider_profile("balanced_no_scraping_calendar_provider")
