# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Walk-Forward Dependencies Module.

Links Phase 151 evaluation contracts to Phase 147 walk-forward & OOS benchmarking contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

WALK_FORWARD_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_147_WF_SPLITS",
        "phase_source": 147,
        "contract_source": "advanced_walk_forward_validation.walk_forward_split_contracts",
        "status": "SATISFIED",
        "description": "Rolling ve expanding walk-forward pencereleri sözleşmeleri.",
    },
    {
        "dependency_id": "DEP_147_OOS_HOLDOUT",
        "phase_source": 147,
        "contract_source": "advanced_walk_forward_validation.oos_holdout_splits",
        "status": "SATISFIED",
        "description": "Mühürlü örneklem dışı (OOS) holdout split sözleşmeleri.",
    },
    {
        "dependency_id": "DEP_147_PURGE_EMBARGO",
        "phase_source": 147,
        "contract_source": "advanced_walk_forward_validation.purge_embargo_policies",
        "status": "SATISFIED",
        "description": "Etiket örtüşmesini önleyen arındırma ve ambargo tamponları sözleşmesi.",
    },
]


def build_evaluation_walk_forward_dependency_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of walk-forward dependencies."""
    rows: List[Dict[str, Any]] = []

    for d in WALK_FORWARD_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "phase_source": d["phase_source"],
                "contract_source": d["contract_source"],
                "dependency_status": d["status"],
                "description": d["description"],
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DEPENDENCY_DOMAIN,
        "total_dependencies": len(df),
        "all_satisfied": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
