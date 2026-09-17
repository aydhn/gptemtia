# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Configuration.

Provides profile management, phase constraints, non-production boundaries,
and strict safety gates for end-to-end Phase 153-157 Portfolio/Risk block acceptance.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class PortfolioAcceptanceProfile:
    """Configuration profile for Phase 157 Portfolio Acceptance block."""
    profile_name: str
    description: str
    current_phase: int = 157
    target_final_phase: int = 160
    next_phase: int = 158
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
    allow_portfolio_construction: bool = False
    allow_position_sizing: bool = False
    allow_portfolio_optimization: bool = False
    allow_capital_allocation: bool = False
    allow_weight_generation: bool = False
    allow_allocation_generation: bool = False
    allow_rebalance_generation: bool = False
    allow_order_generation: bool = False
    allow_risk_budget_generation: bool = False
    allow_risk_reporting_execution: bool = False
    allow_exposure_attribution_execution: bool = False
    allow_limit_monitoring_execution: bool = False
    allow_scenario_execution: bool = False
    allow_drawdown_control_execution: bool = False
    allow_portfolio_adjustment: bool = False
    allow_hedge_derisk_generation: bool = False
    allow_alert_generation: bool = False
    allow_dashboard_generation: bool = False
    allow_metric_calculation: bool = False
    allow_var_calculation: bool = False
    allow_expected_shortfall_calculation: bool = False
    allow_exposure_calculation: bool = False
    allow_optimizer_execution: bool = False
    allow_result_claim: bool = False
    allow_performance_claim: bool = False
    allow_strategy_approval: bool = False
    allow_portfolio_approval: bool = False
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
    allow_web_scraping: bool = False
    allow_credential_output: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False
    enable_component_checkpoints: bool = True
    enable_phase_acceptance: bool = True
    enable_dependency_evidence: bool = True
    enable_boundaries: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_158_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, PortfolioAcceptanceProfile] = {
    "balanced_local_portfolio_acceptance_contracts": PortfolioAcceptanceProfile(
        profile_name="balanced_local_portfolio_acceptance_contracts",
        description="Dengeli yerel Portfolio Acceptance kabul ve yonetisim profili (Phase 153-156 konsolide).",
        current_phase=157,
        target_final_phase=160,
        next_phase=158,
        min_readiness_score=0.50,
    ),
    "strict_non_production_portfolio_acceptance_safety": PortfolioAcceptanceProfile(
        profile_name="strict_non_production_portfolio_acceptance_safety",
        description="Siki non-production, no-live-trading ve sifir portfoy/risk execution odakli guvenlik kabul profili.",
        current_phase=157,
        target_final_phase=160,
        next_phase=158,
        min_readiness_score=0.65,
    ),
    "dry_run_phase_153_157_acceptance_focus": PortfolioAcceptanceProfile(
        profile_name="dry_run_phase_153_157_acceptance_focus",
        description="Dry-run uyumlu, manifest ve Phase 158 full-system integration devri odakli kabul profili.",
        current_phase=157,
        target_final_phase=160,
        next_phase=158,
        min_readiness_score=0.45,
    ),
}


def get_portfolio_acceptance_profile(name: Optional[str] = None) -> PortfolioAcceptanceProfile:
    """Retrieve a portfolio acceptance profile by name or return default."""
    if not name:
        return get_default_portfolio_acceptance_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown portfolio acceptance profile: {name}")
    return PROFILES[name]


def get_default_portfolio_acceptance_profile() -> PortfolioAcceptanceProfile:
    """Return the default portfolio acceptance profile."""
    return PROFILES["balanced_local_portfolio_acceptance_contracts"]


def list_portfolio_acceptance_profiles(enabled_only: bool = True) -> List[PortfolioAcceptanceProfile]:
    """List available portfolio acceptance profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_portfolio_acceptance_profiles() -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    for profile in PROFILES.values():
        if profile.current_phase != 157:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 158:
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
            profile.allow_portfolio_construction
            or profile.allow_position_sizing
            or profile.allow_portfolio_optimization
            or profile.allow_capital_allocation
            or profile.allow_weight_generation
            or profile.allow_allocation_generation
            or profile.allow_rebalance_generation
            or profile.allow_order_generation
            or profile.allow_risk_budget_generation
            or profile.allow_risk_reporting_execution
            or profile.allow_exposure_attribution_execution
            or profile.allow_limit_monitoring_execution
            or profile.allow_scenario_execution
            or profile.allow_drawdown_control_execution
            or profile.allow_portfolio_adjustment
            or profile.allow_hedge_derisk_generation
            or profile.allow_metric_calculation
            or profile.allow_optimizer_execution
            or profile.allow_strategy_approval
            or profile.allow_portfolio_approval
            or profile.allow_result_claim
            or profile.allow_performance_claim
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited portfolio/risk execution or claims.")
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
            or profile.allow_live_trading_approval
            or profile.allow_official_approval_claim
            or profile.allow_production_ready_claim
            or profile.allow_broker_ready_claim
        ):
            raise ValueError(f"Profile {profile.profile_name} allows unauthorized deployment or approval.")
        if (
            profile.allow_web_scraping
            or profile.allow_credential_output
        ):
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
