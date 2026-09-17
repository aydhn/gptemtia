# -*- coding: utf-8 -*-
"""Phase 149: Path Perturbation Placeholders Module.

Defines specifications for price path warping, volatility rescaling, and drift modification.
Zero simulated paths are generated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    PATH_PERTURBATION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

PATH_PERTURBATIONS: List[Dict[str, Any]] = [
    {
        "perturbation_type": "drift_suppression_path_perturbation",
        "transformation": "r_perturbed = r_t - mean(r)",
        "economic_rationale": "Evaluates whether strategy alpha survives when underlying market beta drift is zeroed out.",
    },
    {
        "perturbation_type": "volatility_expansion_path_perturbation",
        "transformation": "r_perturbed = r_t * (1 + delta_vol)",
        "economic_rationale": "Evaluates margin call risk and maximum drawdown under uniformly scaled volatility regimes.",
    },
    {
        "perturbation_type": "gap_dilation_path_perturbation",
        "transformation": "gap_open = gap_open * 1.50",
        "economic_rationale": "Assesses stop-loss execution slippage under dilated weekend and overnight opening gaps.",
    },
]


def build_path_perturbation_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the path perturbation placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for p in PATH_PERTURBATIONS:
        rows.append(
            {
                "perturbation_type": p["perturbation_type"],
                "transformation": p["transformation"],
                "economic_rationale": p["economic_rationale"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "perturbation_executed": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": PATH_PERTURBATION_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": PATH_PERTURBATION_PLACEHOLDER_DOMAIN,
        "total_perturbations": len(df),
        "total_placeholders": len(df),
        "all_unexecuted": bool((~df["perturbation_executed"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
