# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Survivorship Bias Guards Module.

Defines point-in-time universe filters and delisting event integration specifications.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    BIAS_GUARD_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

SURVIVORSHIP_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_name": "point_in_time_commodity_contracts_guard",
        "scope": "Historical expired futures contracts",
        "rule": "Resampled paths must draw from contemporaneous tradable contracts, not backward-looking continuous splices only.",
        "status": "ACTIVE",
    },
    {
        "guard_name": "delisted_fx_pair_inclusion_guard",
        "scope": "Peg breakages and currency reorganizations",
        "rule": "Historical FX series must retain peg breakdowns and re-denominations to avoid survivor skew.",
        "status": "ACTIVE",
    },
]


def build_monte_carlo_survivorship_bias_guard_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the survivorship bias guard registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for g in SURVIVORSHIP_GUARDS:
        rows.append(
            {
                "guard_name": g["guard_name"],
                "scope": g["scope"],
                "rule": g["rule"],
                "status": g["status"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": BIAS_GUARD_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": BIAS_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": bool((df["status"] == "ACTIVE").all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
