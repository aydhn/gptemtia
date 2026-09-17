# -*- coding: utf-8 -*-
"""Phase 147: Expanding Window Validation Contracts.

Specifications for expanding window validation splits accumulating historical data.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

EXPANDING_CONTRACTS: List[Dict[str, Any]] = [
    {
        "split_name": "standard_expanding_window",
        "window_type": "EXPANDING",
        "min_train_bars": 252,
        "expansion_step_bars": 21,
        "val_period_bars": 63,
        "test_period_bars": 63,
        "max_train_bars": 1260,
        "description": "Minimum 252 bar baslangic ile her adimda 21 bar genisleyen pencere dogrulama sozlesmesi.",
    },
    {
        "split_name": "macro_expanding_window",
        "window_type": "EXPANDING",
        "min_train_bars": 504,
        "expansion_step_bars": 63,
        "val_period_bars": 126,
        "test_period_bars": 126,
        "max_train_bars": 2520,
        "description": "Makro rejimleri kapsayan minimum 504 bar ve ceyreklik adimlarla genisleyen pencere.",
    },
]


def build_expanding_window_validation_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for expanding window validation contracts."""
    rows = []
    for c in EXPANDING_CONTRACTS:
        rows.append(
            {
                "split_name": c["split_name"],
                "window_type": c["window_type"],
                "min_train_bars": c["min_train_bars"],
                "expansion_step_bars": c["expansion_step_bars"],
                "val_period_bars": c["val_period_bars"],
                "test_period_bars": c["test_period_bars"],
                "max_train_bars": c["max_train_bars"],
                "description": c["description"],
                "execution_allowed": False,
                "data_split_executed": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_expanding_contracts": len(df),
        "all_execution_blocked": True,
        "all_data_split_unexecuted": True,
        "non_signal": True,
    }
    return df, summary
