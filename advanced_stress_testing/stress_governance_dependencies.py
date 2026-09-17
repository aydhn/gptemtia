# -*- coding: utf-8 -*-
"""Phase 148: Stress Governance Dependencies.

Provides specifications and registry linking stress contracts with Phase 144 Model Governance
and Phase 145 Advanced ML Acceptance.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

GOVERNANCE_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "model_cards_and_audit_trail_dependency",
        "source_phase": 144,
        "component_name": "advanced_model_governance",
        "description": "Model kartları, denetim izi ve üretim onay sınırları referansı.",
        "status": "SATISFIED",
    },
    {
        "dependency_id": "ml_acceptance_report_dependency",
        "source_phase": 145,
        "component_name": "advanced_ml_acceptance",
        "description": "Konsolide ML kabul raporu ve non-production hazır bulunuşluk sınırı referansı.",
        "status": "SATISFIED",
    },
]


def build_stress_governance_dependency_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of governance dependencies."""
    rows: List[Dict[str, Any]] = []
    for d in GOVERNANCE_DEPENDENCIES:
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
        "total_governance_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
