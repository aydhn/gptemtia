# -*- coding: utf-8 -*-
"""Phase 147: Validation Governance Dependencies.

Specifies governance dependencies connecting Phase 147 to Phase 144 Model Governance
and Phase 139 GPU Training Governance.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

GOVERNANCE_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP-GOV-01",
        "module": "advanced_model_governance",
        "source_phase": 144,
        "status": "BOUND",
        "description": "Model yonetisim katmani, onay kapilari ve audit registry entegrasyonu.",
    },
    {
        "dependency_id": "DEP-GOV-02",
        "module": "advanced_gpu_training_governance",
        "source_phase": 139,
        "status": "BOUND",
        "description": "GPU kaynak yonetisimi ve yerel calisma sinirlari entegrasyonu.",
    },
]


def build_validation_governance_dependency_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance dependencies."""
    rows = []
    for d in GOVERNANCE_DEPENDENCIES:
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
        "total_governance_dependencies": len(df),
        "all_bound": True,
        "non_signal": True,
    }
    return df, summary
