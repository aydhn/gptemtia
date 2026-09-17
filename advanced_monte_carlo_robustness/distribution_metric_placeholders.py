# -*- coding: utf-8 -*-
"""Phase 149: Distribution Metric Placeholders Module.

Consolidates all statistical distribution moments and quantile definitions.
Zero distribution sampling or empirical statistics computed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

DISTRIBUTION_METRICS: List[Dict[str, Any]] = [
    {
        "distribution_metric": "empirical_quantile_q05",
        "statistic_type": "adverse_tail_quantile",
        "formula": "Q_0.05 = F^(-1)(0.05)",
        "description": "5th percentile adverse outcome.",
    },
    {
        "distribution_metric": "empirical_quantile_q50",
        "statistic_type": "median_quantile",
        "formula": "Q_0.50 = F^(-1)(0.50)",
        "description": "50th percentile median outcome.",
    },
    {
        "distribution_metric": "empirical_quantile_q95",
        "statistic_type": "favorable_quantile",
        "formula": "Q_0.95 = F^(-1)(0.95)",
        "description": "95th percentile favorable outcome.",
    },
    {
        "distribution_metric": "interquartile_range_iqr",
        "statistic_type": "dispersion_measure",
        "formula": "IQR = Q_0.75 - Q_0.25",
        "description": "Interquartile range measuring central performance spread.",
    },
]


def build_distribution_metric_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the distribution metric placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for d in DISTRIBUTION_METRICS:
        rows.append(
            {
                "distribution_metric": d["distribution_metric"],
                "statistic_type": d["statistic_type"],
                "formula": d["formula"],
                "description": d["description"],
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
        "total_distribution_metrics": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
