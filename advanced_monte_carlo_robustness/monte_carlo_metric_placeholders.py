# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Metric Placeholders Module.

Defines mathematical formulas and placeholder metadata for Monte Carlo performance metrics.
Zero real calculation or return distribution computation is performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISTRIBUTION_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

CORE_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "monte_carlo_return_distribution_placeholder",
        "metric_category": "return_distribution",
        "target_distribution": "terminal_wealth_pct",
        "formula_definition": "R_terminal,i = prod(1 + r_t,i) - 1 across simulations i=1..N",
    },
    {
        "metric_name": "monte_carlo_drawdown_distribution_placeholder",
        "metric_category": "drawdown_distribution",
        "target_distribution": "maximum_peak_to_trough_loss",
        "formula_definition": "MDD_i = max_{t} (Peak_t,i - Equity_t,i) / Peak_t,i",
    },
    {
        "metric_name": "monte_carlo_sharpe_distribution_placeholder",
        "metric_category": "risk_adjusted_performance",
        "target_distribution": "annualized_sharpe_ratio",
        "formula_definition": "Sharpe_i = sqrt(252) * mean(r_t,i) / std(r_t,i)",
    },
    {
        "metric_name": "monte_carlo_win_rate_distribution_placeholder",
        "metric_category": "trade_profitability",
        "target_distribution": "win_loss_percentage",
        "formula_definition": "WR_i = count(trades_i > 0) / count(trades_i)",
    },
    {
        "metric_name": "monte_carlo_var_placeholder",
        "metric_category": "tail_risk",
        "target_distribution": "value_at_risk_quantile",
        "formula_definition": "VaR_alpha = - quantile_alpha(Cumulative_Returns)",
    },
    {
        "metric_name": "monte_carlo_expected_shortfall_placeholder",
        "metric_category": "tail_risk",
        "target_distribution": "conditional_tail_expectation",
        "formula_definition": "ES_alpha = - E[R | R <= - VaR_alpha]",
    },
]


def build_monte_carlo_metric_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo metric placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for m in CORE_METRIC_PLACEHOLDERS:
        rows.append(
            {
                "metric_name": m["metric_name"],
                "metric_category": m["metric_category"],
                "target_distribution": m["target_distribution"],
                "formula_definition": m["formula_definition"],
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
        "total_metric_placeholders": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
