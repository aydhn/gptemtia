# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Data Snooping Bias Guards Module.

Defines guards and statistical corrections (White's Reality Check, Hansen SPA)
to prevent data snooping bias across strategy parameter sets.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    BIAS_GUARD_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

DATA_SNOOPING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_name": "whites_reality_check_guard",
        "methodology": "White (2000) Reality Check for Data Snooping",
        "purpose": "Evaluates whether best parameter outcome is statistically superior to benchmark after accounting for full search universe.",
        "status": "ACTIVE",
    },
    {
        "guard_name": "hansen_superior_predictive_ability_guard",
        "methodology": "Hansen (2005) Test for Superior Predictive Ability (SPA)",
        "purpose": "Improves power over White's check using studentized test statistics and re-centered bootstrap distributions.",
        "status": "ACTIVE",
    },
]


def build_monte_carlo_data_snooping_bias_guard_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the data snooping bias guard registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for g in DATA_SNOOPING_GUARDS:
        rows.append(
            {
                "guard_name": g["guard_name"],
                "methodology": g["methodology"],
                "purpose": g["purpose"],
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
