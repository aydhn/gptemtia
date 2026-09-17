# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Comparison Report Contracts Module.

Defines the formal contracts for benchmark comparison reporting across local,
OOS, walk-forward, cost-adjusted, regime-aware, stress-aware, and governance domains.
All contracts enforce zero simulation execution and zero metric calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_REPORT_CONTRACT_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BENCHMARK_COMPARISON_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "local_benchmark_comparison_report_contract",
        "report_family": "local_baseline_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_buy_and_hold_contract",
        "metric_placeholder_ref": "benchmark_comparison_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "Yerel çevrimdışı benchmark karşılaştırma raporu sözleşmesi.",
    },
    {
        "contract_name": "oos_benchmark_comparison_report_contract",
        "report_family": "out_of_sample_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_cash_risk_free_contract",
        "metric_placeholder_ref": "relative_performance_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "Örneklem dışı (OOS) benchmark karşılaştırma raporu sözleşmesi.",
    },
    {
        "contract_name": "walk_forward_benchmark_comparison_report_contract",
        "report_family": "walk_forward_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_equal_weight_basket_contract",
        "metric_placeholder_ref": "relative_performance_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "Walk-forward pencereleri benchmark karşılaştırma raporu sözleşmesi.",
    },
    {
        "contract_name": "cost_adjusted_benchmark_comparison_report_contract",
        "report_family": "cost_adjusted_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_cost_adjusted_contract",
        "metric_placeholder_ref": "cost_adjusted_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "İşlem maliyeti düzeltmeli benchmark karşılaştırma raporu sözleşmesi.",
    },
    {
        "contract_name": "slippage_adjusted_benchmark_comparison_report_contract",
        "report_family": "slippage_adjusted_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_buy_and_hold_contract",
        "metric_placeholder_ref": "cost_adjusted_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "Kayma ve likidite düzeltmeli benchmark karşılaştırma raporu sözleşmesi.",
    },
    {
        "contract_name": "regime_aware_benchmark_comparison_report_contract",
        "report_family": "regime_aware_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_regime_aware_contract",
        "metric_placeholder_ref": "relative_performance_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "Piyasa rejimlerine duyarlı benchmark karşılaştırma raporu sözleşmesi.",
    },
    {
        "contract_name": "stress_aware_benchmark_comparison_report_contract",
        "report_family": "stress_aware_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_cash_risk_free_contract",
        "metric_placeholder_ref": "robustness_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "Kriz ve stres senaryoları benchmark karşılaştırma raporu sözleşmesi.",
    },
    {
        "contract_name": "monte_carlo_aware_benchmark_comparison_report_contract",
        "report_family": "monte_carlo_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_equal_weight_basket_contract",
        "metric_placeholder_ref": "robustness_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "Monte Carlo dayanıklılık ve zarf benchmark karşılaştırma raporu sözleşmesi.",
    },
    {
        "contract_name": "governance_aware_benchmark_comparison_report_contract",
        "report_family": "governance_aware_comparison",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "benchmark_universe_ref": "universe_commodity_fx_contract",
        "benchmark_baseline_ref": "baseline_buy_and_hold_contract",
        "metric_placeholder_ref": "benchmark_comparison_metric_placeholders",
        "result_claim_guard_ref": "evaluation_result_claim_guard",
        "performance_claim_guard_ref": "evaluation_performance_claim_guard",
        "description": "Yönetişim, denetim izi ve yanlılık kontrollü benchmark karşılaştırma sözleşmesi.",
    },
]


def build_benchmark_comparison_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of all benchmark comparison report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in BENCHMARK_COMPARISON_CONTRACTS:
        item = dict(c)
        item.update(
            {
                "benchmark_execution_allowed": False,
                "metric_calculation_allowed": False,
                "result_claim_allowed": False,
                "performance_claim_allowed": False,
                "strategy_approval_allowed": False,
                "live_trading_allowed": False,
                "broker_execution_allowed": False,
                "signal_generation_allowed": False,
                "manual_review_required": True,
                "non_signal": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
            }
        )
        rows.append(item)

    df = pd.DataFrame(rows)
    summary = summarize_benchmark_comparison_report_contracts(df)
    return df, summary


def validate_benchmark_comparison_report_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single benchmark comparison report contract against negative invariants."""
    is_valid = True
    issues: List[str] = []

    if contract.get("benchmark_execution_allowed", False):
        is_valid = False
        issues.append("benchmark_execution_allowed must be False.")
    if contract.get("metric_calculation_allowed", False):
        is_valid = False
        issues.append("metric_calculation_allowed must be False.")
    if contract.get("result_claim_allowed", False):
        is_valid = False
        issues.append("result_claim_allowed must be False.")
    if contract.get("performance_claim_allowed", False):
        is_valid = False
        issues.append("performance_claim_allowed must be False.")
    if contract.get("strategy_approval_allowed", False):
        is_valid = False
        issues.append("strategy_approval_allowed must be False.")
    if contract.get("live_trading_allowed", False):
        is_valid = False
        issues.append("live_trading_allowed must be False.")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": is_valid,
        "issues": issues,
        "non_signal": True,
    }


def summarize_benchmark_comparison_report_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize benchmark comparison contracts registry."""
    return {
        "domain": LABEL_BENCHMARK_REPORT_CONTRACT_DOMAIN,
        "total_contracts": len(df),
        "all_execution_disabled": not bool(df["benchmark_execution_allowed"].any()) if not df.empty else True,
        "all_metrics_disabled": not bool(df["metric_calculation_allowed"].any()) if not df.empty else True,
        "all_claims_disabled": not bool(df["result_claim_allowed"].any()) if not df.empty else True,
        "all_approvals_disabled": not bool(df["strategy_approval_allowed"].any()) if not df.empty else True,
        "manual_review_required": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
