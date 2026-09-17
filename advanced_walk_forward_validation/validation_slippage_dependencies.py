# -*- coding: utf-8 -*-
"""Phase 147: Validation Slippage Dependencies.

Specifies dependencies connecting Phase 147 to Phase 146 Slippage Model contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

SLIPPAGE_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP-SLP-01",
        "slippage_model": "volatility_adaptive_slippage_model",
        "source_phase": 146,
        "status": "BOUND",
        "description": "Piyasa oynakligina gore olceklenen dinamik kayma modeli sozlesmesi.",
    },
    {
        "dependency_id": "DEP-SLP-02",
        "slippage_model": "liquidity_based_slippage_model",
        "source_phase": 146,
        "status": "BOUND",
        "description": "Hacim ve likiditeye gore kayma hesaplayan model sozlesmesi.",
    },
]


def build_validation_slippage_dependency_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for slippage dependencies."""
    rows = []
    for d in SLIPPAGE_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "slippage_model": d["slippage_model"],
                "source_phase": d["source_phase"],
                "status": d["status"],
                "description": d["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_slippage_dependencies": len(df),
        "all_bound": True,
        "non_signal": True,
    }
    return df, summary
