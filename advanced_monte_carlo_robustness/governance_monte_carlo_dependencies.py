# -*- coding: utf-8 -*-
"""Phase 149: Governance Monte Carlo Dependencies Module.

Tracks dependencies on Phase 144 model governance and audit trails.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DEPENDENCY_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

GOVERNANCE_DEPS: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_MODEL_GOVERNANCE_POLICIES",
        "source_phase": 144,
        "description": "Model governance risk tiering, non-production sign-off, and audit logging specifications.",
        "status": "SATISFIED",
    },
    {
        "dependency_id": "DEP_ML_ACCEPTANCE_CRITERIA",
        "source_phase": 145,
        "description": "Advanced ML model acceptance report gating requirements.",
        "status": "SATISFIED",
    },
]


def build_governance_monte_carlo_dependency_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the governance Monte Carlo dependency registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for d in GOVERNANCE_DEPS:
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
