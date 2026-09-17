# -*- coding: utf-8 -*-
"""Phase 147: Validation Transaction Cost Dependencies.

Specifies dependencies connecting Phase 147 to Phase 146 Transaction Cost contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

COST_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP-CST-01",
        "cost_model": "commission_fee_spread_model",
        "source_phase": 146,
        "status": "BOUND",
        "description": "Komisyon, borsa ucreti ve alis-satis farki sozlesmeleri entegrasyonu.",
    },
    {
        "dependency_id": "DEP-CST-02",
        "cost_model": "tier_based_institutional_cost_model",
        "source_phase": 146,
        "status": "BOUND",
        "description": "Kademeli kurumsal islem maliyeti sozlesmesi baglantisi.",
    },
]


def build_validation_transaction_cost_dependency_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for transaction cost dependencies."""
    rows = []
    for d in COST_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "cost_model": d["cost_model"],
                "source_phase": d["source_phase"],
                "status": d["status"],
                "description": d["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_cost_dependencies": len(df),
        "all_bound": True,
        "non_signal": True,
    }
    return df, summary
