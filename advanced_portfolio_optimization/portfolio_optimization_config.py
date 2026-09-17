# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization and Allocation Constraints Configuration.

Provides profile management, phase constraints, non-production boundaries,
and strict safety gates for offline/local portfolio optimization contracts.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class PortfolioOptimizationProfile:
    """Configuration profile for Phase 154 Portfolio Optimization block."""
    profile_name: str
    description: str
    current_phase: int = 154
    target_final_phase: int = 160
    next_phase: int = 155
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
    allow_portfolio_optimization: bool = False
    allow_portfolio_construction: bool = False
    allow_position_sizing: bool = False
    allow_capital_allocation: bool = False
    allow_weight_generation: bool = False
    allow_allocation_generation: bool = False
    allow_rebalance_generation: bool = False
    allow_order_generation: bool = False
    allow_risk_budget_generation: bool = False
    allow_exposure_limit_generation: bool = False
    allow_leverage_margin_recommendation: bool = False
    allow_optimizer_execution: bool = False
    allow_solver_execution: bool = False
    allow_grid_search_execution: bool = False
    allow_efficient_frontier_generation: bool = False
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
    enable_optimization_contracts: bool = True
    enable_objective_contracts: bool = True
    enable_constraint_contracts: bool = True
    enable_solver_placeholders: bool = True
    enable_claim_guards: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_155_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True

    def validate(self) -> bool:
        """Validate non-production safety invariants for this profile."""
        if self.allow_live_trading or self.allow_broker_integration or self.allow_real_order:
            raise ValueError(f"{self.profile_name}: Live trading or broker integration strictly prohibited!")
        if self.allow_portfolio_optimization or self.allow_weight_generation or self.allow_order_generation:
            raise ValueError(f"{self.profile_name}: Portfolio optimization and weight generation strictly prohibited!")
        if not self.non_production or not self.dry_run_default:
            raise ValueError(f"{self.profile_name}: Must be non-production dry-run profile!")
        return True


PROFILES: Dict[str, PortfolioOptimizationProfile] = {
    "balanced_local_portfolio_optimization_contracts": PortfolioOptimizationProfile(
        profile_name="balanced_local_portfolio_optimization_contracts",
        description="Dengeli yerel Portfolio Optimization ve Allocation Constraints sozlesme profili.",
        current_phase=154,
        target_final_phase=160,
        next_phase=155,
        min_readiness_score=0.50,
    ),
    "strict_non_production_portfolio_optimization_safety": PortfolioOptimizationProfile(
        profile_name="strict_non_production_portfolio_optimization_safety",
        description="Siki guvenlikli non-production portfoy optimizasyon ve kisit sozlesme profili.",
        current_phase=154,
        target_final_phase=160,
        next_phase=155,
        min_readiness_score=0.65,
    ),
    "dry_run_phase_154_optimization_contracts_focus": PortfolioOptimizationProfile(
        profile_name="dry_run_phase_154_optimization_contracts_focus",
        description="Dry-run odakli portfoy optimizasyon ve kisit sozlesme profili.",
        current_phase=154,
        target_final_phase=160,
        next_phase=155,
        min_readiness_score=0.50,
    ),
    "dry_run_phase_154_allocation_constraints_focus": PortfolioOptimizationProfile(
        profile_name="dry_run_phase_154_allocation_constraints_focus",
        description="Dry-run odakli portfoy optimizasyon ve kisit sozlesme profili (alias).",
        current_phase=154,
        target_final_phase=160,
        next_phase=155,
        min_readiness_score=0.50,
    ),
}

PORTFOLIO_OPTIMIZATION_PROFILES = PROFILES


def get_portfolio_optimization_profile(profile_name: str) -> PortfolioOptimizationProfile:
    """Retrieve profile by name or raise KeyError."""
    if profile_name not in PROFILES:
        raise KeyError(
            f"Profile '{profile_name}' not found. Available profiles: {list(PROFILES.keys())}"
        )
    return PROFILES[profile_name]


def get_default_portfolio_optimization_profile() -> PortfolioOptimizationProfile:
    """Return default profile."""
    return PROFILES["balanced_local_portfolio_optimization_contracts"]


def list_portfolio_optimization_profiles(enabled_only: bool = True) -> List[PortfolioOptimizationProfile]:
    """List registered profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_portfolio_optimization_profiles() -> bool:
    """Ensure all registered profiles satisfy strict non-production invariants."""
    for name, p in PROFILES.items():
        assert p.current_phase == 154, f"{name}: current_phase must be 154"
        assert p.target_final_phase == 160, f"{name}: target_final_phase must be 160"
        assert p.next_phase == 155, f"{name}: next_phase must be 155"
        assert p.dry_run_default is True, f"{name}: dry_run_default must be True"
        assert p.local_only is True, f"{name}: local_only must be True"
        assert p.non_production is True, f"{name}: non_production must be True"
        assert p.research_only is True, f"{name}: research_only must be True"
        assert p.allow_live_trading is False, f"{name}: allow_live_trading must be False"
        assert p.allow_broker_integration is False, f"{name}: allow_broker_integration must be False"
        assert p.allow_real_order is False, f"{name}: allow_real_order must be False"
        assert p.allow_investment_advice is False, f"{name}: allow_investment_advice must be False"
        assert p.allow_signal_generation is False, f"{name}: allow_signal_generation must be False"
        assert p.allow_portfolio_optimization is False, f"{name}: allow_portfolio_optimization must be False"
        assert p.allow_portfolio_construction is False, f"{name}: allow_portfolio_construction must be False"
        assert p.allow_position_sizing is False, f"{name}: allow_position_sizing must be False"
        assert p.allow_capital_allocation is False, f"{name}: allow_capital_allocation must be False"
        assert p.allow_weight_generation is False, f"{name}: allow_weight_generation must be False"
        assert p.allow_allocation_generation is False, f"{name}: allow_allocation_generation must be False"
        assert p.allow_rebalance_generation is False, f"{name}: allow_rebalance_generation must be False"
        assert p.allow_order_generation is False, f"{name}: allow_order_generation must be False"
        assert p.allow_optimizer_execution is False, f"{name}: allow_optimizer_execution must be False"
        assert p.allow_solver_execution is False, f"{name}: allow_solver_execution must be False"
        assert p.allow_grid_search_execution is False, f"{name}: allow_grid_search_execution must be False"
        assert p.allow_efficient_frontier_generation is False, f"{name}: allow_efficient_frontier_generation must be False"
        assert p.allow_metric_calculation is False, f"{name}: allow_metric_calculation must be False"
        assert p.allow_result_claim is False, f"{name}: allow_result_claim must be False"
        assert p.allow_performance_claim is False, f"{name}: allow_performance_claim must be False"
        assert p.allow_strategy_approval is False, f"{name}: allow_strategy_approval must be False"
        assert p.allow_model_training is False, f"{name}: allow_model_training must be False"
        assert p.allow_model_predict is False, f"{name}: allow_model_predict must be False"
        assert p.allow_target_label_generation is False, f"{name}: allow_target_label_generation must be False"
        assert p.allow_prediction_generation is False, f"{name}: allow_prediction_generation must be False"
        assert p.allow_model_registry_write is False, f"{name}: allow_model_registry_write must be False"
        assert p.allow_artifact_persistence is False, f"{name}: allow_artifact_persistence must be False"
        assert p.allow_model_deployment is False, f"{name}: allow_model_deployment must be False"
        assert p.allow_production_deployment is False, f"{name}: allow_production_deployment must be False"
        assert p.allow_production_approval is False, f"{name}: allow_production_approval must be False"
        assert p.allow_broker_ready_approval is False, f"{name}: allow_broker_ready_approval must be False"
        assert p.allow_live_trading_approval is False, f"{name}: allow_live_trading_approval must be False"
        assert p.allow_official_approval_claim is False, f"{name}: allow_official_approval_claim must be False"
        assert p.allow_production_ready_claim is False, f"{name}: allow_production_ready_claim must be False"
        assert p.allow_broker_ready_claim is False, f"{name}: allow_broker_ready_claim must be False"
        assert p.allow_full_article_usage is False, f"{name}: allow_full_article_usage must be False"
        assert p.allow_source_overwrite is False, f"{name}: allow_source_overwrite must be False"
    return True
