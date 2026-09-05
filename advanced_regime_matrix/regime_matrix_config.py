"""Phase 127: Regime Feature Matrix and State Dataset Contracts Configuration.

Defines operational profiles and safety invariants for Phase 127.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class RegimeMatrixProfile:
    """Operational profile for Phase 127 Regime Feature Matrix and State Dataset Contracts."""

    profile_name: str
    description: str
    current_phase: int = 127
    target_final_phase: int = 160
    next_phase: int = 128
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
    allow_matrix_as_signal: bool = False
    allow_state_dataset_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
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
    enable_feature_matrix_contracts: bool = True
    enable_state_dataset_contracts: bool = True
    enable_entity_registry: bool = True
    enable_namespace_schema: bool = True
    enable_input_registries: bool = True
    enable_timestamp_alignment: bool = True
    enable_no_lookahead_guard: bool = True
    enable_integrity_manifest: bool = True
    enable_dependency_registries: bool = True
    enable_non_signal_policies: bool = True
    enable_phase_128_handoff: bool = True

    # Readiness & reporting
    min_readiness_score: float = 0.45
    save_reports: bool = True
    extra_metadata: Dict[str, str] = field(default_factory=dict)


REGIME_MATRIX_PROFILES: Dict[str, RegimeMatrixProfile] = {
    "balanced_local_regime_matrix_contracts": RegimeMatrixProfile(
        profile_name="balanced_local_regime_matrix_contracts",
        description="Standard balanced local offline regime feature matrix and state dataset contract profile.",
        min_readiness_score=0.45,
    ),
    "strict_non_signal_regime_matrix_safety": RegimeMatrixProfile(
        profile_name="strict_non_signal_regime_matrix_safety",
        description="Strict safety profile enforcing zero-tolerance non-signal boundaries and heightened readiness thresholds.",
        min_readiness_score=0.60,
    ),
    "dry_run_regime_dataset_contract_focus": RegimeMatrixProfile(
        profile_name="dry_run_regime_dataset_contract_focus",
        description="Dry-run focused profile prioritizing state dataset schema contracts and candidate context definitions.",
        min_readiness_score=0.45,
    ),
}


def get_regime_matrix_profile(name: Optional[str] = None) -> RegimeMatrixProfile:
    """Return profile by name or default."""
    if not name:
        return REGIME_MATRIX_PROFILES["balanced_local_regime_matrix_contracts"]
    if name not in REGIME_MATRIX_PROFILES:
        raise KeyError(f"Unknown RegimeMatrixProfile: '{name}'")
    return REGIME_MATRIX_PROFILES[name]


def list_regime_matrix_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    return list(REGIME_MATRIX_PROFILES.keys())


def validate_regime_matrix_profiles() -> bool:
    """Verify that all profiles satisfy Phase 127 invariants."""
    for p_name, profile in REGIME_MATRIX_PROFILES.items():
        if profile.current_phase != 127:
            return False
        if profile.target_final_phase != 160:
            return False
        if profile.next_phase != 128:
            return False
        if not (profile.dry_run_default and profile.local_only and profile.non_production and profile.research_only):
            return False
        if profile.allow_live_trading or profile.allow_broker_integration or profile.allow_real_order:
            return False
        if profile.allow_investment_advice or profile.allow_matrix_as_signal or profile.allow_state_dataset_as_signal:
            return False
        if profile.allow_directional_claim or profile.allow_strategy_generation:
            return False
        if profile.allow_backtest_execution or profile.allow_optimizer_execution:
            return False
        if profile.allow_model_training or profile.allow_clustering_execution or profile.allow_unsupervised_execution:
            return False
        if profile.allow_target_label_generation or profile.allow_prediction_generation:
            return False
        if profile.allow_official_approval_claim or profile.allow_production_ready_claim or profile.allow_broker_ready_claim:
            return False
        if profile.allow_model_deployment or profile.allow_production_deployment:
            return False
        if profile.allow_source_overwrite or profile.allow_auto_destructive_cleaning or profile.allow_file_deletion:
            return False
        if profile.allow_auto_imputation or profile.allow_auto_feature_drop:
            return False
    return True


def get_default_regime_matrix_profile() -> RegimeMatrixProfile:
    """Return the default regime matrix profile."""
    return get_regime_matrix_profile("balanced_local_regime_matrix_contracts")
