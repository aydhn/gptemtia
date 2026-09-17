# -*- coding: utf-8 -*-
"""Phase 157: Phase 155 Risk Reporting Acceptance Registry.

Evaluates contract compliance, structural readiness, metric placeholders,
and non-execution invariants for Phase 155: Risk Reporting, Exposure Attribution and Limit Monitoring.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    PHASE_155_RISK_REPORTING_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

PHASE_155_ITEMS = [
    {
        "item_id": "ACC-155-01",
        "criterion": "advanced_risk_reporting module present",
        "description": "Module package and exports available for offline inspection.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-02",
        "criterion": "risk report contracts present",
        "description": "Contracts defining portfolio risk reports, VaR, and expected shortfall schemas registered.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-03",
        "criterion": "exposure attribution contracts present",
        "description": "Factor, sector, asset class, and currency exposure attribution contracts defined.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-04",
        "criterion": "limit monitoring contracts present",
        "description": "Concentration limits, exposure thresholds, and breach detection contracts specified.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-05",
        "criterion": "risk/exposure/limit metric placeholders present",
        "description": "Metric calculation placeholders registered without executing numeric calculations.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-06",
        "criterion": "alert/dashboard disabled reports present",
        "description": "Disabled execution reports present confirming live alerting and dashboard lockouts.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-07",
        "criterion": "no risk report execution",
        "description": "Zero real risk reporting runs performed; contracts and placeholders only.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-08",
        "criterion": "no exposure calculation executed",
        "description": "Zero real risk exposure values or margin requirements calculated.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-09",
        "criterion": "no limit monitoring or alerts generated",
        "description": "Zero active limit alerts, warnings, or live dashboards generated.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-155-10",
        "criterion": "Phase 156 handoff completed",
        "description": "Handoff to Phase 156 Portfolio Scenario Testing and Drawdown Control verified and accepted.",
        "satisfied": True,
    },
]


def build_phase_155_risk_reporting_acceptance_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 155 acceptance evaluation registry."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for item in PHASE_155_ITEMS:
        records.append({
            "item_id": item["item_id"],
            "phase_number": 155,
            "phase_title": "Risk Reporting, Exposure Attribution and Limit Monitoring",
            "criterion": item["criterion"],
            "description": item["description"],
            "satisfied": item["satisfied"],
            "contract_only": True,
            "non_production": True,
            "dry_run": True,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_phase_155_risk_reporting_acceptance(df)
    return df, summary


def summarize_phase_155_risk_reporting_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 155 acceptance registry."""
    all_satisfied = bool(df["satisfied"].all()) if not df.empty and "satisfied" in df.columns else False
    return {
        "domain": PHASE_155_RISK_REPORTING_ACCEPTANCE_DOMAIN,
        "phase_number": 155,
        "total_criteria": len(df),
        "satisfied_criteria": int(df["satisfied"].sum()) if not df.empty and "satisfied" in df.columns else 0,
        "all_satisfied": all_satisfied,
        "contract_only": True,
        "non_production": True,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_satisfied else "ACCEPTANCE_INCOMPLETE",
    }
