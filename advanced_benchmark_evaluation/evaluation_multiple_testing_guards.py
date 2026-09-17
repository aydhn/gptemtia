# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Multiple Testing Guards Module.

Guards against multiple testing bias by enforcing statistical significance corrections.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

MULTIPLE_TESTING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_BONFERRONI_HOLM_MANDATE",
        "guard_name": "Family-Wise Error Rate (FWER) Mandate Guard",
        "correction_family": "bonferroni_holm",
        "description": "Çoklu hipotez testlerinde p-değeri eşiklerinin sıkılaştırılmasını şart koşan muhafız.",
    },
    {
        "guard_id": "GUARD_FDR_BENJAMINI_HOCHBERG",
        "guard_name": "False Discovery Rate (FDR) Mandate Guard",
        "correction_family": "benjamini_hochberg",
        "description": "Büyük kural havuzlarında sahte keşif oranını sınırlandıran muhafız.",
    },
]


def build_evaluation_multiple_testing_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of multiple testing guards."""
    rows: List[Dict[str, Any]] = []

    for g in MULTIPLE_TESTING_GUARDS:
        rows.append(
            {
                "guard_id": g["guard_id"],
                "guard_name": g["guard_name"],
                "correction_family": g["correction_family"],
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
