# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Robustness and Parameter Stability Configuration.

Defines MonteCarloProfile dataclass, preset profiles, and safety boundaries.
Enforces local/offline research parameters with zero live trading and zero execution.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class MonteCarloProfile:
    """Configuration profile for Phase 149 Monte Carlo Robustness Contract Layer."""

    profile_name: str
    description: str
    current_phase: int = 149
    target_final_phase: int = 160
    next_phase: int = 150
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
    allow_parameter_optimization: bool = False
    allow_parameter_sweep_execution: bool = False
    allow_monte_carlo_execution: bool = False
    allow_bootstrap_execution: bool = False
    allow_resampling_execution: bool = False
    allow_metric_calculation: bool = False
    allow_robustness_metric_calculation: bool = False
    allow_parameter_stability_metric_calculation: bool = False
    allow_distribution_calculation: bool = False
    allow_var_calculation: bool = False
    allow_expected_shortfall_calculation: bool = False
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
    enable_robustness_contracts: bool = True
    enable_resampling_placeholders: bool = True
    enable_parameter_stability_contracts: bool = True
    enable_metric_placeholders: bool = True
    enable_bias_guards: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_150_handoff: bool = True
    min_readiness_score: float = 0.50
    save_reports: bool = True
    resampling_iterations_placeholder: int = 1000
    block_length_default: int = 20
    confidence_interval_level: float = 0.95
    parameter_perturbation_pct: float = 0.10


PROFILES: Dict[str, MonteCarloProfile] = {
    "balanced_local_monte_carlo_robustness_contracts": MonteCarloProfile(
        profile_name="balanced_local_monte_carlo_robustness_contracts",
        description="Standard balanced local/offline Monte Carlo robustness and parameter stability contract profile.",
        resampling_iterations_placeholder=1000,
        block_length_default=20,
        confidence_interval_level=0.95,
        parameter_perturbation_pct=0.10,
    ),
    "conservative_local_monte_carlo_contracts": MonteCarloProfile(
        profile_name="conservative_local_monte_carlo_contracts",
        description="Conservative contract profile with wider confidence bands and strict perturbation thresholds.",
        resampling_iterations_placeholder=2000,
        block_length_default=30,
        confidence_interval_level=0.99,
        parameter_perturbation_pct=0.05,
    ),
    "deep_stress_resampling_contracts": MonteCarloProfile(
        profile_name="deep_stress_resampling_contracts",
        description="Deep stress resampling linkage contract profile exploring extreme path resamplings and heavy tail risks.",
        resampling_iterations_placeholder=5000,
        block_length_default=15,
        confidence_interval_level=0.99,
        parameter_perturbation_pct=0.20,
    ),
}


def get_default_monte_carlo_profile() -> MonteCarloProfile:
    """Return the default Monte Carlo robustness profile."""
    return PROFILES["balanced_local_monte_carlo_robustness_contracts"]


def get_monte_carlo_profile(name: Optional[str] = None) -> MonteCarloProfile:
    """Get a specific Monte Carlo profile by name or default."""
    if not name:
        return get_default_monte_carlo_profile()
    if name not in PROFILES:
        raise KeyError(f"Unknown Monte Carlo profile: {name}. Available: {list(PROFILES.keys())}")
    return PROFILES[name]


def list_monte_carlo_profiles(enabled_only: bool = True) -> List[MonteCarloProfile]:
    """List all available Monte Carlo profiles."""
    return list(PROFILES.values())


def validate_monte_carlo_profiles() -> bool:
    """Validate all registered profiles adhere to safety invariants."""
    for name, p in PROFILES.items():
        assert p.current_phase == 149, f"{name}: current_phase must be 149"
        assert p.target_final_phase == 160, f"{name}: target_final_phase must be 160"
        assert p.next_phase == 150, f"{name}: next_phase must be 150"
        assert p.dry_run_default is True, f"{name}: dry_run_default must be True"
        assert p.local_only is True, f"{name}: local_only must be True"
        assert p.non_production is True, f"{name}: non_production must be True"
        assert p.research_only is True, f"{name}: research_only must be True"
        assert p.allow_live_trading is False, f"{name}: allow_live_trading must be False"
        assert p.allow_broker_integration is False, f"{name}: allow_broker_integration must be False"
        assert p.allow_real_order is False, f"{name}: allow_real_order must be False"
        assert p.allow_investment_advice is False, f"{name}: allow_investment_advice must be False"
        assert p.allow_signal_generation is False, f"{name}: allow_signal_generation must be False"
        assert p.allow_optimizer_execution is False, f"{name}: allow_optimizer_execution must be False"
        assert p.allow_parameter_optimization is False, f"{name}: allow_parameter_optimization must be False"
        assert p.allow_parameter_sweep_execution is False, f"{name}: allow_parameter_sweep_execution must be False"
        assert p.allow_monte_carlo_execution is False, f"{name}: allow_monte_carlo_execution must be False"
        assert p.allow_bootstrap_execution is False, f"{name}: allow_bootstrap_execution must be False"
        assert p.allow_resampling_execution is False, f"{name}: allow_resampling_execution must be False"
        assert p.allow_metric_calculation is False, f"{name}: allow_metric_calculation must be False"
        assert p.allow_robustness_metric_calculation is False, f"{name}: allow_robustness_metric_calculation must be False"
        assert p.allow_distribution_calculation is False, f"{name}: allow_distribution_calculation must be False"
        assert p.allow_var_calculation is False, f"{name}: allow_var_calculation must be False"
        assert p.allow_model_training is False, f"{name}: allow_model_training must be False"
        assert p.allow_model_predict is False, f"{name}: allow_model_predict must be False"
        assert p.allow_production_ready_claim is False, f"{name}: allow_production_ready_claim must be False"
        assert p.allow_broker_ready_claim is False, f"{name}: allow_broker_ready_claim must be False"
        assert p.allow_source_overwrite is False, f"{name}: allow_source_overwrite must be False"
    return True
