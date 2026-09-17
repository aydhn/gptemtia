# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Configuration and Profile Management.

Defines BaselineMlModelProfile dataclass, profiles, and helpers enforcing
strict dry-run contracts with zero real model training, zero prediction,
and non-signal boundaries.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class BaselineMlModelProfile:
    """Configuration profile for Phase 138 Baseline ML Model Contracts & Dry-Run Harness."""

    name: str = "balanced_local_baseline_ml_contracts"
    description: str = "Balanced local offline baseline ML model contracts and dry-run harness"
    enabled: bool = True
    current_phase: int = 138
    target_final_phase: int = 160
    next_phase: int = 139
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True

    # Absolute Safety Boundaries (All False)
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_signal_generation: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
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
    allow_calibration_execution: bool = False
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

    # Feature Toggles
    enable_model_contracts: bool = True
    enable_dry_run_harness_contracts: bool = True
    enable_trainer_stubs: bool = True
    enable_disabled_execution_reports: bool = True
    enable_metric_placeholders: bool = True
    enable_input_guards: bool = True
    enable_experiment_linkage: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_139_handoff: bool = True

    # Scoring & Reporting
    min_readiness_score: float = 0.45
    save_reports: bool = True
    tags: List[str] = field(default_factory=lambda: ["baseline_ml", "dry_run", "contracts", "phase_138"])


PROFILES: Dict[str, BaselineMlModelProfile] = {
    "balanced_local_baseline_ml_contracts": BaselineMlModelProfile(
        name="balanced_local_baseline_ml_contracts",
        description="Standard balanced local profile for Phase 138 baseline model contracts and dry-run training harness.",
        tags=["balanced", "local", "dry_run", "contracts", "phase_138"],
    ),
    "strict_no_real_training_baseline_safety": BaselineMlModelProfile(
        name="strict_no_real_training_baseline_safety",
        description="High safety profile emphasizing absolute zero-training boundary and strict non-execution policies.",
        tags=["strict", "safety", "no_real_training", "contracts", "phase_138"],
    ),
    "dry_run_harness_contract_focus": BaselineMlModelProfile(
        name="dry_run_harness_contract_focus",
        description="Focused profile for dry-run training harness interfaces, validation stubs, and Phase 139 readiness.",
        tags=["dry_run_focus", "harness", "interfaces", "stubs", "phase_138"],
    ),
}


def get_baseline_ml_model_profile(name: Optional[str] = None) -> BaselineMlModelProfile:
    """Get profile by name, fallback to default."""
    if not name or name not in PROFILES:
        return PROFILES["balanced_local_baseline_ml_contracts"]
    return PROFILES[name]


def list_baseline_ml_model_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    if enabled_only:
        return [k for k, v in PROFILES.items() if v.enabled]
    return list(PROFILES.keys())


def validate_baseline_ml_model_profiles() -> bool:
    """Validate that all defined profiles adhere strictly to Phase 138 limits."""
    for p in PROFILES.values():
        if p.current_phase != 138:
            return False
        if p.target_final_phase != 160:
            return False
        if p.next_phase != 139:
            return False
        if not p.dry_run_default or not p.local_only or not p.non_production or not p.research_only:
            return False
        if p.allow_live_trading or p.allow_broker_integration or p.allow_real_order:
            return False
        if p.allow_signal_generation or p.allow_directional_claim or p.allow_investment_advice:
            return False
        if p.allow_real_model_training or p.allow_model_training or p.allow_model_fit:
            return False
        if p.allow_model_predict or p.allow_model_inference or p.allow_model_transform:
            return False
        if p.allow_dataset_materialization or p.allow_feature_snapshot_materialization:
            return False
        if p.allow_target_label_generation or p.allow_prediction_generation:
            return False
        if p.allow_artifact_persistence or p.allow_model_registry_write:
            return False
        if p.allow_official_approval_claim or p.allow_production_ready_claim or p.allow_broker_ready_claim:
            return False
        if p.allow_web_scraping or p.allow_credential_output or p.allow_source_overwrite:
            return False
        if p.allow_auto_destructive_cleaning or p.allow_auto_imputation or p.allow_auto_feature_drop:
            return False
    return True


def get_default_baseline_ml_model_profile() -> BaselineMlModelProfile:
    """Get the default profile."""
    return get_baseline_ml_model_profile("balanced_local_baseline_ml_contracts")
