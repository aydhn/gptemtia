# -*- coding: utf-8 -*-
"""Phase 143: Explainability and Feature Attribution Configuration."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class ExplainabilityProfile:
    """Configuration profile for Phase 143 Explainability and Feature Attribution Contracts."""

    name: str = "balanced_local_explainability_contracts"
    profile_name: str = "balanced_local_explainability_contracts"
    display_name: str = "Balanced Local Explainability Contracts"
    description: str = "Standard balanced local offline explainability and feature attribution report contracts profile."
    current_phase: int = 143
    target_final_phase: int = 160
    next_phase: int = 144
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
    allow_calibration_execution: bool = False
    allow_uncertainty_estimation: bool = False
    allow_drift_calculation: bool = False

    # Explainability & Attribution prohibitions
    allow_explainability_calculation: bool = False
    allow_feature_attribution_calculation: bool = False
    allow_feature_importance_calculation: bool = False
    allow_shap_execution: bool = False
    allow_lime_execution: bool = False
    allow_permutation_importance_execution: bool = False
    allow_pdp_execution: bool = False
    allow_ice_execution: bool = False
    allow_surrogate_model_execution: bool = False
    allow_counterfactual_generation: bool = False
    allow_explanation_model_action: bool = False

    # Execution prohibitions
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_supervised_execution: bool = False
    allow_ensemble_execution: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
    allow_metric_calculation: bool = False
    allow_performance_claim: bool = False

    # Content and Metadata boundary guards
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
    enable_report_contracts: bool = True
    enable_attribution_contracts: bool = True
    enable_method_placeholders: bool = True
    enable_disabled_execution_reports: bool = True
    enable_linkage_contracts: bool = True
    enable_dependency_inputs: bool = True
    enable_audit_placeholders: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_144_handoff: bool = True
    min_readiness_score: float = 0.45
    save_reports: bool = True


PROFILES: Dict[str, ExplainabilityProfile] = {
    "balanced_local_explainability_contracts": ExplainabilityProfile(
        name="balanced_local_explainability_contracts",
        profile_name="balanced_local_explainability_contracts",
        display_name="Balanced Local Explainability Contracts",
        description="Standard balanced local offline explainability and feature attribution report contracts profile.",
    ),
    "strict_non_executing_xai_safety": ExplainabilityProfile(
        name="strict_non_executing_xai_safety",
        profile_name="strict_non_executing_xai_safety",
        display_name="Strict Non-Executing XAI Safety",
        description="Strict safety profile enforcing zero explainability calculation, zero SHAP/LIME computation, and zero model action.",
        min_readiness_score=0.50,
    ),
    "dry_run_attribution_report_governance_focus": ExplainabilityProfile(
        name="dry_run_attribution_report_governance_focus",
        profile_name="dry_run_attribution_report_governance_focus",
        display_name="Dry Run Attribution Report Governance Focus",
        description="Governance-focused profile validating attribution contracts, explainability linkages, and audit placeholders.",
        min_readiness_score=0.40,
    ),
}


def get_explainability_profile(name: Optional[str] = None) -> ExplainabilityProfile:
    """Retrieve profile by name or return default."""
    if not name or name not in PROFILES:
        return PROFILES["balanced_local_explainability_contracts"]
    return PROFILES[name]


def list_explainability_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    return list(PROFILES.keys())


def validate_explainability_profiles() -> bool:
    """Validate all profiles adhere to non-signal, zero-execution, and phase invariants."""
    for prof in PROFILES.values():
        if prof.current_phase != 143 or prof.target_final_phase != 160 or prof.next_phase != 144:
            return False
        if not prof.dry_run_default or not prof.local_only or not prof.non_production or not prof.research_only:
            return False
        if prof.allow_live_trading or prof.allow_broker_integration or prof.allow_real_order:
            return False
        if prof.allow_signal_generation or prof.allow_directional_claim or prof.allow_investment_advice:
            return False
        if prof.allow_model_training or prof.allow_model_fit or prof.allow_model_predict or prof.allow_model_inference:
            return False
        if prof.allow_explainability_calculation or prof.allow_feature_attribution_calculation:
            return False
        if prof.allow_feature_importance_calculation or prof.allow_shap_execution or prof.allow_lime_execution:
            return False
        if prof.allow_permutation_importance_execution or prof.allow_pdp_execution or prof.allow_ice_execution:
            return False
        if prof.allow_surrogate_model_execution or prof.allow_counterfactual_generation or prof.allow_explanation_model_action:
            return False
        if prof.allow_probability_prediction or prof.allow_calibration_execution or prof.allow_uncertainty_estimation:
            return False
        if prof.allow_drift_calculation or prof.allow_dataset_materialization or prof.allow_feature_snapshot_materialization:
            return False
        if prof.allow_target_label_generation or prof.allow_prediction_generation:
            return False
        if prof.allow_metric_calculation or prof.allow_performance_claim:
            return False
        if prof.allow_sentiment_model_output or prof.allow_full_article_usage or prof.allow_article_body_usage:
            return False
        if prof.allow_raw_content_usage or prof.allow_scraped_html_usage or prof.allow_embedding_generation or prof.allow_vector_db:
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


def get_default_explainability_profile() -> ExplainabilityProfile:
    """Return the default profile."""
    return PROFILES["balanced_local_explainability_contracts"]


def get_strict_explainability_profile() -> ExplainabilityProfile:
    """Return the strict non-executing safety profile."""
    return PROFILES["strict_non_executing_xai_safety"]


def get_governance_focus_explainability_profile() -> ExplainabilityProfile:
    """Return the governance focus profile."""
    return PROFILES["dry_run_attribution_report_governance_focus"]
