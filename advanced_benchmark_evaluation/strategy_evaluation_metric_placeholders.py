# -*- coding: utf-8 -*-
"""Phase 151: Strategy Evaluation Metric Placeholders Module.

Defines uncalculated metric placeholders for strategy evaluation.
Strictly ensures zero Sharpe, return, win rate, or drawdown calculations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_METRIC_PLACEHOLDER_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STRATEGY_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "total_return_placeholder",
        "category": "return_metric",
        "formula_spec": "(end_nav - start_nav) / start_nav",
        "target_role": "cumulative_performance_hypothesis",
        "description": "Kümülatif toplam getiri yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "annualized_return_placeholder",
        "category": "return_metric",
        "formula_spec": "(1 + total_return) ** (252 / days) - 1",
        "target_role": "annualized_performance_hypothesis",
        "description": "Yıllıklandırılmış getiri yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "volatility_placeholder",
        "category": "risk_metric",
        "formula_spec": "std(daily_returns) * sqrt(252)",
        "target_role": "annualized_risk_hypothesis",
        "description": "Yıllıklandırılmış getiri volatilitesi yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "drawdown_placeholder",
        "category": "risk_metric",
        "formula_spec": "min((nav - rolling_peak) / rolling_peak)",
        "target_role": "drawdown_risk_hypothesis",
        "description": "Zirveden dibe maksimum kayıp yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "win_rate_placeholder",
        "category": "trade_metric",
        "formula_spec": "winning_trades / total_trades",
        "target_role": "hit_rate_hypothesis",
        "description": "Başarılı işlem oranı yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "profit_factor_placeholder",
        "category": "trade_metric",
        "formula_spec": "gross_profits / abs(gross_losses)",
        "target_role": "profitability_ratio_hypothesis",
        "description": "Kâr faktörü oranı yer tutucusu (hesaplanmamış).",
    },
]


def build_strategy_evaluation_metric_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of strategy evaluation metric placeholders."""
    rows: List[Dict[str, Any]] = []

    for m in STRATEGY_METRIC_PLACEHOLDERS:
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
