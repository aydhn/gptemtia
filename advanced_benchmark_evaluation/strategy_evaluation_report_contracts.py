# -*- coding: utf-8 -*-
"""Phase 151: Strategy Evaluation Report Contracts Module.

Defines the formal contracts for strategy evaluation reporting across cost,
slippage, regime, walk-forward, OOS, stress, Monte Carlo, and governance dimensions.
Enforces zero strategy approval, zero capital allocation, and zero trading recommendations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_STRATEGY_EVALUATION_REPORT_CONTRACT_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STRATEGY_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "local_strategy_evaluation_report_contract",
        "report_family": "local_strategy_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "strategy_evaluation_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "Yerel temel strateji değerlendirme raporu sözleşmesi.",
    },
    {
        "contract_name": "cost_adjusted_strategy_evaluation_report_contract",
        "report_family": "cost_adjusted_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "cost_adjusted_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "İşlem maliyetleri düzeltilmiş strateji değerlendirme raporu sözleşmesi.",
    },
    {
        "contract_name": "slippage_adjusted_strategy_evaluation_report_contract",
        "report_family": "slippage_adjusted_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "cost_adjusted_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "Kayma ve piyasa etkisi düzeltilmiş strateji değerlendirme raporu sözleşmesi.",
    },
    {
        "contract_name": "regime_aware_strategy_evaluation_report_contract",
        "report_family": "regime_aware_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "strategy_evaluation_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "Farklı piyasa rejimlerindeki davranışı inceleyen strateji değerlendirme sözleşmesi.",
    },
    {
        "contract_name": "walk_forward_strategy_evaluation_report_contract",
        "report_family": "walk_forward_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "robustness_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "Walk-forward adım stabilitesi strateji değerlendirme sözleşmesi.",
    },
    {
        "contract_name": "oos_strategy_evaluation_report_contract",
        "report_family": "oos_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "robustness_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "Kilitli örneklem dışı (OOS) dönem strateji değerlendirme sözleşmesi.",
    },
    {
        "contract_name": "stress_aware_strategy_evaluation_report_contract",
        "report_family": "stress_aware_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "risk_adjusted_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "Kriz ve aşırı piyasa şokları altında strateji dayanıklılık değerlendirmesi.",
    },
    {
        "contract_name": "monte_carlo_robustness_strategy_evaluation_report_contract",
        "report_family": "monte_carlo_robustness_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "robustness_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "Monte Carlo yeniden örnekleme ve yol varyansı strateji değerlendirme sözleşmesi.",
    },
    {
        "contract_name": "governance_bias_control_strategy_evaluation_report_contract",
        "report_family": "governance_bias_control_evaluation",
        "phase_146_ref": "realistic_backtest_contracts",
        "phase_147_ref": "oos_benchmarking_contracts",
        "phase_148_ref": "stress_scenario_contracts",
        "phase_149_ref": "monte_carlo_contracts",
        "phase_150_ref": "backtest_governance_contracts",
        "evaluation_scope_ref": "scope_offline_evaluation",
        "metric_placeholder_ref": "strategy_evaluation_metric_placeholders",
        "claim_guard_ref": "evaluation_strategy_approval_guard",
        "description": "Yönetişim, denetim izi ve yanlılık kontrolleri strateji değerlendirme sözleşmesi.",
    },
]


def build_strategy_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of all strategy evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in STRATEGY_EVALUATION_CONTRACTS:
        item = dict(c)
        item.update(
            {
                "strategy_approval_allowed": False,
                "capital_allocation_allowed": False,
                "portfolio_construction_allowed": False,
                "position_sizing_allowed": False,
                "investment_advice_allowed": False,
                "signal_generation_allowed": False,
                "live_trading_allowed": False,
                "broker_execution_allowed": False,
                "manual_review_required": True,
                "non_signal": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
            }
        )
        rows.append(item)

    df = pd.DataFrame(rows)
    summary = summarize_strategy_evaluation_report_contracts(df)
    return df, summary


def validate_strategy_evaluation_report_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single strategy evaluation report contract against negative invariants."""
    is_valid = True
    issues: List[str] = []

    if contract.get("strategy_approval_allowed", False):
        is_valid = False
        issues.append("strategy_approval_allowed must be False.")
    if contract.get("capital_allocation_allowed", False):
        is_valid = False
        issues.append("capital_allocation_allowed must be False.")
    if contract.get("portfolio_construction_allowed", False):
        is_valid = False
        issues.append("portfolio_construction_allowed must be False.")
    if contract.get("position_sizing_allowed", False):
        is_valid = False
        issues.append("position_sizing_allowed must be False.")
    if contract.get("investment_advice_allowed", False):
        is_valid = False
        issues.append("investment_advice_allowed must be False.")
    if contract.get("signal_generation_allowed", False):
        is_valid = False
        issues.append("signal_generation_allowed must be False.")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": is_valid,
        "issues": issues,
        "non_signal": True,
    }


def summarize_strategy_evaluation_report_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize strategy evaluation contracts registry."""
    return {
        "domain": LABEL_STRATEGY_EVALUATION_REPORT_CONTRACT_DOMAIN,
        "total_contracts": len(df),
        "all_approvals_disabled": not bool(df["strategy_approval_allowed"].any()) if not df.empty else True,
        "all_capital_allocation_disabled": not bool(df["capital_allocation_allowed"].any()) if not df.empty else True,
        "all_portfolio_construction_disabled": not bool(df["portfolio_construction_allowed"].any()) if not df.empty else True,
        "all_signals_disabled": not bool(df["signal_generation_allowed"].any()) if not df.empty else True,
        "manual_review_required": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
