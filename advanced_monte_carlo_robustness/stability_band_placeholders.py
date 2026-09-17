# -*- coding: utf-8 -*-
"""Phase 149: Stability Band Placeholders Module.

Defines placeholders for strategy stability tolerance bands and performance corridor limits.
Zero empirical corridors are calculated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    STABILITY_BAND_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

STABILITY_BANDS: List[Dict[str, Any]] = [
    {
        "band_name": "sharpe_ratio_stability_band",
        "lower_tolerance_limit": "0.75 * Baseline_Sharpe",
        "upper_tolerance_limit": "1.25 * Baseline_Sharpe",
        "metric_target": "Sharpe_Ratio",
        "description": "Corridor defining acceptable Sharpe variance under resampling and perturbation.",
    },
    {
        "band_name": "max_drawdown_ceiling_band",
        "lower_tolerance_limit": "0.00",
        "upper_tolerance_limit": "1.30 * Baseline_Max_Drawdown",
        "metric_target": "Max_Drawdown_Pct",
        "description": "Ceiling tolerance band preventing tail drawdowns from exceeding 130% of backtest baseline.",
    },
    {
        "band_name": "win_rate_corridor_band",
        "lower_tolerance_limit": "Baseline_WR - 0.08",
        "upper_tolerance_limit": "Baseline_WR + 0.08",
        "metric_target": "Win_Rate",
        "description": "Win-rate corridor tolerance ensuring strategy edge remains statistically stable.",
    },
]


def build_stability_band_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the stability band placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for b in STABILITY_BANDS:
        rows.append(
            {
                "band_name": b["band_name"],
                "lower_tolerance_limit": b["lower_tolerance_limit"],
                "upper_tolerance_limit": b["upper_tolerance_limit"],
                "metric_target": b["metric_target"],
                "description": b["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "value": None,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": STABILITY_BAND_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": STABILITY_BAND_PLACEHOLDER_DOMAIN,
        "total_stability_bands": len(df),
        "total_bands": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
