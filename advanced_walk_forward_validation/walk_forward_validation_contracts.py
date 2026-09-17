# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Validation Contracts.

Provides specifications and registry for walk-forward validation strategies,
ensuring strict contract-only mode with zero live execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import WalkForwardValidationContract

VALIDATION_CONTRACT_SPECS: List[Dict[str, Any]] = [
    {
        "contract_name": "local_walk_forward_validation_contract",
        "validation_family": "LOCAL_GENERIC",
        "description": "Yerel genel walk-forward zaman serisi dogrulama sozlesmesi.",
        "data_contract_ref": "data_contract_v1",
        "feature_input_contract_ref": "feature_input_contract_v1",
        "signal_input_contract_ref": "signal_input_contract_v1",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "split_policy_ref": "rolling_window_policy_v1",
        "embargo_policy_ref": "standard_embargo_policy_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "bias_guard_ref": "comprehensive_bias_guard",
    },
    {
        "contract_name": "rolling_walk_forward_validation_contract",
        "validation_family": "ROLLING_WINDOW",
        "description": "Sabit uzunluklu kayan pencere dogrulama sozlesmesi.",
        "data_contract_ref": "data_contract_v1",
        "feature_input_contract_ref": "feature_input_contract_v1",
        "signal_input_contract_ref": "signal_input_contract_v1",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "split_policy_ref": "rolling_window_split_policy",
        "embargo_policy_ref": "rolling_embargo_policy",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "bias_guard_ref": "comprehensive_bias_guard",
    },
    {
        "contract_name": "expanding_walk_forward_validation_contract",
        "validation_family": "EXPANDING_WINDOW",
        "description": "Gecmisi biriktirerek buyuyen genisleyen pencere dogrulama sozlesmesi.",
        "data_contract_ref": "data_contract_v1",
        "feature_input_contract_ref": "feature_input_contract_v1",
        "signal_input_contract_ref": "signal_input_contract_v1",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "split_policy_ref": "expanding_window_split_policy",
        "embargo_policy_ref": "expanding_embargo_policy",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "bias_guard_ref": "comprehensive_bias_guard",
    },
    {
        "contract_name": "anchored_walk_forward_validation_contract",
        "validation_family": "ANCHORED_WINDOW",
        "description": "Sabit t0 baslangicli capalanmis pencere dogrulama sozlesmesi.",
        "data_contract_ref": "data_contract_v1",
        "feature_input_contract_ref": "feature_input_contract_v1",
        "signal_input_contract_ref": "signal_input_contract_v1",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "split_policy_ref": "anchored_window_split_policy",
        "embargo_policy_ref": "anchored_embargo_policy",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "bias_guard_ref": "comprehensive_bias_guard",
    },
    {
        "contract_name": "purged_embargo_walk_forward_validation_contract",
        "validation_family": "PURGED_EMBARGO",
        "description": "Etiket cakismasini ve otoregresif sizintiyi onleyen purged-embargo sozlesmesi.",
        "data_contract_ref": "data_contract_v1",
        "feature_input_contract_ref": "feature_input_contract_v1",
        "signal_input_contract_ref": "signal_input_contract_v1",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "split_policy_ref": "purged_split_policy",
        "embargo_policy_ref": "strict_embargo_policy",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "bias_guard_ref": "comprehensive_bias_guard",
    },
    {
        "contract_name": "regime_aware_walk_forward_validation_contract",
        "validation_family": "REGIME_AWARE",
        "description": "Rejim gecislerine ve piyasa durumlarina duyarlastirilmis dogrulama sozlesmesi.",
        "data_contract_ref": "data_contract_v1",
        "feature_input_contract_ref": "feature_input_contract_v1",
        "signal_input_contract_ref": "signal_input_contract_v1",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "split_policy_ref": "regime_aware_split_policy",
        "embargo_policy_ref": "regime_conditioned_embargo_policy",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "bias_guard_ref": "comprehensive_bias_guard",
    },
    {
        "contract_name": "cost_aware_walk_forward_validation_contract",
        "validation_family": "COST_AWARE",
        "description": "Islem maliyeti ve kayma modeli entegrasyonlu OOS dogrulama sozlesmesi.",
        "data_contract_ref": "data_contract_v1",
        "feature_input_contract_ref": "feature_input_contract_v1",
        "signal_input_contract_ref": "signal_input_contract_v1",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "split_policy_ref": "cost_aware_split_policy",
        "embargo_policy_ref": "cost_aware_embargo_policy",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "bias_guard_ref": "comprehensive_bias_guard",
    },
]


def build_walk_forward_validation_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for walk-forward validation contracts."""
    rows = []
    for spec in VALIDATION_CONTRACT_SPECS:
        contract = WalkForwardValidationContract(
            contract_name=spec["contract_name"],
            validation_family=spec["validation_family"],
            description=spec["description"],
            data_contract_ref=spec["data_contract_ref"],
            feature_input_contract_ref=spec["feature_input_contract_ref"],
            signal_input_contract_ref=spec["signal_input_contract_ref"],
            realistic_backtest_ref=spec["realistic_backtest_ref"],
            transaction_cost_ref=spec["transaction_cost_ref"],
            slippage_model_ref=spec["slippage_model_ref"],
            split_policy_ref=spec["split_policy_ref"],
            embargo_policy_ref=spec["embargo_policy_ref"],
            no_lookahead_guard_ref=spec["no_lookahead_guard_ref"],
            bias_guard_ref=spec["bias_guard_ref"],
            walk_forward_execution_allowed=False,
            optimizer_execution_allowed=False,
            benchmark_execution_allowed=False,
            metric_calculation_allowed=False,
            live_trading_allowed=False,
            broker_execution_allowed=False,
            signal_generation_allowed=False,
            manual_review_required=True,
            non_signal=True,
            local_only=True,
        )
        rows.append(
            {
                "contract_name": contract.contract_name,
                "validation_family": contract.validation_family,
                "description": contract.description,
                "data_contract_ref": contract.data_contract_ref,
                "feature_input_contract_ref": contract.feature_input_contract_ref,
                "signal_input_contract_ref": contract.signal_input_contract_ref,
                "realistic_backtest_ref": contract.realistic_backtest_ref,
                "transaction_cost_ref": contract.transaction_cost_ref,
                "slippage_model_ref": contract.slippage_model_ref,
                "split_policy_ref": contract.split_policy_ref,
                "embargo_policy_ref": contract.embargo_policy_ref,
                "no_lookahead_guard_ref": contract.no_lookahead_guard_ref,
                "bias_guard_ref": contract.bias_guard_ref,
                "walk_forward_execution_allowed": contract.walk_forward_execution_allowed,
                "optimizer_execution_allowed": contract.optimizer_execution_allowed,
                "benchmark_execution_allowed": contract.benchmark_execution_allowed,
                "metric_calculation_allowed": contract.metric_calculation_allowed,
                "live_trading_allowed": contract.live_trading_allowed,
                "broker_execution_allowed": contract.broker_execution_allowed,
                "signal_generation_allowed": contract.signal_generation_allowed,
                "manual_review_required": contract.manual_review_required,
                "non_signal": contract.non_signal,
                "local_only": contract.local_only,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_walk_forward_validation_contracts(df)
    return df, summary


def validate_walk_forward_validation_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single walk-forward validation contract."""
    errors = []
    if contract.get("walk_forward_execution_allowed", False):
        errors.append("walk_forward_execution_allowed must be False")
    if contract.get("optimizer_execution_allowed", False):
        errors.append("optimizer_execution_allowed must be False")
    if contract.get("live_trading_allowed", False):
        errors.append("live_trading_allowed must be False")
    if contract.get("broker_execution_allowed", False):
        errors.append("broker_execution_allowed must be False")
    if contract.get("metric_calculation_allowed", False):
        errors.append("metric_calculation_allowed must be False")
    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": True,
    }


def summarize_walk_forward_validation_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize walk-forward validation contract registry."""
    return {
        "total_contracts": len(df),
        "all_execution_blocked": not bool(df["walk_forward_execution_allowed"].any()) if not df.empty else True,
        "all_optimizer_blocked": not bool(df["optimizer_execution_allowed"].any()) if not df.empty else True,
        "all_live_trading_blocked": not bool(df["live_trading_allowed"].any()) if not df.empty else True,
        "all_broker_blocked": not bool(df["broker_execution_allowed"].any()) if not df.empty else True,
        "all_metric_calculation_blocked": not bool(df["metric_calculation_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
