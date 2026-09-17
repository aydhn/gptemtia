# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Overfitting Guards Module.

Guards against strategy overfitting using Deflated Sharpe Ratio (DSR) and
Probability of Backtest Overfitting (PBO) metadata formulas.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    BIAS_GUARD_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

OVERFITTING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_name": "deflated_sharpe_ratio_guard",
        "methodology": "Bailey and Lopez de Prado (2014) Deflated Sharpe Ratio",
        "formula": "DSR = F_Z( (SR - SR_0) / sqrt(V(SR)) )",
        "purpose": "Adjusts Sharpe ratio for non-normality and total number of strategy variations tested.",
        "status": "ACTIVE",
    },
    {
        "guard_name": "probability_of_backtest_overfitting_guard",
        "methodology": "Combinatorially Symmetric Cross-Validation (CSCV) / PBO",
        "formula": "PBO = sum_{c} I(lambda_c* <= 0) / N_combinations",
        "purpose": "Measures probability that the in-sample optimal strategy underperforms median OOS.",
        "status": "ACTIVE",
    },
]


def build_monte_carlo_overfitting_guard_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the overfitting guard registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for g in OVERFITTING_GUARDS:
        rows.append(
            {
                "guard_name": g["guard_name"],
                "methodology": g["methodology"],
                "formula": g["formula"],
                "purpose": g["purpose"],
                "status": g["status"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "domain": BIAS_GUARD_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": BIAS_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": bool((df["status"] == "ACTIVE").all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
