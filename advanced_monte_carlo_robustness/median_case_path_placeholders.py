# -*- coding: utf-8 -*-
"""Phase 149: Median Case Path Placeholders Module.

Defines placeholders and metadata for identifying the central tendency median simulated path.
Zero path simulation is executed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

MEDIAN_CASE_SPECS: List[Dict[str, Any]] = [
    {
        "path_selector": "median_terminal_equity_path",
        "selection_criterion": "argmin(|Terminal_Equity_i - median(Terminal_Equity)|)",
        "description": "Trajectory most closely tracking the 50th percentile terminal wealth level.",
    },
    {
        "path_selector": "median_drawdown_profile_path",
        "selection_criterion": "argmin(|Max_Drawdown_i - median(Max_Drawdown)|)",
        "description": "Trajectory exhibiting median maximum drawdown behavior across the simulation set.",
    },
]


def build_median_case_path_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the median case path placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in MEDIAN_CASE_SPECS:
        rows.append(
            {
                "path_selector": s["path_selector"],
                "selection_criterion": s["selection_criterion"],
                "description": s["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "path_data": None,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
        "total_median_case_selectors": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
