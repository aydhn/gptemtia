# -*- coding: utf-8 -*-
"""Phase 149: Stationary Bootstrap Contracts Module.

Defines Politis-Romano stationary bootstrap contracts using geometric block lengths,
ensuring strict stationarity of the resampled series without sample generation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    STATIONARY_BOOTSTRAP_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

STATIONARY_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "politis_romano_stationary_bootstrap",
        "geometric_p_formula": "p = 1 / mean_block_length",
        "mean_block_length_default": 20,
        "preserves_stationarity": True,
        "asymptotic_consistency": "Consistent for stationary weakly dependent processes",
        "description": "Politis and Romano (1994) stationary bootstrap with geometrically distributed random block lengths.",
    },
    {
        "contract_id": "adaptive_stationary_bootstrap",
        "geometric_p_formula": "p_adapt = f(autocorrelation_decay_rate)",
        "mean_block_length_default": 15,
        "preserves_stationarity": True,
        "asymptotic_consistency": "Adaptive rate tuning per asset class",
        "description": "Stationary bootstrap with parameter p dynamically tuned to commodity/FX memory horizons.",
    },
]


def build_stationary_bootstrap_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the stationary bootstrap contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for c in STATIONARY_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "geometric_p_formula": c["geometric_p_formula"],
                "mean_block_length_default": c["mean_block_length_default"],
                "preserves_stationarity": c["preserves_stationarity"],
                "asymptotic_consistency": c["asymptotic_consistency"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "execution_allowed": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": STATIONARY_BOOTSTRAP_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": STATIONARY_BOOTSTRAP_CONTRACT_DOMAIN,
        "total_contracts": len(df),
        "execution_allowed": False,
        "all_unexecuted": True,
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
