# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Profile Registry Module.

Compiles profile metadata and enforces safety constraints for all registered profiles.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import (
    MonteCarloProfile,
    list_monte_carlo_profiles,
)
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    MONTE_CARLO_PROFILE_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)


def build_monte_carlo_profile_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo profile registry DataFrame and summary."""
    profiles = list_monte_carlo_profiles()
    rows: List[Dict[str, Any]] = []

    for p in profiles:
        is_active = p.profile_name == profile.profile_name
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "is_active": is_active,
                "dry_run": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "allow_live_trading": p.allow_live_trading,
                "allow_broker_integration": p.allow_broker_integration,
                "allow_real_order": p.allow_real_order,
                "allow_investment_advice": p.allow_investment_advice,
                "allow_signal_generation": p.allow_signal_generation,
                "allow_monte_carlo_execution": p.allow_monte_carlo_execution,
                "allow_bootstrap_execution": p.allow_bootstrap_execution,
                "allow_resampling_execution": p.allow_resampling_execution,
                "allow_parameter_optimization": p.allow_parameter_optimization,
                "allow_parameter_sweep_execution": p.allow_parameter_sweep_execution,
                "allow_metric_calculation": p.allow_metric_calculation,
                "allow_model_training": p.allow_model_training,
                "allow_model_predict": p.allow_model_predict,
                "allow_production_ready_claim": p.allow_production_ready_claim,
                "allow_broker_ready_claim": p.allow_broker_ready_claim,
                "allow_performance_claim": p.allow_performance_claim,
                "resampling_iterations_placeholder": p.resampling_iterations_placeholder,
                "block_length_default": p.block_length_default,
                "confidence_interval_level": p.confidence_interval_level,
                "parameter_perturbation_pct": p.parameter_perturbation_pct,
                "non_signal": True,
                "broker_ready": False,
                "live_trading_ready": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": MONTE_CARLO_PROFILE_DOMAIN,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": MONTE_CARLO_PROFILE_DOMAIN,
        "total_profiles": len(df),
        "active_profile": profile.profile_name,
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "all_local_only": bool(df["local_only"].all()),
        "all_non_production": bool(df["non_production"].all()),
        "all_zero_execution": bool(
            (~df["allow_live_trading"]).all()
            and (~df["allow_broker_integration"]).all()
            and (~df["allow_monte_carlo_execution"]).all()
            and (~df["allow_bootstrap_execution"]).all()
            and (~df["allow_parameter_optimization"]).all()
        ),
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
