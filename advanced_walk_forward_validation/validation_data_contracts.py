# -*- coding: utf-8 -*-
"""Phase 147: Validation Data Contracts.

Specifications linking data lake datasets to walk-forward validation contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

DATA_CONTRACTS: List[Dict[str, Any]] = [
    {
        "data_contract_id": "DAT-147-01",
        "dataset_name": "commodities_daily_ohlcv_dataset",
        "timeframe": "1D",
        "immutability_enforced": True,
        "description": "Emtia gunluk OHLCV zaman serisi veri sozlesmesi.",
    },
    {
        "data_contract_id": "DAT-147-02",
        "dataset_name": "forex_daily_ohlcv_dataset",
        "timeframe": "1D",
        "immutability_enforced": True,
        "description": "Doviz pariteleri gunluk OHLCV zaman serisi veri sozlesmesi.",
    },
]


def build_validation_data_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for validation data contracts."""
    rows = []
    for d in DATA_CONTRACTS:
        rows.append(
            {
                "data_contract_id": d["data_contract_id"],
                "dataset_name": d["dataset_name"],
                "timeframe": d["timeframe"],
                "immutability_enforced": d["immutability_enforced"],
                "description": d["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_data_contracts": len(df),
        "all_immutable": True,
        "non_signal": True,
    }
    return df, summary
