"""Phase 123 Feature Quality and Drift Diagnostics Configuration.

Provides immutable profile configurations for feature and factor-level quality metrics,
drift diagnostics, stability monitoring, and safety invariants. Strictly non-signal,
local/offline, and research-only.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class FeatureQualityDriftProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 123
    target_final_phase: int = 160
    next_phase: int = 124
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_quality_as_signal: bool = False
    allow_drift_as_signal: bool = False
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
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    enable_quality_metrics: bool = True
    enable_drift_metrics: bool = True
    enable_missingness: bool = True
    enable_infinite_value: bool = True
    enable_all_nan: bool = True
    enable_zero_variance: bool = True
    enable_duplicate_values: bool = True
    enable_distribution_summary: bool = True
    enable_distribution_drift: bool = True
    enable_rolling_stability: bool = True
    enable_staleness: bool = True
    enable_namespace_quality: bool = True
    enable_factor_quality: bool = True
    enable_macro_cross_asset_quality: bool = True
    enable_findings: bool = True
    enable_scoring: bool = True
    enable_manifest: bool = True
    enable_phase_124_handoff: bool = True
    min_quality_score: float = 0.45
    min_drift_score: float = 0.45
    enabled: bool = True
    notes: str = ""


_PROFILES: Dict[str, FeatureQualityDriftProfile] = {
    "balanced_local_feature_quality_drift": FeatureQualityDriftProfile(
        name="balanced_local_feature_quality_drift",
        description="Dengeli yerel özellik kalite ve drift teşhis profili.",
        notes="Standart yerel araştırma profilidir. Bütün kalite kontrolleri ve drift tanıları aktiftir.",
    ),
    "strict_non_signal_quality_drift_safety": FeatureQualityDriftProfile(
        name="strict_non_signal_quality_drift_safety",
        description="Katı sinyalsiz ve güvenlik odaklı özellik kalite/drift profili.",
        notes="Sıkı manuel inceleme kuyruğu ve katı sınır kontrolleri uygulayan profil.",
    ),
    "dry_run_quality_drift_diagnostics_focus": FeatureQualityDriftProfile(
        name="dry_run_quality_drift_diagnostics_focus",
        description="Hızlı dry-run özellik kalite ve stabilite teşhis profili.",
        notes="Geliştirme ve hızlı doğrulama süreçleri için tasarlanmış test profili.",
    ),
}


def get_feature_quality_drift_profile(name: str) -> FeatureQualityDriftProfile:
    """Retrieve profile by name or default to balanced profile."""
    if name in _PROFILES:
        return _PROFILES[name]
    return _PROFILES["balanced_local_feature_quality_drift"]


def list_feature_quality_drift_profiles(enabled_only: bool = True) -> List[FeatureQualityDriftProfile]:
    """List all available profiles."""
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_feature_quality_drift_profiles() -> None:
    """Validate all configured profiles adhere to safety invariants."""
    for p in _PROFILES.values():
        if p.current_phase != 123:
            raise ValueError(f"Profile {p.name} current_phase must be 123")
        if p.target_final_phase != 160:
            raise ValueError(f"Profile {p.name} target_final_phase must be 160")
        if p.next_phase != 124:
            raise ValueError(f"Profile {p.name} next_phase must be 124")
        if not p.dry_run_default or not p.local_only or not p.non_production or not p.research_only:
            raise ValueError(f"Profile {p.name} must enforce local, dry_run, non-production constraints")
        if (
            p.allow_live_trading
            or p.allow_broker_integration
            or p.allow_real_order
            or p.allow_investment_advice
            or p.allow_quality_as_signal
            or p.allow_drift_as_signal
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
            or p.allow_auto_imputation
            or p.allow_auto_feature_drop
            or p.allow_cloud_publish
            or p.allow_docker_push
            or p.allow_git_tag
            or p.allow_archive_creation
        ):
            raise ValueError(f"Profile {p.name} violates safety invariant permissions")


def get_default_feature_quality_drift_profile() -> FeatureQualityDriftProfile:
    """Return default profile for Phase 123."""
    return _PROFILES["balanced_local_feature_quality_drift"]
