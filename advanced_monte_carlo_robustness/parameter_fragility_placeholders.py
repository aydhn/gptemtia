# -*- coding: utf-8 -*-
"""Phase 149: Parameter Fragility Placeholders Module.

Defines parameter fragility indicators, cliff-edge flags, and over-optimization warning criteria.
Zero fragility calculation or trade recommendations generated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    PARAMETER_FRAGILITY_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

FRAGILITY_FLAGS: List[Dict[str, Any]] = [
    {
        "fragility_flag_id": "FLAG_PARAM_ISOLATED_PEAK",
        "description": "Triggered if baseline parameter performance exceeds neighbor mean by more than 50%.",
        "severity": "HIGH",
        "detection_rule": "(Baseline_Metric - Neighbor_Mean) / Neighbor_Mean > 0.50",
    },
    {
        "fragility_flag_id": "FLAG_PARAM_SIGN_REVERSAL",
        "description": "Triggered if perturbing parameters by 10% flips cumulative strategy return from positive to negative.",
        "severity": "CRITICAL",
        "detection_rule": "PnL(theta_baseline) > 0 and PnL(theta_perturbed) < 0",
    },
    {
        "fragility_flag_id": "FLAG_PARAM_DRAWDOWN_SPIKE",
        "description": "Triggered if local parameter deviation produces max drawdown exceeding 2x the baseline drawdown.",
        "severity": "CRITICAL",
        "detection_rule": "MaxDD(theta_perturbed) > 2.0 * MaxDD(theta_baseline)",
    },
    {
        "fragility_flag_id": "FLAG_PARAM_TRADE_COLLAPSE",
        "description": "Triggered if small parameter shift reduces trade frequency by more than 75%.",
        "severity": "MEDIUM",
        "detection_rule": "TradeCount(theta_perturbed) < 0.25 * TradeCount(theta_baseline)",
    },
]


def build_parameter_fragility_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter fragility placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for f in FRAGILITY_FLAGS:
        rows.append(
            {
                "fragility_flag_id": f["fragility_flag_id"],
                "description": f["description"],
                "severity": f["severity"],
                "detection_rule": f["detection_rule"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "flag_triggered": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": PARAMETER_FRAGILITY_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": PARAMETER_FRAGILITY_PLACEHOLDER_DOMAIN,
        "total_fragility_flags": len(df),
        "total_placeholders": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "all_unexecuted": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
