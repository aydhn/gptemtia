# -*- coding: utf-8 -*-
"""Phase 149: Stress Monte Carlo Linkage Module.

Links Phase 148 stress testing contracts and shock libraries directly into Monte Carlo contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    LINKAGE_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

STRESS_LINKAGES: List[Dict[str, Any]] = [
    {
        "linkage_id": "LINK_STRESS_VOLATILITY_SHOCKS",
        "phase_148_ref": "volatility_shock_scenario_contracts",
        "monte_carlo_application": "variance_scaling_priors",
        "status": "SATISFIED",
    },
    {
        "linkage_id": "LINK_STRESS_LIQUIDITY_SHOCKS",
        "phase_148_ref": "liquidity_shock_scenario_contracts",
        "monte_carlo_application": "volume_thinning_in_drawdowns",
        "status": "SATISFIED",
    },
    {
        "linkage_id": "LINK_STRESS_REGIME_BREAKDOWNS",
        "phase_148_ref": "regime_shock_scenario_contracts",
        "monte_carlo_application": "cross_asset_correlation_breakdowns",
        "status": "SATISFIED",
    },
]


def build_stress_monte_carlo_linkage_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the stress Monte Carlo linkage registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in STRESS_LINKAGES:
        rows.append(
            {
                "linkage_id": s["linkage_id"],
                "phase_148_ref": s["phase_148_ref"],
                "monte_carlo_application": s["monte_carlo_application"],
                "status": s["status"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": LINKAGE_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": LINKAGE_DOMAIN,
        "total_stress_linkages": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
