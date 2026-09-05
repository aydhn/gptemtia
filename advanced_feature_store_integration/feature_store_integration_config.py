"""Phase 124 Feature Store Integration Config and Profiles.

Provides configuration profiles for local/offline, validation-aware,
quality/drift metadata storage in a non-signal feature store layer.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class FeatureStoreIntegrationProfile:
    """Immutable configuration profile for Feature Store Integration Expansion."""

    name: str
    description: str
    language: str = "tr"
    current_phase: int = 124
    target_final_phase: int = 160
    next_phase: int = 125
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_store_as_signal: bool = False
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
    allow_broker_ready_claim: bool = False
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
    enable_contract_registry: bool = True
    enable_entity_registry: bool = True
    enable_feature_registry: bool = True
    enable_factor_registry: bool = True
    enable_namespace_registry: bool = True
    enable_schema_registry: bool = True
    enable_version_policy: bool = True
    enable_partition_policy: bool = True
    enable_lineage_references: bool = True
    enable_validation_status: bool = True
    enable_quality_scores: bool = True
    enable_drift_scores: bool = True
    enable_manual_review_blockers: bool = True
    enable_metadata_manifest: bool = True
    enable_read_write_query_contracts: bool = True
    enable_policy_registries: bool = True
    enable_catalog_reports: bool = True
    enable_phase_125_handoff: bool = True
    min_readiness_score: float = 0.45
    enabled: bool = True
    notes: str = ""


PROFILES: Dict[str, FeatureStoreIntegrationProfile] = {
    "balanced_local_feature_store_integration": FeatureStoreIntegrationProfile(
        name="balanced_local_feature_store_integration",
        description="Dengeli yerel araştırma odaklı feature store entegrasyon profili.",
        notes="Standard local offline profile with complete contract and catalog coverage.",
    ),
    "strict_non_signal_feature_store_safety": FeatureStoreIntegrationProfile(
        name="strict_non_signal_feature_store_safety",
        description="Katı sinyal karşıtı ve kaynak koruma odaklı güvenlik profili.",
        min_readiness_score=0.60,
        notes="Enhanced safety boundaries prohibiting any signal or forecast interpretations.",
    ),
    "dry_run_feature_store_contract_focus": FeatureStoreIntegrationProfile(
        name="dry_run_feature_store_contract_focus",
        description="Sözleşme ve şema doğrulamaya odaklı simülasyon/dry-run profili.",
        min_readiness_score=0.40,
        notes="Focuses on contract validation, schema checks, and non-destructive audits.",
    ),
}


def get_feature_store_integration_profile(name: str) -> FeatureStoreIntegrationProfile:
    """Retrieve profile by name, fallback to balanced_local_feature_store_integration."""
    if name not in PROFILES:
        raise KeyError(f"Feature store integration profile '{name}' not recognized. Available: {list(PROFILES.keys())}")
    return PROFILES[name]


def list_feature_store_integration_profiles(enabled_only: bool = True) -> List[FeatureStoreIntegrationProfile]:
    """List registered profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_feature_store_integration_profiles() -> None:
    """Validate all configured profiles against Phase 124 invariants."""
    for prof in PROFILES.values():
        if prof.current_phase != 124:
            raise ValueError(f"Profile {prof.name} must have current_phase=124")
        if prof.target_final_phase != 160:
            raise ValueError(f"Profile {prof.name} must have target_final_phase=160")
        if prof.next_phase != 125:
            raise ValueError(f"Profile {prof.name} must have next_phase=125")
        if not prof.dry_run_default or not prof.local_only or not prof.non_production or not prof.research_only:
            raise ValueError(f"Profile {prof.name} safety flags violated")
        if prof.allow_live_trading or prof.allow_broker_integration or prof.allow_real_order:
            raise ValueError(f"Profile {prof.name} allows trading actions")
        if prof.allow_store_as_signal or prof.allow_directional_claim or prof.allow_strategy_generation:
            raise ValueError(f"Profile {prof.name} allows signal generation")
        if prof.allow_backtest_execution or prof.allow_optimizer_execution or prof.allow_model_training:
            raise ValueError(f"Profile {prof.name} allows model/backtest execution")
        if prof.allow_source_overwrite or prof.allow_auto_imputation or prof.allow_auto_feature_drop:
            raise ValueError(f"Profile {prof.name} allows destructive data operations")


def get_default_feature_store_integration_profile() -> FeatureStoreIntegrationProfile:
    """Return default balanced local profile."""
    return PROFILES["balanced_local_feature_store_integration"]
