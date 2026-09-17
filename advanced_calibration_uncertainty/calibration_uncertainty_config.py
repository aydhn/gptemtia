# -*- coding: utf-8 -*-
"""Phase 141: Probability Calibration and Uncertainty Estimation Configuration."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class CalibrationUncertaintyProfile:
    """Configuration profile for Phase 141 Probability Calibration and Uncertainty Estimation Contracts."""

    name: str = "balanced_local_calibration_uncertainty_contracts"
    description: str = "Balanced local offline probability calibration and uncertainty estimation contracts profile."
    current_phase: int = 141
    target_final_phase: int = 160
    next_phase: int = 142
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
    allow_probability_prediction: bool = False
    allow_confidence_score_calculation: bool = False
    allow_calibration_execution: bool = False
    allow_calibration_fit: bool = False
    allow_calibration_transform: bool = False
    allow_uncertainty_estimation: bool = False
    allow_prediction_interval_calculation: bool = False
    allow_conformal_prediction_execution: bool = False
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_supervised_execution: bool = False
    allow_ensemble_execution: bool = False
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
    enable_calibration_contracts: bool = True
    enable_uncertainty_contracts: bool = True
    enable_method_placeholders: bool = True
    enable_disabled_execution_reports: bool = True
    enable_metric_placeholders: bool = True
    enable_quality_gates: bool = True
    enable_dependency_inputs: bool = True
    enable_audit_placeholders: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_142_handoff: bool = True
    min_readiness_score: float = 0.45
    save_reports: bool = True


PROFILES: Dict[str, CalibrationUncertaintyProfile] = {
    "balanced_local_calibration_uncertainty_contracts": CalibrationUncertaintyProfile(
        name="balanced_local_calibration_uncertainty_contracts",
        description="Standard balanced local offline probability calibration and uncertainty estimation contracts profile.",
    ),
    "strict_non_executing_calibration_safety": CalibrationUncertaintyProfile(
        name="strict_non_executing_calibration_safety",
        description="Strict safety profile enforcing zero calibration or uncertainty estimation execution.",
        min_readiness_score=0.50,
    ),
    "dry_run_uncertainty_governance_focus": CalibrationUncertaintyProfile(
        name="dry_run_uncertainty_governance_focus",
        description="Governance-focused profile validating calibration contracts, uncertainty gates, and audit trails.",
        min_readiness_score=0.40,
    ),
}


def get_calibration_uncertainty_profile(name: Optional[str] = None) -> CalibrationUncertaintyProfile:
    """Retrieve profile by name or return default."""
    if not name or name not in PROFILES:
        return PROFILES["balanced_local_calibration_uncertainty_contracts"]
    return PROFILES[name]


def list_calibration_uncertainty_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    return list(PROFILES.keys())


def validate_calibration_uncertainty_profiles() -> bool:
    """Validate all profiles adhere to non-signal, zero-execution, and phase invariants."""
    for prof in PROFILES.values():
        if prof.current_phase != 141 or prof.target_final_phase != 160 or prof.next_phase != 142:
            return False
        if not prof.dry_run_default or not prof.local_only or not prof.non_production or not prof.research_only:
            return False
        if prof.allow_live_trading or prof.allow_broker_integration or prof.allow_real_order:
            return False
        if prof.allow_signal_generation or prof.allow_directional_claim or prof.allow_investment_advice:
            return False
        if prof.allow_model_training or prof.allow_model_fit or prof.allow_model_predict:
            return False
        if prof.allow_probability_prediction or prof.allow_confidence_score_calculation:
            return False
        if prof.allow_calibration_execution or prof.allow_calibration_fit or prof.allow_calibration_transform:
            return False
        if prof.allow_uncertainty_estimation or prof.allow_prediction_interval_calculation:
            return False
        if prof.allow_conformal_prediction_execution:
            return False
        if prof.allow_dataset_materialization or prof.allow_feature_snapshot_materialization:
            return False
        if prof.allow_target_label_generation or prof.allow_prediction_generation:
            return False
        if prof.allow_metric_calculation or prof.allow_performance_claim:
            return False
        if prof.allow_sentiment_model_output or prof.allow_full_article_usage:
            return False
        if prof.allow_embedding_generation or prof.allow_vector_db:
            return False
        if prof.allow_artifact_persistence or prof.allow_model_registry_write:
            return False
        if prof.allow_official_approval_claim or prof.allow_production_ready_claim or prof.allow_broker_ready_claim:
            return False
        if prof.allow_source_overwrite or prof.allow_auto_destructive_cleaning:
            return False
        if prof.allow_auto_imputation or prof.allow_auto_feature_drop:
            return False
    return True


def get_default_calibration_uncertainty_profile() -> CalibrationUncertaintyProfile:
    """Return the default profile."""
    return PROFILES["balanced_local_calibration_uncertainty_contracts"]
