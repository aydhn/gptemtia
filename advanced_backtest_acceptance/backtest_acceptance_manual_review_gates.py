# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Manual Review Gates."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    MANUAL_REVIEW_GATE_DOMAIN,
    ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
)

REVIEW_GATES: List[Dict[str, Any]] = [
    {
        "gate_id": "GATE-146",
        "gate_name": "phase_146_realistic_backtest_review_gate",
        "phase_ref": "Phase 146",
        "topic": "Realistic backtest cost and slippage models",
        "review_requirement": "Verify transaction cost and slippage parameters reflect realistic assumptions.",
        "action_required": "Operator must confirm spread, fee, and slippage specifications prior to research evaluation.",
    },
    {
        "gate_id": "GATE-147",
        "gate_name": "phase_147_walk_forward_oos_review_gate",
        "phase_ref": "Phase 147",
        "topic": "Walk-forward validation and out-of-sample partitioning",
        "review_requirement": "Verify temporal split boundaries, anchoring, and purge/embargo windows.",
        "action_required": "Operator must inspect split definitions to ensure zero leakage across validation folds.",
    },
    {
        "gate_id": "GATE-148",
        "gate_name": "phase_148_stress_testing_review_gate",
        "phase_ref": "Phase 148",
        "topic": "Stress testing scenarios and crisis shocks",
        "review_requirement": "Verify stress scenario parameters match intended macro/commodity shock regimes.",
        "action_required": "Operator review of shock definitions and extreme tail risk contracts.",
    },
    {
        "gate_id": "GATE-149",
        "gate_name": "phase_149_monte_carlo_review_gate",
        "phase_ref": "Phase 149",
        "topic": "Monte Carlo resampling and parameter stability",
        "review_requirement": "Verify resampling methodology (block bootstrap vs stationary) and stability envelopes.",
        "action_required": "Operator review of bootstrap block sizes and stability criteria.",
    },
    {
        "gate_id": "GATE-150",
        "gate_name": "phase_150_backtest_governance_review_gate",
        "phase_ref": "Phase 150",
        "topic": "Backtest governance and bias controls",
        "review_requirement": "Verify survivorship, selection bias, and data snooping guards are fully documented.",
        "action_required": "Operator review of bias audit trail and negative claim enforcement.",
    },
    {
        "gate_id": "GATE-151",
        "gate_name": "phase_151_benchmark_evaluation_review_gate",
        "phase_ref": "Phase 151",
        "topic": "Benchmark comparison and strategy evaluation reports",
        "review_requirement": "Verify benchmark universe baselines and disclaimers are intact.",
        "action_required": "Operator review of evaluation templates and uncalculated metric placeholders.",
    },
    {
        "gate_id": "GATE-153",
        "gate_name": "phase_153_portfolio_boundary_review_gate",
        "phase_ref": "Phase 153",
        "topic": "Portfolio construction and position sizing handoff boundary",
        "review_requirement": "Ensure Phase 153 remains strictly contract-only with zero live capital allocation.",
        "action_required": "Operator review of Phase 153 prerequisites and non-live research scope boundary.",
    },
]


def build_backtest_acceptance_manual_review_gate_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for manual review gates."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for g in REVIEW_GATES:
        records.append({
            "gate_id": g["gate_id"],
            "gate_name": g["gate_name"],
            "phase_ref": g["phase_ref"],
            "topic": g["topic"],
            "review_requirement": g["review_requirement"],
            "action_required": g["action_required"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "manual_review_required": True,
            "status": ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": MANUAL_REVIEW_GATE_DOMAIN,
        "active_profile": active.profile_name,
        "total_gates": len(records),
        "manual_review_required_count": len(records),
        "all_require_review": True,
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
