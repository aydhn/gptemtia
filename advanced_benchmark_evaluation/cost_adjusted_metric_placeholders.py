# -*- coding: utf-8 -*-
"""Phase 151: Cost-Adjusted Metric Placeholders Module.

Defines uncalculated metric placeholders for friction-adjusted evaluation.
Zero real calculation is performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_COST_ADJUSTED_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

COST_ADJUSTED_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "cost_adjusted_return_placeholder",
        "category": "cost_adjusted_return",
        "formula_spec": "gross_return - cumulative_commissions_bps - cumulative_exchange_fees_bps",
        "target_role": "net_of_commission_hypothesis",
        "description": "Komisyon ve borsa ücretleri düşülmüş net getiri yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "slippage_adjusted_return_placeholder",
        "category": "slippage_adjusted_return",
        "formula_spec": "gross_return - cumulative_slippage_bps - market_impact_bps",
        "target_role": "net_of_slippage_hypothesis",
        "description": "Kayma ve piyasa etkisi düşülmüş net getiri yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "all_in_friction_drag_placeholder",
        "category": "friction_drag",
        "formula_spec": "cumulative_costs + cumulative_slippage + cumulative_carry",
        "target_role": "total_friction_drag_hypothesis",
        "description": "Tüm sürtünmelerin getiri üzerindeki kümülatif erozyonu yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "turnover_cost_ratio_placeholder",
        "category": "friction_efficiency",
        "formula_spec": "all_in_friction_drag / annualized_gross_return",
        "target_role": "friction_efficiency_ratio_hypothesis",
        "description": "Sürtünme maliyetlerinin brüt getiriye oranı yer tutucusu (hesaplanmamış).",
    },
]


def build_cost_adjusted_metric_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of cost-adjusted metric placeholders."""
    rows: List[Dict[str, Any]] = []

    for m in COST_ADJUSTED_METRIC_PLACEHOLDERS:
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
        "domain": LABEL_COST_ADJUSTED_EVALUATION_DOMAIN,
        "total_metrics": len(df),
        "all_uncalculated": True,
        "all_claims_blocked": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
