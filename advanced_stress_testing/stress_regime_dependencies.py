# -*- coding: utf-8 -*-
"""Phase 148: Stress Regime Dependencies.

Provides specifications and registry linking stress contracts with Phase 135 Regime Classification Acceptance.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

REGIME_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "regime_classification_engine_dependency",
        "source_phase": 135,
        "component_name": "regime_classification_acceptance",
        "description": "Volatilite, trend ve likidite rejim sınıflandırma standartları referansı.",
        "status": "SATISFIED",
    },
]


def build_stress_regime_dependency_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of regime dependencies."""
    rows: List[Dict[str, Any]] = []
    for d in REGIME_DEPENDENCIES:
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
        "total_regime_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
