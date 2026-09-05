from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass(frozen=True)
class CrossAssetAlignmentProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 119
    target_final_phase: int = 160
    next_phase: int = 120
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_aligned_feature_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
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
    enable_asset_universe_alignment: bool = True
    enable_symbol_mapping: bool = True
    enable_feature_namespace: bool = True
    enable_timestamp_alignment: bool = True
    enable_session_calendar_alignment: bool = True
    enable_feature_matrix_contracts: bool = True
    enable_join_policies: bool = True
    enable_asof_join_policies: bool = True
    enable_no_lookahead_guard: bool = True
    enable_cross_domain_matrix: bool = True
    enable_metadata_registry: bool = True
    enable_domain_alignment_registries: bool = True
    enable_validation_rules: bool = True
    enable_phase_120_handoff: bool = True
    min_readiness_score: float = 0.45
    future_data_allowed: bool = False
    non_signal: bool = True
    enabled: bool = True
    notes: str = ""


_PROFILES: Dict[str, CrossAssetAlignmentProfile] = {
    "balanced_local_cross_asset_alignment": CrossAssetAlignmentProfile(
        name="balanced_local_cross_asset_alignment",
        description="Dengeli yerel cross-asset feature alignment profili (FX, emtia, makro, takvim ve haber metadata).",
        notes="Offline araştırma ve multi-domain matrix contracts için varsayılan profil.",
    ),
    "strict_no_signal_cross_asset_safety": CrossAssetAlignmentProfile(
        name="strict_no_signal_cross_asset_safety",
        description="Sıkı güvenlik ve kesin non-signal/no-lookahead cross-asset alignment profili.",
        notes="Sıfır toleranslı lookahead ve forbidden column kontrolleri.",
    ),
    "dry_run_cross_asset_alignment_focus": CrossAssetAlignmentProfile(
        name="dry_run_cross_asset_alignment_focus",
        description="Dry-run odaklı cross-asset feature alignment profili.",
        notes="Sentetik ve placeholder feature matrix doğrulama odaklı.",
    ),
}


def get_cross_asset_alignment_profile(name: str) -> CrossAssetAlignmentProfile:
    if name not in _PROFILES:
        return get_default_cross_asset_alignment_profile()
    return _PROFILES[name]


def list_cross_asset_alignment_profiles(enabled_only: bool = True) -> List[CrossAssetAlignmentProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def list_available_cross_asset_alignment_profiles() -> List[str]:
    return list(_PROFILES.keys())


def validate_cross_asset_alignment_profile(profile: CrossAssetAlignmentProfile | None = None) -> bool:
    target = profile or get_default_cross_asset_alignment_profile()
    if target.current_phase != 119:
        raise ValueError(f"Profil {target.name} current_phase 119 olmalıdır, bulunan: {target.current_phase}")
    if target.target_final_phase != 160:
        raise ValueError(f"Profil {target.name} target_final_phase 160 olmalıdır, bulunan: {target.target_final_phase}")
    if target.next_phase != 120:
        raise ValueError(f"Profil {target.name} next_phase 120 olmalıdır, bulunan: {target.next_phase}")
    if not target.local_only or not target.non_production or not target.research_only:
        raise ValueError(f"Profil {target.name} local_only, non_production ve research_only True olmalıdır.")
    if target.allow_live_trading or target.allow_broker_integration or target.allow_real_order:
        raise ValueError(f"Profil {target.name} live trading veya broker izni içeremez.")
    if target.allow_aligned_feature_as_signal or target.allow_directional_claim:
        raise ValueError(f"Profil {target.name} feature-as-signal veya directional claim izni içeremez.")
    if target.allow_model_training or target.allow_target_label_generation or target.allow_prediction_generation:
        raise ValueError(f"Profil {target.name} model training, target label veya prediction üretimi izni içeremez.")
    if target.allow_web_scraping or target.allow_html_scraping or target.allow_news_page_scraping:
        raise ValueError(f"Profil {target.name} web/news scraping izni içeremez.")
    return True


def validate_cross_asset_alignment_profiles() -> None:
    for name, p in _PROFILES.items():
        validate_cross_asset_alignment_profile(p)


def get_default_cross_asset_alignment_profile() -> CrossAssetAlignmentProfile:
    return _PROFILES["balanced_local_cross_asset_alignment"]

