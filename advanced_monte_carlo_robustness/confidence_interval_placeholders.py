# -*- coding: utf-8 -*-
"""Phase 149: Confidence Interval Placeholders Module.

Defines placeholders and mathematical definitions for bootstrap confidence intervals
(Percentile, BCa, Studentized) across performance distributions. Zero CI computed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    CONFIDENCE_INTERVAL_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

CI_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "ci_method": "percentile_bootstrap_ci",
        "confidence_level": 0.95,
        "lower_percentile": 2.5,
        "upper_percentile": 97.5,
        "description": "Standard empirical percentile confidence interval bounds.",
    },
    {
        "ci_method": "bca_bias_corrected_accelerated_ci",
        "confidence_level": 0.95,
        "lower_percentile": 2.5,
        "upper_percentile": 97.5,
        "description": "Efron BCa interval adjusting for skewness and median bias in return distributions.",
    },
    {
        "ci_method": "conservative_tail_ci",
        "confidence_level": 0.99,
        "lower_percentile": 0.5,
        "upper_percentile": 99.5,
        "description": "99% coverage interval for tail-risk and catastrophic drawdown bounds.",
    },
]


def build_confidence_interval_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the confidence interval placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for c in CI_PLACEHOLDERS:
        rows.append(
            {
                "ci_method": c["ci_method"],
                "confidence_level": profile.confidence_interval_level or c["confidence_level"],
                "lower_percentile": c["lower_percentile"],
                "upper_percentile": c["upper_percentile"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "lower_bound_value": None,
                "upper_bound_value": None,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": CONFIDENCE_INTERVAL_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": CONFIDENCE_INTERVAL_PLACEHOLDER_DOMAIN,
        "total_ci_placeholders": len(df),
        "total_intervals": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
