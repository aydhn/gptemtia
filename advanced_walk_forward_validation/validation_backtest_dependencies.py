# -*- coding: utf-8 -*-
"""Phase 147: Validation Realistic Backtest Dependencies.

Specifies dependencies connecting Phase 147 to Phase 146 Realistic Backtest Engine contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

BACKTEST_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP-BKT-01",
        "component": "realistic_backtest_engine_contracts",
        "source_phase": 146,
        "status": "BOUND",
        "description": "Olay tabanli ve vektorize backtest motor sozlesmeleri baglantisi.",
    },
    {
        "dependency_id": "DEP-BKT-02",
        "component": "order_simulation_contracts",
        "source_phase": 146,
        "status": "BOUND",
        "description": "Emir simulasyonu ve fill modeli sozlesmeleri baglantisi.",
    },
]


def build_validation_backtest_dependency_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest dependencies."""
    rows = []
    for d in BACKTEST_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "component": d["component"],
                "source_phase": d["source_phase"],
                "status": d["status"],
                "description": d["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_backtest_dependencies": len(df),
        "all_bound": True,
        "non_signal": True,
    }
    return df, summary
