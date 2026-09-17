# -*- coding: utf-8 -*-
"""Phase 149: Slippage Monte Carlo Dependencies Module.

Tracks dependencies on Phase 146 non-linear slippage and market impact models.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DEPENDENCY_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

SLIPPAGE_DEPS: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_SQUARE_ROOT_SLIPPAGE_MODEL",
        "source_phase": 146,
        "description": "Almgren-Chriss square root market impact model for trade volume penalty in resampled paths.",
        "status": "SATISFIED",
    },
    {
        "dependency_id": "DEP_VOLATILITY_SCALED_SPREADS",
        "source_phase": 146,
        "description": "Dynamic spread widening models scaling slippage penalties during high-volatility draws.",
        "status": "SATISFIED",
    },
]


def build_slippage_monte_carlo_dependency_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the slippage Monte Carlo dependency registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for d in SLIPPAGE_DEPS:
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
