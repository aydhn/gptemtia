# -*- coding: utf-8 -*-
"""Phase 149: Parameter Perturbation Contracts Module.

Defines parameter perturbation grids, step sizes, and discrete neighborhood specs.
Zero parameter perturbation sweeps or evaluations are executed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    PARAMETER_PERTURBATION_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

PERTURBATION_SPECS: List[Dict[str, Any]] = [
    {
        "parameter_group": "trend_following_indicators",
        "perturbation_mode": "relative_percentage_steps",
        "step_increments": "[-20%, -10%, -5%, 0%, +5%, +10%, +20%]",
        "minimum_points_required": 7,
        "description": "Grid of relative increments to evaluate response surface curvature around baseline.",
    },
    {
        "parameter_group": "volatility_thresholds",
        "perturbation_mode": "absolute_unit_steps",
        "step_increments": "[-0.50, -0.25, 0.0, +0.25, +0.50]",
        "minimum_points_required": 5,
        "description": "Fixed discrete step intervals for ATR, standard deviation, and quantile thresholds.",
    },
    {
        "parameter_group": "time_filters",
        "perturbation_mode": "session_shift_minutes",
        "step_increments": "[-60m, -30m, 0m, +30m, +60m]",
        "minimum_points_required": 5,
        "description": "Session open/close entry window perturbation evaluating intraday timing sensitivity.",
    },
]


def build_parameter_perturbation_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter perturbation contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in PERTURBATION_SPECS:
        rows.append(
            {
                "parameter_group": s["parameter_group"],
                "perturbation_mode": s["perturbation_mode"],
                "step_increments": s["step_increments"],
                "minimum_points_required": s["minimum_points_required"],
                "description": s["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "perturbation_executed": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": PARAMETER_PERTURBATION_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": PARAMETER_PERTURBATION_CONTRACT_DOMAIN,
        "total_specs": len(df),
        "total_contracts": len(df),
        "all_unexecuted": bool((~df["perturbation_executed"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
