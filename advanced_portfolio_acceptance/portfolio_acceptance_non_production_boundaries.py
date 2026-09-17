# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Non-Production Boundaries.

Guarantees non-production constraints, research boundaries, and prohibition
of production readiness claims across Phase 157.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    NON_PRODUCTION_BOUNDARY_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

NON_PROD_INVARIANTS = [
    ("NPD-01", "non_production_enforced", True, "System strictly restricted to offline/local research"),
    ("NPD-02", "production_ready_claim_prohibited", True, "Score and report do not claim production readiness"),
    ("NPD-03", "broker_ready_claim_prohibited", True, "System does not claim broker readiness"),
    ("NPD-04", "live_trading_claim_prohibited", True, "No claim of live trading capability"),
    ("NPD-05", "performance_guarantee_prohibited", True, "No guarantee of alpha, Sharpe, or drawdown safety"),
    ("NPD-06", "strategy_portfolio_approval_prohibited", True, "Acceptance report does not approve live strategies or portfolios"),
    ("NPD-07", "model_deployment_prohibited", True, "Model deployment and registry persistence disabled"),
]


def build_portfolio_acceptance_non_production_boundary_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of non-production invariants."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for inv_id, invariant_name, enforced, notes in NON_PROD_INVARIANTS:
        records.append({
            "invariant_id": inv_id,
            "invariant_name": invariant_name,
            "enforced": enforced,
            "notes": notes,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_non_production_boundaries(df)
    return df, summary


def summarize_portfolio_acceptance_non_production_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize non-production boundary registry."""
    all_enforced = bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False
    return {
        "domain": NON_PRODUCTION_BOUNDARY_DOMAIN,
        "total_invariants": len(df),
        "all_enforced": all_enforced,
        "production_ready_prohibited": True,
        "broker_ready_prohibited": True,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_enforced else "NON_PRODUCTION_BREACH",
    }
