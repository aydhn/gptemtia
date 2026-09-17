# -*- coding: utf-8 -*-
"""Phase 148: Stress Transaction Cost Dependencies.

Provides specifications and registry linking stress contracts with Phase 146 transaction cost models.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

TRANSACTION_COST_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "tier_commission_model_dependency",
        "source_phase": 146,
        "component_name": "transaction_cost_model_contracts",
        "description": "Kademeli komisyon ve döviz/emtia takas masrafları referansı.",
        "status": "SATISFIED",
    },
]


def build_stress_transaction_cost_dependency_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of transaction cost dependencies."""
    rows: List[Dict[str, Any]] = []
    for d in TRANSACTION_COST_DEPENDENCIES:
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
        "total_cost_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
