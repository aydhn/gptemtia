# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Signal Input Contracts Module.

Defines schemas for historical strategy signals being evaluated under Monte Carlo contracts.
Strictly non-signal, historical-only metadata without live trading implications.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    OUTPUT_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

SIGNAL_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "signal_contract_name": "historical_strategy_allocations_contract",
        "signal_nature": "historical_simulation_weights",
        "live_trading_allowed": False,
        "directional_advice": False,
        "description": "Historical position weight series across strategy models evaluated for order stability.",
    },
    {
        "signal_contract_name": "historical_entry_exit_trigger_contract",
        "signal_nature": "historical_rule_activations",
        "live_trading_allowed": False,
        "directional_advice": False,
        "description": "Historical discrete trigger timestamps evaluated under parameter perturbation shifts.",
    },
]


def build_monte_carlo_signal_input_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo signal input contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in SIGNAL_INPUT_CONTRACTS:
        rows.append(
            {
                "signal_contract_name": s["signal_contract_name"],
                "signal_nature": s["signal_nature"],
                "live_trading_allowed": s["live_trading_allowed"],
                "directional_advice": s["directional_advice"],
                "description": s["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": OUTPUT_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": OUTPUT_CONTRACT_DOMAIN,
        "total_signal_input_contracts": len(df),
        "all_non_live": bool((~df["live_trading_allowed"]).all() and (~df["directional_advice"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
