"""Phase 122 Factor Metadata Configuration and Profile Management.

Provides immutable profile configurations for factor taxonomy, contracts,
dependencies, and quality handoffs. Strictly non-signal, local/offline, and research-only.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class FactorMetadataProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 122
    target_final_phase: int = 160
    next_phase: int = 123
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_factor_as_signal: bool = False
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
    enable_family_registry: bool = True
    enable_contract_registry: bool = True
    enable_input_feature_sets: bool = True
    enable_namespace_registry: bool = True
    enable_output_schema: bool = True
    enable_dependency_registry: bool = True
    enable_validation_dependencies: bool = True
    enable_quality_dependencies: bool = True
    enable_technical_factors: bool = True
    enable_macro_event_news_factors: bool = True
    enable_cross_asset_context_factors: bool = True
    enable_regime_prep_placeholders: bool = True
    enable_composite_factor_placeholders: bool = True
    enable_manifest: bool = True
    enable_manual_review: bool = True
    enable_phase_123_handoff: bool = True
    min_readiness_score: float = 0.45
    enabled: bool = True
    notes: str = ""


_PROFILES: Dict[str, FactorMetadataProfile] = {
    "balanced_local_factor_metadata": FactorMetadataProfile(
        name="balanced_local_factor_metadata",
        description="Dengeli yerel faktör metadata, taksonomi ve sözleşme profili.",
        notes="Standart yerel araştırma faktör metadata profili. Tamamen sinyalsiz ve güvenli.",
    ),
    "strict_non_signal_factor_metadata": FactorMetadataProfile(
        name="strict_non_signal_factor_metadata",
        description="Katı sinyalsiz yönetişim ve sözleşme doğrulama odaklı faktör profili.",
        notes="Sıkı yasaklı kolon ve no-lookahead doğrulaması gerektiren profil.",
    ),
    "dry_run_factor_contract_focus": FactorMetadataProfile(
        name="dry_run_factor_contract_focus",
        description="Hızlı dry-run sözleşme ve bağımlılık test profili.",
        notes="Geliştirme ve test süreçleri için hafifleştirilmiş dry-run profili.",
    ),
}


def get_factor_metadata_profile(name: str) -> FactorMetadataProfile:
    """Retrieve factor metadata profile by name or default to balanced profile."""
    if name in _PROFILES:
        return _PROFILES[name]
    return _PROFILES["balanced_local_factor_metadata"]


def list_factor_metadata_profiles(enabled_only: bool = True) -> List[FactorMetadataProfile]:
    """List all available factor metadata profiles."""
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_factor_metadata_profiles() -> None:
    """Validate all configured profiles adhere to safety invariants."""
    for p in _PROFILES.values():
        if p.current_phase != 122:
            raise ValueError(f"Profile {p.name} current_phase must be 122")
        if p.target_final_phase != 160:
            raise ValueError(f"Profile {p.name} target_final_phase must be 160")
        if p.next_phase != 123:
            raise ValueError(f"Profile {p.name} next_phase must be 123")
        if not p.dry_run_default or not p.local_only or not p.non_production or not p.research_only:
            raise ValueError(f"Profile {p.name} must enforce local, dry_run, non-production constraints")
        if (
            p.allow_live_trading
            or p.allow_broker_integration
            or p.allow_real_order
            or p.allow_investment_advice
            or p.allow_factor_as_signal
            or p.allow_directional_claim
            or p.allow_strategy_generation
            or p.allow_backtest_execution
            or p.allow_optimizer_execution
            or p.allow_model_training
            or p.allow_target_label_generation
            or p.allow_prediction_generation
            or p.allow_sentiment_model_output
            or p.allow_full_article_usage
            or p.allow_official_approval_claim
            or p.allow_production_ready_claim
            or p.allow_model_deployment
            or p.allow_production_deployment
            or p.allow_web_server
            or p.allow_dashboard
            or p.allow_gui_tui
            or p.allow_external_llm
            or p.allow_vector_db
            or p.allow_embedding_api
            or p.allow_web_scraping
            or p.allow_html_scraping
            or p.allow_news_page_scraping
            or p.allow_browser_automation_scraping
            or p.allow_hidden_api_reverse_engineering
            or p.allow_paywall_bypass
            or p.allow_rate_limit_abuse
            or p.allow_required_network_call
            or p.allow_required_paid_api
            or p.allow_credential_output
            or p.allow_full_article_download
            or p.allow_copyrighted_article_copy
            or p.allow_source_overwrite
            or p.allow_auto_destructive_cleaning
            or p.allow_file_deletion
            or p.allow_file_move
            or p.allow_overwrite
            or p.allow_cloud_publish
            or p.allow_docker_push
            or p.allow_git_tag
            or p.allow_archive_creation
        ):
            raise ValueError(f"Profile {p.name} violates safety invariant permissions")


def get_default_factor_metadata_profile() -> FactorMetadataProfile:
    """Return default profile for Phase 122."""
    return _PROFILES["balanced_local_factor_metadata"]
