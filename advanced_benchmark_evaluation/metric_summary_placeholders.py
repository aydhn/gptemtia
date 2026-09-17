# -*- coding: utf-8 -*-
"""Phase 151: Metric Summary Placeholders Module.

Defines metric summary placeholders organized by evaluation dimensions.
All metrics remain strictly uncalculated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_METRIC_PLACEHOLDER_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

METRIC_SUMMARIES: List[Dict[str, Any]] = [
    {
        "summary_id": "METRIC_SUM_RETURN_RISK",
        "title": "Return and Volatility Metric Summary Placeholder",
        "dimension": "absolute_performance",
        "placeholders_included": ["total_return_placeholder", "annualized_return_placeholder", "volatility_placeholder"],
        "description": "Getiri ve volatilite metriklerinin yer tutucu tablosu.",
    },
    {
        "summary_id": "METRIC_SUM_RISK_ADJUSTED",
        "title": "Risk-Adjusted Efficiency Summary Placeholder",
        "dimension": "risk_adjusted",
        "placeholders_included": ["sharpe_placeholder", "sortino_placeholder", "calmar_placeholder"],
        "description": "Riske göre düzeltilmiş performans oranları yer tutucu tablosu.",
    },
    {
        "summary_id": "METRIC_SUM_BENCHMARK_RELATIVE",
        "title": "Benchmark-Relative Metrics Summary Placeholder",
        "dimension": "relative_performance",
        "placeholders_included": ["alpha_placeholder", "beta_placeholder", "information_ratio_placeholder", "tracking_error_placeholder"],
        "description": "Benchmarka kıyasla artık getiri ve korelasyon metrikleri yer tutucu tablosu.",
    },
    {
        "summary_id": "METRIC_SUM_ROBUSTNESS",
        "title": "Robustness and Stability Metrics Summary Placeholder",
        "dimension": "robustness",
        "placeholders_included": ["oos_stability_placeholder", "monte_carlo_robustness_placeholder", "parameter_stability_placeholder"],
        "description": "Sağlamlık, yeniden örnekleme ve parametre plato metrikleri yer tutucu tablosu.",
    },
]


def build_metric_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of metric summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for s in METRIC_SUMMARIES:
        rows.append(
            {
                "summary_id": s["summary_id"],
                "title": s["title"],
                "dimension": s["dimension"],
                "metrics_included": ",".join(s["placeholders_included"]),
                "metric_count": len(s["placeholders_included"]),
                "description": s["description"],
                "is_calculated": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_METRIC_PLACEHOLDER_DOMAIN,
        "total_summaries": len(df),
        "all_uncalculated": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
