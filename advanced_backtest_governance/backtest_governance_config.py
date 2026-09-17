# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance and Bias Control Configuration.

Defines BacktestGovernanceProfile dataclass, preset profiles, and safety boundaries.
Enforces local/offline research parameters with zero live trading and zero execution.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class BacktestGovernanceProfile:
    """Configuration profile for Phase 150 Backtest Governance Contract Layer."""

    profile_name: str
    description: str
    current_phase: int = 150
    target_final_phase: int = 160
    next_phase: int = 151
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
    allow_backtest_execution: bool = False
    allow_benchmark_execution: bool = False
    allow_metric_calculation: bool = False
    allow_result_claim: bool = False
    allow_performance_claim: bool = False
    allow_strategy_approval: bool = False
    allow_optimizer_execution: bool = False
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
    enable_bias_controls: bool = True
    enable_result_boundaries: bool = True
    enable_realism_governance: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_151_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    lookahead_guard_strictness: str = "absolute_zero_tolerance"
    survivorship_policy_mode: str = "point_in_time_reconstitution"
    snooping_penalty_rate: float = 0.05
    max_allowable_multiple_tests: int = 20
    audit_trail_retention_days: int = 365


PROFILES: Dict[str, BacktestGovernanceProfile] = {
    "balanced_local_backtest_governance_contracts": BacktestGovernanceProfile(
        profile_name="balanced_local_backtest_governance_contracts",
        description="Standard balanced local/offline backtest governance and bias control contract profile.",
        min_readiness_score=0.50,
        lookahead_guard_strictness="absolute_zero_tolerance",
        survivorship_policy_mode="point_in_time_reconstitution",
        snooping_penalty_rate=0.05,
        max_allowable_multiple_tests=20,
    ),
    "conservative_local_backtest_governance_contracts": BacktestGovernanceProfile(
        profile_name="conservative_local_backtest_governance_contracts",
        description="Conservative backtest governance profile with stricter bias thresholds and manual review requirements.",
        min_readiness_score=0.60,
        lookahead_guard_strictness="absolute_zero_tolerance",
        survivorship_policy_mode="point_in_time_reconstitution",
        snooping_penalty_rate=0.10,
        max_allowable_multiple_tests=10,
    ),
    "strict_audit_backtest_governance_contracts": BacktestGovernanceProfile(
        profile_name="strict_audit_backtest_governance_contracts",
        description="Strict audit backtest governance profile requiring exhaustive evidence preservation and zero claim tolerance.",
        min_readiness_score=0.75,
        lookahead_guard_strictness="absolute_zero_tolerance",
        survivorship_policy_mode="point_in_time_reconstitution",
        snooping_penalty_rate=0.15,
        max_allowable_multiple_tests=5,
    ),
}


def get_default_backtest_governance_profile() -> BacktestGovernanceProfile:
    """Return the default Backtest Governance profile."""
    return PROFILES["balanced_local_backtest_governance_contracts"]


def get_backtest_governance_profile(name: Optional[str] = None) -> BacktestGovernanceProfile:
    """Get a specific Backtest Governance profile by name or default."""
    if not name:
        return get_default_backtest_governance_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown Backtest Governance profile: {name}. Available: {list(PROFILES.keys())}")
    return PROFILES[name]


def list_backtest_governance_profiles(enabled_only: bool = True) -> List[BacktestGovernanceProfile]:
    """List all available Backtest Governance profiles."""
    return list(PROFILES.values())


def validate_backtest_governance_profiles() -> bool:
    """Validate all registered profiles adhere to safety invariants."""
    for name, p in PROFILES.items():
        assert p.current_phase == 150, f"{name}: current_phase must be 150"
        assert p.target_final_phase == 160, f"{name}: target_final_phase must be 160"
        assert p.next_phase == 151, f"{name}: next_phase must be 151"
        assert p.dry_run_default is True, f"{name}: dry_run_default must be True"
        assert p.local_only is True, f"{name}: local_only must be True"
        assert p.non_production is True, f"{name}: non_production must be True"
        assert p.research_only is True, f"{name}: research_only must be True"
        assert p.allow_live_trading is False, f"{name}: allow_live_trading must be False"
        assert p.allow_broker_integration is False, f"{name}: allow_broker_integration must be False"
        assert p.allow_real_order is False, f"{name}: allow_real_order must be False"
        assert p.allow_investment_advice is False, f"{name}: allow_investment_advice must be False"
        assert p.allow_signal_generation is False, f"{name}: allow_signal_generation must be False"
        assert p.allow_backtest_execution is False, f"{name}: allow_backtest_execution must be False"
        assert p.allow_benchmark_execution is False, f"{name}: allow_benchmark_execution must be False"
        assert p.allow_metric_calculation is False, f"{name}: allow_metric_calculation must be False"
        assert p.allow_result_claim is False, f"{name}: allow_result_claim must be False"
        assert p.allow_performance_claim is False, f"{name}: allow_performance_claim must be False"
        assert p.allow_strategy_approval is False, f"{name}: allow_strategy_approval must be False"
        assert p.allow_optimizer_execution is False, f"{name}: allow_optimizer_execution must be False"
        assert p.allow_model_training is False, f"{name}: allow_model_training must be False"
        assert p.allow_model_predict is False, f"{name}: allow_model_predict must be False"
        assert p.allow_target_label_generation is False, f"{name}: allow_target_label_generation must be False"
        assert p.allow_production_ready_claim is False, f"{name}: allow_production_ready_claim must be False"
        assert p.allow_broker_ready_claim is False, f"{name}: allow_broker_ready_claim must be False"
        assert p.allow_source_overwrite is False, f"{name}: allow_source_overwrite must be False"
    return True
