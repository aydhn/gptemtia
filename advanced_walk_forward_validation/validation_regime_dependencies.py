# -*- coding: utf-8 -*-
"""Phase 147: Validation Regime Dependencies.

Specifies dependencies connecting Phase 147 to Phase 126-135 Regime Acceptance and Integration layers.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

REGIME_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP-RGM-01",
        "module": "advanced_regime_acceptance",
        "source_phase": 135,
        "status": "BOUND",
        "description": "Rejim kabul ve gecis matrisi sozlesmeleri baglantisi.",
    },
    {
        "dependency_id": "DEP-RGM-02",
        "module": "advanced_regime_featurestore_integration",
        "source_phase": 134,
        "status": "BOUND",
        "description": "Rejim ozelliklerinin FeatureStore uzerinden dogrulama katmanina erisimi.",
    },
]


def build_validation_regime_dependency_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime dependencies."""
    rows = []
    for d in REGIME_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "module": d["module"],
                "source_phase": d["source_phase"],
                "status": d["status"],
                "description": d["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_regime_dependencies": len(df),
        "all_bound": True,
        "non_signal": True,
    }
    return df, summary
