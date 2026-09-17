# -*- coding: utf-8 -*-
"""Phase 149: Tail Risk Distribution Placeholders Module.

Defines placeholders and formula definitions for tail-risk metrics: Value at Risk (VaR),
Expected Shortfall (CVaR), and tail decay. Zero VaR/ES calculated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

TAIL_RISK_ITEMS: List[Dict[str, Any]] = [
    {
        "metric_name": "historical_resampled_var_95",
        "confidence_level": 0.95,
        "formula": "VaR_alpha = - quantile_alpha(Returns)",
        "description": "95% Value at Risk under Monte Carlo return path resampling.",
    },
    {
        "metric_name": "historical_resampled_var_99",
        "confidence_level": 0.99,
        "formula": "VaR_alpha = - quantile_alpha(Returns)",
        "description": "99% Value at Risk evaluating severe adverse loss thresholds.",
    },
    {
        "metric_name": "expected_shortfall_cvar_95",
        "confidence_level": 0.95,
        "formula": "CVaR_alpha = - E[R | R <= - VaR_alpha]",
        "description": "Conditional expectation of loss given that the 95% VaR threshold is breached.",
    },
    {
        "metric_name": "expected_shortfall_cvar_99",
        "confidence_level": 0.99,
        "formula": "CVaR_alpha = - E[R | R <= - VaR_alpha]",
        "description": "Conditional expectation of loss given that the 99% VaR threshold is breached.",
    },
]


def build_tail_risk_distribution_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the tail risk distribution placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for t in TAIL_RISK_ITEMS:
        rows.append(
            {
                "metric_name": t["metric_name"],
                "confidence_level": t["confidence_level"],
                "formula": t["formula"],
                "description": t["description"],
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
        "total_tail_risk_items": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
