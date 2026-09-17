# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Contracts & Candidate Model Registry Configuration."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class EnsembleModelProfile:
    """Configuration profile for Phase 140 Ensemble Model Contracts and Candidate Model Registry."""

    name: str = "balanced_local_ensemble_model_contracts"
    description: str = "Balanced local offline ensemble model contracts and candidate model registry profile."
    current_phase: int = 140
    target_final_phase: int = 160
    next_phase: int = 141
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True

    # Strict non-execution & trading invariants
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_signal_generation: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False

    # Materialization & Training prohibitions
    allow_dataset_materialization: bool = False
    allow_feature_snapshot_materialization: bool = False
    allow_real_model_training: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_model_inference: bool = False
    allow_model_transform: bool = False
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_supervised_execution: bool = False
    allow_ensemble_execution: bool = False
    allow_voting_execution: bool = False
    allow_blending_execution: bool = False
    allow_stacking_execution: bool = False
    allow_calibration_execution: bool = False
    allow_uncertainty_estimation: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
    allow_metric_calculation: bool = False
    allow_performance_claim: bool = False

    # Metadata & content boundary guards
    allow_sentiment_model_output: bool = False
    allow_full_article_usage: bool = False
    allow_article_body_usage: bool = False
    allow_raw_content_usage: bool = False
    allow_scraped_html_usage: bool = False
    allow_embedding_generation: bool = False
    allow_vector_db: bool = False
    allow_artifact_persistence: bool = False
    allow_model_registry_write: bool = False
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

    # Component enablement flags
    enable_candidate_contracts: bool = True
    enable_eligibility_gates: bool = True
    enable_compatibility_matrix: bool = True
    enable_ensemble_strategy_contracts: bool = True
    enable_voting_blending_stacking_placeholders: bool = True
    enable_disabled_execution_reports: bool = True
    enable_dependency_inputs: bool = True
    enable_audit_placeholders: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_141_handoff: bool = True
    min_readiness_score: float = 0.45
    save_reports: bool = True


PROFILES: Dict[str, EnsembleModelProfile] = {
    "balanced_local_ensemble_model_contracts": EnsembleModelProfile(
        name="balanced_local_ensemble_model_contracts",
        description="Standard balanced local offline candidate model registry and ensemble strategy contracts profile.",
        min_readiness_score=0.45,
    ),
    "strict_non_executing_ensemble_safety": EnsembleModelProfile(
        name="strict_non_executing_ensemble_safety",
        description="Strict profile maximizing execution blocking checks and safety validations for ensembles.",
        min_readiness_score=0.50,
    ),
    "dry_run_candidate_registry_focus": EnsembleModelProfile(
        name="dry_run_candidate_registry_focus",
        description="Focused profile prioritizing candidate model contract registration and dependency audits.",
        min_readiness_score=0.40,
    ),
}


def get_default_ensemble_model_profile() -> EnsembleModelProfile:
    """Return the default Phase 140 profile."""
    return PROFILES["balanced_local_ensemble_model_contracts"]


def get_ensemble_model_profile(name: Optional[str] = None) -> EnsembleModelProfile:
    """Return a profile by name or default if not found."""
    if not name or name not in PROFILES:
        return get_default_ensemble_model_profile()
    return PROFILES[name]


def list_ensemble_model_profiles(enabled_only: bool = True) -> List[str]:
    """List available ensemble model profile names."""
    return list(PROFILES.keys())


def validate_ensemble_model_profile(profile: EnsembleModelProfile) -> bool:
    """Validate a single ensemble model profile."""
    if not isinstance(profile, EnsembleModelProfile):
        return False
    if profile.current_phase != 140 or profile.target_final_phase != 160 or profile.next_phase != 141:
        return False
    if not profile.dry_run_default or not profile.local_only or not profile.non_production:
        return False
    if (
        profile.allow_live_trading
        or profile.allow_broker_integration
        or profile.allow_real_order
        or profile.allow_investment_advice
        or profile.allow_signal_generation
        or profile.allow_directional_claim
        or profile.allow_real_model_training
        or profile.allow_model_training
        or profile.allow_model_fit
        or profile.allow_model_predict
        or profile.allow_model_inference
        or profile.allow_model_transform
        or profile.allow_clustering_execution
        or profile.allow_unsupervised_execution
        or profile.allow_supervised_execution
        or profile.allow_ensemble_execution
        or profile.allow_voting_execution
        or profile.allow_blending_execution
        or profile.allow_stacking_execution
        or profile.allow_calibration_execution
        or profile.allow_uncertainty_estimation
        or profile.allow_target_label_generation
        or profile.allow_prediction_generation
        or profile.allow_metric_calculation
        or profile.allow_performance_claim
        or profile.allow_artifact_persistence
        or profile.allow_model_registry_write
        or profile.allow_source_overwrite
        or profile.allow_auto_destructive_cleaning
        or profile.allow_file_deletion
        or profile.allow_auto_imputation
        or profile.allow_auto_feature_drop
    ):
        return False
    return True


def validate_ensemble_model_profiles() -> bool:
    """Validate that all profiles strictly conform to Phase 140 non-execution invariants."""
    for profile in PROFILES.values():
        if not validate_ensemble_model_profile(profile):
            return False
    return True

