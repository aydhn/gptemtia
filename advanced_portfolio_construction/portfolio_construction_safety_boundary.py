# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Safety Boundary Engine."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_construction_config import (
    PortfolioConstructionProfile,
    get_default_portfolio_construction_profile,
)
from .portfolio_construction_labels import (
    PORTFOLIO_SAFETY_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

NO_GO_RULES: List[str] = [
    "live trading",
    "broker execution",
    "investment advice",
    "real capital allocation",
    "real position sizing (lot/contracts)",
    "real portfolio weights calculation",
    "optimizer numerical execution",
    "portfolio metric calculation (Sharpe, VaR, ES)",
    "model training or fitting",
    "model prediction or inference",
    "target or label generation",
    "production deployment",
    "broker API calls",
    "web scraping",
    "raw source overwrite",
]

SAFE_GO_RULES: List[str] = [
    "local offline portfolio construction contract generation",
    "universe and asset eligibility contract definitions",
    "position sizing placeholder specifications",
    "risk budget placeholder specifications",
    "exposure and concentration limit contract definitions",
    "non-production readiness scoring",
    "manual review gate registrations",
    "findings and gap documentation",
    "master manifest verification",
    "Phase 154 optimization handoff report",
]


def build_portfolio_construction_no_go_conditions(
    profile: Optional[PortfolioConstructionProfile] = None,
) -> List[Dict[str, Any]]:
    """Return structured NO-GO conditions."""
    return [{"rule_id": f"NGO-153-{i+1:02d}", "name": rule, "prohibited": True} for i, rule in enumerate(NO_GO_RULES)]


def build_portfolio_construction_safe_go_conditions(
    profile: Optional[PortfolioConstructionProfile] = None,
) -> List[Dict[str, Any]]:
    """Return structured SAFE-GO conditions."""
    return [{"rule_id": f"SGO-153-{i+1:02d}", "name": rule, "permitted_offline": True} for i, rule in enumerate(SAFE_GO_RULES)]


def build_portfolio_construction_safety_boundary_report(
    profile: Optional[PortfolioConstructionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for portfolio construction safety boundaries."""
    active = profile or get_default_portfolio_construction_profile()

    rows = []
    for ngo in build_portfolio_construction_no_go_conditions(active):
        rows.append({
            "rule_id": ngo["rule_id"],
            "boundary_type": "NO_GO",
            "rule_name": ngo["name"],
            "is_enforced": True,
            "current_phase": active.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })
    for sgo in build_portfolio_construction_safe_go_conditions(active):
        rows.append({
            "rule_id": sgo["rule_id"],
            "boundary_type": "SAFE_GO",
            "rule_name": sgo["name"],
            "is_enforced": True,
            "current_phase": active.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary: Dict[str, Any] = {
        "domain": PORTFOLIO_SAFETY_DOMAIN,
        "active_profile": active.profile_name,
        "total_rules": len(df),
        "no_go_count": len(NO_GO_RULES),
        "safe_go_count": len(SAFE_GO_RULES),
        "all_enforced": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
