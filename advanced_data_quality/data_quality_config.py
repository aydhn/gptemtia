from dataclasses import dataclass
from typing import List

class ConfigError(ValueError):
    """Configuration error for data quality profiles."""
    pass

@dataclass(frozen=True)
class DataQualityProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 112
    target_final_phase: int = 160
    next_phase: int = 113
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_quality_score_as_signal: bool = False
    allow_provider_official_approval: bool = False
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
    allow_news_page_scraping: bool = False
    allow_browser_automation_scraping: bool = False
    allow_hidden_api_reverse_engineering: bool = False
    allow_paywall_bypass: bool = False
    allow_rate_limit_abuse: bool = False
    allow_required_network_call: bool = False
    allow_required_paid_api: bool = False
    allow_credential_output: bool = False
    allow_full_article_download: bool = False
    allow_copyrighted_article_copy: bool = False
    allow_auto_overwrite_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    enable_schema_compliance: bool = True
    enable_missing_checks: bool = True
    enable_stale_checks: bool = True
    enable_duplicate_checks: bool = True
    enable_outlier_placeholder_checks: bool = True
    enable_timestamp_integrity: bool = True
    enable_frequency_unit_consistency: bool = True
    enable_fx_quality_rules: bool = True
    enable_commodity_quality_rules: bool = True
    enable_macro_quality_rules: bool = True
    enable_calendar_quality_rules: bool = True
    enable_news_metadata_quality_rules: bool = True
    enable_provider_metadata_quality_rules: bool = True
    enable_ohlc_consistency: bool = True
    enable_quote_consistency: bool = True
    enable_event_release_consistency: bool = True
    enable_news_copyright_quality: bool = True
    enable_manual_review_queue: bool = True
    enable_provider_quality_score: bool = True
    enable_dataset_quality_score: bool = True
    min_dataset_quality_score: float = 0.45
    min_provider_quality_score: float = 0.45
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


def list_data_quality_profiles(enabled_only: bool = True) -> List[DataQualityProfile]:
    profiles = [
        DataQualityProfile(
            name="balanced_local_data_quality",
            description="Phase 112 local/offline data quality engine için dengeli profil.",
            current_phase=112,
            target_final_phase=160,
            next_phase=113,
            dry_run_default=True,
            local_only=True,
            non_production=True,
            research_only=True,
            min_dataset_quality_score=0.45,
            min_provider_quality_score=0.45,
            notes="Phase 112 local/offline data quality engine için dengeli profil."
        ),
        DataQualityProfile(
            name="strict_data_quality_safety",
            description="Quality score’un sinyal/official approval gibi sunulmasını, scraping’i, overwrite cleaning’i, credential output’u ve deployment’ı sıkı engelleyen data quality profili.",
            current_phase=112,
            target_final_phase=160,
            next_phase=113,
            dry_run_default=True,
            local_only=True,
            non_production=True,
            research_only=True,
            min_dataset_quality_score=0.65,
            min_provider_quality_score=0.65,
            notes="Quality score’un sinyal/official approval gibi sunulmasını, scraping’i, overwrite cleaning’i, credential output’u ve deployment’ı sıkı engelleyen data quality profili."
        ),
        DataQualityProfile(
            name="dry_run_quality_contract_focus",
            description="Gerçek veri indirmeden fixture/contract dataframe’ler üzerinde kalite kontratlarını test eden profil.",
            current_phase=112,
            target_final_phase=160,
            next_phase=113,
            dry_run_default=True,
            local_only=True,
            non_production=True,
            research_only=True,
            notes="Gerçek veri indirmeden fixture/contract dataframe’ler üzerinde kalite kontratlarını test eden profil."
        )
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles


def get_data_quality_profile(name: str) -> DataQualityProfile:
    profiles = {p.name: p for p in list_data_quality_profiles(enabled_only=False)}
    if name not in profiles:
        raise ConfigError(f"Unknown data quality profile: {name}")
    return profiles[name]


def validate_data_quality_profiles() -> None:
    for profile in list_data_quality_profiles(enabled_only=False):
        if profile.current_phase != 112:
            raise ConfigError(f"current_phase must be 112, got {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ConfigError(f"target_final_phase must be 160, got {profile.target_final_phase}")
        if profile.next_phase != 113:
            raise ConfigError(f"next_phase must be 113, got {profile.next_phase}")
        if not profile.dry_run_default:
            raise ConfigError("dry_run_default must be True")
        if not (profile.local_only and profile.non_production and profile.research_only):
            raise ConfigError("local_only, non_production, research_only must be True")
        if any([
            profile.allow_live_trading, profile.allow_broker_integration, profile.allow_real_order,
            profile.allow_investment_advice, profile.allow_quality_score_as_signal, profile.allow_provider_official_approval,
            profile.allow_model_deployment, profile.allow_production_deployment,
            profile.allow_web_server, profile.allow_dashboard, profile.allow_gui_tui,
            profile.allow_external_llm, profile.allow_vector_db, profile.allow_embedding_api,
            profile.allow_web_scraping, profile.allow_html_scraping, profile.allow_news_page_scraping,
            profile.allow_browser_automation_scraping, profile.allow_hidden_api_reverse_engineering,
            profile.allow_paywall_bypass, profile.allow_rate_limit_abuse,
            profile.allow_required_network_call, profile.allow_required_paid_api, profile.allow_credential_output,
            profile.allow_full_article_download, profile.allow_copyrighted_article_copy,
            profile.allow_auto_overwrite_cleaning, profile.allow_file_deletion, profile.allow_file_move,
            profile.allow_overwrite, profile.allow_cloud_publish, profile.allow_docker_push,
            profile.allow_git_tag, profile.allow_archive_creation
        ]):
            raise ConfigError("All dangerous allow flags must be False")
        if not (0.0 <= profile.min_dataset_quality_score <= 1.0) or not (0.0 <= profile.min_provider_quality_score <= 1.0):
            raise ConfigError("Quality scores must be between 0.0 and 1.0")


def get_default_data_quality_profile() -> DataQualityProfile:
    return get_data_quality_profile("balanced_local_data_quality")
