# -*- coding: utf-8 -*-
"""Phase 149: Walk Forward Monte Carlo Linkage Module.

Links Phase 147 Walk-Forward Validation OOS splits with Monte Carlo resampling contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    LINKAGE_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

WF_LINKAGES: List[Dict[str, Any]] = [
    {
        "linkage_id": "LINK_WF_OOS_SPLITS",
        "phase_147_ref": "walk_forward_split_contracts",
        "integration_purpose": "Resample within discrete out-of-sample test windows without in-sample contamination.",
        "status": "SATISFIED",
    },
    {
        "linkage_id": "LINK_WF_BENCHMARK_STABILITY",
        "phase_147_ref": "walk_forward_benchmark_contracts",
        "integration_purpose": "Benchmark distribution comparison across anchor asset benchmarks.",
        "status": "SATISFIED",
    },
]


def build_walk_forward_monte_carlo_linkage_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the walk forward Monte Carlo linkage registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for w in WF_LINKAGES:
        rows.append(
            {
                "linkage_id": w["linkage_id"],
                "phase_147_ref": w["phase_147_ref"],
                "integration_purpose": w["integration_purpose"],
                "status": w["status"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": LINKAGE_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": LINKAGE_DOMAIN,
        "total_wf_linkages": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
