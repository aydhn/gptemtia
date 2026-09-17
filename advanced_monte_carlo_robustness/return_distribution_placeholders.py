# -*- coding: utf-8 -*-
"""Phase 149: Return Distribution Placeholders Module.

Defines placeholders and statistical moments for resampled cumulative return distributions.
Zero returns or empirical distributions are computed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

RETURN_MOMENTS: List[Dict[str, Any]] = [
    {
        "distribution_item": "resampled_mean_annualized_return",
        "moment_order": 1,
        "description": "Expected annualized return across simulated trajectories.",
    },
    {
        "distribution_item": "resampled_return_standard_deviation",
        "moment_order": 2,
        "description": "Cross-sectional standard deviation of simulated equity curves.",
    },
    {
        "distribution_item": "resampled_return_skewness",
        "moment_order": 3,
        "description": "Distribution asymmetry measuring right-tail upside vs left-tail loss.",
    },
    {
        "distribution_item": "resampled_return_kurtosis",
        "moment_order": 4,
        "description": "Tail heaviness assessing excess risk of extreme moves.",
    },
    {
        "distribution_item": "probability_of_loss_q0",
        "moment_order": 0,
        "description": "Fraction of resampled paths with negative cumulative return at terminal horizon.",
    },
]


def build_return_distribution_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the return distribution placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for m in RETURN_MOMENTS:
        rows.append(
            {
                "distribution_item": m["distribution_item"],
                "moment_order": m["moment_order"],
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
        "total_return_moments": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
