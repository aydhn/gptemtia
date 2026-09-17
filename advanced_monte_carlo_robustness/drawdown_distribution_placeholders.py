# -*- coding: utf-8 -*-
"""Phase 149: Drawdown Distribution Placeholders Module.

Defines placeholders and mathematical moments for resampled maximum drawdown distributions.
Zero empirical drawdowns are calculated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

DRAWDOWN_MOMENTS: List[Dict[str, Any]] = [
    {
        "moment_name": "mean_resampled_drawdown",
        "description": "Expected value of maximum drawdown across all resampled paths.",
    },
    {
        "moment_name": "median_resampled_drawdown",
        "description": "50th percentile drawdown across resampled paths.",
    },
    {
        "moment_name": "drawdown_quantile_q95",
        "description": "95th percentile worst drawdown under Monte Carlo resampling.",
    },
    {
        "moment_name": "drawdown_quantile_q99",
        "description": "99th percentile catastrophic drawdown bound under Monte Carlo resampling.",
    },
    {
        "moment_name": "drawdown_duration_distribution",
        "description": "Distribution of underwater duration (days from peak to recovery).",
    },
]


def build_drawdown_distribution_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the drawdown distribution placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for m in DRAWDOWN_MOMENTS:
        rows.append(
            {
                "moment_name": m["moment_name"],
                "description": m["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "value": None,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": DISTRIBUTION_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISTRIBUTION_PLACEHOLDER_DOMAIN,
        "total_drawdown_moments": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
