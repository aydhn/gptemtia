# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Configuration.

Provides profile management, phase constraints, freeze controls, non-production boundaries,
and strict safety gates for the Phase 159 Final Hardening, Operator Runbook & Release Candidate layer.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class FinalHardeningProfile:
    """Configuration profile for Phase 159 Final Hardening and Release Candidate block."""
    profile_name: str
    description: str
    current_phase: int = 159
    target_final_phase: int = 160
    next_phase: int = 160
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
    allow_release_deployment: bool = False
    allow_production_deployment: bool = False
    allow_production_approval: bool = False
    allow_broker_ready_approval: bool = False
    allow_live_ready_approval: bool = False
    allow_official_approval_claim: bool = False
    allow_production_ready_claim: bool = False
    allow_broker_ready_claim: bool = False
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
    allow_web_scraping: bool = False
    allow_credential_output: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False
    enable_release_candidate_contracts: bool = True
    enable_operator_runbook: bool = True
    enable_freeze_audits: bool = True
    enable_inventory_reports: bool = True
    enable_boundaries: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_160_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, FinalHardeningProfile] = {
    "balanced_local_final_hardening_contracts": FinalHardeningProfile(
        profile_name="balanced_local_final_hardening_contracts",
        description="Dengeli yerel Final Hardening, Operator Runbook ve Release Candidate profili (Phases 1-158 konsolide).",
        current_phase=159,
        target_final_phase=160,
        next_phase=160,
        min_readiness_score=0.50,
    ),
    "strict_non_production_hardening_safety": FinalHardeningProfile(
        profile_name="strict_non_production_hardening_safety",
        description="Siki non-production, no-live-trading ve sifir execution odakli final hardening guvenlik profili.",
        current_phase=159,
        target_final_phase=160,
        next_phase=160,
        min_readiness_score=0.65,
    ),
    "dry_run_release_candidate_focus": FinalHardeningProfile(
        profile_name="dry_run_release_candidate_focus",
        description="Dry-run uyumlu, release candidate kontrol listesi ve Phase 160 final devri odakli profil.",
        current_phase=159,
        target_final_phase=160,
        next_phase=160,
        min_readiness_score=0.45,
    ),
}

FINAL_HARDENING_PROFILES = PROFILES


def get_final_hardening_profile(name: Optional[str] = None) -> FinalHardeningProfile:
    """Retrieve a final hardening profile by name or return default."""
    if not name:
        return get_default_final_hardening_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown final hardening profile: {name}")
    return PROFILES[name]


def get_default_final_hardening_profile() -> FinalHardeningProfile:
    """Return the default final hardening profile."""
    return PROFILES["balanced_local_final_hardening_contracts"]


def list_final_hardening_profiles(enabled_only: bool = True) -> List[FinalHardeningProfile]:
    """List available final hardening profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_final_hardening_profiles() -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    for profile in PROFILES.values():
        if profile.current_phase != 159:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 160:
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
            or profile.allow_release_deployment
            or profile.allow_production_deployment
            or profile.allow_production_approval
            or profile.allow_broker_ready_approval
            or profile.allow_live_ready_approval
            or profile.allow_official_approval_claim
            or profile.allow_production_ready_claim
            or profile.allow_broker_ready_claim
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited execution or approval claims.")
        if (
            profile.allow_backtest_execution
            or profile.allow_benchmark_execution
            or profile.allow_portfolio_execution
            or profile.allow_risk_execution
            or profile.allow_scenario_execution
            or profile.allow_order_generation
            or profile.allow_metric_calculation
            or profile.allow_optimizer_execution
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited analytical execution actions.")
        if (
            profile.allow_model_training
            or profile.allow_model_fit
            or profile.allow_model_predict
            or profile.allow_model_inference
            or profile.allow_prediction_generation
            or profile.allow_target_label_generation
        ):
            raise ValueError(f"Profile {profile.profile_name} allows model training or inference.")
        if profile.allow_model_registry_write or profile.allow_artifact_persistence or profile.allow_model_deployment:
            raise ValueError(f"Profile {profile.profile_name} allows model registry write, artifact persistence, or model deployment.")
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
