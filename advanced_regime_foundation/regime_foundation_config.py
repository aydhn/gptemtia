"""Phase 126: Regime Classification and Market Behavior Foundation Configuration.

Defines operational profiles and safety invariants for Phase 126.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class RegimeFoundationProfile:
    """Operational profile for Phase 126 Regime Classification Foundation."""

    profile_name: str
    description: str
    current_phase: int = 126
    target_final_phase: int = 160
    next_phase: int = 127
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
    allow_regime_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
    allow_clustering_execution: bool = False
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
    enable_market_behavior_taxonomy: bool = True
    enable_regime_state_taxonomy: bool = True
    enable_regime_families: bool = True
    enable_context_registries: bool = True
    enable_contracts_dependencies: bool = True
    enable_non_signal_policies: bool = True
    enable_manifest: bool = True
    enable_phase_127_handoff: bool = True

    # Readiness & reporting
    min_readiness_score: float = 0.45
    save_reports: bool = True
    extra_metadata: Dict[str, str] = field(default_factory=dict)


REGIME_FOUNDATION_PROFILES: Dict[str, RegimeFoundationProfile] = {
    "balanced_local_regime_foundation": RegimeFoundationProfile(
        profile_name="balanced_local_regime_foundation",
        description="Standard balanced local offline regime foundation profile with full taxonomy, context and non-signal contracts.",
        min_readiness_score=0.45,
    ),
    "strict_non_signal_regime_safety": RegimeFoundationProfile(
        profile_name="strict_non_signal_regime_safety",
        description="Strict safety profile enforcing zero-tolerance non-signal boundaries and heightened readiness thresholds.",
        min_readiness_score=0.60,
    ),
    "dry_run_regime_taxonomy_focus": RegimeFoundationProfile(
        profile_name="dry_run_regime_taxonomy_focus",
        description="Dry-run taxonomy focused profile prioritizing market behavior and regime state taxonomies.",
        min_readiness_score=0.45,
    ),
}


def get_regime_foundation_profile(name: Optional[str] = None) -> RegimeFoundationProfile:
    """Return profile by name or default."""
    if not name:
        return REGIME_FOUNDATION_PROFILES["balanced_local_regime_foundation"]
    if name not in REGIME_FOUNDATION_PROFILES:
        raise KeyError(f"Unknown RegimeFoundationProfile: '{name}'")
    return REGIME_FOUNDATION_PROFILES[name]


def list_regime_foundation_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    return list(REGIME_FOUNDATION_PROFILES.keys())


def validate_regime_foundation_profiles() -> bool:
    """Verify that all profiles satisfy Phase 126 invariants."""
    for p_name, profile in REGIME_FOUNDATION_PROFILES.items():
        if profile.current_phase != 126:
            return False
        if profile.target_final_phase != 160:
            return False
        if profile.next_phase != 127:
            return False
        if not (profile.dry_run_default and profile.local_only and profile.non_production and profile.research_only):
            return False
        if profile.allow_live_trading or profile.allow_broker_integration or profile.allow_real_order:
            return False
        if profile.allow_investment_advice or profile.allow_regime_as_signal or profile.allow_directional_claim:
            return False
        if profile.allow_strategy_generation or profile.allow_backtest_execution or profile.allow_optimizer_execution:
            return False
        if profile.allow_model_training or profile.allow_clustering_execution:
            return False
        if profile.allow_target_label_generation or profile.allow_prediction_generation:
            return False
        if profile.allow_official_approval_claim or profile.allow_production_ready_claim or profile.allow_broker_ready_claim:
            return False
        if profile.allow_source_overwrite or profile.allow_auto_destructive_cleaning or profile.allow_auto_imputation:
            return False
        if profile.allow_auto_feature_drop:
            return False
    return True


def get_default_regime_foundation_profile() -> RegimeFoundationProfile:
    """Return the default regime foundation profile."""
    return get_regime_foundation_profile("balanced_local_regime_foundation")
