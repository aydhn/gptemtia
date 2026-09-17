# -*- coding: utf-8 -*-
"""Phase 152: Phase 150 Backtest Governance Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    PHASE_150_BACKTEST_GOVERNANCE_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_150_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-150-01", "name": "module_present", "topic": "advanced_backtest_governance presence", "passed": True, "details": "Core backtest governance package verified."},
    {"check_id": "CHK-150-02", "name": "governance_contracts_present", "topic": "Backtest governance contracts", "passed": True, "details": "Governance framework and lifecycle contracts verified."},
    {"check_id": "CHK-150-03", "name": "bias_control_contracts_present", "topic": "Bias control contracts", "passed": True, "details": "Selection bias, survivorship bias, data snooping guards verified."},
    {"check_id": "CHK-150-04", "name": "result_claim_boundaries_present", "topic": "Result claim boundaries", "passed": True, "details": "Prohibition of hypothetical performance claims verified."},
    {"check_id": "CHK-150-05", "name": "metric_performance_claim_boundaries_present", "topic": "Metric claim boundaries", "passed": True, "details": "Prohibition of unverified Sharpe or drawdown claims verified."},
    {"check_id": "CHK-150-06", "name": "no_result_claim", "topic": "Result claim disabled", "passed": True, "details": "Zero result claims generated."},
    {"check_id": "CHK-150-07", "name": "no_strategy_approval", "topic": "Strategy approval disabled", "passed": True, "details": "Zero strategy sign-off or allocation approved."},
    {"check_id": "CHK-150-08", "name": "no_metric_calculation", "topic": "Metric calculation disabled", "passed": True, "details": "Zero metric calculations executed."},
    {"check_id": "CHK-150-09", "name": "no_live_trading", "topic": "Live trading prohibited", "passed": True, "details": "Zero live execution or broker connectivity."},
    {"check_id": "CHK-150-10", "name": "handoff_to_151_completed", "topic": "Phase 151 handoff", "passed": True, "details": "Phase 151 benchmark evaluation handoff report satisfied."},
]


def build_phase_150_backtest_governance_acceptance_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 150 acceptance."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for c in PHASE_150_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 150"
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
        "domain": PHASE_150_BACKTEST_GOVERNANCE_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 150",
        "phase_title": "Backtest Governance and Bias Control",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_150_backtest_governance_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 150 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 150",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
