# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest, Transaction Cost & Slippage Modeling Configuration.

Provides configuration profiles, non-production boundaries, negative invariants,
and strict validation for realistic backtesting contracts.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class RealisticBacktestProfile:
    """Configuration profile for Phase 146 realistic backtest contracts."""

    profile_name: str
    description: str
    current_phase: int = 146
    target_final_phase: int = 160
    next_phase: int = 147
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
    allow_walk_forward_execution: bool = False
    allow_benchmark_execution: bool = False
    allow_stress_test_execution: bool = False
    allow_monte_carlo_execution: bool = False
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
    allow_metric_calculation: bool = False
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
    enable_engine_contracts: bool = True
    enable_order_simulation_contracts: bool = True
    enable_transaction_cost_models: bool = True
    enable_slippage_models: bool = True
    enable_bias_guards: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_147_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, RealisticBacktestProfile] = {
    "balanced_local_realistic_backtest_contracts": RealisticBacktestProfile(
        profile_name="balanced_local_realistic_backtest_contracts",
        description="Dengeli yerel gercekci backtest, islem maliyeti ve kayma sozlesmeleri profili.",
        current_phase=146,
        target_final_phase=160,
        next_phase=147,
        min_readiness_score=0.50,
    ),
    "strict_safety_backtest_contracts": RealisticBacktestProfile(
        profile_name="strict_safety_backtest_contracts",
        description="Siki guvenlik, sifir canli islem, sifir broker ve sifir lookahead backtest sozlesme profili.",
        current_phase=146,
        target_final_phase=160,
        next_phase=147,
        min_readiness_score=0.65,
    ),
    "dry_run_backtest_contract_focus": RealisticBacktestProfile(
        profile_name="dry_run_backtest_contract_focus",
        description="Dry-run odakli, simule maliyet bilesenleri ve Phase 147 handoff hazirlik profili.",
        current_phase=146,
        target_final_phase=160,
        next_phase=147,
        min_readiness_score=0.45,
    ),
}


def get_realistic_backtest_profile(name: Optional[str] = None) -> RealisticBacktestProfile:
    """Retrieve a realistic backtest profile by name or return default."""
    if not name:
        return get_default_realistic_backtest_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown realistic backtest profile: {name}")
    return PROFILES[name]


def get_default_realistic_backtest_profile() -> RealisticBacktestProfile:
    """Return the default realistic backtest profile."""
    return PROFILES["balanced_local_realistic_backtest_contracts"]


def list_realistic_backtest_profiles(enabled_only: bool = True) -> List[RealisticBacktestProfile]:
    """List available realistic backtest profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_realistic_backtest_profiles() -> bool:
    """Validate all configured profiles against strict security and phase bounds."""
    for profile in PROFILES.values():
        if profile.current_phase != 146:
            raise ValueError(f"Profile {profile.profile_name} has invalid current_phase: {profile.current_phase}")
        if profile.target_final_phase != 160:
            raise ValueError(f"Profile {profile.profile_name} has invalid target_final_phase: {profile.target_final_phase}")
        if profile.next_phase != 147:
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
            or profile.allow_walk_forward_execution
            or profile.allow_benchmark_execution
            or profile.allow_stress_test_execution
            or profile.allow_monte_carlo_execution
        ):
            raise ValueError(f"Profile {profile.profile_name} allows optimizer/walk-forward/benchmark execution.")
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
        if profile.allow_metric_calculation or profile.allow_performance_claim:
            raise ValueError(f"Profile {profile.profile_name} allows real metric or performance calculation.")
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
