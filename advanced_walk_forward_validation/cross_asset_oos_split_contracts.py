# -*- coding: utf-8 -*-
"""Phase 147: Cross-Asset Out-of-Sample Split Contracts.

Specifications for evaluating generalization across different commodity and forex assets.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

CROSS_ASSET_SPECS: List[Dict[str, Any]] = [
    {
        "split_name": "precious_to_industrial_metals_transfer",
        "source_asset_cluster": "PRECIOUS_METALS",
        "target_oos_cluster": "INDUSTRIAL_METALS",
        "description": "Degerli metallerde test edilmis kurallarin sanayi metalleri OOS uzerinde genellenebilirlik sozlesmesi.",
    },
    {
        "split_name": "energy_to_commodities_transfer",
        "source_asset_cluster": "ENERGY",
        "target_oos_cluster": "AGRICULTURE",
        "description": "Enerji emtialarindan tarimsal emtialara model genellenebilirlik sozlesmesi.",
    },
    {
        "split_name": "g10_forex_to_em_forex_transfer",
        "source_asset_cluster": "G10_FOREX",
        "target_oos_cluster": "EM_FOREX",
        "description": "G10 doviz paritelerinden gelismekte olan ulke paritelerine OOS aktarim sozlesmesi.",
    },
]


def build_cross_asset_oos_split_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for cross-asset OOS split contract registry."""
    rows = []
    for c in CROSS_ASSET_SPECS:
        rows.append(
            {
                "split_name": c["split_name"],
                "source_asset_cluster": c["source_asset_cluster"],
                "target_oos_cluster": c["target_oos_cluster"],
                "description": c["description"],
                "transfer_executed": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_cross_asset_splits": len(df),
        "all_transfers_unexecuted": True,
        "non_signal": True,
    }
    return df, summary
