# -*- coding: utf-8 -*-
"""Phase 144: Model Governance, Model Cards and Audit Trail Configuration."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class ModelGovernanceProfile:
    """Configuration profile for Phase 144 Model Governance and Model Cards."""

    name: str = "balanced_local_model_governance_contracts"
    profile_name: str = "balanced_local_model_governance_contracts"
    display_name: str = "Balanced Local Model Governance Contracts"
    description: str = "Standard balanced local offline model governance, model cards and audit trail contracts profile."
    current_phase: int = 144
    target_final_phase: int = 160
    next_phase: int = 145
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
    allow_explainability_calculation: bool = False
    allow_feature_attribution_calculation: bool = False

    # Governance, Approval & Registry Prohibitions
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
    allow_web_scraping: bool = False
    allow_credential_output: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False

    # Component enablement flags
    enable_model_cards: bool = True
    enable_audit_trail_placeholders: bool = True
    enable_approval_boundaries: bool = True
    enable_release_boundaries: bool = True
    enable_risk_register: bool = True
    enable_control_checklists: bool = True
    enable_disabled_execution_reports: bool = True
    enable_dependency_inputs: bool = True
    enable_audit_placeholders: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_145_handoff: bool = True
    min_readiness_score: float = 0.45
    save_reports: bool = True


PROFILES: Dict[str, ModelGovernanceProfile] = {
    "balanced_local_model_governance_contracts": ModelGovernanceProfile(
        name="balanced_local_model_governance_contracts",
        profile_name="balanced_local_model_governance_contracts",
        display_name="Balanced Local Model Governance Contracts",
        description="Standard balanced local offline model governance, model cards and audit trail contracts profile.",
    ),
    "strict_non_production_governance_safety": ModelGovernanceProfile(
        name="strict_non_production_governance_safety",
        profile_name="strict_non_production_governance_safety",
        display_name="Strict Non-Production Governance Safety",
        description="Strict safety profile enforcing zero approval, zero deployment, zero model registry write and zero live trading.",
        min_readiness_score=0.50,
    ),
    "dry_run_model_cards_audit_focus": ModelGovernanceProfile(
        name="dry_run_model_cards_audit_focus",
        profile_name="dry_run_model_cards_audit_focus",
        display_name="Dry Run Model Cards Audit Focus",
        description="Governance-focused profile validating model card templates, limitations, prohibited-use metadata and audit placeholders.",
        min_readiness_score=0.40,
    ),
}


def get_model_governance_profile(name: Optional[str] = None) -> ModelGovernanceProfile:
    """Retrieve profile by name or return default."""
    if not name or name not in PROFILES:
        return PROFILES["balanced_local_model_governance_contracts"]
    return PROFILES[name]


def list_model_governance_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    return list(PROFILES.keys())


def validate_model_governance_profiles() -> bool:
    """Validate all profiles adhere to non-signal, zero-execution, and phase invariants."""
    for prof in PROFILES.values():
        if prof.current_phase != 144 or prof.target_final_phase != 160 or prof.next_phase != 145:
            return False
        if not prof.dry_run_default or not prof.local_only or not prof.non_production or not prof.research_only:
            return False
        if prof.allow_live_trading or prof.allow_broker_integration or prof.allow_real_order:
            return False
        if prof.allow_signal_generation or prof.allow_directional_claim or prof.allow_investment_advice:
            return False
        if prof.allow_model_training or prof.allow_model_fit or prof.allow_model_predict or prof.allow_model_inference:
            return False
        if prof.allow_model_registry_write or prof.allow_artifact_persistence or prof.allow_model_deployment:
            return False
        if prof.allow_production_deployment or prof.allow_production_approval or prof.allow_broker_ready_approval:
            return False
        if prof.allow_live_trading_approval or prof.allow_official_approval_claim or prof.allow_production_ready_claim:
            return False
        if prof.allow_broker_ready_claim or prof.allow_release_approval or prof.allow_real_audit_log:
            return False
        if prof.allow_dataset_materialization or prof.allow_feature_snapshot_materialization:
            return False
        if prof.allow_target_label_generation or prof.allow_prediction_generation:
            return False
        if prof.allow_metric_calculation or prof.allow_performance_claim:
            return False
        if prof.allow_sentiment_model_output or prof.allow_full_article_usage or prof.allow_article_body_usage:
            return False
        if prof.allow_raw_content_usage or prof.allow_scraped_html_usage or prof.allow_embedding_generation or prof.allow_vector_db:
            return False
        if prof.allow_source_overwrite or prof.allow_auto_destructive_cleaning:
            return False
        if prof.allow_auto_imputation or prof.allow_auto_feature_drop:
            return False
    return True


def get_default_model_governance_profile() -> ModelGovernanceProfile:
    """Return the default profile."""
    return PROFILES["balanced_local_model_governance_contracts"]


def get_strict_model_governance_profile() -> ModelGovernanceProfile:
    """Return the strict non-production safety profile."""
    return PROFILES["strict_non_production_governance_safety"]


def get_audit_focus_model_governance_profile() -> ModelGovernanceProfile:
    """Return the audit focus profile."""
    return PROFILES["dry_run_model_cards_audit_focus"]
