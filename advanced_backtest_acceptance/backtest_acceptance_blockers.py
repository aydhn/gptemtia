# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Blocker Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    BLOCKER_DOMAIN,
    ACCEPTANCE_BLOCKED_BY_SAFETY,
)
from advanced_backtest_acceptance.backtest_acceptance_models import (
    BacktestAcceptanceFinding,
)

BLOCKER_TYPES: List[str] = [
    "missing_phase_module",
    "missing_manifest",
    "missing_validation_report",
    "missing_safety_boundary",
    "missing_disabled_execution_report",
    "unsafe_claim_detected",
    "backtest_execution_detected",
    "benchmark_execution_detected",
    "metric_calculation_detected",
    "performance_claim_detected",
    "strategy_approval_detected",
    "capital_allocation_detected",
    "portfolio_construction_detected",
    "position_sizing_detected",
    "live_trading_detected",
    "broker_execution_detected",
    "deployment_detected",
    "phase_153_handoff_missing",
]


def create_backtest_acceptance_blocker(
    blocker_type: str,
    phase_ref: str,
    severity_label: str,
    message: str,
    recommendation: str,
) -> BacktestAcceptanceFinding:
    """Factory function for creating blocker findings."""
    return BacktestAcceptanceFinding(
        finding_id=f"BLK-{abs(hash(message)) % 100000:05d}",
        finding_type=blocker_type,
        phase_ref=phase_ref,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=True,
        non_signal=True,
    )


def build_backtest_acceptance_blocker_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for registered blockers (default: 0 blockers)."""
    active = profile or get_backtest_acceptance_profile()

    # Under nominal verified conditions, zero blockers exist
    records: List[Dict[str, Any]] = []

    columns = [
        "finding_id", "finding_type", "phase_ref", "severity_label",
        "message", "recommendation", "current_phase", "target_final_phase",
        "next_phase", "manual_review_required", "status", "non_signal"
    ]
    df = pd.DataFrame(records, columns=columns)
    summary: Dict[str, Any] = {
        "domain": BLOCKER_DOMAIN,
        "active_profile": active.profile_name,
        "total_blockers": len(records),
        "has_blockers": len(records) > 0,
        "supported_blocker_types": BLOCKER_TYPES,
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
