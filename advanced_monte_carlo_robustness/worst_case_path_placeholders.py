# -*- coding: utf-8 -*-
"""Phase 149: Worst Case Path Placeholders Module.

Defines placeholders and metadata for identifying the worst-case simulated path.
Zero path simulation or trajectory generation is executed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

WORST_CASE_SPECS: List[Dict[str, Any]] = [
    {
        "path_selector": "worst_terminal_equity_path",
        "selection_criterion": "argmin(Terminal_Equity_i)",
        "description": "Trajectory with the lowest ending wealth across all generated resampled simulations.",
    },
    {
        "path_selector": "worst_peak_to_trough_drawdown_path",
        "selection_criterion": "argmax(Max_Drawdown_i)",
        "description": "Trajectory experiencing the single deepest drawdown drop in the simulation set.",
    },
    {
        "path_selector": "longest_underwater_duration_path",
        "selection_criterion": "argmax(Max_Underwater_Days_i)",
        "description": "Trajectory remaining submerged longest without reaching a new equity high.",
    },
]


def build_worst_case_path_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the worst case path placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in WORST_CASE_SPECS:
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
        "total_worst_case_selectors": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
