# -*- coding: utf-8 -*-
"""Phase 147: Validation Model Contract Dependencies.

Specifies dependencies connecting Phase 147 to Phase 145 Advanced ML Acceptance
and candidate model contract definitions.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

MODEL_CONTRACT_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP-MDL-01",
        "contract": "advanced_ml_acceptance",
        "source_phase": 145,
        "status": "BOUND",
        "description": "ML kabul kriterleri ve aday model sozlesme gereksinimleri baglantisi.",
    },
    {
        "dependency_id": "DEP-MDL-02",
        "contract": "advanced_baseline_ml_models",
        "source_phase": 136,
        "status": "BOUND",
        "description": "Temel ML modelleri sozlesme katalogu baglantisi.",
    },
]


def build_validation_model_contract_dependency_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model contract dependencies."""
    rows = []
    for d in MODEL_CONTRACT_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "contract": d["contract"],
                "source_phase": d["source_phase"],
                "status": d["status"],
                "description": d["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_model_dependencies": len(df),
        "all_bound": True,
        "non_signal": True,
    }
    return df, summary
