# -*- coding: utf-8 -*-
"""Phase 147: Out-of-Sample Metric Placeholders.

Placeholders for realized out-of-sample metrics (Return, Drawdown, Sharpe, Sortino, Calmar, Win-rate).
Strictly disables real metric calculation or performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import ValidationMetricPlaceholder

OOS_METRICS: List[Dict[str, Any]] = [
    {
        "metric_name": "oos_return_placeholder",
        "metric_category": "OOS_PROFITABILITY",
        "description": "Orneklem disi net toplam getiri formulu yer tutucusu.",
        "formula_spec": "OOS_Return = (Equity_end - Equity_start) / Equity_start",
    },
    {
        "metric_name": "oos_drawdown_placeholder",
        "metric_category": "OOS_RISK",
        "description": "Orneklem disi tepe-dip arasi en buyuk kayip formulu yer tutucusu.",
        "formula_spec": "OOS_MaxDD = Min((Equity_t - Peak_t) / Peak_t)",
    },
    {
        "metric_name": "oos_sharpe_placeholder",
        "metric_category": "OOS_RISK_ADJUSTED",
        "description": "Orneklem disi yilliklandirilmis Sharpe orani formulu yer tutucusu.",
        "formula_spec": "OOS_Sharpe = sqrt(252) * (Mean(R_t - R_f) / Std(R_t))",
    },
    {
        "metric_name": "oos_sortino_placeholder",
        "metric_category": "OOS_DOWNSIDE_RISK",
        "description": "Orneklem disi yalnizca asagi yonlu oynakligi cezalandiran Sortino orani.",
        "formula_spec": "OOS_Sortino = sqrt(252) * (Mean(R_t - R_f) / DownsideDeviation(R_t))",
    },
    {
        "metric_name": "oos_calmar_placeholder",
        "metric_category": "OOS_DRAWDOWN_RATIO",
        "description": "Orneklem disi yillik getirinin maksimum kayba orani formulu.",
        "formula_spec": "OOS_Calmar = AnnualizedReturn / Abs(OOS_MaxDD)",
    },
    {
        "metric_name": "oos_win_rate_placeholder",
        "metric_category": "OOS_HIT_RATIO",
        "description": "Orneklem disi karli gun veya islem yuzdesi formulu yer tutucusu.",
        "formula_spec": "OOS_WinRate = Count(PnL > 0) / TotalTrades",
    },
    {
        "metric_name": "cost_adjusted_oos_return_placeholder",
        "metric_category": "OOS_NET_PROFITABILITY",
        "description": "Tum komisyon ve ucretler dusulmus OOS getiri formulu.",
        "formula_spec": "OOS_NetReturn = GrossReturn - TotalCosts",
    },
    {
        "metric_name": "slippage_adjusted_oos_return_placeholder",
        "metric_category": "OOS_REALISTIC_PROFITABILITY",
        "description": "Kayma etkisi ve likidite maliyeti dahil edilmis net OOS getiri formulu.",
        "formula_spec": "OOS_SlippageAdjusted = GrossReturn - TotalCosts - TotalSlippage",
    },
]


def build_oos_metric_placeholder_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for OOS metric placeholders."""
    rows = []
    for m in OOS_METRICS:
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
        "total_oos_metrics": len(df),
        "all_metrics_uncalculated": True,
        "zero_performance_claims": True,
        "non_signal": True,
    }
    return df, summary
