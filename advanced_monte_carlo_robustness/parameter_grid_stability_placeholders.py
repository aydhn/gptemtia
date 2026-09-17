# -*- coding: utf-8 -*-
"""Phase 149: Parameter Grid Stability Placeholders Module.

Defines placeholders and formula metadata for grid neighborhood stability scores.
Zero grid searches or parameter evaluations are executed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    PARAMETER_GRID_STABILITY_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

GRID_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_id": "neighborhood_stability_score_placeholder",
        "stability_metric_definition": "Ratio of neighbor mean performance to central baseline performance.",
        "formula": "Stability_Score = mean(Metric_neighbors) / Metric_center",
        "threshold_target": ">= 0.85 (less than 15% decay across immediate neighbors)",
        "description": "Grid score measuring performance degradation across adjacent parameter coordinates.",
    },
    {
        "placeholder_id": "grid_variance_coefficient_placeholder",
        "stability_metric_definition": "Normalized standard deviation of performance across the localized grid.",
        "formula": "CV = std(Metric_grid) / mean(Metric_grid)",
        "threshold_target": "<= 0.20 (low variance indicates robust plateau)",
        "description": "Coefficient of variation evaluating local parameter flatness.",
    },
]


def build_parameter_grid_stability_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter grid stability placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for g in GRID_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_id": g["placeholder_id"],
                "stability_metric_definition": g["stability_metric_definition"],
                "formula": g["formula"],
                "threshold_target": g["threshold_target"],
                "description": g["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "value": None,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": PARAMETER_GRID_STABILITY_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": PARAMETER_GRID_STABILITY_PLACEHOLDER_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "all_unexecuted": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
