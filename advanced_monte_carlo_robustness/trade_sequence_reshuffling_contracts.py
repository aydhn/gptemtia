# -*- coding: utf-8 -*-
"""Phase 149: Trade Sequence Reshuffling Contracts Module.

Defines trade sequence reshuffling and permutation contracts to evaluate
order-dependent risk, drawdown paths, and time-under-water under zero live execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    TRADE_SEQUENCE_RESHUFFLING_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

RESHUFFLE_CONTRACTS: List[Dict[str, Any]] = [
    {
        "reshuffle_contract_name": "uniform_random_trade_permutation",
        "unit_of_reshuffling": "individual_closed_trade_pnl",
        "preserves_total_pnl": True,
        "evaluates_drawdown_order_risk": True,
        "permutation_count_placeholder": 1000,
        "description": "Permutes trade execution order randomly without replacement to examine maximum drawdown sensitivity to trade sequencing.",
    },
    {
        "reshuffle_contract_name": "block_trade_reshuffling",
        "unit_of_reshuffling": "consecutive_trade_clusters",
        "preserves_total_pnl": True,
        "evaluates_drawdown_order_risk": True,
        "permutation_count_placeholder": 1000,
        "description": "Reshuffles clusters of contiguous trades to preserve strategy streakiness and win/loss clustering.",
    },
    {
        "reshuffle_contract_name": "trade_replacement_bootstrap",
        "unit_of_reshuffling": "trade_pnl_with_replacement",
        "preserves_total_pnl": False,
        "evaluates_drawdown_order_risk": True,
        "permutation_count_placeholder": 1000,
        "description": "Draws trades with replacement to assess cumulative return variance and profit-factor dispersion.",
    },
]


def build_trade_sequence_reshuffling_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the trade sequence reshuffling contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for c in RESHUFFLE_CONTRACTS:
        rows.append(
            {
                "reshuffle_contract_name": c["reshuffle_contract_name"],
                "unit_of_reshuffling": c["unit_of_reshuffling"],
                "preserves_total_pnl": c["preserves_total_pnl"],
                "evaluates_drawdown_order_risk": c["evaluates_drawdown_order_risk"],
                "permutation_count_placeholder": c["permutation_count_placeholder"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "reshuffling_executed": False,
                "permutations_generated": 0,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": TRADE_SEQUENCE_RESHUFFLING_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": TRADE_SEQUENCE_RESHUFFLING_DOMAIN,
        "total_contracts": len(df),
        "all_unexecuted": bool((~df["reshuffling_executed"]).all() and (df["permutations_generated"] == 0).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
