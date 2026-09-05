from dataclasses import dataclass
from typing import List, Dict


class ConfigError(Exception):
    """Raised when configuration validation fails."""
    pass


@dataclass(frozen=True)
class DataNormalizationProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 113
    target_final_phase: int = 160
    next_phase: int = 114
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_normalized_data_as_signal: bool = False
    allow_official_approval_claim: bool = False
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
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    enable_canonical_schema_registry: bool = True
    enable_canonical_field_registry: bool = True
    enable_schema_version_normalization: bool = True
    enable_provider_name_normalization: bool = True
    enable_symbol_normalization: bool = True
    enable_region_currency_normalization: bool = True
    enable_timestamp_timezone_normalization: bool = True
    enable_session_alignment_requirements: bool = True
    enable_frequency_normalization: bool = True
    enable_unit_normalization: bool = True
    enable_numeric_type_normalization: bool = True
    enable_string_case_slug_normalization: bool = True
    enable_duplicate_key_normalization: bool = True
    enable_normalized_views: bool = True
    enable_manual_review_queue: bool = True
    enable_phase_114_handoff: bool = True
    min_normalization_score: float = 0.45
    enabled: bool = True
    notes: str = ""

    @property
    def dry_run(self) -> bool:
        return self.dry_run_default


_PROFILES: Dict[str, DataNormalizationProfile] = {
    "balanced_non_destructive_normalization": DataNormalizationProfile(
        name="balanced_non_destructive_normalization",
        description="Phase 113 non-destructive data normalization layer dengeli profili.",
        notes="Phase 113 non-destructive data normalization layer için dengeli profil.",
        min_normalization_score=0.45,
    ),
    "strict_non_destructive_normalization_safety": DataNormalizationProfile(
        name="strict_non_destructive_normalization_safety",
        description="Sıkı güvenlik ve non-destructive kontrollerine odaklı profil.",
        notes="Source overwrite, destructive cleaning, normalized data as signal, official approval, scraping, credential output ve deployment sınırlarını sıkı denetleyen normalization profili.",
        min_normalization_score=0.65,
    ),
    "dry_run_normalization_contract_focus": DataNormalizationProfile(
        name="dry_run_normalization_contract_focus",
        description="Dry-run sözleşme ve fixture doğrulama profili.",
        notes="Gerçek veri indirmeden fixture/contract dataframe’ler üzerinde normalization contract testlerine odaklı profil.",
        min_normalization_score=0.45,
    ),
}


def get_data_normalization_profile(name: str) -> DataNormalizationProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Bilinmeyen data normalization profili: '{name}'. Geçerli profiller: {list(_PROFILES.keys())}")
    return _PROFILES[name]


def list_data_normalization_profiles(enabled_only: bool = True) -> List[DataNormalizationProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def get_default_data_normalization_profile() -> DataNormalizationProfile:
    return get_data_normalization_profile("balanced_non_destructive_normalization")


def validate_data_normalization_profiles() -> None:
    for name, p in _PROFILES.items():
        if p.current_phase != 113:
            raise ConfigError(f"Profil '{name}' current_phase 113 olmalı, bulunan: {p.current_phase}")
        if p.target_final_phase != 160:
            raise ConfigError(f"Profil '{name}' target_final_phase 160 olmalı, bulunan: {p.target_final_phase}")
        if p.next_phase != 114:
            raise ConfigError(f"Profil '{name}' next_phase 114 olmalı, bulunan: {p.next_phase}")
        if not p.dry_run_default:
            raise ConfigError(f"Profil '{name}' dry_run_default True olmalı.")
        if not p.local_only or not p.non_production or not p.research_only:
            raise ConfigError(f"Profil '{name}' local_only, non_production ve research_only True olmalı.")
        if not (0.0 <= p.min_normalization_score <= 1.0):
            raise ConfigError(f"Profil '{name}' min_normalization_score [0, 1] aralığında olmalı: {p.min_normalization_score}")
        # Validate risky allow flags
        risky_flags = [
            ("allow_live_trading", p.allow_live_trading),
            ("allow_broker_integration", p.allow_broker_integration),
            ("allow_real_order", p.allow_real_order),
            ("allow_investment_advice", p.allow_investment_advice),
            ("allow_normalized_data_as_signal", p.allow_normalized_data_as_signal),
            ("allow_official_approval_claim", p.allow_official_approval_claim),
            ("allow_model_deployment", p.allow_model_deployment),
            ("allow_production_deployment", p.allow_production_deployment),
            ("allow_web_server", p.allow_web_server),
            ("allow_dashboard", p.allow_dashboard),
            ("allow_gui_tui", p.allow_gui_tui),
            ("allow_external_llm", p.allow_external_llm),
            ("allow_vector_db", p.allow_vector_db),
            ("allow_embedding_api", p.allow_embedding_api),
            ("allow_web_scraping", p.allow_web_scraping),
            ("allow_html_scraping", p.allow_html_scraping),
            ("allow_news_page_scraping", p.allow_news_page_scraping),
            ("allow_browser_automation_scraping", p.allow_browser_automation_scraping),
            ("allow_hidden_api_reverse_engineering", p.allow_hidden_api_reverse_engineering),
            ("allow_paywall_bypass", p.allow_paywall_bypass),
            ("allow_rate_limit_abuse", p.allow_rate_limit_abuse),
            ("allow_required_network_call", p.allow_required_network_call),
            ("allow_required_paid_api", p.allow_required_paid_api),
            ("allow_credential_output", p.allow_credential_output),
            ("allow_full_article_download", p.allow_full_article_download),
            ("allow_copyrighted_article_copy", p.allow_copyrighted_article_copy),
            ("allow_source_overwrite", p.allow_source_overwrite),
            ("allow_auto_destructive_cleaning", p.allow_auto_destructive_cleaning),
            ("allow_file_deletion", p.allow_file_deletion),
            ("allow_file_move", p.allow_file_move),
            ("allow_overwrite", p.allow_overwrite),
            ("allow_cloud_publish", p.allow_cloud_publish),
            ("allow_docker_push", p.allow_docker_push),
            ("allow_git_tag", p.allow_git_tag),
            ("allow_archive_creation", p.allow_archive_creation),
        ]
        for flag_name, flag_val in risky_flags:
            if flag_val:
                raise ConfigError(f"Profil '{name}' güvenlik ihlali: {flag_name} True olamaz.")
