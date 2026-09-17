# -*- coding: utf-8 -*-
"""Phase 148: Stress Scenario Contracts.

Provides specifications and registry for core stress scenario contracts,
ensuring strict contract-only mode with zero live execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressScenarioContract

STRESS_SCENARIO_SPECS: List[Dict[str, Any]] = [
    {
        "contract_name": "local_stress_testing_contract",
        "scenario_family": "LOCAL_GENERIC",
        "description": "Yerel genel stres testi sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
    {
        "contract_name": "historical_scenario_contract",
        "scenario_family": "HISTORICAL_CRISIS",
        "description": "Tarihsel kriz donemleri simülasyon sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
    {
        "contract_name": "hypothetical_scenario_contract",
        "scenario_family": "HYPOTHETICAL_SHOCK",
        "description": "Varsayimsal makro ve jeopolitik kriz sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
    {
        "contract_name": "regime_shock_contract",
        "scenario_family": "REGIME_TRANSITION",
        "description": "Ani rejim degisimi ve kirilma soku sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
    {
        "contract_name": "volatility_shock_contract",
        "scenario_family": "VOLATILITY_EXPANSION",
        "description": "Ani volatilite genislemesi ve patlamasi sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
    {
        "contract_name": "liquidity_shock_contract",
        "scenario_family": "LIQUIDITY_DROUGHT",
        "description": "Derinlik kaybi ve likidite kurakligi sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
    {
        "contract_name": "spread_widening_contract",
        "scenario_family": "SPREAD_DISRUPTION",
        "description": "Asiri spread genislemesi ve alis-satis sok sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
    {
        "contract_name": "cross_asset_contagion_contract",
        "scenario_family": "CONTAGION_SPREAD",
        "description": "Varliklar arasi kriz bulasma sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
    {
        "contract_name": "cost_slippage_shock_contract",
        "scenario_family": "EXECUTION_FRICTION",
        "description": "Stresli maliyet ve katastrofik kayma sozlesmesi.",
        "realistic_backtest_ref": "realistic_backtest_engine_v1",
        "walk_forward_ref": "walk_forward_engine_v1",
        "transaction_cost_ref": "cost_model_v1",
        "slippage_model_ref": "slippage_model_v1",
        "regime_context_ref": "regime_context_v1",
        "no_lookahead_guard_ref": "strict_no_lookahead_guard",
        "scenario_leakage_guard_ref": "strict_scenario_leakage_guard",
    },
]


def build_stress_scenario_contract_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of all stress scenario contracts."""
    rows: List[Dict[str, Any]] = []
    for spec in STRESS_SCENARIO_SPECS:
        contract = StressScenarioContract(
            contract_name=spec["contract_name"],
            scenario_family=spec["scenario_family"],
            description=spec["description"],
            realistic_backtest_ref=spec["realistic_backtest_ref"],
            walk_forward_ref=spec["walk_forward_ref"],
            transaction_cost_ref=spec["transaction_cost_ref"],
            slippage_model_ref=spec["slippage_model_ref"],
            regime_context_ref=spec["regime_context_ref"],
            no_lookahead_guard_ref=spec["no_lookahead_guard_ref"],
            scenario_leakage_guard_ref=spec["scenario_leakage_guard_ref"],
            stress_execution_allowed=False,
            scenario_simulation_allowed=False,
            metric_calculation_allowed=False,
            optimizer_execution_allowed=False,
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
                "scenario_family": contract.scenario_family,
                "description": contract.description,
                "realistic_backtest_ref": contract.realistic_backtest_ref,
                "walk_forward_ref": contract.walk_forward_ref,
                "transaction_cost_ref": contract.transaction_cost_ref,
                "slippage_model_ref": contract.slippage_model_ref,
                "regime_context_ref": contract.regime_context_ref,
                "no_lookahead_guard_ref": contract.no_lookahead_guard_ref,
                "scenario_leakage_guard_ref": contract.scenario_leakage_guard_ref,
                "stress_execution_allowed": contract.stress_execution_allowed,
                "scenario_simulation_allowed": contract.scenario_simulation_allowed,
                "metric_calculation_allowed": contract.metric_calculation_allowed,
                "optimizer_execution_allowed": contract.optimizer_execution_allowed,
                "live_trading_allowed": contract.live_trading_allowed,
                "broker_execution_allowed": contract.broker_execution_allowed,
                "signal_generation_allowed": contract.signal_generation_allowed,
                "manual_review_required": contract.manual_review_required,
                "non_signal": contract.non_signal,
                "local_only": contract.local_only,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_stress_scenario_contracts(df)
    return df, summary


def validate_stress_scenario_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single stress scenario contract."""
    errors = []
    if contract.get("stress_execution_allowed", False):
        errors.append("stress_execution_allowed must be False")
    if contract.get("scenario_simulation_allowed", False):
        errors.append("scenario_simulation_allowed must be False")
    if contract.get("optimizer_execution_allowed", False):
        errors.append("optimizer_execution_allowed must be False")
    if contract.get("live_trading_allowed", False):
        errors.append("live_trading_allowed must be False")
    if contract.get("broker_execution_allowed", False):
        errors.append("broker_execution_allowed must be False")
    if contract.get("metric_calculation_allowed", False):
        errors.append("metric_calculation_allowed must be False")
    if contract.get("signal_generation_allowed", False):
        errors.append("signal_generation_allowed must be False")
    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": True,
    }


def summarize_stress_scenario_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize stress scenario contract registry."""
    return {
        "total_contracts": len(df),
        "all_stress_execution_blocked": not bool(df["stress_execution_allowed"].any()) if not df.empty else True,
        "all_scenario_simulation_blocked": not bool(df["scenario_simulation_allowed"].any()) if not df.empty else True,
        "all_optimizer_blocked": not bool(df["optimizer_execution_allowed"].any()) if not df.empty else True,
        "all_live_trading_blocked": not bool(df["live_trading_allowed"].any()) if not df.empty else True,
        "all_broker_blocked": not bool(df["broker_execution_allowed"].any()) if not df.empty else True,
        "all_metric_calculation_blocked": not bool(df["metric_calculation_allowed"].any()) if not df.empty else True,
        "all_signal_generation_blocked": not bool(df["signal_generation_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
