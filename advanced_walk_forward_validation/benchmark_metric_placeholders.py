# -*- coding: utf-8 -*-
"""Phase 147: Benchmark Metric Placeholders.

Placeholders for relative benchmark metrics (Alpha, Beta, Information Ratio, Tracking Error).
Strictly disables real metric calculation or performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import ValidationMetricPlaceholder

BENCHMARK_METRICS: List[Dict[str, Any]] = [
    {
        "metric_name": "alpha_placeholder",
        "metric_category": "RELATIVE_PERFORMANCE",
        "description": "Stratejinin benchmark getirisinden arindirilmis fazla getiri formulu yer tutucusu.",
        "formula_spec": "Alpha = R_strategy - (R_f + Beta * (R_benchmark - R_f))",
        "benchmark_relative": True,
    },
    {
        "metric_name": "beta_placeholder",
        "metric_category": "SYSTEMATIC_RISK",
        "description": "Stratejinin benchmark hareketlerine duyarliligini olcen formul yer tutucusu.",
        "formula_spec": "Beta = Cov(R_strategy, R_benchmark) / Var(R_benchmark)",
        "benchmark_relative": True,
    },
    {
        "metric_name": "information_ratio_placeholder",
        "metric_category": "ACTIVE_RISK_ADJUSTED",
        "description": "Aktif getirinin takip hatasina orani formulu yer tutucusu.",
        "formula_spec": "IR = (Mean(R_strategy - R_benchmark)) / Std(R_strategy - R_benchmark)",
        "benchmark_relative": True,
    },
    {
        "metric_name": "tracking_error_placeholder",
        "metric_category": "BENCHMARK_DIVERGENCE",
        "description": "Strateji ile benchmark arasindaki getiri farkinin standart sapmasi formulu yer tutucusu.",
        "formula_spec": "TE = Std(R_strategy - R_benchmark) * sqrt(252)",
        "benchmark_relative": True,
    },
    {
        "metric_name": "benchmark_relative_performance_placeholder",
        "metric_category": "CUMULATIVE_SPREAD",
        "description": "Kümülatif strateji getirisinin kümülatif benchmark getirisinden farki.",
        "formula_spec": "RelativePerf = CumReturn_strategy - CumReturn_benchmark",
        "benchmark_relative": True,
    },
]


def build_benchmark_metric_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for benchmark metric placeholders."""
    rows = []
    for m in BENCHMARK_METRICS:
        p = ValidationMetricPlaceholder(
            metric_name=m["metric_name"],
            metric_category=m["metric_category"],
            description=m["description"],
            formula_spec=m["formula_spec"],
            benchmark_relative=m["benchmark_relative"],
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
                "benchmark_relative": p.benchmark_relative,
                "metric_calculated": p.metric_calculated,
                "performance_claim_generated": p.performance_claim_generated,
                "non_signal": p.non_signal,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_benchmark_metrics": len(df),
        "all_metrics_uncalculated": True,
        "zero_performance_claims": True,
        "non_signal": True,
    }
    return df, summary
