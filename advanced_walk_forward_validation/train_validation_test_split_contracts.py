# -*- coding: utf-8 -*-
"""Phase 147: Train / Validation / Test Split Contracts.

Specifications for partitioning time-series data without generating targets, predictions, or lookahead.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

SPLIT_SPECS: List[Dict[str, Any]] = [
    {
        "split_name": "standard_60_20_20_split",
        "train_ratio": 0.60,
        "val_ratio": 0.20,
        "test_ratio": 0.20,
        "embargo_bars": 10,
        "purge_bars": 5,
        "description": "Standart %60 egitim, %20 ic dogrulama, %20 OOS test orani ve purge/embargo korumali sozlesme.",
    },
    {
        "split_name": "conservative_70_15_15_split",
        "train_ratio": 0.70,
        "val_ratio": 0.15,
        "test_ratio": 0.15,
        "embargo_bars": 15,
        "purge_bars": 10,
        "description": "Daha uzun egitim gecmisi gerektiren modeller icin %70-%15-%15 bolum sozlesmesi.",
    },
    {
        "split_name": "strict_holdout_50_25_25_split",
        "train_ratio": 0.50,
        "val_ratio": 0.25,
        "test_ratio": 0.25,
        "embargo_bars": 21,
        "purge_bars": 10,
        "description": "Genis OOS test donemi sunan %50-%25-%25 bolumleme sozlesmesi.",
    },
]


def build_train_validation_test_split_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for train/validation/test split contracts."""
    rows = []
    for s in SPLIT_SPECS:
        rows.append(
            {
                "split_name": s["split_name"],
                "train_ratio": s["train_ratio"],
                "val_ratio": s["val_ratio"],
                "test_ratio": s["test_ratio"],
                "embargo_bars": s["embargo_bars"],
                "purge_bars": s["purge_bars"],
                "description": s["description"],
                "split_executed": False,
                "targets_generated": False,
                "predictions_generated": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_split_contracts": len(df),
        "all_splits_unexecuted": True,
        "zero_targets_generated": True,
        "zero_predictions_generated": True,
        "non_signal": True,
    }
    return df, summary
