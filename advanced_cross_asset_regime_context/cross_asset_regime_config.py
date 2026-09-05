"""Phase 131: Cross-Asset Regime Context Expansion Configuration.

Defines operational profiles and strict non-signal, zero-execution safety invariants
for Phase 131 Cross-Asset Regime Context Expansion layer.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class CrossAssetRegimeProfile:
    """Operational profile for Phase 131 Cross-Asset Regime Context Expansion."""

    profile_name: str
    description: str
    current_phase: int = 131
    target_final_phase: int = 160
    next_phase: int = 132
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True

    # Strict non-signal, non-execution, non-model boundaries
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_context_as_signal: bool = False
    allow_correlation_as_signal: bool = False
    allow_divergence_as_signal: bool = False
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

    # Feature flags
    enable_entity_pair_registry: bool = True
    enable_relationship_taxonomy: bool = True
    enable_fx_commodity_context: bool = True
    enable_macro_context: bool = True
    enable_calendar_news_context: bool = True
    enable_transition_alignment: bool = True
    enable_volatility_trend_range_linkage: bool = True
    enable_divergence_convergence_context: bool = True
    enable_correlation_placeholders: bool = True
    enable_lead_lag_placeholders: bool = True
    enable_no_lookahead_guard: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_132_handoff: bool = True

    # Quality & reporting thresholds
    min_context_score: float = 0.45
    save_reports: bool = True
    extra_metadata: Dict[str, str] = field(default_factory=dict)


CROSS_ASSET_REGIME_PROFILES: Dict[str, CrossAssetRegimeProfile] = {
    "balanced_local_cross_asset_regime_context": CrossAssetRegimeProfile(
        profile_name="balanced_local_cross_asset_regime_context",
        description="Standard balanced local offline cross-asset regime context expansion and linkage profile.",
        min_context_score=0.45,
    ),
    "strict_non_signal_cross_asset_regime_safety": CrossAssetRegimeProfile(
        profile_name="strict_non_signal_cross_asset_regime_safety",
        description="Strict safety profile enforcing zero-tolerance non-signal cross-asset boundaries and heightened threshold gates.",
        min_context_score=0.60,
    ),
    "dry_run_cross_asset_context_focus": CrossAssetRegimeProfile(
        profile_name="dry_run_cross_asset_context_focus",
        description="Dry-run focused profile prioritizing offline multi-asset context relationship validation without live execution.",
        min_context_score=0.45,
    ),
}


def get_cross_asset_regime_profile(name: Optional[str] = None) -> CrossAssetRegimeProfile:
    """Return profile by name or default balanced profile."""
    if not name:
        name = "balanced_local_cross_asset_regime_context"
    if name not in CROSS_ASSET_REGIME_PROFILES:
        raise KeyError(
            f"Unknown cross-asset regime profile: {name}. "
            f"Available profiles: {list(CROSS_ASSET_REGIME_PROFILES.keys())}"
        )
    return CROSS_ASSET_REGIME_PROFILES[name]


def list_cross_asset_regime_profiles(enabled_only: bool = True) -> List[str]:
    """List all registered profile names."""
    return list(CROSS_ASSET_REGIME_PROFILES.keys())


def validate_cross_asset_regime_profiles() -> bool:
    """Validate all operational profiles satisfy strict non-signal Phase 131 invariants."""
    for name, profile in CROSS_ASSET_REGIME_PROFILES.items():
        if profile.current_phase != 131:
            raise ValueError(f"Profile {name} current_phase must be 131, got {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {name} target_final_phase must be 160, got {profile.target_final_phase}")
        if profile.next_phase != 132:
            raise ValueError(f"Profile {name} next_phase must be 132, got {profile.next_phase}")
        if not profile.local_only or not profile.non_production or not profile.research_only:
            raise ValueError(f"Profile {name} must enforce local_only, non_production, and research_only")
        if profile.allow_live_trading or profile.allow_broker_integration or profile.allow_real_order:
            raise ValueError(f"Profile {name} cannot allow trading or broker integration")
        if profile.allow_context_as_signal or profile.allow_correlation_as_signal or profile.allow_divergence_as_signal:
            raise ValueError(f"Profile {name} cannot allow cross-asset context, correlation, or divergence as signals")
        if profile.allow_directional_claim:
            raise ValueError(f"Profile {name} cannot allow directional claims")
        if profile.allow_model_training or profile.allow_model_fit or profile.allow_model_predict:
            raise ValueError(f"Profile {name} cannot allow model training, fit, or predict")
        if profile.allow_clustering_execution or profile.allow_unsupervised_execution:
            raise ValueError(f"Profile {name} cannot allow clustering or unsupervised execution")
        if profile.allow_target_label_generation or profile.allow_prediction_generation:
            raise ValueError(f"Profile {name} cannot allow target label or prediction generation")
        if profile.allow_source_overwrite or profile.allow_auto_destructive_cleaning:
            raise ValueError(f"Profile {name} cannot allow source overwrite or destructive cleaning")
        if profile.allow_auto_imputation or profile.allow_auto_feature_drop:
            raise ValueError(f"Profile {name} cannot allow auto imputation or feature dropping")
    return True


def get_default_cross_asset_regime_profile() -> CrossAssetRegimeProfile:
    """Return default balanced local profile."""
    return get_cross_asset_regime_profile("balanced_local_cross_asset_regime_context")
