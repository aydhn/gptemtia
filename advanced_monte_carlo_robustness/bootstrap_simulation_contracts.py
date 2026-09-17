# -*- coding: utf-8 -*-
"""Phase 149: Bootstrap Simulation Contracts Module.

Defines bootstrap sampling contract specifications, mathematical assumptions,
and block configurations with zero sampling execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    BOOTSTRAP_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

BOOTSTRAP_METHODS: List[Dict[str, Any]] = [
    {
        "method_name": "standard_iid_bootstrap",
        "resampling_type": "uniform_replacement",
        "preserves_autocorrelation": False,
        "resampling_block_size_formula": "b = 1 (single observation)",
        "requires_iid_assumption": True,
        "description": "Standard Efron IID bootstrap drawing returns with replacement, destroying serial correlation.",
    },
    {
        "method_name": "circular_block_bootstrap",
        "resampling_type": "wrapped_block_replacement",
        "preserves_autocorrelation": True,
        "resampling_block_size_formula": "b = ceil(T^(1/3))",
        "requires_iid_assumption": False,
        "description": "Circular block bootstrap wrapping ends of the series to ensure uniform observation probability.",
    },
    {
        "method_name": "wild_bootstrap_heteroskedastic",
        "resampling_type": "residual_multiplier",
        "preserves_autocorrelation": False,
        "resampling_block_size_formula": "v ~ Rademacher distribution {-1, 1}",
        "requires_iid_assumption": False,
        "description": "Wild bootstrap preserving conditional heteroskedasticity in time series innovations.",
    },
    {
        "method_name": "studentized_bootstrap",
        "resampling_type": "t_statistic_resampling",
        "preserves_autocorrelation": False,
        "resampling_block_size_formula": "t* = (theta* - theta) / se*",
        "requires_iid_assumption": True,
        "description": "Second-order accurate bootstrap for confidence interval estimation without normal approximation.",
    },
]


def build_bootstrap_simulation_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the bootstrap simulation contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for m in BOOTSTRAP_METHODS:
        rows.append(
            {
                "method_name": m["method_name"],
                "resampling_type": m["resampling_type"],
                "preserves_autocorrelation": m["preserves_autocorrelation"],
                "resampling_block_size_formula": m["resampling_block_size_formula"],
                "requires_iid_assumption": m["requires_iid_assumption"],
                "description": m["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "simulation_executed": False,
                "sample_generated": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": BOOTSTRAP_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": BOOTSTRAP_CONTRACT_DOMAIN,
        "total_methods": len(df),
        "all_unexecuted": bool((~df["simulation_executed"]).all() and (~df["sample_generated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
