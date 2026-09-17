# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Blocker Registry.

Identifies, registers, and tracks potential critical blockers that would prevent
advancement to Phase 158 Full-System Integration.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    BLOCKER_DOMAIN,
    SEVERITY_CRITICAL,
    PORTFOLIO_ACCEPTANCE_READY,
)
from .portfolio_acceptance_models import PortfolioAcceptanceFinding

KNOWN_BLOCKER_TYPES = [
    "missing_phase_module",
    "missing_manifest",
    "missing_validation_report",
    "missing_safety_boundary",
    "missing_disabled_execution_report",
    "unsafe_claim_detected",
    "portfolio_construction_detected",
    "position_sizing_detected",
    "portfolio_optimization_detected",
    "allocation_generation_detected",
    "weight_generation_detected",
    "rebalance_generation_detected",
    "order_generation_detected",
    "risk_reporting_execution_detected",
    "exposure_attribution_detected",
    "limit_monitoring_detected",
    "scenario_execution_detected",
    "drawdown_control_detected",
    "portfolio_adjustment_detected",
    "hedge_derisk_detected",
    "alert_dashboard_detected",
    "live_trading_detected",
    "broker_execution_detected",
    "deployment_detected",
    "phase_158_handoff_missing",
]


def create_portfolio_acceptance_blocker(
    blocker_type: str,
    phase_ref: str,
    severity_label: str = SEVERITY_CRITICAL,
    message: str = "",
    recommendation: str = "",
) -> PortfolioAcceptanceFinding:
    """Create a structured PortfolioAcceptanceFinding representing a blocker."""
    return PortfolioAcceptanceFinding(
        finding_id=f"BLK-{blocker_type.upper()[:12]}",
        finding_type=blocker_type,
        phase_ref=phase_ref,
        severity_label=severity_label,
        message=message or f"Blocker detected: {blocker_type}",
        recommendation=recommendation or "Review and resolve before Phase 158.",
        manual_review_required=True,
        is_blocking=True,
    )


def build_portfolio_acceptance_blocker_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build blocker registry. In clean state, zero active blockers are present."""
    active = profile or get_portfolio_acceptance_profile()
    records = []

    for b_type in KNOWN_BLOCKER_TYPES:
        records.append({
            "blocker_type": b_type,
            "phase_ref": "Portfolio Block (153-157)",
            "severity_label": SEVERITY_CRITICAL,
            "is_active": False,
            "message": f"Rule monitored: {b_type}",
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })

    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_blockers(df)
    return df, summary


def summarize_portfolio_acceptance_blockers(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize blocker registry."""
    active_blockers = len(df[df["is_active"]]) if not df.empty and "is_active" in df.columns else 0
    return {
        "domain": BLOCKER_DOMAIN,
        "total_monitored_blocker_types": len(df),
        "active_blockers_count": active_blockers,
        "has_active_blockers": (active_blockers > 0),
        "status": PORTFOLIO_ACCEPTANCE_READY if active_blockers == 0 else "BLOCKED_BY_SAFETY",
    }
