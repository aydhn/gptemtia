# -*- coding: utf-8 -*-
"""Phase 149: Return Path Resampling Contracts Module.

Defines return series path resampling specifications, sampling replacement rules,
and lookahead prohibition constraints. Zero path generation permitted.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    RETURN_PATH_RESAMPLING_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

RESAMPLING_CONTRACTS: List[Dict[str, Any]] = [
    {
        "resampling_contract_name": "full_history_return_resampling",
        "sampling_unit": "daily_log_returns",
        "replacement": True,
        "sample_size_matches_history": True,
        "lookahead_forbidden": True,
        "description": "Contracts sampling entire historical return distribution with replacement to generate pseudo-paths.",
    },
    {
        "resampling_contract_name": "stratified_volatility_resampling",
        "sampling_unit": "volatility_bucketed_returns",
        "replacement": True,
        "sample_size_matches_history": True,
        "lookahead_forbidden": True,
        "description": "Stratified sampling ensuring representative draws across low, medium, and high volatility regimes.",
    },
    {
        "resampling_contract_name": "stress_weighted_return_resampling",
        "sampling_unit": "crisis_weighted_returns",
        "replacement": True,
        "sample_size_matches_history": True,
        "lookahead_forbidden": True,
        "description": "Contracts giving elevated sampling probability to historical drawdown periods.",
    },
]


def build_return_path_resampling_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the return path resampling contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for c in RESAMPLING_CONTRACTS:
        rows.append(
            {
                "resampling_contract_name": c["resampling_contract_name"],
                "sampling_unit": c["sampling_unit"],
                "replacement": c["replacement"],
                "sample_size_matches_history": c["sample_size_matches_history"],
                "lookahead_forbidden": c["lookahead_forbidden"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "resampling_executed": False,
                "paths_generated_count": 0,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": RETURN_PATH_RESAMPLING_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": RETURN_PATH_RESAMPLING_DOMAIN,
        "total_contracts": len(df),
        "all_unexecuted": bool((~df["resampling_executed"]).all() and (df["paths_generated_count"] == 0).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
