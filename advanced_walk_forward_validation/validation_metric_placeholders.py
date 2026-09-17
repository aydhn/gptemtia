# -*- coding: utf-8 -*-
"""Phase 147: Validation Metric Placeholders.

Placeholders for fold stability, generalization gaps, and parameter sensitivity metrics.
Strictly disables real metric calculation or performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import ValidationMetricPlaceholder

VALIDATION_METRICS: List[Dict[str, Any]] = [
    {
        "metric_name": "fold_stability_placeholder",
        "metric_category": "STABILITY",
        "description": "Katmanlar arasi getiri veya Sharpe varyasyonunu olcen istikrar metrigi formulu.",
        "formula_spec": "FoldStability = 1.0 - Std(Sharpe_folds) / Mean(Sharpe_folds)",
    },
    {
        "metric_name": "generalization_gap_placeholder",
        "metric_category": "OVERFITTING_RISK",
        "description": "In-sample egitim performansi ile OOS performans arasindaki acik formulu.",
        "formula_spec": "GenGap = Sharpe_train - Sharpe_oos",
    },
    {
        "metric_name": "parameter_sensitivity_placeholder",
        "metric_category": "SENSITIVITY",
        "description": "Pencere boyutu veya parametre degisimine karsi sonuc duyarliligi formulu.",
        "formula_spec": "Sensitivity = MaxVariation(Score(theta +- delta)) / Score(theta)",
    },
]


def build_validation_metric_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for validation metric placeholders."""
    rows = []
    for m in VALIDATION_METRICS:
        p = ValidationMetricPlaceholder(
            metric_name=m["metric_name"],
            metric_category=m["metric_category"],
            description=m["description"],
            formula_spec=m["formula_spec"],
            benchmark_relative=False,
            metric_calculated=False,
            performance_claim_generated=False,
            non_signal=True,
        )
        rows.append(
            {
                "metric_name": p.metric_name,
                "metric_category": p.metric_category,
                "description": p.description,
                "formula_spec": p.formula_spec,
                "metric_calculated": p.metric_calculated,
                "performance_claim_generated": p.performance_claim_generated,
                "non_signal": p.non_signal,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_validation_metrics": len(df),
        "all_metrics_uncalculated": True,
        "zero_performance_claims": True,
        "non_signal": True,
    }
    return df, summary
