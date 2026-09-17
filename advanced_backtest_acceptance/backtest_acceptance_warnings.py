# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Warning Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    WARNING_DOMAIN,
    ACCEPTANCE_READY_WITH_WARNINGS,
)
from advanced_backtest_acceptance.backtest_acceptance_models import (
    BacktestAcceptanceFinding,
)

STANDARD_WARNINGS: List[Dict[str, Any]] = [
    {
        "warning_id": "WRN-152-01",
        "warning_type": "contract_only_acceptance",
        "phase_ref": "Phase 146-152",
        "severity_label": "INFO",
        "message": "Backtest block acceptance is purely contract-level; no real trading engines were executed.",
        "recommendation": "Maintain contract-only boundaries throughout subsequent phases.",
    },
    {
        "warning_id": "WRN-152-02",
        "warning_type": "placeholder_only_evidence",
        "phase_ref": "Phase 148-151",
        "severity_label": "INFO",
        "message": "Performance and stress metrics are uncalculated placeholders, not empirical returns.",
        "recommendation": "Do not interpret placeholder data as investment or strategy results.",
    },
    {
        "warning_id": "WRN-152-03",
        "warning_type": "no_real_backtest",
        "phase_ref": "Phase 146",
        "severity_label": "WARNING",
        "message": "No historical backtest simulation loop was executed in this phase.",
        "recommendation": "Strictly observe zero backtest execution boundary.",
    },
    {
        "warning_id": "WRN-152-04",
        "warning_type": "no_real_benchmark",
        "phase_ref": "Phase 147, 151",
        "severity_label": "WARNING",
        "message": "No live or real benchmark comparison calculations were performed.",
        "recommendation": "Observe zero benchmark execution boundary.",
    },
    {
        "warning_id": "WRN-152-05",
        "warning_type": "no_real_metric_calculation",
        "phase_ref": "Phase 146-151",
        "severity_label": "WARNING",
        "message": "Sharpe, Sortino, drawdowns, and VaR are explicitly uncalculated.",
        "recommendation": "Do not treat readiness score as performance metrics.",
    },
    {
        "warning_id": "WRN-152-06",
        "warning_type": "no_strategy_approval",
        "phase_ref": "Phase 150, 151",
        "severity_label": "WARNING",
        "message": "Acceptance completion does NOT constitute strategy approval or commercial authorization.",
        "recommendation": "Do not treat readiness score as strategy approval or authorization.",
    },
    {
        "warning_id": "WRN-152-07",
        "warning_type": "manual_review_required",
        "phase_ref": "Phase 152",
        "severity_label": "INFO",
        "message": "Human operator manual review gates must be confirmed before production consideration.",
        "recommendation": "Operator review required on registered gates prior to deployment discussions.",
    },
    {
        "warning_id": "WRN-152-08",
        "warning_type": "phase_153_must_remain_non_live",
        "phase_ref": "Phase 153",
        "severity_label": "CRITICAL_INFO",
        "message": "Phase 153 Portfolio Construction must remain local, offline, and contract-bound.",
        "recommendation": "Enforce zero broker connectivity and zero live capital allocation in Phase 153.",
    },
]


def create_backtest_acceptance_warning(
    warning_type: str,
    phase_ref: str,
    severity_label: str,
    message: str,
    recommendation: str,
) -> BacktestAcceptanceFinding:
    """Factory function for creating warning findings."""
    return BacktestAcceptanceFinding(
        finding_id=f"WRN-{abs(hash(message)) % 100000:05d}",
        finding_type=warning_type,
        phase_ref=phase_ref,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=True,
        non_signal=True,
    )


def build_backtest_acceptance_warning_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for standard backtest acceptance warnings."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for w in STANDARD_WARNINGS:
        records.append({
            "finding_id": w["warning_id"],
            "finding_type": w["warning_type"],
            "phase_ref": w["phase_ref"],
            "severity_label": w["severity_label"],
            "message": w["message"],
            "recommendation": w["recommendation"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "manual_review_required": True,
            "status": ACCEPTANCE_READY_WITH_WARNINGS,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": WARNING_DOMAIN,
        "active_profile": active.profile_name,
        "total_warnings": len(records),
        "warning_types": [w["warning_type"] for w in STANDARD_WARNINGS],
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
