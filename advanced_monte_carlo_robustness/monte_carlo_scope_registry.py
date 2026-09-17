# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Scope Registry Module.

Defines operational scope boundaries: local/offline contracts, zero execution, zero signals.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    MONTE_CARLO_SCOPE_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

SCOPE_ITEMS: List[Dict[str, Any]] = [
    {
        "scope_key": "local_offline_contract_layer",
        "description": "Monte Carlo robustness and parameter stability contract definitions executed locally/offline.",
        "is_in_scope": True,
        "enforcement": "MANDATORY",
    },
    {
        "scope_key": "resampling_and_bootstrap_specifications",
        "description": "Block bootstrap, stationary bootstrap, and return path resampling schemas.",
        "is_in_scope": True,
        "enforcement": "MANDATORY",
    },
    {
        "scope_key": "parameter_stability_and_sensitivity_contracts",
        "description": "Parameter perturbation ranges, plateau detection, and fragility indicators.",
        "is_in_scope": True,
        "enforcement": "MANDATORY",
    },
    {
        "scope_key": "bias_and_lookahead_guards",
        "description": "Guards preventing resampling data leakage, data snooping, and survivorship bias.",
        "is_in_scope": True,
        "enforcement": "MANDATORY",
    },
    {
        "scope_key": "phase_150_governance_handoff",
        "description": "Prerequisite compilation for Phase 150 Backtest Governance and Bias Control.",
        "is_in_scope": True,
        "enforcement": "MANDATORY",
    },
    {
        "scope_key": "true_monte_carlo_execution",
        "description": "Generating actual simulated random paths or synthesized asset prices.",
        "is_in_scope": False,
        "enforcement": "PROHIBITED",
    },
    {
        "scope_key": "bootstrap_simulation_execution",
        "description": "Drawing physical bootstrap samples or calculating resampled distributions.",
        "is_in_scope": False,
        "enforcement": "PROHIBITED",
    },
    {
        "scope_key": "parameter_optimization_and_sweeps",
        "description": "Running grid search, evolutionary algorithms, or parameter optimization.",
        "is_in_scope": False,
        "enforcement": "PROHIBITED",
    },
    {
        "scope_key": "real_metric_and_var_calculation",
        "description": "Computing actual VaR, Expected Shortfall, or empirical Sharpe distributions.",
        "is_in_scope": False,
        "enforcement": "PROHIBITED",
    },
    {
        "scope_key": "model_training_and_prediction",
        "description": "Model fitting, ML inference, prediction generation, or target label creation.",
        "is_in_scope": False,
        "enforcement": "PROHIBITED",
    },
    {
        "scope_key": "live_trading_and_broker_execution",
        "description": "Connecting to broker APIs, placing real/paper orders, or generating trade signals.",
        "is_in_scope": False,
        "enforcement": "PROHIBITED",
    },
    {
        "scope_key": "investment_advice_and_performance_guarantees",
        "description": "Producing directional recommendations or claiming guaranteed strategy returns.",
        "is_in_scope": False,
        "enforcement": "PROHIBITED",
    },
]


def build_monte_carlo_scope_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo scope registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for item in SCOPE_ITEMS:
        rows.append(
            {
                "scope_key": item["scope_key"],
                "description": item["description"],
                "is_in_scope": item["is_in_scope"],
                "enforcement": item["enforcement"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": MONTE_CARLO_SCOPE_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    in_scope_count = int(df["is_in_scope"].sum())
    prohibited_count = len(df) - in_scope_count

    summary = {
        "domain": MONTE_CARLO_SCOPE_DOMAIN,
        "total_scope_items": len(df),
        "in_scope_count": in_scope_count,
        "prohibited_count": prohibited_count,
        "profile_name": profile.profile_name,
        "all_prohibitions_enforced": True,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
