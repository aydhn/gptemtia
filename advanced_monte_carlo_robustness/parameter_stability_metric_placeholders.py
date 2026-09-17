# -*- coding: utf-8 -*-
"""Phase 149: Parameter Stability Metric Placeholders Module.

Defines formulas and metadata for parameter stability and sensitivity scores.
Zero parameter scoring or optimization calculations are performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

STABILITY_METRICS: List[Dict[str, Any]] = [
    {
        "metric_name": "parameter_stability_score_placeholder",
        "formula_definition": "PSS = 1.0 - (std(Sharpe_neighborhood) / mean(Sharpe_neighborhood))",
        "target_range": "[0.0, 1.0], higher indicates broader plateau",
        "description": "Normalized stability index measuring parameter performance smoothness.",
    },
    {
        "metric_name": "parameter_sensitivity_score_placeholder",
        "formula_definition": "Sensitivity = mean_{k} |d Metric / d theta_k| * (theta_k / Metric)",
        "target_range": ">= 0.0, lower indicates lower parameter sensitivity",
        "description": "Aggregate elasticity across parameter axes around baseline configuration.",
    },
]


def build_parameter_stability_metric_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter stability metric placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in STABILITY_METRICS:
        rows.append(
            {
                "metric_name": s["metric_name"],
                "formula_definition": s["formula_definition"],
                "target_range": s["target_range"],
                "description": s["description"],
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
        "total_stability_metrics": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
