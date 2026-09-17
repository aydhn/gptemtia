# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Robustness Contracts Module.

Defines the master suite of robustness contracts across resampling, bootstrap,
parameter perturbation, and stress linkages with zero execution permitted.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    ROBUSTNESS_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

CORE_ROBUSTNESS_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "local_monte_carlo_robustness_contract",
        "robustness_family": "local_offline_envelope",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "Baseline contract establishing overall envelope boundaries for local robustness evaluation.",
    },
    {
        "contract_name": "bootstrap_robustness_contract",
        "robustness_family": "standard_iid_bootstrap",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "IID return resampling contract under unconditioned distribution assumptions.",
    },
    {
        "contract_name": "block_bootstrap_robustness_contract",
        "robustness_family": "block_bootstrap_autocorrelation_preserving",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "Moving block bootstrap contract preserving volatility clustering and temporal autocorrelation.",
    },
    {
        "contract_name": "trade_sequence_reshuffle_contract",
        "robustness_family": "trade_order_permutation",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "Trade sequence permutation contract measuring equity path dependency and sequence risk.",
    },
    {
        "contract_name": "return_path_resampling_contract",
        "robustness_family": "path_resampling",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "Resampled return series contract identifying drawdown distribution quantiles without lookahead.",
    },
    {
        "contract_name": "parameter_perturbation_robustness_contract",
        "robustness_family": "parameter_neighborhood_stability",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "Hyperparameter neighborhood perturbation contract testing for overfitted razor-thin optima.",
    },
    {
        "contract_name": "stress_linked_monte_carlo_contract",
        "robustness_family": "crisis_scenario_resampling",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "Joint contract linking Monte Carlo resampling with Phase 148 historical and hypothetical stress shocks.",
    },
    {
        "contract_name": "walk_forward_linked_monte_carlo_contract",
        "robustness_family": "out_of_sample_resampling",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "OOS validation window resampling contract benchmarking roll-forward performance stability.",
    },
    {
        "contract_name": "cost_slippage_aware_monte_carlo_contract",
        "robustness_family": "frictional_decay_resampling",
        "realistic_backtest_ref": "PHASE_146_REALISTIC_BACKTEST_V1",
        "walk_forward_ref": "PHASE_147_WALK_FORWARD_V1",
        "stress_testing_ref": "PHASE_148_STRESS_TESTING_V1",
        "transaction_cost_ref": "PHASE_146_TIERED_COST_MODEL",
        "slippage_model_ref": "PHASE_146_SQUARE_ROOT_SLIPPAGE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "no_lookahead_guard_ref": "GUARD_NO_LOOKAHEAD_149_01",
        "resampling_leakage_guard_ref": "GUARD_RESAMPLING_LEAKAGE_149_02",
        "description": "Friction-adjusted resampling contract compounding variable spreads and non-linear market impact.",
    },
]


def validate_monte_carlo_robustness_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that a single contract satisfies all safety conditions."""
    required_keys = [
        "contract_name",
        "robustness_family",
        "realistic_backtest_ref",
        "walk_forward_ref",
        "stress_testing_ref",
        "transaction_cost_ref",
        "slippage_model_ref",
        "regime_context_ref",
        "no_lookahead_guard_ref",
        "resampling_leakage_guard_ref",
    ]
    for k in required_keys:
        if k not in contract or not contract[k]:
            return {"valid": False, "reason": f"Missing required contract key: {k}"}

    # Verify execution prohibition invariants
    prohibited_flags = [
        "monte_carlo_execution_allowed",
        "bootstrap_execution_allowed",
        "resampling_execution_allowed",
        "metric_calculation_allowed",
        "optimizer_execution_allowed",
        "parameter_optimization_allowed",
        "live_trading_allowed",
        "broker_execution_allowed",
        "signal_generation_allowed",
    ]
    for flag in prohibited_flags:
        if contract.get(flag, False) is True:
            return {"valid": False, "reason": f"Prohibited execution flag enabled: {flag}"}

    return {"valid": True, "reason": "Contract satisfies all local research invariants."}


def summarize_monte_carlo_robustness_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the robustness contracts DataFrame."""
    all_valid = True
    for _, row in df.iterrows():
        res = validate_monte_carlo_robustness_contract(row.to_dict())
        if not res["valid"]:
            all_valid = False
            break

    return {
        "domain": ROBUSTNESS_CONTRACT_DOMAIN,
        "total_contracts": len(df),
        "all_contracts_valid": all_valid,
        "all_executions_blocked": bool(
            (~df["monte_carlo_execution_allowed"]).all()
            and (~df["bootstrap_execution_allowed"]).all()
            and (~df["resampling_execution_allowed"]).all()
            and (~df["live_trading_allowed"]).all()
            and (~df["broker_execution_allowed"]).all()
        ),
        "status": MONTE_CARLO_CONTRACT_READY if all_valid else "BLOCKED",
    }


def build_monte_carlo_robustness_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the master Monte Carlo robustness contract registry."""
    rows: List[Dict[str, Any]] = []
    for c in CORE_ROBUSTNESS_CONTRACTS:
        rows.append(
            {
                "contract_name": c["contract_name"],
                "robustness_family": c["robustness_family"],
                "realistic_backtest_ref": c["realistic_backtest_ref"],
                "walk_forward_ref": c["walk_forward_ref"],
                "stress_testing_ref": c["stress_testing_ref"],
                "transaction_cost_ref": c["transaction_cost_ref"],
                "slippage_model_ref": c["slippage_model_ref"],
                "regime_context_ref": c["regime_context_ref"],
                "no_lookahead_guard_ref": c["no_lookahead_guard_ref"],
                "resampling_leakage_guard_ref": c["resampling_leakage_guard_ref"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "monte_carlo_execution_allowed": False,
                "bootstrap_execution_allowed": False,
                "resampling_execution_allowed": False,
                "metric_calculation_allowed": False,
                "optimizer_execution_allowed": False,
                "parameter_optimization_allowed": False,
                "live_trading_allowed": False,
                "broker_execution_allowed": False,
                "signal_generation_allowed": False,
                "manual_review_required": True,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": ROBUSTNESS_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_monte_carlo_robustness_contracts(df)
    return df, summary
