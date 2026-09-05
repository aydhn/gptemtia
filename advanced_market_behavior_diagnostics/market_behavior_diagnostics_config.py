"""Phase 129: Market Behavior Diagnostics and Regime Quality Configuration.

Defines operational profiles and strict non-signal, zero-execution safety invariants
for Phase 129 Market Behavior Diagnostics and Regime Quality layer.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class MarketBehaviorDiagnosticsProfile:
    """Operational profile for Phase 129 Market Behavior Diagnostics and Regime Quality."""

    profile_name: str
    description: str
    current_phase: int = 129
    target_final_phase: int = 160
    next_phase: int = 130
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
    allow_quality_as_signal: bool = False
    allow_behavior_as_signal: bool = False
    allow_candidate_state_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_dimensionality_reduction_execution: bool = False
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
    enable_quality_metrics: bool = True
    enable_candidate_state_quality: bool = True
    enable_pseudo_state_quality: bool = True
    enable_candidate_state_coverage: bool = True
    enable_candidate_state_consistency: bool = True
    enable_candidate_state_ambiguity: bool = True
    enable_candidate_state_stability: bool = True
    enable_regime_family_quality: bool = True
    enable_behavior_diagnostics: bool = True
    enable_transition_readiness: bool = True
    enable_stability_readiness: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_130_handoff: bool = True

    # Quality & reporting thresholds
    min_quality_score: float = 0.45
    save_reports: bool = True
    extra_metadata: Dict[str, str] = field(default_factory=dict)


MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES: Dict[str, MarketBehaviorDiagnosticsProfile] = {
    "balanced_local_market_behavior_diagnostics": MarketBehaviorDiagnosticsProfile(
        profile_name="balanced_local_market_behavior_diagnostics",
        description="Standard balanced local offline market behavior diagnostics and candidate state quality profile.",
        min_quality_score=0.45,
    ),
    "strict_non_signal_behavior_quality_safety": MarketBehaviorDiagnosticsProfile(
        profile_name="strict_non_signal_behavior_quality_safety",
        description="Strict safety profile enforcing zero-tolerance non-signal behavior boundaries and heightened quality thresholds.",
        min_quality_score=0.60,
    ),
    "dry_run_behavior_diagnostics_focus": MarketBehaviorDiagnosticsProfile(
        profile_name="dry_run_behavior_diagnostics_focus",
        description="Dry-run focused profile prioritizing offline diagnostics execution, reporting rehearsal, and non-executable quality checks.",
        min_quality_score=0.45,
    ),
}


def get_market_behavior_diagnostics_profile(name: Optional[str] = None) -> MarketBehaviorDiagnosticsProfile:
    """Return profile by name or default balanced profile."""
    if not name:
        name = "balanced_local_market_behavior_diagnostics"
    if name not in MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES:
        raise KeyError(
            f"Unknown market behavior diagnostics profile: {name}. "
            f"Available profiles: {list(MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES.keys())}"
        )
    return MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES[name]


def list_market_behavior_diagnostics_profiles(enabled_only: bool = True) -> List[str]:
    """List all registered profile names."""
    return list(MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES.keys())


def validate_market_behavior_diagnostics_profiles() -> bool:
    """Validate all operational profiles satisfy strict non-signal Phase 129 invariants."""
    for name, profile in MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES.items():
        if profile.current_phase != 129:
            raise ValueError(f"Profile {name} current_phase must be 129, got {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {name} target_final_phase must be 160, got {profile.target_final_phase}")
        if profile.next_phase != 130:
            raise ValueError(f"Profile {name} next_phase must be 130, got {profile.next_phase}")
        if not profile.local_only or not profile.non_production or not profile.research_only:
            raise ValueError(f"Profile {name} must enforce local_only, non_production, and research_only")
        if profile.allow_live_trading or profile.allow_broker_integration or profile.allow_real_order:
            raise ValueError(f"Profile {name} cannot allow trading or broker integration")
        if profile.allow_quality_as_signal or profile.allow_behavior_as_signal or profile.allow_candidate_state_as_signal:
            raise ValueError(f"Profile {name} cannot allow quality or behavior diagnostics as signals")
        if profile.allow_model_training or profile.allow_model_fit or profile.allow_model_predict:
            raise ValueError(f"Profile {name} cannot allow model training, fit, or predict")
        if profile.allow_clustering_execution or profile.allow_unsupervised_execution or profile.allow_dimensionality_reduction_execution:
            raise ValueError(f"Profile {name} cannot allow clustering or unsupervised execution")
        if profile.allow_target_label_generation or profile.allow_prediction_generation:
            raise ValueError(f"Profile {name} cannot allow target label or prediction generation")
        if profile.allow_source_overwrite or profile.allow_auto_destructive_cleaning:
            raise ValueError(f"Profile {name} cannot allow source overwrite or destructive cleaning")
        if profile.allow_auto_imputation or profile.allow_auto_feature_drop:
            raise ValueError(f"Profile {name} cannot allow auto imputation or feature dropping")
    return True


def get_default_market_behavior_diagnostics_profile() -> MarketBehaviorDiagnosticsProfile:
    """Return default balanced local profile."""
    return get_market_behavior_diagnostics_profile("balanced_local_market_behavior_diagnostics")
