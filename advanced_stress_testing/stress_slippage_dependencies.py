# -*- coding: utf-8 -*-
"""Phase 148: Stress Slippage Dependencies.

Provides specifications and registry linking stress contracts with Phase 146 slippage models.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

SLIPPAGE_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "volatility_spread_slippage_model_dependency",
        "source_phase": 146,
        "component_name": "slippage_model_contracts",
        "description": "Volatilite ve spread duyarlı dinamik kayma modelleri referansı.",
        "status": "SATISFIED",
    },
]


def build_stress_slippage_dependency_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of slippage dependencies."""
    rows: List[Dict[str, Any]] = []
    for d in SLIPPAGE_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "source_phase": d["source_phase"],
                "component_name": d["component_name"],
                "description": d["description"],
                "status": d["status"],
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_slippage_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
