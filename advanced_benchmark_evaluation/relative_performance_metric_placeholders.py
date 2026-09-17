# -*- coding: utf-8 -*-
"""Phase 151: Relative Performance Metric Placeholders Module.

Defines uncalculated metric placeholders for relative performance evaluation.
Zero real calculation is performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_STRATEGY_VS_BENCHMARK_REPORT_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

RELATIVE_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "information_ratio_placeholder",
        "category": "relative_efficiency",
        "formula_spec": "(annualized_strategy_return - annualized_benchmark_return) / tracking_error",
        "target_role": "active_management_efficiency_hypothesis",
        "description": "Bilgi oranı (Information Ratio) yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "up_capture_placeholder",
        "category": "market_capture",
        "formula_spec": "mean(strategy_return[bench > 0]) / mean(bench_return[bench > 0])",
        "target_role": "bull_market_capture_hypothesis",
        "description": "Yükseliş piyasası katılım oranı yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "down_capture_placeholder",
        "category": "market_capture",
        "formula_spec": "mean(strategy_return[bench < 0]) / mean(bench_return[bench < 0])",
        "target_role": "bear_market_capture_hypothesis",
        "description": "Düşüş piyasası katılım oranı yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "relative_drawdown_spread_placeholder",
        "category": "relative_risk",
        "formula_spec": "max_drawdown_strategy - max_drawdown_benchmark",
        "target_role": "relative_drawdown_differential_hypothesis",
        "description": "Benchmark ile strateji arasındaki azami kayıp farkı yer tutucusu (hesaplanmamış).",
    },
]


def build_relative_performance_metric_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of relative performance metric placeholders."""
    rows: List[Dict[str, Any]] = []

    for m in RELATIVE_METRIC_PLACEHOLDERS:
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
        "domain": LABEL_STRATEGY_VS_BENCHMARK_REPORT_DOMAIN,
        "total_metrics": len(df),
        "all_uncalculated": True,
        "all_claims_blocked": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
