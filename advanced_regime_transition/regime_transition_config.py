"""Phase 130: Regime Transition and Stability Analysis Configuration.

Defines operational profiles and strict non-signal, zero-execution safety invariants
for Phase 130 Regime Transition and Stability Analysis layer.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class RegimeTransitionProfile:
    """Operational profile for Phase 130 Regime Transition and Stability Analysis."""

    profile_name: str
    description: str
    current_phase: int = 130
    target_final_phase: int = 160
    next_phase: int = 131
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
    allow_transition_as_signal: bool = False
    allow_stability_as_signal: bool = False
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
    enable_sequence_contracts: bool = True
    enable_transition_metrics: bool = True
    enable_stability_metrics: bool = True
    enable_persistence_diagnostics: bool = True
    enable_frequency_diagnostics: bool = True
    enable_ambiguity_diagnostics: bool = True
    enable_continuity_diagnostics: bool = True
    enable_stability_diagnostics: bool = True
    enable_context_reports: bool = True
    enable_cross_asset_prep: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_131_handoff: bool = True

    # Quality & reporting thresholds
    min_stability_score: float = 0.45
    save_reports: bool = True
    extra_metadata: Dict[str, str] = field(default_factory=dict)


REGIME_TRANSITION_PROFILES: Dict[str, RegimeTransitionProfile] = {
    "balanced_local_regime_transition": RegimeTransitionProfile(
        profile_name="balanced_local_regime_transition",
        description="Standard balanced local offline regime transition and sequence stability analysis profile.",
        min_stability_score=0.45,
    ),
    "strict_non_signal_transition_safety": RegimeTransitionProfile(
        profile_name="strict_non_signal_transition_safety",
        description="Strict safety profile enforcing zero-tolerance non-signal transition boundaries and heightened stability thresholds.",
        min_stability_score=0.60,
    ),
    "dry_run_transition_diagnostics_focus": RegimeTransitionProfile(
        profile_name="dry_run_transition_diagnostics_focus",
        description="Dry-run focused profile prioritizing offline transition sequence diagnostics rehearsal and non-executable checks.",
        min_stability_score=0.45,
    ),
}


def get_regime_transition_profile(name: Optional[str] = None) -> RegimeTransitionProfile:
    """Return profile by name or default balanced profile."""
    if not name:
        name = "balanced_local_regime_transition"
    if name not in REGIME_TRANSITION_PROFILES:
        raise KeyError(
            f"Unknown regime transition profile: {name}. "
            f"Available profiles: {list(REGIME_TRANSITION_PROFILES.keys())}"
        )
    return REGIME_TRANSITION_PROFILES[name]


def list_regime_transition_profiles(enabled_only: bool = True) -> List[str]:
    """List all registered profile names."""
    return list(REGIME_TRANSITION_PROFILES.keys())


def validate_regime_transition_profiles() -> bool:
    """Validate all operational profiles satisfy strict non-signal Phase 130 invariants."""
    for name, profile in REGIME_TRANSITION_PROFILES.items():
        if profile.current_phase != 130:
            raise ValueError(f"Profile {name} current_phase must be 130, got {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {name} target_final_phase must be 160, got {profile.target_final_phase}")
        if profile.next_phase != 131:
            raise ValueError(f"Profile {name} next_phase must be 131, got {profile.next_phase}")
        if not profile.local_only or not profile.non_production or not profile.research_only:
            raise ValueError(f"Profile {name} must enforce local_only, non_production, and research_only")
        if profile.allow_live_trading or profile.allow_broker_integration or profile.allow_real_order:
            raise ValueError(f"Profile {name} cannot allow trading or broker integration")
        if profile.allow_transition_as_signal or profile.allow_stability_as_signal or profile.allow_directional_claim:
            raise ValueError(f"Profile {name} cannot allow transition or stability diagnostics as signals")
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


def get_default_regime_transition_profile() -> RegimeTransitionProfile:
    """Return default balanced local profile."""
    return get_regime_transition_profile("balanced_local_regime_transition")
