from dataclasses import dataclass
from typing import List

class ConfigError(ValueError):
    """Configuration error for news metadata provider profiles."""
    pass

@dataclass(frozen=True)
class NewsProviderProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 111
    target_final_phase: int = 160
    next_phase: int = 112
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_news_directional_claim: bool = False
    allow_sentiment_as_signal: bool = False
    allow_full_article_download: bool = False
    allow_copyrighted_article_copy: bool = False
    allow_model_deployment: bool = False
    allow_nlp_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_server: bool = False
    allow_dashboard: bool = False
    allow_gui_tui: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_web_scraping: bool = False
    allow_news_page_scraping: bool = False
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
    enable_source_registry: bool = True
    enable_metadata_schema: bool = True
    enable_item_reference_schema: bool = True
    enable_asset_tags: bool = True
    enable_macro_tags: bool = True
    enable_commodity_tags: bool = True
    enable_fx_tags: bool = True
    enable_event_linkage: bool = True
    enable_topic_taxonomy: bool = True
    enable_sentiment_placeholder_requirements: bool = True
    enable_impact_placeholder_requirements: bool = True
    enable_freshness_requirements: bool = True
    enable_deduplication_requirements: bool = True
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

    @property
    def dry_run(self) -> bool:
        return self.dry_run_default

    @property
    def no_scraping(self) -> bool:
        return not self.allow_web_scraping

    @property
    def metadata_only(self) -> bool:
        return not self.allow_full_article_download

def get_news_provider_profile(name: str) -> NewsProviderProfile:
    profiles = {p.name: p for p in list_news_provider_profiles(enabled_only=False)}
    if name not in profiles:
        raise ConfigError(f"Unknown news provider profile: {name}")
    return profiles[name]

def list_news_provider_profiles(enabled_only: bool = True) -> List[NewsProviderProfile]:
    profiles = [
        NewsProviderProfile(
            name="balanced_no_scraping_news_metadata_provider",
            description="Phase 111 no-scraping news metadata provider layer için dengeli profil.",
            notes="Phase 111 no-scraping news metadata provider layer için dengeli profil."
        ),
        NewsProviderProfile(
            name="strict_news_metadata_safety",
            description="Scraping, haber tam metni toplama, telifli içerik kopyalama, credential output, live/broker, deployment, sentiment-as-signal ve yatırım tavsiyesi sınırlarını sıkı denetleyen news metadata profili.",
            min_readiness_score=0.65,
            min_quality_score=0.65,
            notes="Scraping, haber tam metni toplama, telifli içerik kopyalama, credential output, live/broker, deployment, sentiment-as-signal ve yatırım tavsiyesi sınırlarını sıkı denetleyen news metadata profili."
        ),
        NewsProviderProfile(
            name="news_metadata_dry_run_fixture_focus",
            description="Gerçek news provider API çağrısı yapmadan news metadata provider contract ve dry-run fixture testlerine odaklı profil.",
            enable_dry_run_fixture_provider=True,
            enable_manual_file_provider=True,
            enable_local_cache_provider=True,
            notes="Gerçek news provider API çağrısı yapmadan news metadata provider contract ve dry-run fixture testlerine odaklı profil."
        )
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_news_provider_profiles() -> dict:
    errors = []
    for profile in list_news_provider_profiles(enabled_only=False):
        if profile.current_phase != 111:
            errors.append(f"current_phase must be 111, got {profile.current_phase}")
        if profile.target_final_phase != 160:
            errors.append(f"target_final_phase must be 160, got {profile.target_final_phase}")
        if profile.next_phase != 112:
            errors.append(f"next_phase must be 112, got {profile.next_phase}")
        if not profile.dry_run_default:
            errors.append("dry_run_default must be True")
        if not (profile.local_only and profile.non_production and profile.research_only):
            errors.append("local_only, non_production, research_only must be True")
        if any([
            profile.allow_live_trading, profile.allow_broker_integration, profile.allow_real_order,
            profile.allow_investment_advice, profile.allow_news_directional_claim, profile.allow_sentiment_as_signal,
            profile.allow_full_article_download, profile.allow_copyrighted_article_copy,
            profile.allow_model_deployment, profile.allow_nlp_model_deployment,
            profile.allow_production_deployment, profile.allow_web_server, profile.allow_dashboard,
            profile.allow_gui_tui, profile.allow_external_llm, profile.allow_vector_db, profile.allow_embedding_api,
            profile.allow_web_scraping, profile.allow_news_page_scraping, profile.allow_html_scraping,
            profile.allow_browser_automation_scraping, profile.allow_hidden_api_reverse_engineering,
            profile.allow_paywall_bypass, profile.allow_rate_limit_abuse,
            profile.allow_required_network_call, profile.allow_required_paid_api, profile.allow_credential_output,
            profile.allow_cloud_publish, profile.allow_docker_push, profile.allow_git_tag, profile.allow_archive_creation,
            profile.allow_file_deletion, profile.allow_file_move, profile.allow_overwrite
        ]):
            errors.append("All risk allow flags must be False")
        if not (0.0 <= profile.min_readiness_score <= 1.0) or not (0.0 <= profile.min_quality_score <= 1.0):
            errors.append("Scores must be between 0 and 1")
    return {"valid": len(errors) == 0, "errors": errors}

def get_default_news_provider_profile() -> NewsProviderProfile:
    return get_news_provider_profile("balanced_no_scraping_news_metadata_provider")
