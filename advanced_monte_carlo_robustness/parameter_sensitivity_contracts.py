# -*- coding: utf-8 -*-
"""Phase 149: Parameter Sensitivity Contracts Module.

Defines local sensitivity gradients, partial derivatives, and elasticity specifications.
Zero gradient descent, optimizer execution, or parameter sweeps permitted.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    PARAMETER_SENSITIVITY_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

SENSITIVITY_CONTRACTS: List[Dict[str, Any]] = [
    {
        "parameter_name": "trend_ema_span_fast",
        "sensitivity_type": "finite_difference_first_order",
        "perturbation_pct": 0.10,
        "fragility_threshold": 0.25,
        "formula": "S = (PnL(theta + h) - PnL(theta - h)) / (2 * h * PnL(theta))",
        "description": "First-order sensitivity of fast EMA window to finite local step perturbations.",
    },
    {
        "parameter_name": "trend_ema_span_slow",
        "sensitivity_type": "finite_difference_first_order",
        "perturbation_pct": 0.10,
        "fragility_threshold": 0.20,
        "formula": "S = (PnL(theta + h) - PnL(theta - h)) / (2 * h * PnL(theta))",
        "description": "First-order sensitivity of slow EMA window ensuring slope gradualism.",
    },
    {
        "parameter_name": "bollinger_bandwidth_k",
        "sensitivity_type": "elasticity_log_derivative",
        "perturbation_pct": 0.05,
        "fragility_threshold": 0.30,
        "formula": "E = (d log(Sharpe)) / (d log(k))",
        "description": "Log-elasticity of Sharpe ratio with respect to Bollinger standard deviation multiplier.",
    },
]


def build_parameter_sensitivity_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter sensitivity contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for c in SENSITIVITY_CONTRACTS:
        rows.append(
            {
                "parameter_name": c["parameter_name"],
                "sensitivity_type": c["sensitivity_type"],
                "perturbation_pct": profile.parameter_perturbation_pct or c["perturbation_pct"],
                "fragility_threshold": c["fragility_threshold"],
                "formula": c["formula"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "optimization_executed": False,
                "sensitivity_calculated": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": PARAMETER_SENSITIVITY_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": PARAMETER_SENSITIVITY_CONTRACT_DOMAIN,
        "total_contracts": len(df),
        "all_unexecuted": bool((~df["optimization_executed"]).all() and (~df["sensitivity_calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
