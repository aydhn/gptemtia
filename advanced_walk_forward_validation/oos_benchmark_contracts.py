# -*- coding: utf-8 -*-
"""Phase 147: Out-of-Sample Benchmark Contracts.

Defines benchmark contract specifications against passive baselines and market universes.
Strictly disallows benchmark execution, metric calculation, or investment advice.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import BenchmarkContract

BENCHMARK_SPECS: List[Dict[str, Any]] = [
    {
        "benchmark_name": "naive_no_trade_baseline_contract",
        "benchmark_type": "NO_TRADE_ZERO_RETURN",
        "description": "Hicbir pozisyon acilmayan, sifir getiri ve sifir islem maliyeti iceren temel referans sozlesmesi.",
        "universe_ref": "single_asset_universe",
        "baseline_strategy_ref": "naive_no_trade_baseline",
        "rebalance_policy": "NONE",
        "transaction_cost_aware": True,
        "slippage_aware": True,
    },
    {
        "benchmark_name": "cash_baseline_contract",
        "benchmark_type": "RISK_FREE_CASH",
        "description": "Portfoyun nakit veya risksiz faizde tutuldugu getiri referans sozlesmesi.",
        "universe_ref": "cash_risk_free_rate",
        "baseline_strategy_ref": "cash_benchmark_placeholder",
        "rebalance_policy": "DAILY_ACCRUAL",
        "transaction_cost_aware": True,
        "slippage_aware": False,
    },
    {
        "benchmark_name": "buy_and_hold_placeholder_contract",
        "benchmark_type": "PASSIVE_BUY_HOLD",
        "description": "Varlik donem basinda alinarak donem sonuna kadar tutulan klasik Buy & Hold referans sozlesmesi.",
        "universe_ref": "single_asset_universe",
        "baseline_strategy_ref": "buy_and_hold_benchmark_placeholder",
        "rebalance_policy": "BUY_ONCE",
        "transaction_cost_aware": True,
        "slippage_aware": True,
    },
    {
        "benchmark_name": "equal_weight_placeholder_contract",
        "benchmark_type": "MULTI_ASSET_EQUAL_WEIGHT",
        "description": "Sepetteki tum emtia ve doviz paritelerine esit agirlik veren 1/N portfoy referans sozlesmesi.",
        "universe_ref": "multi_asset_commodity_forex_universe",
        "baseline_strategy_ref": "equal_weight_benchmark_placeholder",
        "rebalance_policy": "MONTHLY_REBALANCE",
        "transaction_cost_aware": True,
        "slippage_aware": True,
    },
    {
        "benchmark_name": "regime_aware_baseline_placeholder_contract",
        "benchmark_type": "REGIME_CONDITIONED_BASELINE",
        "description": "Yuksek volatilite donemlerinde nakde gecen, sakin donemlerde Buy & Hold uygulayan rejim tabanli referans.",
        "universe_ref": "regime_conditioned_universe",
        "baseline_strategy_ref": "regime_benchmark_placeholder",
        "rebalance_policy": "ON_REGIME_CHANGE",
        "transaction_cost_aware": True,
        "slippage_aware": True,
    },
    {
        "benchmark_name": "cost_aware_baseline_placeholder_contract",
        "benchmark_type": "COST_AWARE_BASELINE",
        "description": "Islem komisyonu ve kayma maliyetlerini net olarak hesaba katan maliyet duyarli benchmark sozlesmesi.",
        "universe_ref": "cost_aware_universe",
        "baseline_strategy_ref": "cost_aware_benchmark_placeholder",
        "rebalance_policy": "PERIODIC",
        "transaction_cost_aware": True,
        "slippage_aware": True,
    },
    {
        "benchmark_name": "random_policy_baseline_placeholder_contract",
        "benchmark_type": "RANDOM_ENTRY_EXIT",
        "description": "Sans faktoru ve sans eseri basariyi test etmek amaciyla rastgele sinyal ureten referans yer tutucu sozlesme.",
        "universe_ref": "single_asset_universe",
        "baseline_strategy_ref": "random_policy_baseline",
        "rebalance_policy": "RANDOM",
        "transaction_cost_aware": True,
        "slippage_aware": True,
    },
]


def build_oos_benchmark_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for OOS benchmark contracts."""
    rows = []
    for spec in BENCHMARK_SPECS:
        b = BenchmarkContract(
            benchmark_name=spec["benchmark_name"],
            benchmark_type=spec["benchmark_type"],
            description=spec["description"],
            universe_ref=spec["universe_ref"],
            baseline_strategy_ref=spec["baseline_strategy_ref"],
            rebalance_policy=spec["rebalance_policy"],
            transaction_cost_aware=spec.get("transaction_cost_aware", True),
            slippage_aware=spec.get("slippage_aware", True),
            benchmark_executed=False,
            metric_calculated=False,
            investment_advice_allowed=False,
            non_signal=True,
            manual_review_required=True,
        )
        rows.append(
            {
                "benchmark_name": b.benchmark_name,
                "benchmark_type": b.benchmark_type,
                "description": b.description,
                "universe_ref": b.universe_ref,
                "baseline_strategy_ref": b.baseline_strategy_ref,
                "rebalance_policy": b.rebalance_policy,
                "transaction_cost_aware": b.transaction_cost_aware,
                "slippage_aware": b.slippage_aware,
                "benchmark_executed": b.benchmark_executed,
                "metric_calculated": b.metric_calculated,
                "investment_advice_allowed": b.investment_advice_allowed,
                "non_signal": b.non_signal,
                "manual_review_required": b.manual_review_required,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_oos_benchmark_contracts(df)
    return df, summary


def validate_oos_benchmark_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate single benchmark contract against strict negative invariants."""
    errors = []
    if contract.get("benchmark_executed", False):
        errors.append("benchmark_executed must be False")
    if contract.get("metric_calculated", False):
        errors.append("metric_calculated must be False")
    if contract.get("investment_advice_allowed", False):
        errors.append("investment_advice_allowed must be False")
    return {
        "benchmark_name": contract.get("benchmark_name", "unknown"),
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": True,
    }


def summarize_oos_benchmark_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize benchmark contract registry."""
    return {
        "total_benchmarks": len(df),
        "all_execution_blocked": not bool(df["benchmark_executed"].any()) if not df.empty else True,
        "all_metrics_uncalculated": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "zero_investment_advice": not bool(df["investment_advice_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
