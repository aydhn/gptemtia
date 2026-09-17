# -*- coding: utf-8 -*-
"""Phase 149: Regime Monte Carlo Dependencies Module.

Tracks dependencies on Phase 135 market regime acceptance contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DEPENDENCY_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

REGIME_DEPS: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_REGIME_CLASSIFICATION_CONTRACTS",
        "source_phase": 135,
        "description": "Regime acceptance classifications (Bullish Trend, Bearish Trend, Mean-Reverting, High-Vol Crisis).",
        "status": "SATISFIED",
    },
    {
        "dependency_id": "DEP_REGIME_TRANSITION_PROBABILITIES",
        "source_phase": 135,
        "description": "Markov transition matrices conditioning block bootstrap sequence generation.",
        "status": "SATISFIED",
    },
]


def build_regime_monte_carlo_dependency_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the regime Monte Carlo dependency registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for d in REGIME_DEPS:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "source_phase": d["source_phase"],
                "description": d["description"],
                "status": d["status"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": DEPENDENCY_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": DEPENDENCY_DOMAIN,
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
