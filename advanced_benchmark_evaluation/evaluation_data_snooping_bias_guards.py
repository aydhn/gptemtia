# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Data Snooping Bias Guards Module.

Guards against data snooping, repeated holdout reuse, and p-hacking.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

DATA_SNOOPING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_HOLDOUT_REUSE_TRACKING",
        "guard_name": "Holdout Reuse Audit Guard",
        "detection_target": "multiple_holdout_access",
        "description": "Örneklem dışı veri üzerinde tekrarlanan testlerin kaydını tutan ve engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_TRIAL_COUNT_PENALTY",
        "guard_name": "Trial Count Deflation Guard",
        "detection_target": "unpenalized_multiple_trials",
        "description": "Deneme sayısı arttıkça raporlanan metriklerin iskonto edilmesini şart koşan muhafız.",
    },
]


def build_evaluation_data_snooping_bias_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of data snooping bias guards."""
    rows: List[Dict[str, Any]] = []

    for g in DATA_SNOOPING_GUARDS:
        rows.append(
            {
                "guard_id": g["guard_id"],
                "guard_name": g["guard_name"],
                "detection_target": g["detection_target"],
                "description": g["description"],
                "is_active": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_CLAIM_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
