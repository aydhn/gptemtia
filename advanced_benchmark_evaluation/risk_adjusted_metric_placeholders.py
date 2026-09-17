# -*- coding: utf-8 -*-
"""Phase 151: Risk-Adjusted Metric Placeholders Module.

Defines uncalculated placeholders for risk-adjusted performance ratios.
Strictly ensures zero Sharpe, Sortino, or Calmar calculations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_METRIC_PLACEHOLDER_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

RISK_ADJUSTED_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "sharpe_placeholder",
        "category": "risk_adjusted_ratio",
        "formula_spec": "(annualized_return - risk_free) / annualized_volatility",
        "target_role": "total_volatility_efficiency_hypothesis",
        "description": "Sharpe oranı yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "sortino_placeholder",
        "category": "risk_adjusted_ratio",
        "formula_spec": "(annualized_return - risk_free) / downside_deviation",
        "target_role": "downside_volatility_efficiency_hypothesis",
        "description": "Sortino oranı yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "calmar_placeholder",
        "category": "risk_adjusted_ratio",
        "formula_spec": "annualized_return / abs(max_drawdown)",
        "target_role": "drawdown_efficiency_hypothesis",
        "description": "Calmar oranı yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "omega_ratio_placeholder",
        "category": "risk_adjusted_ratio",
        "formula_spec": "gain_probability_integral / loss_probability_integral",
        "target_role": "probability_threshold_efficiency_hypothesis",
        "description": "Omega oranı yer tutucusu (hesaplanmamış).",
    },
]


def build_risk_adjusted_metric_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of risk-adjusted metric placeholders."""
    rows: List[Dict[str, Any]] = []

    for m in RISK_ADJUSTED_METRIC_PLACEHOLDERS:
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
        "domain": LABEL_METRIC_PLACEHOLDER_DOMAIN,
        "total_metrics": len(df),
        "all_uncalculated": True,
        "all_claims_blocked": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
