# -*- coding: utf-8 -*-
"""Phase 148: Stress Walk-Forward Dependencies.

Provides specifications and registry linking stress contracts with Phase 147 Walk-Forward Validation foundations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

WALK_FORWARD_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "walk_forward_split_contracts_dependency",
        "source_phase": 147,
        "component_name": "walk_forward_split_contracts",
        "description": "Zaman serisi bölümleme, rolling/expanding pencere sözleşmeleri referansı.",
        "status": "SATISFIED",
    },
    {
        "dependency_id": "oos_benchmark_contracts_dependency",
        "source_phase": 147,
        "component_name": "oos_benchmark_contracts",
        "description": "Örneklem dışı benchmark karşılaştırma standartları referansı.",
        "status": "SATISFIED",
    },
]


def build_stress_walk_forward_dependency_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of walk-forward dependencies."""
    rows: List[Dict[str, Any]] = []
    for d in WALK_FORWARD_DEPENDENCIES:
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
        "total_walk_forward_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
