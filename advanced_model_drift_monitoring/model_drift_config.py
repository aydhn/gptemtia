# -*- coding: utf-8 -*-
"""Phase 142: Model Drift Monitoring and Data/Feature Drift Linkage Configuration."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class ModelDriftProfile:
    """Configuration profile for Phase 142 Model Drift Monitoring and Data/Feature Drift Linkage Contracts."""

    name: str = "balanced_local_model_drift_contracts"
    description: str = "Balanced local offline model, data, and feature drift monitoring contracts profile."
    current_phase: int = 142
    target_final_phase: int = 160
    next_phase: int = 143
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

    # Drift calculation & automated actions prohibitions
    allow_drift_calculation: bool = False
    allow_data_drift_calculation: bool = False
    allow_feature_drift_calculation: bool = False
    allow_model_drift_calculation: bool = False
    allow_drift_metric_calculation: bool = False
    allow_live_monitoring: bool = False
    allow_alerting: bool = False
    allow_retraining_trigger: bool = False
    allow_model_action: bool = False

    # ML & learning prohibitions
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
    enable_monitoring_contracts: bool = True
    enable_linkage_contracts: bool = True
    enable_window_policies: bool = True
    enable_threshold_placeholders: bool = True
    enable_metric_placeholders: bool = True
    enable_disabled_execution_reports: bool = True
    enable_dependency_inputs: bool = True
    enable_audit_placeholders: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_143_handoff: bool = True
    min_readiness_score: float = 0.45
    save_reports: bool = True

    @property
    def profile_name(self) -> str:
        return self.name

    @property
    def display_name(self) -> str:
        return self.name.replace("_", " ").title()

    @property
    def allow_live_drift_monitoring(self) -> bool:
        return self.allow_live_monitoring

    @property
    def allow_drift_alerting(self) -> bool:
        return self.allow_alerting

    @property
    def allow_drift_retraining_trigger(self) -> bool:
        return self.allow_retraining_trigger

    @property
    def allow_drift_model_actions(self) -> bool:
        return self.allow_model_action

    @property
    def allow_prediction_distribution_drift_execution(self) -> bool:
        return self.allow_prediction_generation

    @property
    def enforce_non_executing_drift_monitoring(self) -> bool:
        return True


PROFILES: Dict[str, ModelDriftProfile] = {
    "balanced_local_model_drift_contracts": ModelDriftProfile(
        name="balanced_local_model_drift_contracts",
        description="Standard balanced local offline model, data, and feature drift monitoring contracts profile.",
    ),
    "strict_non_executing_drift_monitoring_safety": ModelDriftProfile(
        name="strict_non_executing_drift_monitoring_safety",
        description="Strict safety profile enforcing zero drift metric calculation, alerting, or retraining triggers.",
        min_readiness_score=0.50,
    ),
    "dry_run_drift_linkage_governance_focus": ModelDriftProfile(
        name="dry_run_drift_linkage_governance_focus",
        description="Governance-focused profile validating drift linkage contracts, window policies, and audit trails.",
        min_readiness_score=0.40,
    ),
}


def get_model_drift_profile(name: Optional[str] = None) -> ModelDriftProfile:
    """Retrieve profile by name or return default."""
    if not name or name not in PROFILES:
        return PROFILES["balanced_local_model_drift_contracts"]
    return PROFILES[name]


def list_model_drift_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    return list(PROFILES.keys())


def validate_model_drift_profiles() -> bool:
    """Validate all profiles adhere to non-signal, zero-execution, and phase invariants."""
    for prof in PROFILES.values():
        if prof.current_phase != 142 or prof.target_final_phase != 160 or prof.next_phase != 143:
            return False
        if not prof.dry_run_default or not prof.local_only or not prof.non_production or not prof.research_only:
            return False
        if prof.allow_live_trading or prof.allow_broker_integration or prof.allow_real_order:
            return False
        if prof.allow_signal_generation or prof.allow_directional_claim or prof.allow_investment_advice:
            return False
        if prof.allow_strategy_generation or prof.allow_backtest_execution or prof.allow_optimizer_execution:
            return False
        if prof.allow_dataset_materialization or prof.allow_feature_snapshot_materialization:
            return False
        if prof.allow_real_model_training or prof.allow_model_training or prof.allow_model_fit:
            return False
        if prof.allow_model_predict or prof.allow_model_inference or prof.allow_model_transform:
            return False
        if prof.allow_probability_prediction or prof.allow_calibration_execution or prof.allow_uncertainty_estimation:
            return False
        if prof.allow_drift_calculation or prof.allow_data_drift_calculation or prof.allow_feature_drift_calculation:
            return False
        if prof.allow_model_drift_calculation or prof.allow_drift_metric_calculation:
            return False
        if prof.allow_live_monitoring or prof.allow_alerting or prof.allow_retraining_trigger or prof.allow_model_action:
            return False
        if prof.allow_clustering_execution or prof.allow_unsupervised_execution or prof.allow_supervised_execution or prof.allow_ensemble_execution:
            return False
        if prof.allow_target_label_generation or prof.allow_prediction_generation:
            return False
        if prof.allow_metric_calculation or prof.allow_performance_claim:
            return False
        if prof.allow_sentiment_model_output or prof.allow_full_article_usage:
            return False
        if prof.allow_article_body_usage or prof.allow_raw_content_usage or prof.allow_scraped_html_usage:
            return False
        if prof.allow_embedding_generation or prof.allow_vector_db:
            return False
        if prof.allow_artifact_persistence or prof.allow_model_registry_write:
            return False
        if prof.allow_official_approval_claim or prof.allow_production_ready_claim or prof.allow_broker_ready_claim:
            return False
        if prof.allow_model_deployment or prof.allow_production_deployment:
            return False
        if prof.allow_web_scraping or prof.allow_credential_output:
            return False
        if prof.allow_source_overwrite or prof.allow_auto_destructive_cleaning or prof.allow_file_deletion or prof.allow_overwrite:
            return False
        if prof.allow_auto_imputation or prof.allow_auto_feature_drop:
            return False
    return True


def get_default_model_drift_profile() -> ModelDriftProfile:
    """Return the default profile."""
    return PROFILES["balanced_local_model_drift_contracts"]


def validate_model_drift_profile(profile: Optional[ModelDriftProfile] = None) -> bool:
    """Validate a single model drift profile (or default if None)."""
    prof = profile or get_model_drift_profile()
    return validate_model_drift_profiles({"profile": prof})

