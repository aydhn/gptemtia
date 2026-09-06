"""Phase 135: Regime Acceptance Configuration.

Provides profile management, phase constraints, non-signal guarantees,
and security gates for end-to-end regime classification block acceptance.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class RegimeAcceptanceProfile:
    """Configuration profile for Phase 135 regime classification block acceptance."""
    profile_name: str
    description: str
    current_phase: int = 135
    target_final_phase: int = 160
    next_phase: int = 136
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_acceptance_as_signal: bool = False
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
    enable_inventory: bool = True
    enable_dependency_report: bool = True
    enable_acceptance_gates: bool = True
    enable_component_acceptance: bool = True
    enable_compliance_reports: bool = True
    enable_contract_reports: bool = True
    enable_manifest: bool = True
    enable_phase_136_handoff: bool = True
    min_score: float = 0.45
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, RegimeAcceptanceProfile] = {
    "balanced_local_regime_acceptance": RegimeAcceptanceProfile(
        profile_name="balanced_local_regime_acceptance",
        description="Dengeli yerel rejim siniflandirma blogu kabul ve yonetisim profili.",
        current_phase=135,
        target_final_phase=160,
        next_phase=136,
        min_score=0.45,
    ),
    "strict_non_signal_regime_block_acceptance": RegimeAcceptanceProfile(
        profile_name="strict_non_signal_regime_block_acceptance",
        description="Siki non-signal, no-lookahead ve kaynak koruma odakli kabul guvenlik profili.",
        current_phase=135,
        target_final_phase=160,
        next_phase=136,
        min_score=0.60,
    ),
    "dry_run_regime_manifest_focus": RegimeAcceptanceProfile(
        profile_name="dry_run_regime_manifest_focus",
        description="Dry-run uyumlu, manifest ve Phase 136 ileri ML/GPU devri odakli kabul profili.",
        current_phase=135,
        target_final_phase=160,
        next_phase=136,
        min_score=0.40,
    ),
}


def get_regime_acceptance_profile(name: Optional[str] = None) -> RegimeAcceptanceProfile:
    """Retrieve a regime acceptance profile by name or return default."""
    if not name:
        return get_default_regime_acceptance_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown regime acceptance profile: {name}")
    return PROFILES[name]


def get_default_regime_acceptance_profile() -> RegimeAcceptanceProfile:
    """Return the default regime acceptance profile."""
    return PROFILES["balanced_local_regime_acceptance"]


def list_regime_acceptance_profiles(enabled_only: bool = True) -> List[RegimeAcceptanceProfile]:
    """List available acceptance profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_regime_acceptance_profiles() -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    for profile in PROFILES.values():
        if profile.current_phase != 135:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 136:
            raise ValueError(f"Profile {profile.profile_name} has invalid next_phase: {profile.next_phase}")
        if profile.allow_live_trading or profile.allow_broker_integration or profile.allow_real_order:
            raise ValueError(f"Profile {profile.profile_name} allows live trading actions.")
        if (
            profile.allow_acceptance_as_signal
            or profile.allow_regime_as_signal
            or profile.allow_validation_as_signal
            or profile.allow_directional_claim
        ):
            raise ValueError(f"Profile {profile.profile_name} allows signal interpretation.")
        if profile.allow_strategy_generation or profile.allow_backtest_execution or profile.allow_optimizer_execution:
            raise ValueError(f"Profile {profile.profile_name} allows strategy/backtest execution.")
        if (
            profile.allow_model_training
            or profile.allow_model_fit
            or profile.allow_model_predict
            or profile.allow_clustering_execution
            or profile.allow_unsupervised_execution
        ):
            raise ValueError(f"Profile {profile.profile_name} allows model training/prediction/clustering execution.")
        if profile.allow_target_label_generation or profile.allow_prediction_generation:
            raise ValueError(f"Profile {profile.profile_name} allows target/prediction generation.")
        if profile.allow_sentiment_model_output or profile.allow_full_article_usage or profile.allow_article_body_usage or profile.allow_raw_content_usage or profile.allow_scraped_html_usage or profile.allow_embedding_generation or profile.allow_vector_db:
            raise ValueError(f"Profile {profile.profile_name} allows prohibited news/NLP/embedding execution.")
        if profile.allow_official_approval_claim or profile.allow_production_ready_claim or profile.allow_broker_ready_claim:
            raise ValueError(f"Profile {profile.profile_name} allows unauthorized approval claims.")
        if profile.allow_source_overwrite or profile.allow_auto_destructive_cleaning or profile.allow_file_deletion or profile.allow_overwrite or profile.allow_auto_imputation or profile.allow_auto_feature_drop:
            raise ValueError(f"Profile {profile.profile_name} allows destructive data actions.")
    return True
