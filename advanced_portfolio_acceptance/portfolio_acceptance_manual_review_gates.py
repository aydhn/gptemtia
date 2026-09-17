# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Manual Review Gates.

Defines human-in-the-loop review gates ensuring all portfolio components
are reviewed prior to Phase 158 Full-System Integration.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    MANUAL_REVIEW_GATE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
)

GATES = [
    {
        "gate_id": "MRG-153",
        "gate_name": "phase_153_portfolio_construction_review_gate",
        "phase_ref": "Phase 153",
        "title": "Portfolio Construction & Position Sizing Review",
        "description": "Operator review of multi-asset sizing specifications, risk budgeting, and allocation guards.",
        "action_required": "Verify all volatility parity and risk budget contracts remain contract-only.",
    },
    {
        "gate_id": "MRG-154",
        "gate_name": "phase_154_portfolio_optimization_review_gate",
        "phase_ref": "Phase 154",
        "title": "Portfolio Optimization & Allocation Constraints Review",
        "description": "Operator review of optimization objective formulas, solver lockouts, and turnover limits.",
        "action_required": "Confirm zero active numerical solvers are executing during dry run.",
    },
    {
        "gate_id": "MRG-155",
        "gate_name": "phase_155_risk_reporting_review_gate",
        "phase_ref": "Phase 155",
        "title": "Risk Reporting & Limit Monitoring Review",
        "description": "Operator review of exposure attribution rules, VaR schemas, and alert lockouts.",
        "action_required": "Confirm live alerting and dashboard broadcast remain completely disabled.",
    },
    {
        "gate_id": "MRG-156",
        "gate_name": "phase_156_portfolio_scenario_control_review_gate",
        "phase_ref": "Phase 156",
        "title": "Scenario Testing & Drawdown Control Review",
        "description": "Operator review of shock scenarios, drawdown tiers, and de-risking control placeholders.",
        "action_required": "Confirm control action placeholders do not trigger automated hedge or stop orders.",
    },
    {
        "gate_id": "MRG-158",
        "gate_name": "phase_158_full_system_integration_review_gate",
        "phase_ref": "Phase 158",
        "title": "Phase 158 Full-System Integration Entry Gate",
        "description": "Operator sign-off before entering full-system integration and acceptance rehearsal.",
        "action_required": "Verify all upstream blocks (data, feature, regime, ML, backtest, portfolio) pass acceptance.",
    },
]


def build_portfolio_acceptance_manual_review_gate_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of manual review gates."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for g in GATES:
        records.append({
            "gate_id": g["gate_id"],
            "gate_name": g["gate_name"],
            "phase_ref": g["phase_ref"],
            "title": g["title"],
            "description": g["description"],
            "action_required": g["action_required"],
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_manual_review_gates(df)
    return df, summary


def summarize_portfolio_acceptance_manual_review_gates(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review gates."""
    return {
        "domain": MANUAL_REVIEW_GATE_DOMAIN,
        "total_gates": len(df),
        "pending_review_count": len(df),
        "status": PORTFOLIO_ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
    }
