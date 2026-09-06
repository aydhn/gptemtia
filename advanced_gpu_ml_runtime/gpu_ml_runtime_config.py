"""Phase 136: GPU Acceleration and Advanced ML Runtime Configuration.

Provides profile management, phase constraints, non-signal guarantees,
hardware discovery flags, and security gates for local/offline ML runtime foundation.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class GpuMlRuntimeProfile:
    """Configuration profile for Phase 136 GPU acceleration and ML runtime foundation."""
    profile_name: str
    description: str
    current_phase: int = 136
    target_final_phase: int = 160
    next_phase: int = 137
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
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_model_inference: bool = False
    allow_model_transform: bool = False
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_ensemble_execution: bool = False
    allow_calibration_execution: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
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
    enable_hardware_discovery: bool = True
    enable_gpu_capability: bool = True
    enable_cpu_memory_capability: bool = True
    enable_dependency_capability: bool = True
    enable_environment_snapshot: bool = True
    enable_safety_contracts: bool = True
    enable_experiment_permissions: bool = True
    enable_input_contracts: bool = True
    enable_artifact_governance_placeholders: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_137_handoff: bool = True
    min_readiness_score: float = 0.45
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, GpuMlRuntimeProfile] = {
    "balanced_local_gpu_ml_runtime_foundation": GpuMlRuntimeProfile(
        profile_name="balanced_local_gpu_ml_runtime_foundation",
        description="Dengeli yerel GPU hizlandirma ve ML calisma zamani temel profili.",
        current_phase=136,
        target_final_phase=160,
        next_phase=137,
        min_readiness_score=0.45,
    ),
    "strict_no_training_gpu_runtime_safety": GpuMlRuntimeProfile(
        profile_name="strict_no_training_gpu_runtime_safety",
        description="Siki model egitimi/tahmin yasakli GPU/ML calisma zamani guvenlik profili.",
        current_phase=136,
        target_final_phase=160,
        next_phase=137,
        min_readiness_score=0.60,
    ),
    "dry_run_ml_capability_discovery_focus": GpuMlRuntimeProfile(
        profile_name="dry_run_ml_capability_discovery_focus",
        description="Dry-run uyumlu donanim ve bagimlilik kesfi odakli calisma zamani profili.",
        current_phase=136,
        target_final_phase=160,
        next_phase=137,
        min_readiness_score=0.40,
    ),
}


def get_gpu_ml_runtime_profile(name: Optional[str] = None) -> GpuMlRuntimeProfile:
    """Retrieve a GPU ML runtime profile by name or return default."""
    if not name:
        return get_default_gpu_ml_runtime_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown GPU ML runtime profile: {name}")
    return PROFILES[name]


def get_default_gpu_ml_runtime_profile() -> GpuMlRuntimeProfile:
    """Return the default GPU ML runtime profile."""
    return PROFILES["balanced_local_gpu_ml_runtime_foundation"]


def list_gpu_ml_runtime_profiles(enabled_only: bool = True) -> List[GpuMlRuntimeProfile]:
    """List available GPU ML runtime profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_gpu_ml_runtime_profiles() -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    for profile in PROFILES.values():
        if profile.current_phase != 136:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 137:
            raise ValueError(f"Profile {profile.profile_name} has invalid next_phase: {profile.next_phase}")
        if profile.allow_live_trading or profile.allow_broker_integration or profile.allow_real_order:
            raise ValueError(f"Profile {profile.profile_name} allows live trading actions.")
        if profile.allow_signal_generation or profile.allow_directional_claim:
            raise ValueError(f"Profile {profile.profile_name} allows signal interpretation.")
        if profile.allow_strategy_generation or profile.allow_backtest_execution or profile.allow_optimizer_execution:
            raise ValueError(f"Profile {profile.profile_name} allows strategy/backtest execution.")
        if (
            profile.allow_model_training
            or profile.allow_model_fit
            or profile.allow_model_predict
            or profile.allow_model_inference
            or profile.allow_model_transform
            or profile.allow_clustering_execution
            or profile.allow_unsupervised_execution
            or profile.allow_ensemble_execution
            or profile.allow_calibration_execution
        ):
            raise ValueError(f"Profile {profile.profile_name} allows model training/inference/execution.")
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
            profile.allow_official_approval_claim
            or profile.allow_production_ready_claim
            or profile.allow_broker_ready_claim
            or profile.allow_model_deployment
            or profile.allow_production_deployment
        ):
            raise ValueError(f"Profile {profile.profile_name} allows unauthorized approval/deployment claims.")
        if (
            profile.allow_source_overwrite
            or profile.allow_auto_destructive_cleaning
            or profile.allow_file_deletion
            or profile.allow_overwrite
            or profile.allow_auto_imputation
            or profile.allow_auto_feature_drop
        ):
            raise ValueError(f"Profile {profile.profile_name} allows destructive data actions.")
        if profile.allow_artifact_persistence or profile.allow_model_registry_write:
            raise ValueError(f"Profile {profile.profile_name} allows artifact persistence or registry write.")
    return True
