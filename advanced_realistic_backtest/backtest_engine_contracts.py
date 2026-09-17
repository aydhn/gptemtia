# -*- coding: utf-8 -*-
"""Phase 146: Backtest Engine Contracts.

Defines master contract specifications for backtesting engines (event-driven,
vectorized, portfolio, multi-asset, regime-aware, and cost-aware).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

ENGINE_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "local_event_driven_backtest_engine_contract",
        "engine_family": "EVENT_DRIVEN",
        "description": "Zaman damgali bar ve fiyat olaylarina duyarli yerel olay tabanli backtest sozlesmesi.",
        "data_contract_ref": "backtest_point_in_time_data_contract",
        "feature_input_contract_ref": "featurestore_point_in_time_input_contract",
        "signal_input_contract_ref": "abstract_strategy_signal_contract",
        "order_simulation_ref": "simulated_order_handler_contract",
        "transaction_cost_ref": "standard_transaction_cost_contract",
        "slippage_model_ref": "regime_aware_slippage_contract",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "bias_guard_ref": "survivorship_and_snooping_guard",
        "backtest_execution_allowed": False,
        "optimizer_execution_allowed": False,
        "walk_forward_allowed": False,
        "benchmark_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "local_vectorized_backtest_engine_contract",
        "engine_family": "VECTORIZED",
        "description": "Yuksek basarimli matris tabanli, gecikme ve maliyet farkindalikli vektorize sozlesme.",
        "data_contract_ref": "aligned_matrix_data_contract",
        "feature_input_contract_ref": "vectorized_feature_grid_contract",
        "signal_input_contract_ref": "vectorized_signal_weight_contract",
        "order_simulation_ref": "vectorized_rebalance_contract",
        "transaction_cost_ref": "matrix_cost_adjustment_contract",
        "slippage_model_ref": "fixed_bps_slippage_contract",
        "no_lookahead_guard_ref": "lag_one_enforcement_guard",
        "bias_guard_ref": "data_snooping_bias_guard",
        "backtest_execution_allowed": False,
        "optimizer_execution_allowed": False,
        "walk_forward_allowed": False,
        "benchmark_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "portfolio_level_backtest_engine_contract",
        "engine_family": "PORTFOLIO",
        "description": "Coklu varlik portfoy agirliklandirma, sermaye tahsisi ve nakit yonetimi sozlesmesi.",
        "data_contract_ref": "multi_asset_panel_data_contract",
        "feature_input_contract_ref": "cross_asset_feature_contract",
        "signal_input_contract_ref": "target_weight_allocation_contract",
        "order_simulation_ref": "portfolio_rebalance_order_contract",
        "transaction_cost_ref": "portfolio_turnover_cost_contract",
        "slippage_model_ref": "liquidity_based_slippage_contract",
        "no_lookahead_guard_ref": "portfolio_lookahead_guard",
        "bias_guard_ref": "survivorship_bias_guard",
        "backtest_execution_allowed": False,
        "optimizer_execution_allowed": False,
        "walk_forward_allowed": False,
        "benchmark_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "multi_asset_backtest_engine_contract",
        "engine_family": "MULTI_ASSET",
        "description": "Emtia ve Doviz capraz varlik etkilesimlerini modelleyen backtest sozlesmesi.",
        "data_contract_ref": "commodity_fx_aligned_data_contract",
        "feature_input_contract_ref": "cross_asset_aligned_feature_contract",
        "signal_input_contract_ref": "multi_asset_signal_contract",
        "order_simulation_ref": "cross_asset_order_simulation_contract",
        "transaction_cost_ref": "multi_asset_cost_model_contract",
        "slippage_model_ref": "spread_based_slippage_contract",
        "no_lookahead_guard_ref": "cross_asset_timestamp_guard",
        "bias_guard_ref": "overfitting_guard",
        "backtest_execution_allowed": False,
        "optimizer_execution_allowed": False,
        "walk_forward_allowed": False,
        "benchmark_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "regime_aware_backtest_engine_contract",
        "engine_family": "REGIME_AWARE",
        "description": "Phase 126-135 rejim baglamlarina duyarli dinamik maliyet ve kayma backtest sozlesmesi.",
        "data_contract_ref": "regime_matrix_point_in_time_contract",
        "feature_input_contract_ref": "regime_state_input_contract",
        "signal_input_contract_ref": "regime_conditional_signal_contract",
        "order_simulation_ref": "regime_aware_order_simulation_contract",
        "transaction_cost_ref": "regime_variable_cost_contract",
        "slippage_model_ref": "regime_aware_slippage_contract",
        "no_lookahead_guard_ref": "regime_no_lookahead_guard",
        "bias_guard_ref": "regime_overfitting_guard",
        "backtest_execution_allowed": False,
        "optimizer_execution_allowed": False,
        "walk_forward_allowed": False,
        "benchmark_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "cost_aware_backtest_engine_contract",
        "engine_family": "COST_AWARE",
        "description": "Net getiri, komisyon, borsa ucreti ve alis-satis farki etkisini inceleyen maliyet sozlesmesi.",
        "data_contract_ref": "tick_and_bar_cost_data_contract",
        "feature_input_contract_ref": "spread_and_depth_feature_contract",
        "signal_input_contract_ref": "cost_filtered_signal_contract",
        "order_simulation_ref": "cost_adjusted_fill_contract",
        "transaction_cost_ref": "master_transaction_cost_contract",
        "slippage_model_ref": "participation_rate_slippage_contract",
        "no_lookahead_guard_ref": "cost_timestamp_guard",
        "bias_guard_ref": "cost_model_bias_guard",
        "backtest_execution_allowed": False,
        "optimizer_execution_allowed": False,
        "walk_forward_allowed": False,
        "benchmark_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
]


def build_backtest_engine_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of master backtest engine contracts."""
    rows = []
    for c in ENGINE_CONTRACTS:
        rows.append(
            {
                "contract_name": c["contract_name"],
                "engine_family": c["engine_family"],
                "description": c["description"],
                "data_contract_ref": c["data_contract_ref"],
                "feature_input_contract_ref": c["feature_input_contract_ref"],
                "signal_input_contract_ref": c["signal_input_contract_ref"],
                "order_simulation_ref": c["order_simulation_ref"],
                "transaction_cost_ref": c["transaction_cost_ref"],
                "slippage_model_ref": c["slippage_model_ref"],
                "no_lookahead_guard_ref": c["no_lookahead_guard_ref"],
                "bias_guard_ref": c["bias_guard_ref"],
                "backtest_execution_allowed": c["backtest_execution_allowed"],
                "optimizer_execution_allowed": c["optimizer_execution_allowed"],
                "walk_forward_allowed": c["walk_forward_allowed"],
                "benchmark_allowed": c["benchmark_allowed"],
                "live_trading_allowed": c["live_trading_allowed"],
                "broker_execution_allowed": c["broker_execution_allowed"],
                "signal_generation_allowed": c["signal_generation_allowed"],
                "manual_review_required": c["manual_review_required"],
                "local_only": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_engine_contracts(df)
    return df, summary


def validate_backtest_engine_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that an engine contract prohibits execution and preserves safety."""
    issues = []
    if contract.get("backtest_execution_allowed", True):
        issues.append("backtest_execution_allowed must be False")
    if contract.get("live_trading_allowed", True):
        issues.append("live_trading_allowed must be False")
    if contract.get("broker_execution_allowed", True):
        issues.append("broker_execution_allowed must be False")
    if contract.get("optimizer_execution_allowed", True):
        issues.append("optimizer_execution_allowed must be False")
    if contract.get("signal_generation_allowed", True):
        issues.append("signal_generation_allowed must be False")
    return {
        "contract_name": contract.get("contract_name", "UNKNOWN"),
        "is_valid": len(issues) == 0,
        "issues": issues,
    }


def summarize_backtest_engine_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize backtest engine contract registry."""
    return {
        "total_contracts": len(df),
        "engine_families": df["engine_family"].unique().tolist() if not df.empty else [],
        "all_execution_blocked": bool((~df["backtest_execution_allowed"]).all()) if not df.empty else True,
        "all_live_trading_blocked": bool((~df["live_trading_allowed"]).all()) if not df.empty else True,
        "all_broker_blocked": bool((~df["broker_execution_allowed"]).all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
