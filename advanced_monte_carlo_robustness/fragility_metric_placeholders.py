# -*- coding: utf-8 -*-
"""Phase 149: Fragility Metric Placeholders Module.

Defines mathematical specifications for Taleb-style fragility indicators and asymmetric convexity.
Zero fragility calculation is performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

FRAGILITY_METRIC_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "parameter_fragility_score_placeholder",
        "formula_definition": "Fragility = (Metric(theta - h) + Metric(theta + h) - 2 * Metric(theta)) / (h^2)",
        "interpretation": "Negative second derivative indicates concave downside vulnerability (fragility).",
    },
    {
        "metric_name": "tail_risk_acceleration_placeholder",
        "formula_definition": "Acceleration = d(CVaR) / d(Stress_Level)",
        "interpretation": "Non-linear acceleration of tail losses under increasing stress increments.",
    },
]


def build_fragility_metric_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the fragility metric placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for f in FRAGILITY_METRIC_SPECS:
        rows.append(
            {
                "metric_name": f["metric_name"],
                "formula_definition": f["formula_definition"],
                "interpretation": f["interpretation"],
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
        "total_fragility_metrics": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
