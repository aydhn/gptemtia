# -*- coding: utf-8 -*-
"""Phase 148: Stress Backtest Dependencies.

Provides specifications and registry linking stress contracts with Phase 146 Realistic Backtest foundations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

BACKTEST_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "realistic_backtest_engine_dependency",
        "source_phase": 146,
        "component_name": "realistic_backtest_profile_registry",
        "description": "Gerçekçi backtest motoru sözleşmeleri ve yürütme engeli referansı.",
        "status": "SATISFIED",
    },
    {
        "dependency_id": "backtest_safety_boundary_dependency",
        "source_phase": 146,
        "component_name": "realistic_backtest_safety_boundary",
        "description": "Canlı emir yasağı ve aracı kurum entegrasyon bariyeri.",
        "status": "SATISFIED",
    },
]


def build_stress_backtest_dependency_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of backtest dependencies."""
    rows: List[Dict[str, Any]] = []
    for d in BACKTEST_DEPENDENCIES:
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
        "total_backtest_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
