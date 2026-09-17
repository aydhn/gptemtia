# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Baseline Report Contracts Module.

Defines passive baseline reference strategies for rigorous relative evaluation.
Zero actual simulation or metric calculation is performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_BASELINE_REPORT_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BENCHMARK_BASELINES: List[Dict[str, Any]] = [
    {
        "baseline_id": "BASE_BUY_AND_HOLD",
        "baseline_name": "Passive Buy and Hold Baseline",
        "strategy_type": "passive_long_only",
        "rebalance_frequency": "none",
        "turnover_assumption": "zero",
        "description": "Temel varlıkta ilk bar alış ve dönemin sonuna kadar tutma referansı.",
    },
    {
        "baseline_id": "BASE_CASH_RISK_FREE",
        "baseline_name": "Cash and Risk-Free Rate Baseline",
        "strategy_type": "capital_preservation",
        "rebalance_frequency": "daily_accrual",
        "turnover_assumption": "zero",
        "description": "Gecelik risksiz faiz (SOFR/Fed Funds) getirisi referansı.",
    },
    {
        "baseline_id": "BASE_EQUAL_WEIGHT_BASKET",
        "baseline_name": "Equal-Weight 1/N Basket Baseline",
        "strategy_type": "diversified_passive",
        "rebalance_frequency": "monthly",
        "turnover_assumption": "low",
        "description": "Tüm evren bileşenlerinin eşit ağırlıklandırıldığı 1/N sepet referansı.",
    },
    {
        "baseline_id": "BASE_REGIME_AWARE_DYNAMIC",
        "baseline_name": "Regime-Aware Dynamic Baseline",
        "strategy_type": "regime_conditioned",
        "rebalance_frequency": "regime_transition",
        "turnover_assumption": "moderate",
        "description": "Volatilite veya trend rejimine göre pasif varlık dağılımı ayarlayan referans.",
    },
    {
        "baseline_id": "BASE_COST_ADJUSTED_PASSIVE",
        "baseline_name": "Cost and Slippage Adjusted Passive Baseline",
        "strategy_type": "frictions_included_passive",
        "rebalance_frequency": "periodic",
        "turnover_assumption": "cost_penalized",
        "description": "İşlem ücreti, taşıma maliyeti ve kayma düşülmüş net pasif getiri referansı.",
    },
]


def build_benchmark_baseline_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of all benchmark baseline contracts."""
    rows: List[Dict[str, Any]] = []

    for b in BENCHMARK_BASELINES:
        rows.append(
            {
                "baseline_id": b["baseline_id"],
                "baseline_name": b["baseline_name"],
                "strategy_type": b["strategy_type"],
                "rebalance_frequency": b["rebalance_frequency"],
                "turnover_assumption": b["turnover_assumption"],
                "description": b["description"],
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_BENCHMARK_BASELINE_REPORT_DOMAIN,
        "total_baselines": len(df),
        "all_execution_disabled": True,
        "all_metrics_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
