# -*- coding: utf-8 -*-
"""Phase 147: Anchored Window Validation Contracts.

Specifications for anchored window validation splits with a fixed origin t0.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

ANCHORED_CONTRACTS: List[Dict[str, Any]] = [
    {
        "split_name": "fixed_anchor_start_contract",
        "window_type": "ANCHORED",
        "anchor_date_placeholder": "HISTORICAL_START_T0",
        "initial_train_bars": 252,
        "test_step_bars": 42,
        "test_period_bars": 42,
        "description": "Baslangic noktasi sabit (anchored) tutulan ve zamanla egitim havuzunu genisleterek ilerleyen sozlesme.",
    },
    {
        "split_name": "structural_break_anchor_contract",
        "window_type": "ANCHORED",
        "anchor_date_placeholder": "POST_REGIME_BREAK_T0",
        "initial_train_bars": 126,
        "test_step_bars": 21,
        "test_period_bars": 21,
        "description": "Yapisal kirilma sonrasi belirlenen sabit t0 noktasina bagli capalanmis pencere sozlesmesi.",
    },
]


def build_anchored_window_validation_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for anchored window validation contracts."""
    rows = []
    for c in ANCHORED_CONTRACTS:
        rows.append(
            {
                "split_name": c["split_name"],
                "window_type": c["window_type"],
                "anchor_date_placeholder": c["anchor_date_placeholder"],
                "initial_train_bars": c["initial_train_bars"],
                "test_step_bars": c["test_step_bars"],
                "test_period_bars": c["test_period_bars"],
                "description": c["description"],
                "execution_allowed": False,
                "data_split_executed": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_anchored_contracts": len(df),
        "all_execution_blocked": True,
        "all_data_split_unexecuted": True,
        "non_signal": True,
    }
    return df, summary
