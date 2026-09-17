# -*- coding: utf-8 -*-
"""Phase 149: Parameter Surface Placeholders Module.

Defines placeholders and mathematical definitions for parameter surface topology:
evaluating whether strategy performance rests on a wide plateau vs a razor-thin needle peak.
Zero surface calculation or plotting executed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    PARAMETER_SURFACE_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

SURFACE_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "surface_feature": "plateau_width_ratio",
        "definition": "Volume of parameter space retaining at least 80% of peak performance.",
        "geometric_interpretation": "Wide plateau indicates robustness to regime shifts and estimation noise.",
        "formula": "Plateau_Ratio = Volume(Metric >= 0.80 * Max_Metric) / Total_Grid_Volume",
    },
    {
        "surface_feature": "surface_gradient_steepness",
        "definition": "Hessian matrix eigenvalue magnitudes evaluating surface curvature.",
        "geometric_interpretation": "High curvature indicates extreme fragility and overfitting risk.",
        "formula": "Curvature = max_eigenvalue(Hessian(Metric))",
    },
    {
        "surface_feature": "asymmetric_cliff_edge_risk",
        "definition": "Maximum directional drop rate in performance when deviating from baseline.",
        "geometric_interpretation": "Identifies asymmetric disaster points where small shifts produce catastrophic losses.",
        "formula": "Cliff_Edge = max_{direction} |d Metric / d theta|",
    },
]


def build_parameter_surface_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter surface placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in SURFACE_PLACEHOLDERS:
        rows.append(
            {
                "surface_feature": s["surface_feature"],
                "definition": s["definition"],
                "geometric_interpretation": s["geometric_interpretation"],
                "formula": s["formula"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "value": None,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": PARAMETER_SURFACE_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": PARAMETER_SURFACE_PLACEHOLDER_DOMAIN,
        "total_surface_placeholders": len(df),
        "total_placeholders": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "all_unexecuted": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
