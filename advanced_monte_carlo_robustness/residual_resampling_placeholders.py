# -*- coding: utf-8 -*-
"""Phase 149: Residual Resampling Placeholders Module.

Defines placeholders and formula metadata for time-series and factor residual bootstrapping.
Zero synthetic residuals or actual innovations are generated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    RESIDUAL_RESAMPLING_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

RESIDUAL_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_id": "arma_garch_residual_resampling",
        "model_baseline": "ARMA(1,1)-GARCH(1,1)",
        "residual_type": "standardized_innovations",
        "formula_spec": "eps_t = z_t * sigma_t, where z_t* ~ empirical distribution(z)",
        "description": "Contracts bootstrapping standardized residuals from volatility models to capture fat-tailed innovations.",
    },
    {
        "placeholder_id": "macro_factor_residual_resampling",
        "model_baseline": "Multi-factor regression model",
        "residual_type": "idiosyncratic_asset_residuals",
        "formula_spec": "r_i,t - beta_i' f_t = eps_i,t*",
        "description": "Resampling idiosyncratic asset return shocks after removing systemic macroeconomic factor variations.",
    },
    {
        "placeholder_id": "regime_transition_residual_resampling",
        "model_baseline": "Markov Switching / HMM baseline",
        "residual_type": "state_conditional_filtered_residuals",
        "formula_spec": "eps_s,t = (r_t - mu_s) / sigma_s",
        "description": "Contracts resampling regime-conditioned filtered innovations across discrete market behavior states.",
    },
]


def build_residual_resampling_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the residual resampling placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for p in RESIDUAL_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_id": p["placeholder_id"],
                "model_baseline": p["model_baseline"],
                "residual_type": p["residual_type"],
                "formula_spec": p["formula_spec"],
                "description": p["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "residuals_generated": 0,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": RESIDUAL_RESAMPLING_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": RESIDUAL_RESAMPLING_PLACEHOLDER_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": bool((~df["calculated"]).all() and (df["residuals_generated"] == 0).all()),
        "all_unexecuted": True,
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
