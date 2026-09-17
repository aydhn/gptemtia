# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Warning Registry.

Registers governance warnings and disclaimers emphasizing that portfolio contracts
are non-executable and do not constitute trading approvals.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    WARNING_DOMAIN,
    SEVERITY_WARNING,
    PORTFOLIO_ACCEPTANCE_READY,
)

WARNING_ITEMS = [
    ("contract_only_acceptance", "Acceptance applies solely to contract structures, schemas, and governance rules."),
    ("placeholder_only_evidence", "Evidence consists of contract definitions and non-executing placeholders."),
    ("no_real_portfolio_construction", "Real multi-asset portfolio construction was NOT executed; weights are zero."),
    ("no_real_position_sizing", "Real position sizing was NOT calculated; risk budget execution is inactive."),
    ("no_real_portfolio_optimization", "Real mathematical optimization was NOT run; solver lockouts remain active."),
    ("no_real_risk_reporting", "Real risk reporting was NOT generated; exposure metrics are contract placeholders."),
    ("no_real_limit_monitoring", "Real limit monitoring was NOT run; live breach alerts remain disabled."),
    ("no_real_scenario_execution", "Real stress scenarios were NOT executed against market positions."),
    ("no_real_drawdown_control", "Real drawdown control actions (de-risking, hedge, stop) were NOT triggered."),
    ("no_strategy_approval", "Zero strategy approval granted; findings do not endorse trading algorithms."),
    ("no_portfolio_approval", "Zero portfolio allocation approval granted; capital allocation remains blocked."),
    ("manual_review_required", "Human-in-the-loop review is mandatory across all portfolio components before Phase 158."),
    ("phase_158_must_remain_non_live", "Phase 158 must remain in local/offline rehearsal mode without live execution."),
]


def build_portfolio_acceptance_warning_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of portfolio acceptance warnings."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for warning_type, message in WARNING_ITEMS:
        records.append({
            "warning_type": warning_type,
            "message": message,
            "severity_label": SEVERITY_WARNING,
            "is_acknowledged": True,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_warnings(df)
    return df, summary


def summarize_portfolio_acceptance_warnings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize warnings registry."""
    return {
        "domain": WARNING_DOMAIN,
        "total_warnings": len(df),
        "all_acknowledged": bool(df["is_acknowledged"].all()) if not df.empty and "is_acknowledged" in df.columns else False,
        "governance_guarantees_enforced": True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
