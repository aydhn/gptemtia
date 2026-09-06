"""Phase 134: Regime FeatureStore Integration Configuration and Profiles.

Provides configuration profiles, strict non-signal safety boundaries,
and metadata contract switches for the local/offline Regime FeatureStore layer.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RegimeFeatureStoreProfile:
    """Configuration profile for Phase 134 Regime FeatureStore Integration."""

    profile_name: str
    description: str
    current_phase: int = 134
    target_final_phase: int = 160
    next_phase: int = 135
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True

    # Absolute safety boundaries (strictly False)
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_store_as_signal: bool = False
    allow_regime_as_signal: bool = False
    allow_validation_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
    allow_sentiment_model_output: bool = False
    allow_full_article_usage: bool = False
    allow_article_body_usage: bool = False
    allow_raw_content_usage: bool = False
    allow_scraped_html_usage: bool = False
    allow_embedding_generation: bool = False
    allow_vector_db: bool = False
    allow_official_approval_claim: bool = False
    allow_production_ready_claim: bool = False
    allow_broker_ready_claim: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_scraping: bool = False
    allow_credential_output: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False

    # FeatureStore Integration switches
    enable_contract_registry: bool = True
    enable_entity_registry: bool = True
    enable_namespace_schema: bool = True
    enable_component_catalogs: bool = True
    enable_accepted_references: bool = True
    enable_dependency_store: bool = True
    enable_lineage_references: bool = True
    enable_manual_review_blockers: bool = True
    enable_read_write_query_contracts: bool = True
    enable_policies: bool = True
    enable_manifest: bool = True
    enable_phase_135_handoff: bool = True

    # Scoring and report generation
    min_readiness_score: float = 0.45
    save_reports: bool = True
    enabled: bool = True
    extra_metadata: Dict[str, Any] = field(default_factory=dict)


PROFILES: Dict[str, RegimeFeatureStoreProfile] = {
    "balanced_local_regime_featurestore_integration": RegimeFeatureStoreProfile(
        profile_name="balanced_local_regime_featurestore_integration",
        description="Standard balanced local profile connecting Phase 126-133 regime outputs to FeatureStore metadata catalogs.",
        min_readiness_score=0.45,
    ),
    "strict_non_signal_regime_featurestore_safety": RegimeFeatureStoreProfile(
        profile_name="strict_non_signal_regime_featurestore_safety",
        description="Strict safety profile enforcing zero-signal claims, metadata-only news purity, and source preservation.",
        min_readiness_score=0.60,
    ),
    "dry_run_regime_store_catalog_focus": RegimeFeatureStoreProfile(
        profile_name="dry_run_regime_store_catalog_focus",
        description="Dry-run audit profile for contract validation, schema checks, and simulated catalog lookups.",
        dry_run_default=True,
        save_reports=False,
        min_readiness_score=0.40,
    ),
}


def get_regime_featurestore_profile(
    name: Optional[str] = None,
) -> RegimeFeatureStoreProfile:
    """Retrieve profile by name or return default balanced profile."""
    profile_key = name or "balanced_local_regime_featurestore_integration"
    if profile_key not in PROFILES:
        raise ValueError(
            f"Unknown Regime FeatureStore profile: {profile_key}. Available: {list(PROFILES.keys())}"
        )
    return PROFILES[profile_key]


def list_regime_featurestore_profiles(
    enabled_only: bool = True,
) -> List[RegimeFeatureStoreProfile]:
    """List configured Regime FeatureStore profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def get_default_regime_featurestore_profile() -> RegimeFeatureStoreProfile:
    """Return canonical default profile."""
    return PROFILES["balanced_local_regime_featurestore_integration"]


def validate_regime_featurestore_profiles() -> bool:
    """Validate all configured profiles adhere to Phase 134 invariants."""
    for name, p in PROFILES.items():
        if p.current_phase != 134:
            raise ValueError(f"Profile {name} has invalid current_phase: {p.current_phase}")
        if p.target_final_phase != 160:
            raise ValueError(f"Profile {name} has invalid target_final_phase: {p.target_final_phase}")
        if p.next_phase != 135:
            raise ValueError(f"Profile {name} has invalid next_phase: {p.next_phase}")
        if not (p.local_only and p.non_production and p.research_only):
            raise ValueError(f"Profile {name} must be local_only, non_production, and research_only")
        if (
            p.allow_live_trading
            or p.allow_broker_integration
            or p.allow_real_order
            or p.allow_investment_advice
            or p.allow_store_as_signal
            or p.allow_regime_as_signal
            or p.allow_validation_as_signal
            or p.allow_directional_claim
            or p.allow_strategy_generation
            or p.allow_backtest_execution
            or p.allow_optimizer_execution
            or p.allow_model_training
            or p.allow_model_fit
            or p.allow_model_predict
            or p.allow_clustering_execution
            or p.allow_unsupervised_execution
            or p.allow_target_label_generation
            or p.allow_prediction_generation
            or p.allow_sentiment_model_output
            or p.allow_full_article_usage
            or p.allow_article_body_usage
            or p.allow_raw_content_usage
            or p.allow_scraped_html_usage
            or p.allow_embedding_generation
            or p.allow_vector_db
            or p.allow_official_approval_claim
            or p.allow_production_ready_claim
            or p.allow_broker_ready_claim
            or p.allow_model_deployment
            or p.allow_production_deployment
            or p.allow_web_scraping
            or p.allow_credential_output
            or p.allow_source_overwrite
            or p.allow_auto_destructive_cleaning
            or p.allow_file_deletion
            or p.allow_overwrite
            or p.allow_auto_imputation
            or p.allow_auto_feature_drop
        ):
            raise ValueError(f"Profile {name} violates non-signal / safe execution invariants")
    return True
