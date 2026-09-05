"""Phase 121 Feature Validation Profiles and Configuration.

Strictly non-signal, research-only, dry-run default.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class FeatureValidationProfile:
    name: str = ""
    description: str = ""
    profile_name: str = ""
    non_signal: bool = True
    language: str = "tr"
    current_phase: int = 121
    target_final_phase: int = 160
    next_phase: int = 122
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_validation_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
    allow_sentiment_model_output: bool = False
    allow_full_article_usage: bool = False
    allow_official_approval_claim: bool = False
    allow_production_ready_claim: bool = False
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
    enable_forbidden_column_rules: bool = True
    enable_no_lookahead_rules: bool = True
    enable_timestamp_order_validation: bool = True
    enable_asof_join_validation: bool = True
    enable_macro_release_lag_validation: bool = True
    enable_event_window_validation: bool = True
    enable_news_metadata_only_validation: bool = True
    enable_warmup_nan_validation: bool = True
    enable_duplicate_feature_validation: bool = True
    enable_namespace_collision_validation: bool = True
    enable_numeric_sanity_validation: bool = True
    enable_missingness_validation: bool = True
    enable_infinite_value_validation: bool = True
    enable_matrix_integrity_manifest: bool = True
    enable_domain_output_validation: bool = True
    enable_scoring: bool = True
    enable_phase_122_handoff: bool = True
    min_validation_score: float = 0.45
    enabled: bool = True
    notes: str = ""

    def __post_init__(self):
        if not self.name and self.profile_name:
            self.name = self.profile_name
        elif not self.profile_name and self.name:
            self.profile_name = self.name


_PROFILES: Dict[str, FeatureValidationProfile] = {
    "balanced_local_feature_validation": FeatureValidationProfile(
        name="balanced_local_feature_validation",
        description="Dengeli yerel feature doğrulama, lookahead koruması ve sızıntı denetim profili.",
        notes="Offline araştırma, çoklu alan validasyonu ve kalite skorlaması için varsayılan profil.",
    ),
    "strict_no_leakage_feature_validation": FeatureValidationProfile(
        name="strict_no_leakage_feature_validation",
        description="Sıkı sıfır sızıntı, kesin lookahead ve yasaklı kolon denetim profili.",
        notes="Sıfır toleranslı lookahead, negatif shift ve forward return koruma profili.",
    ),
    "dry_run_feature_validation_contract_focus": FeatureValidationProfile(
        name="dry_run_feature_validation_contract_focus",
        description="Sentetik ve kuru çalışma sözleşme doğrulama odaklı feature validasyon profili.",
        notes="Girdi/çıktı kontrat bütünlüğü ve Phase 122 devri için hafifletilmiş kuru çalışma profili.",
    ),
}


def get_feature_validation_profile(name: str) -> FeatureValidationProfile:
    """Retrieve profile by name or raise ValueError if not found."""
    # Support aliases
    alias_map = {
        "default": "balanced_local_feature_validation",
        "strict": "strict_no_leakage_feature_validation",
        "lenient": "dry_run_feature_validation_contract_focus",
        "dry_run": "dry_run_feature_validation_contract_focus",
    }
    resolved = alias_map.get(name, name)
    if resolved not in _PROFILES:
        raise ValueError(
            f"Unknown feature validation profile '{name}'. "
            f"Available profiles: {list(_PROFILES.keys())}"
        )
    return _PROFILES[resolved]


def list_feature_validation_profiles(enabled_only: bool = True) -> List[FeatureValidationProfile]:
    """List registered feature validation profiles."""
    profiles = list(_PROFILES.values())
    if enabled_only:
        profiles = [p for p in profiles if p.enabled]
    return profiles


def validate_feature_validation_profiles() -> None:
    """Validate invariants across all registered profiles."""
    for name, p in _PROFILES.items():
        if p.current_phase != 121:
            raise ValueError(f"Profile '{name}' current_phase must be 121, got {p.current_phase}")
        if p.target_final_phase != 160:
            raise ValueError(f"Profile '{name}' target_final_phase must be 160, got {p.target_final_phase}")
        if p.next_phase != 122:
            raise ValueError(f"Profile '{name}' next_phase must be 122, got {p.next_phase}")
        if not p.dry_run_default:
            raise ValueError(f"Profile '{name}' dry_run_default must be True")
        if not p.local_only or not p.non_production or not p.research_only:
            raise ValueError(f"Profile '{name}' must be local_only, non_production, and research_only")
        if p.allow_live_trading or p.allow_broker_integration or p.allow_real_order:
            raise ValueError(f"Profile '{name}' violates live trading boundaries")
        if p.allow_validation_as_signal or p.allow_directional_claim:
            raise ValueError(f"Profile '{name}' violates non-signal boundary")
        if p.allow_strategy_generation or p.allow_backtest_execution or p.allow_optimizer_execution:
            raise ValueError(f"Profile '{name}' violates strategy/backtest boundary")
        if p.allow_model_training or p.allow_target_label_generation or p.allow_prediction_generation:
            raise ValueError(f"Profile '{name}' violates ML training/label boundary")
        if p.allow_source_overwrite or p.allow_auto_destructive_cleaning:
            raise ValueError(f"Profile '{name}' violates non-destructive boundary")


def get_default_feature_validation_profile() -> FeatureValidationProfile:
    """Return the default feature validation profile."""
    return get_feature_validation_profile("balanced_local_feature_validation")


@dataclass
class FeatureValidationConfig:
    current_phase: int = 121
    target_final_phase: int = 160
    next_phase: int = 122
    dry_run: bool = True
    non_signal: bool = True
    destructive_action_allowed: bool = False
    max_missingness_ratio: float = 0.35
    warmup_window: int = 50


def get_feature_validation_config() -> FeatureValidationConfig:
    return FeatureValidationConfig()

