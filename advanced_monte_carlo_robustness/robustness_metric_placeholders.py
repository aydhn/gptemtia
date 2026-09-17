# -*- coding: utf-8 -*-
"""Phase 149: Robustness Metric Placeholders Module.

Defines mathematical specifications for envelope widths, spread bounds, and extreme loss metrics.
Zero empirical calculation executed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

ROBUSTNESS_METRICS: List[Dict[str, Any]] = [
    {
        "metric_name": "robustness_envelope_width_placeholder",
        "formula_definition": "Envelope_Width(t) = Upper_Envelope_q95(t) - Lower_Envelope_q05(t)",
        "interpretation": "Measures uncertainty growth of cumulative wealth over time.",
    },
    {
        "metric_name": "confidence_interval_width_placeholder",
        "formula_definition": "CI_Width = Upper_Percentile(0.975) - Lower_Percentile(0.025)",
        "interpretation": "Width of the empirical parameter confidence band.",
    },
    {
        "metric_name": "worst_case_loss_placeholder",
        "formula_definition": "Worst_Loss = min(Terminal_Equity_i - Initial_Equity)",
        "interpretation": "Maximum negative scenario outcome across simulations.",
    },
    {
        "metric_name": "best_case_gain_placeholder",
        "formula_definition": "Best_Gain = max(Terminal_Equity_i - Initial_Equity)",
        "interpretation": "Maximum positive scenario outcome across simulations (metadata only, no claim).",
    },
    {
        "metric_name": "median_case_return_placeholder",
        "formula_definition": "Median_Return = median(Terminal_Returns)",
        "interpretation": "Central 50th percentile simulated path expectation.",
    },
]


def build_robustness_metric_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the robustness metric placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for r in ROBUSTNESS_METRICS:
        rows.append(
            {
                "metric_name": r["metric_name"],
                "formula_definition": r["formula_definition"],
                "interpretation": r["interpretation"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "value": None,
                "performance_claim": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": DISTRIBUTION_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISTRIBUTION_PLACEHOLDER_DOMAIN,
        "total_robustness_metrics": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
