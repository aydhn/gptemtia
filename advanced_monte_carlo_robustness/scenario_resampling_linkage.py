# -*- coding: utf-8 -*-
"""Phase 149: Scenario Resampling Linkage Module.

Links Monte Carlo resampling procedures with structured macro and market scenarios.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    LINKAGE_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

SCENARIO_LINKAGES: List[Dict[str, Any]] = [
    {
        "linkage_name": "historical_crisis_window_resampling",
        "scenario_source": "Phase 148 Historical Stress Scenarios",
        "integration_mode": "conditioned_block_resampling",
        "status": "SATISFIED",
        "description": "Links historical crisis event return blocks (e.g. 2008, 2020) as conditioned sampling pools.",
    },
    {
        "linkage_name": "hypothetical_shock_path_resampling",
        "scenario_source": "Phase 148 Hypothetical Stress Scenarios",
        "integration_mode": "synthetic_mean_shift_injection",
        "status": "SATISFIED",
        "description": "Links severe hypothetical shocks as parameter shift priors for robustness envelope bounds.",
    },
]


def build_scenario_resampling_linkage_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the scenario resampling linkage registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for l in SCENARIO_LINKAGES:
        rows.append(
            {
                "linkage_name": l["linkage_name"],
                "scenario_source": l["scenario_source"],
                "integration_mode": l["integration_mode"],
                "status": l["status"],
                "description": l["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": LINKAGE_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": LINKAGE_DOMAIN,
        "total_linkages": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
