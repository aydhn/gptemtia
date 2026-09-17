# -*- coding: utf-8 -*-
"""Phase 149: Robustness Envelope Placeholders Module.

Defines placeholders for upper, lower, and median robustness envelope curves.
Zero empirical curves are computed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

ENVELOPE_BOUNDS: List[Dict[str, Any]] = [
    {
        "envelope_bound": "upper_quantile_envelope_q95",
        "quantile_level": 0.95,
        "description": "95th percentile cumulative equity envelope across resampled scenarios.",
    },
    {
        "envelope_bound": "median_expectation_envelope_q50",
        "quantile_level": 0.50,
        "description": "50th percentile (median) equity path representing central tendency.",
    },
    {
        "envelope_bound": "lower_quantile_envelope_q05",
        "quantile_level": 0.05,
        "description": "5th percentile adverse equity envelope representing conservative downside.",
    },
    {
        "envelope_bound": "extreme_tail_envelope_q01",
        "quantile_level": 0.01,
        "description": "1st percentile stress envelope assessing extreme path deterioration.",
    },
]


def build_robustness_envelope_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the robustness envelope placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for b in ENVELOPE_BOUNDS:
        rows.append(
            {
                "envelope_bound": b["envelope_bound"],
                "quantile_level": b["quantile_level"],
                "description": b["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "value": None,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
        "total_envelope_bounds": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
