# -*- coding: utf-8 -*-
"""Phase 149: Block Bootstrap Contracts Module.

Defines block bootstrap contracts designed to preserve autocorrelation,
conditional volatility, and time-structure dependencies in financial series.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    BLOCK_BOOTSTRAP_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

BLOCK_CONTRACTS: List[Dict[str, Any]] = [
    {
        "block_method": "moving_block_bootstrap_mbb",
        "block_length": 20,
        "block_selection_mode": "overlapping",
        "dependency_preserved": "short_term_autocorrelation",
        "optimal_block_formula": "b_opt = (2 * rho / (1 - rho^2))^(2/3) * T^(1/3)",
        "description": "Kunsch (1989) overlapping moving block bootstrap preserving lag structure.",
    },
    {
        "block_method": "non_overlapping_block_bootstrap_nbb",
        "block_length": 25,
        "block_selection_mode": "non_overlapping",
        "dependency_preserved": "medium_term_volatility_clustering",
        "optimal_block_formula": "b_opt = T / k_partitions",
        "description": "Carlstein (1986) non-overlapping block bootstrap with discrete window boundaries.",
    },
    {
        "block_method": "circular_block_bootstrap_cbb",
        "block_length": 20,
        "block_selection_mode": "circular_wrapping",
        "dependency_preserved": "all_sample_point_probabilities_equal",
        "optimal_block_formula": "b_opt = 1.75 * T^(1/3)",
        "description": "Politis and Romano (1992) circular block bootstrap eliminating edge bias.",
    },
    {
        "block_method": "regime_conditioned_block_bootstrap",
        "block_length": 15,
        "block_selection_mode": "regime_stratified",
        "dependency_preserved": "regime_specific_serial_correlation",
        "optimal_block_formula": "b_opt = min(b_regime_length, 20)",
        "description": "Block bootstrap drawing contiguous chunks strictly within matching Phase 135 market regimes.",
    },
]


def build_block_bootstrap_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the block bootstrap contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for c in BLOCK_CONTRACTS:
        rows.append(
            {
                "block_method": c["block_method"],
                "block_length": profile.block_length_default or c["block_length"],
                "block_selection_mode": c["block_selection_mode"],
                "dependency_preserved": c["dependency_preserved"],
                "optimal_block_formula": c["optimal_block_formula"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "execution_allowed": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": BLOCK_BOOTSTRAP_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": BLOCK_BOOTSTRAP_CONTRACT_DOMAIN,
        "total_block_contracts": len(df),
        "total_contracts": len(df),
        "execution_allowed": False,
        "all_unexecuted": True,
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
