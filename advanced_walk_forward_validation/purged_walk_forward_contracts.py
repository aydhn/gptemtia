# -*- coding: utf-8 -*-
"""Phase 147: Purged Walk-Forward Contracts.

Specifications for purged walk-forward validation splits to prevent label overlap and leakage.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

PURGED_CONTRACTS: List[Dict[str, Any]] = [
    {
        "split_name": "standard_purged_walk_forward_contract",
        "purge_mechanism": "LABEL_OVERLAP_PURGE",
        "purge_window_bars": 5,
        "embargo_window_bars": 10,
        "description": "Egitim ve test araligi arasindaki etiket cakismasini onlemek icin 5 bar temizleme (purge) ve 10 bar embargo uygulayan sozlesme.",
    },
    {
        "split_name": "extended_purged_walk_forward_contract",
        "purge_mechanism": "SERIAL_CORRELATION_PURGE",
        "purge_window_bars": 15,
        "embargo_window_bars": 21,
        "description": "Otoregresif kalinti ve yuksek gecikmeli etiketler icin 15 bar purge ve 21 bar embargo sozlesmesi.",
    },
]


def build_purged_walk_forward_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for purged walk-forward contracts."""
    rows = []
    for c in PURGED_CONTRACTS:
        rows.append(
            {
                "split_name": c["split_name"],
                "purge_mechanism": c["purge_mechanism"],
                "purge_window_bars": c["purge_window_bars"],
                "embargo_window_bars": c["embargo_window_bars"],
                "description": c["description"],
                "execution_allowed": False,
                "purge_executed": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_purged_contracts": len(df),
        "all_execution_blocked": True,
        "all_purge_unexecuted": True,
        "non_signal": True,
    }
    return df, summary
