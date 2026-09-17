# -*- coding: utf-8 -*-
"""Phase 147: Rolling Window Validation Contracts.

Specifications for fixed-size rolling window validation splits.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

ROLLING_CONTRACTS: List[Dict[str, Any]] = [
    {
        "split_name": "standard_rolling_window_3m",
        "window_type": "ROLLING",
        "train_period_bars": 252,
        "val_period_bars": 63,
        "test_period_bars": 63,
        "step_size_bars": 21,
        "anchored": False,
        "description": "252 gun egitim, 63 gun OOS test ve 21 gunluk adimla kayan pencere.",
    },
    {
        "split_name": "short_horizon_rolling_window_1m",
        "window_type": "ROLLING",
        "train_period_bars": 126,
        "val_period_bars": 21,
        "test_period_bars": 21,
        "step_size_bars": 10,
        "anchored": False,
        "description": "Kisa vadeli piyasa degisimlerine duyarli 126 gun egitim, 21 gun OOS kayan pencere.",
    },
    {
        "split_name": "long_horizon_rolling_window_6m",
        "window_type": "ROLLING",
        "train_period_bars": 504,
        "val_period_bars": 126,
        "test_period_bars": 126,
        "step_size_bars": 63,
        "anchored": False,
        "description": "2 yillik (504 bar) genis egitim ve 126 gunluk OOS adimla kayan makro pencere.",
    },
]


def build_rolling_window_validation_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for rolling window validation contracts."""
    rows = []
    for c in ROLLING_CONTRACTS:
        rows.append(
            {
                "split_name": c["split_name"],
                "window_type": c["window_type"],
                "train_period_bars": c["train_period_bars"],
                "val_period_bars": c["val_period_bars"],
                "test_period_bars": c["test_period_bars"],
                "step_size_bars": c["step_size_bars"],
                "anchored": c["anchored"],
                "description": c["description"],
                "execution_allowed": False,
                "data_split_executed": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_rolling_contracts": len(df),
        "all_execution_blocked": True,
        "all_data_split_unexecuted": True,
        "non_signal": True,
    }
    return df, summary
