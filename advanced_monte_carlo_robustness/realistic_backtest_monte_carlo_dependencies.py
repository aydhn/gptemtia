# -*- coding: utf-8 -*-
"""Phase 149: Realistic Backtest Monte Carlo Dependencies Module.

Tracks dependencies on Phase 146 realistic backtest contracts and execution accounting.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DEPENDENCY_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

BACKTEST_DEPS: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_REALISTIC_BACKTEST_CONTRACTS",
        "source_phase": 146,
        "description": "Realistic backtest execution schema, fill modeling, and cash accounting contracts.",
        "status": "SATISFIED",
    },
    {
        "dependency_id": "DEP_REALISTIC_TRADE_BLOTTER",
        "source_phase": 146,
        "description": "Trade sequence ledger and execution timestamps required for trade reshuffling.",
        "status": "SATISFIED",
    },
]


def build_realistic_backtest_monte_carlo_dependency_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the realistic backtest Monte Carlo dependency registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for d in BACKTEST_DEPS:
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
