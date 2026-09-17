# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Comparison Metric Placeholders Module.

Defines uncalculated metric placeholders for benchmark comparison.
Strictly ensures zero alpha, beta, or tracking error calculations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_REPORT_CONTRACT_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BENCHMARK_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "alpha_placeholder",
        "category": "relative_performance",
        "formula_spec": "strategy_return - (risk_free + beta * (benchmark_return - risk_free))",
        "target_role": "excess_alpha_hypothesis",
        "description": "Jensen alfası artık getiri hipotezi yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "beta_placeholder",
        "category": "systematic_risk",
        "formula_spec": "cov(strategy_returns, benchmark_returns) / var(benchmark_returns)",
        "target_role": "market_sensitivity_hypothesis",
        "description": "Piyasa duyarlılığı ve korelasyon eğimi yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "tracking_error_placeholder",
        "category": "tracking_risk",
        "formula_spec": "std(strategy_returns - benchmark_returns) * sqrt(252)",
        "target_role": "tracking_divergence_hypothesis",
        "description": "Benchmarktan sapma volatilitesi yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "benchmark_relative_return_placeholder",
        "category": "relative_return",
        "formula_spec": "strategy_cumulative_return - benchmark_cumulative_return",
        "target_role": "relative_spread_hypothesis",
        "description": "Benchmarka kıyasla artık kümülatif getiri yer tutucusu (hesaplanmamış).",
    },
]


def build_benchmark_comparison_metric_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of benchmark comparison metric placeholders."""
    rows: List[Dict[str, Any]] = []

    for m in BENCHMARK_METRIC_PLACEHOLDERS:
        rows.append(
            {
                "metric_name": m["metric_name"],
                "category": m["category"],
                "formula_spec": m["formula_spec"],
                "target_role": m["target_role"],
                "description": m["description"],
                "is_calculated": False,
                "actual_value": None,
                "performance_claim_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_BENCHMARK_REPORT_CONTRACT_DOMAIN,
        "total_metrics": len(df),
        "all_uncalculated": True,
        "all_claims_blocked": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
