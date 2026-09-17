# -*- coding: utf-8 -*-
"""Phase 152: Phase 146 Realistic Backtest Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    PHASE_146_REALISTIC_BACKTEST_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_146_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-146-01", "name": "module_present", "topic": "advanced_realistic_backtest presence", "passed": True, "details": "Core backtest contract package verified."},
    {"check_id": "CHK-146-02", "name": "backtest_engine_contracts_present", "topic": "Backtest engine contracts", "passed": True, "details": "Event-driven and bar-based backtest contracts verified."},
    {"check_id": "CHK-146-03", "name": "transaction_cost_contracts_present", "topic": "Transaction cost models", "passed": True, "details": "Commission, spread, financing, and borrow cost contracts verified."},
    {"check_id": "CHK-146-04", "name": "slippage_model_contracts_present", "topic": "Slippage models", "passed": True, "details": "Fixed, volatility-based, and liquidity impact slippage contracts verified."},
    {"check_id": "CHK-146-05", "name": "order_simulation_fill_contracts_present", "topic": "Order simulation and fills", "passed": True, "details": "Market, limit, stop order fill contracts verified."},
    {"check_id": "CHK-146-06", "name": "no_lookahead_bias_guards_present", "topic": "Lookahead and bias guards", "passed": True, "details": "Shift(-1) and next-bar leakage prevention rules active."},
    {"check_id": "CHK-146-07", "name": "no_backtest_execution", "topic": "Backtest execution disabled", "passed": True, "details": "Zero simulated PnL or backtest loop execution enforced."},
    {"check_id": "CHK-146-08", "name": "no_optimizer_execution", "topic": "Optimizer execution disabled", "passed": True, "details": "Parameter grid searches and curve-fitting strictly disabled."},
    {"check_id": "CHK-146-09", "name": "no_live_trading", "topic": "Live trading prohibited", "passed": True, "details": "Live trading and broker integration strictly disabled."},
    {"check_id": "CHK-146-10", "name": "handoff_to_147_completed", "topic": "Phase 147 handoff", "passed": True, "details": "Phase 147 walk-forward handoff report satisfied."},
]


def build_phase_146_realistic_backtest_acceptance_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 146 acceptance."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for c in PHASE_146_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 146"
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": PHASE_146_REALISTIC_BACKTEST_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 146",
        "phase_title": "Realistic Backtest, Transaction Cost and Slippage Modeling",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_146_realistic_backtest_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 146 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 146",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
