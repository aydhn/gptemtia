# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing and Scenario Simulation Configuration.

Provides configuration profiles, non-production boundaries, negative invariants,
and strict validation for stress testing and scenario simulation contracts.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class StressTestingProfile:
    """Configuration profile for Phase 148 stress testing contracts."""

    profile_name: str
    description: str
    current_phase: int = 148
    target_final_phase: int = 160
    next_phase: int = 149
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
    allow_optimizer_execution: bool = False
    allow_stress_test_execution: bool = False
    allow_scenario_simulation_execution: bool = False
    allow_monte_carlo_execution: bool = False
    allow_metric_calculation: bool = False
    allow_stress_metric_calculation: bool = False
    allow_scenario_metric_calculation: bool = False
    allow_dataset_materialization: bool = False
    allow_feature_snapshot_materialization: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_model_inference: bool = False
    allow_prediction_generation: bool = False
    allow_target_label_generation: bool = False
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
    allow_performance_claim: bool = False
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
    enable_scenario_contracts: bool = True
    enable_shock_placeholders: bool = True
    enable_metric_placeholders: bool = True
    enable_bias_guards: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_149_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, StressTestingProfile] = {
    "balanced_local_stress_testing_contracts": StressTestingProfile(
        profile_name="balanced_local_stress_testing_contracts",
        description="Dengeli yerel stres testi sozlesmeleri, senaryo kutuphanesi ve sok yer tutuculari profili.",
        current_phase=148,
        target_final_phase=160,
        next_phase=149,
        min_readiness_score=0.50,
    ),
    "strict_safety_stress_contracts": StressTestingProfile(
        profile_name="strict_safety_stress_contracts",
        description="Siki guvenlik, sifir canli islem, sifir broker, sifir lookahead ve genisletilmis sok muhafizlari profili.",
        current_phase=148,
        target_final_phase=160,
        next_phase=149,
        min_readiness_score=0.65,
    ),
    "dry_run_scenario_contracts": StressTestingProfile(
        profile_name="dry_run_scenario_contracts",
        description="Dry-run odakli senaryo sozlesmeleri, sok katalogu ve Phase 149 handoff hazirlik profili.",
        current_phase=148,
        target_final_phase=160,
        next_phase=149,
        min_readiness_score=0.45,
    ),
}


def get_stress_testing_profile(name: Optional[str] = None) -> StressTestingProfile:
    """Retrieve a stress testing profile by name or return default."""
    if not name:
        return get_default_stress_testing_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown stress testing profile: {name}")
    return PROFILES[name]


def get_default_stress_testing_profile() -> StressTestingProfile:
    """Return the default stress testing profile."""
    return PROFILES["balanced_local_stress_testing_contracts"]


def list_stress_testing_profiles(enabled_only: bool = True) -> List[StressTestingProfile]:
    """List available stress testing profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_stress_testing_profiles() -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    for profile in PROFILES.values():
        if profile.current_phase != 148:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 149:
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
            profile.allow_optimizer_execution
            or profile.allow_stress_test_execution
            or profile.allow_scenario_simulation_execution
            or profile.allow_monte_carlo_execution
        ):
            raise ValueError(f"Profile {profile.profile_name} allows optimizer/stress/scenario/Monte Carlo execution.")
        if (
            profile.allow_metric_calculation
            or profile.allow_stress_metric_calculation
            or profile.allow_scenario_metric_calculation
            or profile.allow_performance_claim
        ):
            raise ValueError(f"Profile {profile.profile_name} allows metric or performance calculation.")
        if (
            profile.allow_model_training
            or profile.allow_model_fit
            or profile.allow_model_predict
            or profile.allow_model_inference
            or profile.allow_prediction_generation
            or profile.allow_target_label_generation
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited training/inference.")
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
        ):
            raise ValueError(f"Profile {profile.profile_name} allows unauthorized deployment or approval.")
        if profile.allow_dataset_materialization or profile.allow_feature_snapshot_materialization:
            raise ValueError(f"Profile {profile.profile_name} allows dataset/snapshot materialization.")
        if (
            profile.allow_full_article_usage
            or profile.allow_article_body_usage
            or profile.allow_raw_content_usage
            or profile.allow_scraped_html_usage
            or profile.allow_embedding_generation
            or profile.allow_vector_db
            or profile.allow_web_scraping
            or profile.allow_credential_output
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited news/scraping/credential output.")
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
