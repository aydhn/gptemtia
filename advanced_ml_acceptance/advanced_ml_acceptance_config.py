# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Configuration.

Provides profile management, phase constraints, non-production boundaries,
and strict safety gates for end-to-end Phase 136-145 Advanced ML acceptance.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class AdvancedMlAcceptanceProfile:
    """Configuration profile for Phase 145 Advanced ML block acceptance."""
    profile_name: str
    description: str
    current_phase: int = 145
    target_final_phase: int = 160
    next_phase: int = 146
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_signal_generation: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_walk_forward_execution: bool = False
    allow_transaction_cost_calculation: bool = False
    allow_slippage_calculation: bool = False
    allow_benchmark_calculation: bool = False
    allow_optimizer_execution: bool = False
    allow_dataset_materialization: bool = False
    allow_feature_snapshot_materialization: bool = False
    allow_real_model_training: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_model_inference: bool = False
    allow_model_transform: bool = False
    allow_probability_prediction: bool = False
    allow_calibration_execution: bool = False
    allow_uncertainty_estimation: bool = False
    allow_drift_calculation: bool = False
    allow_explainability_calculation: bool = False
    allow_feature_attribution_calculation: bool = False
    allow_model_registry_write: bool = False
    allow_artifact_persistence: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_production_approval: bool = False
    allow_broker_ready_approval: bool = False
    allow_live_trading_approval: bool = False
    allow_official_approval_claim: bool = False
    allow_production_ready_claim: bool = False
    allow_broker_ready_claim: bool = False
    allow_release_approval: bool = False
    allow_real_audit_log: bool = False
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_supervised_execution: bool = False
    allow_ensemble_execution: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
    allow_metric_calculation: bool = False
    allow_performance_claim: bool = False
    allow_sentiment_model_output: bool = False
    allow_full_article_usage: bool = False
    allow_article_body_usage: bool = False
    allow_raw_content_usage: bool = False
    allow_scraped_html_usage: bool = False
    allow_embedding_generation: bool = False
    allow_vector_db: bool = False
    allow_web_scraping: bool = False
    allow_credential_output: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False
    enable_component_checkpoints: bool = True
    enable_phase_acceptance: bool = True
    enable_dependency_evidence: bool = True
    enable_boundaries: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_146_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, AdvancedMlAcceptanceProfile] = {
    "balanced_local_advanced_ml_acceptance": AdvancedMlAcceptanceProfile(
        profile_name="balanced_local_advanced_ml_acceptance",
        description="Dengeli yerel Advanced ML blogu kabul ve yonetisim profili (Phase 136-144 konsolide).",
        current_phase=145,
        target_final_phase=160,
        next_phase=146,
        min_readiness_score=0.50,
    ),
    "strict_non_production_advanced_ml_acceptance_safety": AdvancedMlAcceptanceProfile(
        profile_name="strict_non_production_advanced_ml_acceptance_safety",
        description="Siki non-production, no-live-trading ve sifir inference odakli guvenlik kabul profili.",
        current_phase=145,
        target_final_phase=160,
        next_phase=146,
        min_readiness_score=0.65,
    ),
    "dry_run_phase_136_145_acceptance_focus": AdvancedMlAcceptanceProfile(
        profile_name="dry_run_phase_136_145_acceptance_focus",
        description="Dry-run uyumlu, manifest ve Phase 146 realistic backtest devri odakli kabul profili.",
        current_phase=145,
        target_final_phase=160,
        next_phase=146,
        min_readiness_score=0.45,
    ),
}


def get_advanced_ml_acceptance_profile(name: Optional[str] = None) -> AdvancedMlAcceptanceProfile:
    """Retrieve an advanced ML acceptance profile by name or return default."""
    if not name:
        return get_default_advanced_ml_acceptance_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown advanced ML acceptance profile: {name}")
    return PROFILES[name]


def get_default_advanced_ml_acceptance_profile() -> AdvancedMlAcceptanceProfile:
    """Return the default advanced ML acceptance profile."""
    return PROFILES["balanced_local_advanced_ml_acceptance"]


def list_advanced_ml_acceptance_profiles(enabled_only: bool = True) -> List[AdvancedMlAcceptanceProfile]:
    """List available advanced ML acceptance profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_advanced_ml_acceptance_profiles() -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    for profile in PROFILES.values():
        if profile.current_phase != 145:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 146:
            raise ValueError(f"Profile {profile.profile_name} has invalid next_phase: {profile.next_phase}")
        if profile.allow_live_trading or profile.allow_broker_integration or profile.allow_real_order:
            raise ValueError(f"Profile {profile.profile_name} allows live trading actions.")
        if (
            profile.allow_signal_generation
            or profile.allow_directional_claim
            or profile.allow_investment_advice
        ):
            raise ValueError(f"Profile {profile.profile_name} allows signal interpretation or advice.")
        if (
            profile.allow_strategy_generation
            or profile.allow_backtest_execution
            or profile.allow_walk_forward_execution
            or profile.allow_transaction_cost_calculation
            or profile.allow_slippage_calculation
            or profile.allow_benchmark_calculation
            or profile.allow_optimizer_execution
        ):
            raise ValueError(f"Profile {profile.profile_name} allows strategy/backtest/cost execution.")
        if (
            profile.allow_real_model_training
            or profile.allow_model_training
            or profile.allow_model_fit
            or profile.allow_model_predict
            or profile.allow_model_inference
            or profile.allow_model_transform
            or profile.allow_probability_prediction
            or profile.allow_calibration_execution
            or profile.allow_uncertainty_estimation
            or profile.allow_drift_calculation
            or profile.allow_explainability_calculation
            or profile.allow_feature_attribution_calculation
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited training/inference/calculation.")
        if profile.allow_model_registry_write or profile.allow_artifact_persistence:
            raise ValueError(f"Profile {profile.profile_name} allows model registry write or artifact persistence.")
        if (
            profile.allow_model_deployment
            or profile.allow_production_deployment
            or profile.allow_production_approval
            or profile.allow_broker_ready_approval
            or profile.allow_live_trading_approval
            or profile.allow_official_approval_claim
            or profile.allow_production_ready_claim
            or profile.allow_broker_ready_claim
            or profile.allow_release_approval
        ):
            raise ValueError(f"Profile {profile.profile_name} allows unauthorized deployment or approval.")
        if profile.allow_dataset_materialization or profile.allow_feature_snapshot_materialization:
            raise ValueError(f"Profile {profile.profile_name} allows dataset/snapshot materialization.")
        if profile.allow_target_label_generation or profile.allow_prediction_generation:
            raise ValueError(f"Profile {profile.profile_name} allows target/prediction generation.")
        if (
            profile.allow_sentiment_model_output
            or profile.allow_full_article_usage
            or profile.allow_article_body_usage
            or profile.allow_raw_content_usage
            or profile.allow_scraped_html_usage
            or profile.allow_embedding_generation
            or profile.allow_vector_db
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited news/NLP/embedding execution.")
        if (
            profile.allow_source_overwrite
            or profile.allow_auto_destructive_cleaning
            or profile.allow_file_deletion
            or profile.allow_overwrite
            or profile.allow_auto_imputation
            or profile.allow_auto_feature_drop
        ):
            raise ValueError(f"Profile {profile.profile_name} allows destructive data actions.")
    return True
