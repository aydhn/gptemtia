# -*- coding: utf-8 -*-
"""Phase 149: Best Case Path Placeholders Module.

Defines placeholders and metadata for identifying best-case simulated paths.
Zero performance claims or upward profit projections are generated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

BEST_CASE_SPECS: List[Dict[str, Any]] = [
    {
        "path_selector": "best_terminal_equity_path",
        "selection_criterion": "argmax(Terminal_Equity_i)",
        "description": "Trajectory with the highest ending wealth across all resampled paths.",
    },
    {
        "path_selector": "highest_sharpe_path",
        "selection_criterion": "argmax(Realized_Sharpe_i)",
        "description": "Trajectory exhibiting maximum risk-adjusted return under favorable ordering.",
    },
]


def build_best_case_path_placeholder_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the best case path placeholder registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for s in BEST_CASE_SPECS:
        rows.append(
            {
                "path_selector": s["path_selector"],
                "selection_criterion": s["selection_criterion"],
                "description": s["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "calculated": False,
                "path_data": None,
                "performance_claim": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": ROBUSTNESS_ENVELOPE_PLACEHOLDER_DOMAIN,
        "total_best_case_selectors": len(df),
        "all_uncalculated": bool((~df["calculated"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
