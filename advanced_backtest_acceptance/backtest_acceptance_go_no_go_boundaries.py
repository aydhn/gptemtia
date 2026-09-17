# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Go / No-Go Boundaries."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    GO_NO_GO_BOUNDARY_DOMAIN,
    GO_CONTRACT_ONLY,
    NO_GO_LIVE_TRADING,
    NO_GO_BROKER_EXECUTION,
    NO_GO_BACKTEST_EXECUTION,
    NO_GO_BENCHMARK_EXECUTION,
    NO_GO_METRIC_CALCULATION,
    NO_GO_STRATEGY_APPROVAL,
    NO_GO_PORTFOLIO_CONSTRUCTION,
    NO_GO_POSITION_SIZING,
    NO_GO_OPTIMIZER,
    NO_GO_MODEL_TRAINING,
    NO_GO_PREDICTION,
    NO_GO_DEPLOYMENT,
)

GO_CONDITIONS: List[Dict[str, Any]] = [
    {"action": "proceed_to_phase_153_portfolio_construction_contracts", "decision": "GO", "boundary_label": GO_CONTRACT_ONLY, "reason": "Authorized: Non-live Phase 153 contract development."},
    {"action": "proceed_to_position_sizing_contract_design", "decision": "GO", "boundary_label": GO_CONTRACT_ONLY, "reason": "Authorized: Conceptual position sizing model specification."},
    {"action": "proceed_to_risk_budgeting_contract_design", "decision": "GO", "boundary_label": GO_CONTRACT_ONLY, "reason": "Authorized: Risk budgeting and volatility allocation contract design."},
    {"action": "proceed_to_non_live_portfolio_boundary_design", "decision": "GO", "boundary_label": GO_CONTRACT_ONLY, "reason": "Authorized: Defining safety gates for portfolio modeling."},
]

NO_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"action": "live_trading", "decision": "NO_GO", "boundary_label": NO_GO_LIVE_TRADING, "reason": "Prohibited: Live order generation is strictly forbidden."},
    {"action": "broker_execution", "decision": "NO_GO", "boundary_label": NO_GO_BROKER_EXECUTION, "reason": "Prohibited: Real broker API integration is strictly forbidden."},
    {"action": "investment_advice", "decision": "NO_GO", "boundary_label": NO_GO_LIVE_TRADING, "reason": "Prohibited: Investment advice and financial recommendations are forbidden."},
    {"action": "signal_generation", "decision": "NO_GO", "boundary_label": NO_GO_LIVE_TRADING, "reason": "Prohibited: Producing directional buy/sell signals is forbidden."},
    {"action": "backtest_execution", "decision": "NO_GO", "boundary_label": NO_GO_BACKTEST_EXECUTION, "reason": "Prohibited: Executing real backtest simulation loops is forbidden."},
    {"action": "benchmark_execution", "decision": "NO_GO", "boundary_label": NO_GO_BENCHMARK_EXECUTION, "reason": "Prohibited: Executing real benchmark comparisons is forbidden."},
    {"action": "metric_calculation", "decision": "NO_GO", "boundary_label": NO_GO_METRIC_CALCULATION, "reason": "Prohibited: Calculating actual performance metrics is forbidden."},
    {"action": "result_claim", "decision": "NO_GO", "boundary_label": NO_GO_BACKTEST_EXECUTION, "reason": "Prohibited: Generating backtest result or return claims is forbidden."},
    {"action": "performance_claim", "decision": "NO_GO", "boundary_label": NO_GO_BACKTEST_EXECUTION, "reason": "Prohibited: Claiming trading performance or profitability is forbidden."},
    {"action": "strategy_approval", "decision": "NO_GO", "boundary_label": NO_GO_STRATEGY_APPROVAL, "reason": "Prohibited: Approving strategies for real trading is forbidden."},
    {"action": "capital_allocation", "decision": "NO_GO", "boundary_label": NO_GO_PORTFOLIO_CONSTRUCTION, "reason": "Prohibited: Allocating real or simulated capital is forbidden in this phase."},
    {"action": "portfolio_construction", "decision": "NO_GO", "boundary_label": NO_GO_PORTFOLIO_CONSTRUCTION, "reason": "Prohibited: Real portfolio construction is forbidden in this acceptance phase."},
    {"action": "position_sizing", "decision": "NO_GO", "boundary_label": NO_GO_POSITION_SIZING, "reason": "Prohibited: Executing real position sizing is forbidden in this phase."},
    {"action": "optimizer_execution", "decision": "NO_GO", "boundary_label": NO_GO_OPTIMIZER, "reason": "Prohibited: Running optimization or parameter fitting is forbidden."},
    {"action": "model_training", "decision": "NO_GO", "boundary_label": NO_GO_MODEL_TRAINING, "reason": "Prohibited: ML model fitting and training are forbidden."},
    {"action": "prediction", "decision": "NO_GO", "boundary_label": NO_GO_PREDICTION, "reason": "Prohibited: Model inference and forward predictions are forbidden."},
    {"action": "deployment", "decision": "NO_GO", "boundary_label": NO_GO_DEPLOYMENT, "reason": "Prohibited: Production or broker deployment is forbidden."},
    {"action": "model_registry_write", "decision": "NO_GO", "boundary_label": NO_GO_DEPLOYMENT, "reason": "Prohibited: Writing model artifacts to registry is forbidden."},
]


def build_backtest_acceptance_go_no_go_boundary_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Go/No-Go boundary conditions."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for g in GO_CONDITIONS:
        records.append({
            "action": g["action"],
            "decision": g["decision"],
            "boundary_label": g["boundary_label"],
            "reason": g["reason"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })
    for ng in NO_GO_CONDITIONS:
        records.append({
            "action": ng["action"],
            "decision": ng["decision"],
            "boundary_label": ng["boundary_label"],
            "reason": ng["reason"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": GO_NO_GO_BOUNDARY_DOMAIN,
        "active_profile": active.profile_name,
        "total_rules": len(records),
        "go_count": len(GO_CONDITIONS),
        "no_go_count": len(NO_GO_CONDITIONS),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def validate_backtest_acceptance_go_no_go_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate an action request against the Go/No-Go boundary policy."""
    action = request if isinstance(request, str) else request.get("action", "")
    action_clean = action.strip().lower()

    for ng in NO_GO_CONDITIONS:
        if ng["action"].lower() == action_clean or action_clean in ng["action"].lower():
            return {
                "action": action,
                "decision": "NO_GO",
                "boundary_label": ng["boundary_label"],
                "allowed": False,
                "reason": ng["reason"],
                "non_signal": True,
            }

    for g in GO_CONDITIONS:
        if g["action"].lower() == action_clean or action_clean in g["action"].lower():
            return {
                "action": action,
                "decision": "GO",
                "boundary_label": g["boundary_label"],
                "allowed": True,
                "reason": g["reason"],
                "non_signal": True,
            }

    # Default unrecognized action to NO_GO for safety
    return {
        "action": action,
        "decision": "NO_GO",
        "boundary_label": "no_go_unknown",
        "allowed": False,
        "reason": f"Action '{action}' is unrecognized and blocked by safety policy.",
        "non_signal": True,
    }
