# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Configuration and Profile Management.

Defines GpuTrainingGovernanceProfile dataclass, profiles, and helpers enforcing
strict resource governance, controlled dry-run execution, zero real training,
zero prediction, zero target/label generation, and non-signal boundaries.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class GpuTrainingGovernanceProfile:
    """Configuration profile for Phase 139 GPU-Accelerated Training Harness and Resource Governance."""

    name: str = "balanced_local_gpu_training_governance"
    description: str = "Balanced local offline GPU training harness and resource governance"
    enabled: bool = True
    current_phase: int = 139
    target_final_phase: int = 160
    next_phase: int = 140
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
    enable_resource_policies: bool = True
    enable_device_selection: bool = True
    enable_memory_budget: bool = True
    enable_cpu_fallback: bool = True
    enable_timeout_policy: bool = True
    enable_harness_stubs: bool = True
    enable_dry_run_guards: bool = True
    enable_disabled_execution_reports: bool = True
    enable_dependency_inputs: bool = True
    enable_audit_placeholders: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_140_handoff: bool = True

    # Scoring & Limits
    min_readiness_score: float = 0.45
    save_reports: bool = True
    max_memory_fraction_limit: float = 0.80
    max_timeout_seconds_limit: int = 3600
    default_batch_size_placeholder: int = 32
    tags: List[str] = field(
        default_factory=lambda: ["gpu_governance", "dry_run", "resource_policy", "phase_139"]
    )


PROFILES: Dict[str, GpuTrainingGovernanceProfile] = {
    "balanced_local_gpu_training_governance": GpuTrainingGovernanceProfile(
        name="balanced_local_gpu_training_governance",
        description="Standard balanced local profile for Phase 139 GPU training resource governance and controlled dry-run harness.",
        tags=["balanced", "local", "dry_run", "resource_governance", "phase_139"],
    ),
    "strict_no_training_resource_governance_safety": GpuTrainingGovernanceProfile(
        name="strict_no_training_resource_governance_safety",
        description="Strict safety profile emphasizing absolute zero-training boundary, blocked execution stubs, and conservative memory caps.",
        tags=["strict", "safety", "no_real_training", "resource_governance", "phase_139"],
    ),
    "dry_run_gpu_resource_contract_focus": GpuTrainingGovernanceProfile(
        name="dry_run_gpu_resource_contract_focus",
        description="Focused profile for dry-run GPU resource policies, device selection verification, and Phase 140 candidate model registry readiness.",
        tags=["dry_run_focus", "harness", "device_selection", "memory_budget", "phase_139"],
    ),
}


def get_gpu_training_governance_profile(name: Optional[str] = None) -> GpuTrainingGovernanceProfile:
    """Get profile by name, fallback to default."""
    if not name or name not in PROFILES:
        return PROFILES["balanced_local_gpu_training_governance"]
    return PROFILES[name]


def list_gpu_training_governance_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    if enabled_only:
        return [k for k, v in PROFILES.items() if v.enabled]
    return list(PROFILES.keys())


def validate_gpu_training_governance_profiles() -> bool:
    """Validate that all defined profiles adhere strictly to Phase 139 limits."""
    for p in PROFILES.values():
        if p.current_phase != 139:
            return False
        if p.target_final_phase != 160:
            return False
        if p.next_phase != 140:
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
        if p.allow_clustering_execution or p.allow_unsupervised_execution or p.allow_supervised_execution:
            return False
        if p.allow_ensemble_execution or p.allow_calibration_execution:
            return False
        if p.allow_dataset_materialization or p.allow_feature_snapshot_materialization:
            return False
        if p.allow_target_label_generation or p.allow_prediction_generation:
            return False
        if p.allow_metric_calculation or p.allow_performance_claim:
            return False
        if p.allow_artifact_persistence or p.allow_model_registry_write:
            return False
        if p.allow_official_approval_claim or p.allow_production_ready_claim or p.allow_broker_ready_claim:
            return False
        if p.allow_model_deployment or p.allow_production_deployment:
            return False
        if p.allow_web_scraping or p.allow_credential_output or p.allow_source_overwrite:
            return False
        if p.allow_auto_destructive_cleaning or p.allow_auto_imputation or p.allow_auto_feature_drop:
            return False
    return True


def get_default_gpu_training_governance_profile() -> GpuTrainingGovernanceProfile:
    """Get the default profile."""
    return get_gpu_training_governance_profile("balanced_local_gpu_training_governance")
