# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Benchmark Selection Bias Guards Module.

Guards against post-hoc benchmark shopping and biased baseline selection.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_SELECTION_BIAS_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BENCHMARK_SELECTION_BIAS_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_PRE_COMMITTED_BENCHMARK",
        "guard_name": "Pre-Committed Benchmark Baseline Guard",
        "detection_target": "post_hoc_benchmark_shopping",
        "description": "Benchmarkın test öncesi taahhüt edilmiş olmasını şart koşan muhafız.",
    },
    {
        "guard_id": "GUARD_NO_EASY_BENCHMARK_SWAP",
        "guard_name": "Prohibition of Weak Benchmark Substitution Guard",
        "detection_target": "benchmark_downgrading",
        "description": "Stratejiyi yapay olarak üstün göstermek için zayıf benchmark seçilmesini engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_MULTI_BASELINE_MANDATE",
        "guard_name": "Multi-Baseline Comparative Mandate Guard",
        "detection_target": "single_cherry_picked_baseline",
        "description": "Değerlendirmenin hem pasif, hem nakit, hem de sepet benchmarklarını içermesini zorunlu kılan kural.",
    },
]


def build_evaluation_benchmark_selection_bias_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of benchmark selection bias guards."""
    rows: List[Dict[str, Any]] = []

    for g in BENCHMARK_SELECTION_BIAS_GUARDS:
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
        "domain": LABEL_BENCHMARK_SELECTION_BIAS_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
