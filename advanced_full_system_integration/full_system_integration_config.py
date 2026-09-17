# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Configuration.

Provides profile management, phase constraints, non-production boundaries,
and strict safety gates for the Phase 158 Full-System Integration & Acceptance Rehearsal layer.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class FullSystemIntegrationProfile:
    """Configuration profile for Phase 158 Full-System Integration block."""
    profile_name: str
    description: str
    current_phase: int = 158
    target_final_phase: int = 160
    next_phase: int = 159
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
    allow_system_execution: bool = False
    allow_end_to_end_run: bool = False
    allow_backtest_execution: bool = False
    allow_benchmark_execution: bool = False
    allow_portfolio_execution: bool = False
    allow_risk_execution: bool = False
    allow_scenario_execution: bool = False
    allow_order_generation: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_model_inference: bool = False
    allow_prediction_generation: bool = False
    allow_target_label_generation: bool = False
    allow_metric_calculation: bool = False
    allow_optimizer_execution: bool = False
    allow_model_registry_write: bool = False
    allow_artifact_persistence: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_production_approval: bool = False
    allow_broker_ready_approval: bool = False
    allow_live_ready_approval: bool = False
    allow_official_approval_claim: bool = False
    allow_production_ready_claim: bool = False
    allow_broker_ready_claim: bool = False
    allow_web_scraping: bool = False
    allow_credential_output: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False
    enable_component_registry: bool = True
    enable_contract_integration: bool = True
    enable_acceptance_rehearsal: bool = True
    enable_boundaries: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_159_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, FullSystemIntegrationProfile] = {
    "balanced_local_full_system_integration_contracts": FullSystemIntegrationProfile(
        profile_name="balanced_local_full_system_integration_contracts",
        description="Dengeli yerel Full-System Integration ve Acceptance Rehearsal profili (Phases 1-157 konsolide).",
        current_phase=158,
        target_final_phase=160,
        next_phase=159,
        min_readiness_score=0.50,
    ),
    "strict_non_production_system_integration_safety": FullSystemIntegrationProfile(
        profile_name="strict_non_production_system_integration_safety",
        description="Siki non-production, no-live-trading ve sifir sistem calistirma odakli guvenlik kabul profili.",
        current_phase=158,
        target_final_phase=160,
        next_phase=159,
        min_readiness_score=0.65,
    ),
    "dry_run_acceptance_rehearsal_focus": FullSystemIntegrationProfile(
        profile_name="dry_run_acceptance_rehearsal_focus",
        description="Dry-run uyumlu, kabul provasi ve Phase 159 release candidate devri odakli profil.",
        current_phase=158,
        target_final_phase=160,
        next_phase=159,
        min_readiness_score=0.45,
    ),
}


def get_full_system_integration_profile(name: Optional[str] = None) -> FullSystemIntegrationProfile:
    """Retrieve a full-system integration profile by name or return default."""
    if not name:
        return get_default_full_system_integration_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown full system integration profile: {name}")
    return PROFILES[name]


def get_default_full_system_integration_profile() -> FullSystemIntegrationProfile:
    """Return the default full-system integration profile."""
    return PROFILES["balanced_local_full_system_integration_contracts"]


def list_full_system_integration_profiles(enabled_only: bool = True) -> List[FullSystemIntegrationProfile]:
    """List available full-system integration profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_full_system_integration_profiles() -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    for profile in PROFILES.values():
        if profile.current_phase != 158:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 159:
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
            profile.allow_system_execution
            or profile.allow_end_to_end_run
            or profile.allow_backtest_execution
            or profile.allow_benchmark_execution
            or profile.allow_portfolio_execution
            or profile.allow_risk_execution
            or profile.allow_scenario_execution
            or profile.allow_order_generation
            or profile.allow_metric_calculation
            or profile.allow_optimizer_execution
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited execution actions.")
        if (
            profile.allow_model_training
            or profile.allow_model_fit
            or profile.allow_model_predict
            or profile.allow_model_inference
            or profile.allow_prediction_generation
            or profile.allow_target_label_generation
        ):
            raise ValueError(f"Profile {profile.profile_name} allows model training or inference.")
        if profile.allow_model_registry_write or profile.allow_artifact_persistence:
            raise ValueError(f"Profile {profile.profile_name} allows model registry write or artifact persistence.")
        if (
            profile.allow_model_deployment
            or profile.allow_production_deployment
            or profile.allow_production_approval
            or profile.allow_broker_ready_approval
            or profile.allow_live_ready_approval
            or profile.allow_official_approval_claim
            or profile.allow_production_ready_claim
            or profile.allow_broker_ready_claim
        ):
            raise ValueError(f"Profile {profile.profile_name} allows unauthorized deployment or approval.")
        if profile.allow_web_scraping or profile.allow_credential_output:
            raise ValueError(f"Profile {profile.profile_name} allows prohibited web scraping or credential output.")
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
