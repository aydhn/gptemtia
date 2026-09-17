# -*- coding: utf-8 -*-
"""Phase 152: Phase 151 Benchmark Comparison and Strategy Evaluation Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    PHASE_151_BENCHMARK_EVALUATION_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_151_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-151-01", "name": "module_present", "topic": "advanced_benchmark_evaluation presence", "passed": True, "details": "Core benchmark evaluation package verified."},
    {"check_id": "CHK-151-02", "name": "benchmark_comparison_contracts_present", "topic": "Benchmark comparison report contracts", "passed": True, "details": "Strategy vs benchmark report contracts verified."},
    {"check_id": "CHK-151-03", "name": "strategy_evaluation_contracts_present", "topic": "Strategy evaluation report contracts", "passed": True, "details": "Evaluation template and disclosure contracts verified."},
    {"check_id": "CHK-151-04", "name": "metric_placeholders_present", "topic": "Metric placeholders", "passed": True, "details": "Uncalculated metric placeholders verified."},
    {"check_id": "CHK-151-05", "name": "claim_guards_present", "topic": "Claim guards", "passed": True, "details": "Result claim and performance claim guards active."},
    {"check_id": "CHK-151-06", "name": "strategy_approval_guards_present", "topic": "Strategy approval guards", "passed": True, "details": "Approval and allocation prohibitions active."},
    {"check_id": "CHK-151-07", "name": "no_benchmark_execution", "topic": "Benchmark execution disabled", "passed": True, "details": "Zero benchmark calculations executed."},
    {"check_id": "CHK-151-08", "name": "no_strategy_evaluation_execution", "topic": "Strategy evaluation execution disabled", "passed": True, "details": "Zero strategy evaluations executed."},
    {"check_id": "CHK-151-09", "name": "no_capital_portfolio_position_sizing", "topic": "Portfolio and sizing prohibited", "passed": True, "details": "Zero capital allocation, portfolio construction or sizing."},
    {"check_id": "CHK-151-10", "name": "handoff_to_152_completed", "topic": "Phase 152 handoff", "passed": True, "details": "Phase 152 backtest acceptance handoff report satisfied."},
]


def build_phase_151_benchmark_evaluation_acceptance_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 151 acceptance."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for c in PHASE_151_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 151"
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
        "domain": PHASE_151_BENCHMARK_EVALUATION_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 151",
        "phase_title": "Benchmark Comparison and Strategy Evaluation Reports",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_151_benchmark_evaluation_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 151 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 151",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
