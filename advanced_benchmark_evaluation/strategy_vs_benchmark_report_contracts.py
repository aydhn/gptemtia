# -*- coding: utf-8 -*-
"""Phase 151: Strategy vs Benchmark Report Contracts Module.

Defines comparison contracts between strategy models and benchmarks.
Strictly ensures zero performance claims, zero alpha/beta calculations, and zero strategy approvals.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_STRATEGY_VS_BENCHMARK_REPORT_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STRATEGY_VS_BENCHMARK_CONTRACTS: List[Dict[str, Any]] = [
    {
        "comparison_id": "COMP_EXCESS_RETURN",
        "comparison_name": "Excess Return Comparison Contract",
        "primary_metric_placeholder": "benchmark_relative_return_placeholder",
        "focus_area": "alpha_hypothesis",
        "claim_boundary": "zero_performance_claim_enforced",
        "description": "Strateji ile benchmark arasındaki getiri farkı hipotezi sözleşmesi.",
    },
    {
        "comparison_id": "COMP_TRACKING_ERROR",
        "comparison_name": "Tracking Error Comparison Contract",
        "primary_metric_placeholder": "tracking_error_placeholder",
        "focus_area": "variance_spread",
        "claim_boundary": "zero_performance_claim_enforced",
        "description": "Benchmarktan sapma volatilitesi sözleşmesi.",
    },
    {
        "comparison_id": "COMP_INFORMATION_RATIO",
        "comparison_name": "Information Ratio Comparison Contract",
        "primary_metric_placeholder": "information_ratio_placeholder",
        "focus_area": "risk_adjusted_excess",
        "claim_boundary": "zero_performance_claim_enforced",
        "description": "Risk birimi başına artık getiri değerlendirme şablonu.",
    },
    {
        "comparison_id": "COMP_BETA_SENSITIVITY",
        "comparison_name": "Benchmark Beta Sensitivity Contract",
        "primary_metric_placeholder": "beta_placeholder",
        "focus_area": "systematic_exposure",
        "claim_boundary": "zero_performance_claim_enforced",
        "description": "Benchmark hareketlerine duyarlılık ve piyasa riski sözleşmesi.",
    },
    {
        "comparison_id": "COMP_CAPTURE_RATIOS",
        "comparison_name": "Up/Down Market Capture Contract",
        "primary_metric_placeholder": "robustness_metric_placeholders",
        "focus_area": "asymmetric_participation",
        "claim_boundary": "zero_performance_claim_enforced",
        "description": "Boğa ve ayı piyasası katılım oranları sözleşmesi.",
    },
]


def build_strategy_vs_benchmark_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of strategy vs benchmark comparison contracts."""
    rows: List[Dict[str, Any]] = []

    for c in STRATEGY_VS_BENCHMARK_CONTRACTS:
        rows.append(
            {
                "comparison_id": c["comparison_id"],
                "comparison_name": c["comparison_name"],
                "primary_metric_placeholder": c["primary_metric_placeholder"],
                "focus_area": c["focus_area"],
                "claim_boundary": c["claim_boundary"],
                "description": c["description"],
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "performance_claim_allowed": False,
                "strategy_approval_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_STRATEGY_VS_BENCHMARK_REPORT_DOMAIN,
        "total_comparisons": len(df),
        "all_execution_disabled": True,
        "all_claims_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
