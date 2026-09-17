# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Overfitting Guards Module.

Guards against model overfitting, curve-fitting, and excessive parameterization.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

OVERFITTING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_DEGREES_OF_FREEDOM",
        "guard_name": "Degrees of Freedom Constraint Guard",
        "detection_target": "excessive_parameters_relative_to_trades",
        "description": "İşlem sayısına kıyasla aşırı serbest parametre kullanımını denetleyen muhafız.",
    },
    {
        "guard_id": "GUARD_IS_OOS_DIVERGENCE_LIMIT",
        "guard_name": "In-Sample vs Out-of-Sample Divergence Guard",
        "detection_target": "massive_performance_collapse",
        "description": "Eğitim ve test performansı arasındaki aşırı uçurumu tespit eden muhafız.",
    },
]


def build_evaluation_overfitting_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of overfitting guards."""
    rows: List[Dict[str, Any]] = []

    for g in OVERFITTING_GUARDS:
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
