# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Configuration.

Provides profile management, phase constraints, freeze controls, non-production boundaries,
and strict safety gates for the Phase 160 Full Advanced Bot Final Delivery layer.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class FinalDeliveryProfile:
    """Configuration profile for Phase 160 Full Advanced Bot Final Delivery block."""
    profile_name: str
    description: str
    current_phase: int = 160
    target_final_phase: int = 160
    next_phase: Optional[int] = None
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
    enable_package_contracts: bool = True
    enable_inventory_reports: bool = True
    enable_evidence_registries: bool = True
    enable_phase_summaries: bool = True
    enable_boundaries: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_160_phase_completion_report: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, FinalDeliveryProfile] = {
    "balanced_local_final_delivery_contracts": FinalDeliveryProfile(
        profile_name="balanced_local_final_delivery_contracts",
        description="Dengeli yerel Final Delivery ve 160 fazlik plan kapanis profili (Phases 1-159 konsolide).",
        current_phase=160,
        target_final_phase=160,
        next_phase=None,
        min_readiness_score=0.50,
    ),
    "strict_non_production_delivery_safety": FinalDeliveryProfile(
        profile_name="strict_non_production_delivery_safety",
        description="Siki non-production, no-live-trading ve sifir execution odakli final delivery guvenlik profili.",
        current_phase=160,
        target_final_phase=160,
        next_phase=None,
        min_readiness_score=0.65,
    ),
    "dry_run_completion_focus": FinalDeliveryProfile(
        profile_name="dry_run_completion_focus",
        description="Dry-run uyumlu, final manifest kontrol listesi ve 160 faz kapanis odakli profil.",
        current_phase=160,
        target_final_phase=160,
        next_phase=None,
        min_readiness_score=0.50,
    ),
}

DEFAULT_PROFILE_NAME = "balanced_local_final_delivery_contracts"


def get_final_delivery_profile(name: Optional[str] = None) -> FinalDeliveryProfile:
    """Retrieve profile by name or default."""
    if not name:
        return PROFILES[DEFAULT_PROFILE_NAME]
    if name not in PROFILES:
        raise ValueError(f"Unknown final delivery profile: {name}. Available: {list(PROFILES.keys())}")
    return PROFILES[name]


def list_final_delivery_profiles(enabled_only: bool = True) -> List[str]:
    """List available profile names."""
    if enabled_only:
        return [k for k, v in PROFILES.items() if v.enabled]
    return list(PROFILES.keys())


def validate_final_delivery_profiles() -> bool:
    """Validate all profiles conform to strict safety boundaries."""
    for p in PROFILES.values():
        if p.current_phase != 160:
            return False
        if p.target_final_phase != 160:
            return False
        if p.next_phase is not None:
            return False
        if (
            p.allow_live_trading
            or p.allow_broker_integration
            or p.allow_real_order
            or p.allow_investment_advice
            or p.allow_signal_generation
            or p.allow_directional_claim
            or p.allow_system_execution
            or p.allow_end_to_end_run
            or p.allow_release_deployment
            or p.allow_production_deployment
            or p.allow_production_approval
            or p.allow_broker_ready_approval
            or p.allow_live_ready_approval
            or p.allow_official_approval_claim
            or p.allow_production_ready_claim
            or p.allow_broker_ready_claim
            or p.allow_backtest_execution
            or p.allow_benchmark_execution
            or p.allow_portfolio_execution
            or p.allow_risk_execution
            or p.allow_scenario_execution
            or p.allow_order_generation
            or p.allow_model_training
            or p.allow_model_fit
            or p.allow_model_predict
            or p.allow_model_inference
            or p.allow_prediction_generation
            or p.allow_target_label_generation
            or p.allow_metric_calculation
            or p.allow_optimizer_execution
            or p.allow_model_registry_write
            or p.allow_artifact_persistence
            or p.allow_model_deployment
            or p.allow_web_scraping
            or p.allow_credential_output
            or p.allow_source_overwrite
            or p.allow_auto_destructive_cleaning
            or p.allow_file_deletion
            or p.allow_overwrite
            or p.allow_auto_imputation
            or p.allow_auto_feature_drop
        ):
            return False
        if not p.local_only or not p.dry_run_default or not p.non_production or not p.research_only:
            return False
    return True


def get_default_final_delivery_profile() -> FinalDeliveryProfile:
    """Return default profile."""
    return PROFILES[DEFAULT_PROFILE_NAME]
