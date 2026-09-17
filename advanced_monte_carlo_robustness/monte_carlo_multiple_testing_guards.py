# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Multiple Testing Guards Module.

Guards against false discovery in hypothesis testing using Bonferroni, Holm,
and Benjamini-Hochberg False Discovery Rate (FDR) corrections.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    BIAS_GUARD_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

MULTIPLE_TESTING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_name": "bonferroni_familywise_error_guard",
        "methodology": "FWER adjustment alpha_adj = alpha / K_tests",
        "description": "Conservative p-value threshold adjustment when testing multiple parameter variations.",
        "status": "ACTIVE",
    },
    {
        "guard_name": "benjamini_hochberg_fdr_guard",
        "methodology": "Benjamini-Hochberg (1995) False Discovery Rate control",
        "description": "Adaptive p-value sorting controlling expected proportion of false positive strategy anomalies.",
        "status": "ACTIVE",
    },
]


def build_monte_carlo_multiple_testing_guard_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the multiple testing guard registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for g in MULTIPLE_TESTING_GUARDS:
        rows.append(
            {
                "guard_name": g["guard_name"],
                "methodology": g["methodology"],
                "description": g["description"],
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
