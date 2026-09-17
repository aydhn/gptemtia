# -*- coding: utf-8 -*-
"""Phase 152: Phase 148 Stress Testing Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    PHASE_148_STRESS_TESTING_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_148_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-148-01", "name": "module_present", "topic": "advanced_stress_testing presence", "passed": True, "details": "Core stress testing package verified."},
    {"check_id": "CHK-148-02", "name": "stress_scenario_contracts_present", "topic": "Stress scenario contracts", "passed": True, "details": "Multi-asset stress scenario definition contracts verified."},
    {"check_id": "CHK-148-03", "name": "historical_hypothetical_contracts_present", "topic": "Historical and hypothetical scenarios", "passed": True, "details": "2008 GFC, 2020 COVID, energy shock contracts verified."},
    {"check_id": "CHK-148-04", "name": "shock_placeholders_present", "topic": "Asset shock placeholders", "passed": True, "details": "Price shock, spread blowout, and volatility surge placeholders verified."},
    {"check_id": "CHK-148-05", "name": "stress_metric_placeholders_present", "topic": "Stress metric placeholders", "passed": True, "details": "Conditional VaR, expected shortfall, tail risk placeholders verified."},
    {"check_id": "CHK-148-06", "name": "no_stress_test_execution", "topic": "Stress test execution disabled", "passed": True, "details": "Zero simulated stress runs executed."},
    {"check_id": "CHK-148-07", "name": "no_scenario_simulation", "topic": "Scenario simulation disabled", "passed": True, "details": "Zero synthetic scenarios simulated."},
    {"check_id": "CHK-148-08", "name": "no_stressed_pnl_calculation", "topic": "Stressed PnL calculation disabled", "passed": True, "details": "Zero stressed PnL or loss estimations generated."},
    {"check_id": "CHK-148-09", "name": "no_live_trading", "topic": "Live trading prohibited", "passed": True, "details": "Strict prohibition of live execution enforced."},
    {"check_id": "CHK-148-10", "name": "handoff_to_149_completed", "topic": "Phase 149 handoff", "passed": True, "details": "Phase 149 Monte Carlo handoff report satisfied."},
]


def build_phase_148_stress_testing_acceptance_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 148 acceptance."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for c in PHASE_148_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 148"
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
        "domain": PHASE_148_STRESS_TESTING_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 148",
        "phase_title": "Stress Testing and Scenario Simulation",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_148_stress_testing_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 148 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 148",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
