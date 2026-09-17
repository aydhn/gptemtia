# -*- coding: utf-8 -*-
"""Phase 149: Transaction Cost Monte Carlo Dependencies Module.

Tracks dependencies on Phase 146 transaction cost and fee schedules.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DEPENDENCY_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

COST_DEPS: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_TIERED_FEE_SCHEDULE",
        "source_phase": 146,
        "description": "Tiered broker commissions and exchange clearing fees for friction compounding.",
        "status": "SATISFIED",
    },
    {
        "dependency_id": "DEP_BORROW_FINANCING_COSTS",
        "source_phase": 146,
        "description": "Overnight swap and carry cost models applied across resampled holding periods.",
        "status": "SATISFIED",
    },
]


def build_transaction_cost_monte_carlo_dependency_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the transaction cost Monte Carlo dependency registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for d in COST_DEPS:
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
