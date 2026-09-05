"""Phase 128: Regime Rule-Free Labeling Contracts and Unsupervised Prep Configuration.

Defines operational profiles and strict safety invariants for Phase 128.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class RegimeRuleFreeProfile:
    """Operational profile for Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep."""

    profile_name: str
    description: str
    current_phase: int = 128
    target_final_phase: int = 160
    next_phase: int = 129
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
    allow_candidate_state_as_signal: bool = False
    allow_pseudo_state_as_signal: bool = False
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
    enable_rule_free_labeling_contracts: bool = True
    enable_candidate_state_assignment_policies: bool = True
    enable_candidate_state_schema: bool = True
    enable_pseudo_state_schema: bool = True
    enable_unsupervised_prep_contracts: bool = True
    enable_clustering_input_contracts: bool = True
    enable_algorithm_placeholders: bool = True
    enable_candidate_feature_sets: bool = True
    enable_integrity_manifest: bool = True
    enable_no_lookahead_guard: bool = True
    enable_non_signal_policies: bool = True
    enable_phase_129_handoff: bool = True

    # Readiness & reporting
    min_readiness_score: float = 0.45
    save_reports: bool = True
    extra_metadata: Dict[str, str] = field(default_factory=dict)


REGIME_RULE_FREE_PROFILES: Dict[str, RegimeRuleFreeProfile] = {
    "balanced_local_regime_rule_free_prep": RegimeRuleFreeProfile(
        profile_name="balanced_local_regime_rule_free_prep",
        description="Standard balanced local offline regime rule-free candidate state labeling and unsupervised prep profile.",
        min_readiness_score=0.45,
    ),
    "strict_non_signal_rule_free_safety": RegimeRuleFreeProfile(
        profile_name="strict_non_signal_rule_free_safety",
        description="Strict safety profile enforcing zero-tolerance non-signal candidate state boundaries and heightened readiness thresholds.",
        min_readiness_score=0.60,
    ),
    "dry_run_unsupervised_prep_contract_focus": RegimeRuleFreeProfile(
        profile_name="dry_run_unsupervised_prep_contract_focus",
        description="Dry-run focused profile prioritizing unsupervised preparation contracts, clustering inputs, and non-executable placeholders.",
        min_readiness_score=0.45,
    ),
}


def get_regime_rule_free_profile(name: Optional[str] = None) -> RegimeRuleFreeProfile:
    """Return profile by name or default."""
    if not name:
        return REGIME_RULE_FREE_PROFILES["balanced_local_regime_rule_free_prep"]
    if name not in REGIME_RULE_FREE_PROFILES:
        raise KeyError(f"Unknown RegimeRuleFreeProfile: '{name}'")
    return REGIME_RULE_FREE_PROFILES[name]


def get_default_regime_rule_free_profile() -> RegimeRuleFreeProfile:
    """Return the default Phase 128 profile."""
    return REGIME_RULE_FREE_PROFILES["balanced_local_regime_rule_free_prep"]


def list_regime_rule_free_profiles(enabled_only: bool = True) -> List[str]:
    """List all available Phase 128 profile names."""
    return list(REGIME_RULE_FREE_PROFILES.keys())


def validate_regime_rule_free_profiles() -> Dict[str, bool]:
    """Validate all configured profiles against strict Phase 128 invariants."""
    results = {}
    for name, p in REGIME_RULE_FREE_PROFILES.items():
        valid = (
            p.current_phase == 128
            and p.target_final_phase == 160
            and p.next_phase == 129
            and p.dry_run_default is True
            and p.local_only is True
            and p.non_production is True
            and p.research_only is True
            and p.allow_live_trading is False
            and p.allow_broker_integration is False
            and p.allow_candidate_state_as_signal is False
            and p.allow_pseudo_state_as_signal is False
            and p.allow_clustering_execution is False
            and p.allow_model_training is False
            and p.allow_model_fit is False
            and p.allow_model_predict is False
            and p.allow_unsupervised_execution is False
            and p.allow_dimensionality_reduction_execution is False
            and p.allow_target_label_generation is False
            and p.allow_prediction_generation is False
            and p.allow_official_approval_claim is False
            and p.allow_production_ready_claim is False
            and p.allow_broker_ready_claim is False
            and p.allow_source_overwrite is False
            and p.allow_auto_imputation is False
            and p.allow_auto_feature_drop is False
        )
        results[name] = valid
    return results
