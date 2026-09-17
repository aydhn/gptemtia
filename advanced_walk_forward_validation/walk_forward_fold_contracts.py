# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Fold Contracts.

Specifications defining the structure of discrete walk-forward folds without running fold execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

FOLD_SPECS: List[Dict[str, Any]] = [
    {
        "fold_contract_name": "5_fold_rolling_walk_forward",
        "num_folds": 5,
        "fold_type": "ROLLING",
        "train_size_bars": 252,
        "test_size_bars": 50,
        "embargo_bars": 10,
        "description": "5 katmanli kayan pencere dogrulama katmani sozlesmesi.",
    },
    {
        "fold_contract_name": "10_fold_expanding_walk_forward",
        "num_folds": 10,
        "fold_type": "EXPANDING",
        "train_size_bars": 126,
        "test_size_bars": 25,
        "embargo_bars": 5,
        "description": "10 katmanli genisleyen pencere dogrulama katmani sozlesmesi.",
    },
]


def build_walk_forward_fold_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for walk-forward fold contracts."""
    rows = []
    for f in FOLD_SPECS:
        rows.append(
            {
                "fold_contract_name": f["fold_contract_name"],
                "num_folds": f["num_folds"],
                "fold_type": f["fold_type"],
                "train_size_bars": f["train_size_bars"],
                "test_size_bars": f["test_size_bars"],
                "embargo_bars": f["embargo_bars"],
                "description": f["description"],
                "folds_executed": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_fold_contracts": len(df),
        "all_folds_unexecuted": True,
        "non_signal": True,
    }
    return df, summary
