# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction, Position Sizing and Risk Budgeting Configuration.

Provides profile management, phase constraints, non-production boundaries,
and strict safety gates for offline/local portfolio contracts.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class PortfolioConstructionProfile:
    """Configuration profile for Phase 153 Portfolio Construction block."""
    profile_name: str
    description: str
    current_phase: int = 153
    target_final_phase: int = 160
    next_phase: int = 154
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
    allow_capital_allocation: bool = False
    allow_weight_generation: bool = False
    allow_order_generation: bool = False
    allow_risk_budget_generation: bool = False
    allow_exposure_limit_generation: bool = False
    allow_leverage_margin_recommendation: bool = False
    allow_optimizer_execution: bool = False
    allow_metric_calculation: bool = False
    allow_result_claim: bool = False
    allow_performance_claim: bool = False
    allow_strategy_approval: bool = False
    allow_backtest_execution: bool = False
    allow_benchmark_execution: bool = False
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
    enable_portfolio_contracts: bool = True
    enable_position_sizing_contracts: bool = True
    enable_risk_budget_contracts: bool = True
    enable_limit_placeholders: bool = True
    enable_claim_guards: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_154_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, PortfolioConstructionProfile] = {
    "balanced_local_portfolio_construction_contracts": PortfolioConstructionProfile(
        profile_name="balanced_local_portfolio_construction_contracts",
        description="Dengeli yerel Portfolio Construction, Position Sizing ve Risk Budgeting sozlesme profili.",
        current_phase=153,
        target_final_phase=160,
        next_phase=154,
        min_readiness_score=0.50,
    ),
    "strict_non_production_portfolio_risk_budget_safety": PortfolioConstructionProfile(
        profile_name="strict_non_production_portfolio_risk_budget_safety",
        description="Siki non-production, no-live-trading ve sifir gercek allocation odakli portfoy sozlesme guvenlik profili.",
        current_phase=153,
        target_final_phase=160,
        next_phase=154,
        min_readiness_score=0.65,
    ),
    "dry_run_phase_153_sizing_contracts_focus": PortfolioConstructionProfile(
        profile_name="dry_run_phase_153_sizing_contracts_focus",
        description="Dry-run uyumlu, position sizing ve risk budget sozlesmeleri ile Phase 154 devri odakli profil.",
        current_phase=153,
        target_final_phase=160,
        next_phase=154,
        min_readiness_score=0.45,
    ),
}

PORTFOLIO_CONSTRUCTION_PROFILES = PROFILES


def get_portfolio_construction_profile(name: Optional[str] = None) -> PortfolioConstructionProfile:
    """Retrieve a portfolio construction profile by name or return default."""
    if not name:
        return get_default_portfolio_construction_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown portfolio construction profile: {name}")
    return PROFILES[name]


def get_default_portfolio_construction_profile() -> PortfolioConstructionProfile:
    """Return the default portfolio construction profile."""
    return PROFILES["balanced_local_portfolio_construction_contracts"]


def list_portfolio_construction_profiles(enabled_only: bool = True) -> List[PortfolioConstructionProfile]:
    """List available portfolio construction profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_portfolio_construction_profiles(
    profiles_dict: Optional[Dict[str, PortfolioConstructionProfile]] = None,
) -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    target_dict = profiles_dict if profiles_dict is not None else PROFILES
    for profile in target_dict.values():
        if profile.current_phase != 153:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 154:
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
            or profile.allow_capital_allocation
            or profile.allow_weight_generation
            or profile.allow_order_generation
            or profile.allow_risk_budget_generation
            or profile.allow_exposure_limit_generation
            or profile.allow_leverage_margin_recommendation
            or profile.allow_optimizer_execution
            or profile.allow_metric_calculation
            or profile.allow_result_claim
            or profile.allow_performance_claim
            or profile.allow_strategy_approval
            or profile.allow_backtest_execution
            or profile.allow_benchmark_execution
        ):
            raise ValueError(f"Profile {profile.profile_name} allows portfolio execution, sizing or metric calculations.")
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
            profile.allow_full_article_usage
            or profile.allow_article_body_usage
            or profile.allow_raw_content_usage
            or profile.allow_scraped_html_usage
            or profile.allow_embedding_generation
            or profile.allow_vector_db
            or profile.allow_web_scraping
            or profile.allow_credential_output
        ):
            raise ValueError(f"Profile {profile.profile_name} allows prohibited content, web, or credential actions.")
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
