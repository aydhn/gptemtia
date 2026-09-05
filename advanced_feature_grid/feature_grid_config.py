from dataclasses import dataclass
from typing import List, Dict


class FeatureGridConfigError(Exception):
    """Raised when an invalid feature grid configuration is detected."""
    pass


@dataclass(frozen=True)
class FeatureGridProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 118
    target_final_phase: int = 160
    next_phase: int = 119
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_feature_grid_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
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
    enable_window_grid_contracts: bool = True
    enable_parameter_grid_registry: bool = True
    enable_naming_registry: bool = True
    enable_output_schema: bool = True
    enable_warmup_nan_policy: bool = True
    enable_no_lookahead_guard: bool = True
    enable_duplicate_detection: bool = True
    enable_moving_average_grid: bool = True
    enable_momentum_grid: bool = True
    enable_volatility_grid: bool = True
    enable_range_channel_grid: bool = True
    enable_mean_reversion_grid: bool = True
    enable_return_grid: bool = True
    enable_quote_placeholders: bool = True
    enable_macro_placeholders: bool = True
    enable_calendar_placeholders: bool = True
    enable_news_metadata_placeholders: bool = True
    enable_computation_rehearsal: bool = True
    enable_metadata_registry: bool = True
    enable_dependency_registry: bool = True
    enable_validation_rules: bool = True
    enable_phase_119_handoff: bool = True
    min_readiness_score: float = 0.45
    enabled: bool = True
    notes: str = ""


FEATURE_GRID_PROFILES: Dict[str, FeatureGridProfile] = {
    "balanced_local_multi_window_feature_grid": FeatureGridProfile(
        name="balanced_local_multi_window_feature_grid",
        description="Phase 118 offline/local multi-window feature grid altyapısı için dengeli profil.",
        current_phase=118,
        target_final_phase=160,
        next_phase=119,
        dry_run_default=True,
        local_only=True,
        non_production=True,
        research_only=True,
        min_readiness_score=0.45,
        notes="Dengeli local/offline feature grid araştırma profili.",
    ),
    "strict_no_signal_feature_grid_safety": FeatureGridProfile(
        name="strict_no_signal_feature_grid_safety",
        description="Feature grid çıktılarının sinyal/yönlü tahmin olarak kullanımını engelleyen sıkı profil.",
        current_phase=118,
        target_final_phase=160,
        next_phase=119,
        dry_run_default=True,
        local_only=True,
        non_production=True,
        research_only=True,
        allow_feature_grid_as_signal=False,
        allow_directional_claim=False,
        allow_strategy_generation=False,
        allow_backtest_execution=False,
        min_readiness_score=0.50,
        notes="Sıkı non-signal ve araştırma sınırları uygulayan profil.",
    ),
    "dry_run_feature_grid_computation_focus": FeatureGridProfile(
        name="dry_run_feature_grid_computation_focus",
        description="Grid hesaplama ve provizyon doğrulama odaklı offline simülasyon profili.",
        current_phase=118,
        target_final_phase=160,
        next_phase=119,
        dry_run_default=True,
        local_only=True,
        non_production=True,
        research_only=True,
        min_readiness_score=0.45,
        notes="Hafif ve hızlı yerel feature grid provizyon odaklı profil.",
    ),
}


def get_feature_grid_profile(name: str) -> FeatureGridProfile:
    if name not in FEATURE_GRID_PROFILES:
        raise FeatureGridConfigError(f"Bilinmeyen feature grid profili: '{name}'. Mevcut profiller: {list(FEATURE_GRID_PROFILES.keys())}")
    return FEATURE_GRID_PROFILES[name]


def list_feature_grid_profiles(enabled_only: bool = True) -> List[FeatureGridProfile]:
    profiles = list(FEATURE_GRID_PROFILES.values())
    if enabled_only:
        profiles = [p for p in profiles if p.enabled]
    return profiles


def validate_feature_grid_profiles() -> None:
    for name, p in FEATURE_GRID_PROFILES.items():
        if p.current_phase != 118:
            raise FeatureGridConfigError(f"Profil {name} current_phase 118 olmalıdır, bulunan: {p.current_phase}")
        if p.target_final_phase != 160:
            raise FeatureGridConfigError(f"Profil {name} target_final_phase 160 olmalıdır, bulunan: {p.target_final_phase}")
        if p.next_phase != 119:
            raise FeatureGridConfigError(f"Profil {name} next_phase 119 olmalıdır, bulunan: {p.next_phase}")
        if not p.local_only or not p.non_production or not p.research_only:
            raise FeatureGridConfigError(f"Profil {name} local_only, non_production ve research_only olmalıdır.")
        if p.allow_live_trading or p.allow_broker_integration or p.allow_real_order:
            raise FeatureGridConfigError(f"Profil {name} canlı trading veya broker izinleri içeremez.")
        if p.allow_feature_grid_as_signal or p.allow_directional_claim or p.allow_strategy_generation:
            raise FeatureGridConfigError(f"Profil {name} feature grid sinyali veya strateji üretimi içeremez.")
        if p.allow_target_label_generation or p.allow_prediction_generation:
            raise FeatureGridConfigError(f"Profil {name} target/label veya prediction üretimi içeremez.")


def get_default_feature_grid_profile() -> FeatureGridProfile:
    return get_feature_grid_profile("balanced_local_multi_window_feature_grid")
