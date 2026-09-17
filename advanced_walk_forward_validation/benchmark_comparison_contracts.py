# -*- coding: utf-8 -*-
"""Phase 147: Benchmark Comparison Contracts.

Contracts governing methodology for comparing strategy candidates with benchmark baselines.
Ensures comparisons are non-signal and strictly forbid performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

COMPARISON_SPECS: List[Dict[str, Any]] = [
    {
        "comparison_name": "alpha_beta_regression_comparison",
        "methodology": "ORDINARY_LEAST_SQUARES",
        "relative_to": "BUY_AND_HOLD",
        "metric_calculated": False,
        "description": "Stratejinin benchmark getirisini ne olcude taklit ettigi ve alfa uretme potansiyeli sozlesmesi.",
    },
    {
        "comparison_name": "tracking_error_and_ir_comparison",
        "methodology": "INFORMATION_RATIO_FORMULA",
        "relative_to": "EQUAL_WEIGHT",
        "metric_calculated": False,
        "description": "Izleme hatasi (tracking error) ve bilgi orani (information ratio) sozlesmesi.",
    },
    {
        "comparison_name": "drawdown_relative_comparison",
        "methodology": "MAX_DRAWDOWN_DELTA",
        "relative_to": "BUY_AND_HOLD",
        "metric_calculated": False,
        "description": "Benchmark ile strateji arasindaki maksimum deger kaybi farkini kiyaslayan sozlesme.",
    },
]


def build_benchmark_comparison_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for benchmark comparison contracts."""
    rows = []
    for c in COMPARISON_SPECS:
        rows.append(
            {
                "comparison_name": c["comparison_name"],
                "methodology": c["methodology"],
                "relative_to": c["relative_to"],
                "metric_calculated": c["metric_calculated"],
                "description": c["description"],
                "investment_advice": False,
                "performance_claim": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_comparisons": len(df),
        "zero_metric_calculated": True,
        "zero_investment_advice": True,
        "zero_performance_claim": True,
        "non_signal": True,
    }
    return df, summary
