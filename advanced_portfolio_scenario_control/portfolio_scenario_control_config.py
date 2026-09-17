# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Testing and Drawdown Control Configuration.

Provides profile management, phase constraints, non-production boundaries,
and strict safety gates for offline/local scenario testing and drawdown control contracts.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class PortfolioScenarioControlProfile:
    """Configuration profile for Phase 156 Portfolio Scenario Testing & Drawdown Control block."""
    profile_name: str
    description: str
    current_phase: int = 156
    target_final_phase: int = 160
    next_phase: int = 157
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
    allow_scenario_execution: bool = False
    allow_drawdown_control_execution: bool = False
    allow_portfolio_control_action: bool = False
    allow_portfolio_adjustment: bool = False
    allow_rebalance_generation: bool = False
    allow_hedge_derisk_generation: bool = False
    allow_exposure_reduction: bool = False
    allow_stop_control: bool = False
    allow_order_generation: bool = False
    allow_alert_generation: bool = False
    allow_dashboard_generation: bool = False
    allow_metric_calculation: bool = False
    allow_drawdown_calculation: bool = False
    allow_scenario_pnl_calculation: bool = False
    allow_var_calculation: bool = False
    allow_expected_shortfall_calculation: bool = False
    allow_exposure_calculation: bool = False
    allow_optimizer_execution: bool = False
    allow_result_claim: bool = False
    allow_performance_claim: bool = False
    allow_strategy_approval: bool = False
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
    enable_scenario_contracts: bool = True
    enable_drawdown_contracts: bool = True
    enable_control_placeholders: bool = True
    enable_claim_guards: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_157_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    enabled: bool = True

    def validate(self) -> bool:
        """Validate non-production safety invariants for this profile."""
        if self.allow_live_trading or self.allow_broker_integration or self.allow_real_order:
            raise ValueError(f"{self.profile_name}: Live trading or broker integration strictly prohibited!")
        if self.allow_scenario_execution or self.allow_drawdown_control_execution or self.allow_portfolio_control_action:
            raise ValueError(f"{self.profile_name}: Real scenario execution or drawdown control strictly prohibited!")
        if self.allow_portfolio_adjustment or self.allow_rebalance_generation or self.allow_hedge_derisk_generation or self.allow_order_generation:
            raise ValueError(f"{self.profile_name}: Portfolio adjustment/rebalance/hedge strictly prohibited!")
        if not self.non_production or not self.dry_run_default:
            raise ValueError(f"{self.profile_name}: Must be non-production dry-run profile!")
        return True


PROFILES: Dict[str, PortfolioScenarioControlProfile] = {
    "balanced_local_portfolio_scenario_control_contracts": PortfolioScenarioControlProfile(
        profile_name="balanced_local_portfolio_scenario_control_contracts",
        description="Dengeli yerel Portfolio Scenario Testing ve Drawdown Control sozlesme profili.",
        current_phase=156,
        target_final_phase=160,
        next_phase=157,
        min_readiness_score=0.50,
    ),
    "strict_non_production_scenario_control_safety": PortfolioScenarioControlProfile(
        profile_name="strict_non_production_scenario_control_safety",
        description="Siki guvenlikli non-production senaryo testi ve drawdown kontrol sozlesme profili.",
        current_phase=156,
        target_final_phase=160,
        next_phase=157,
        min_readiness_score=0.65,
    ),
    "dry_run_phase_156_scenario_control_focus": PortfolioScenarioControlProfile(
        profile_name="dry_run_phase_156_scenario_control_focus",
        description="Dry-run odakli portfoy senaryo test sozlesme profili.",
        current_phase=156,
        target_final_phase=160,
        next_phase=157,
        min_readiness_score=0.50,
    ),
    "dry_run_phase_156_drawdown_control_focus": PortfolioScenarioControlProfile(
        profile_name="dry_run_phase_156_drawdown_control_focus",
        description="Dry-run odakli portfoy drawdown kontrol ve aksiyon yer tutucu profili.",
        current_phase=156,
        target_final_phase=160,
        next_phase=157,
        min_readiness_score=0.50,
    ),
}

PORTFOLIO_SCENARIO_CONTROL_PROFILES = PROFILES


def get_portfolio_scenario_control_profile(name: str) -> PortfolioScenarioControlProfile:
    """Retrieve profile by name or raise KeyError."""
    if name not in PROFILES:
        raise KeyError(
            f"Profile '{name}' not found. Available profiles: {list(PROFILES.keys())}"
        )
    return PROFILES[name]


def get_default_portfolio_scenario_control_profile() -> PortfolioScenarioControlProfile:
    """Return default profile for Phase 156."""
    return PROFILES["balanced_local_portfolio_scenario_control_contracts"]


def list_portfolio_scenario_control_profiles() -> List[str]:
    """Return list of available profile names."""
    return list(PROFILES.keys())
