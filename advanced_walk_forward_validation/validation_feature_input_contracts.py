# -*- coding: utf-8 -*-
"""Phase 147: Validation Feature Input Contracts.

Specifications linking FeatureStore feature catalog to walk-forward validation contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

FEATURE_CONTRACTS: List[Dict[str, Any]] = [
    {
        "feature_contract_id": "FTR-147-01",
        "catalog_source": "Phase 124 FeatureStore Catalog",
        "feature_family": "MOMENTUM_TREND",
        "leakage_free": True,
        "description": "Zaman damgasi geriye donuk olarak kesinlestirilmis momentum ozellik girdi sozlesmesi.",
    },
    {
        "feature_contract_id": "FTR-147-02",
        "catalog_source": "Phase 124 FeatureStore Catalog",
        "feature_family": "VOLATILITY_RISK",
        "leakage_free": True,
        "description": "Gecmis pencere uzerinden hesaplanan oynaklik girdi sozlesmesi.",
    },
]


def build_validation_feature_input_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for validation feature input contracts."""
    rows = []
    for f in FEATURE_CONTRACTS:
        rows.append(
            {
                "feature_contract_id": f["feature_contract_id"],
                "catalog_source": f["catalog_source"],
                "feature_family": f["feature_family"],
                "leakage_free": f["leakage_free"],
                "description": f["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_feature_contracts": len(df),
        "all_leakage_free": True,
        "non_signal": True,
    }
    return df, summary
