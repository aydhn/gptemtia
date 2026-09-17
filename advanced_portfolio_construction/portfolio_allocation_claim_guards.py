# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Allocation Claim Guards Module.

Guards against premature claims of real capital allocation, live weight deployment,
or automated execution of portfolio rebalancing.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

ALLOCATION_CLAIM_TERMS = [
    "live_allocated",
    "real_capital_deployed",
    "weights_enforced_live",
    "auto_rebalance_executed",
    "optimal_portfolio_achieved",
    "production_ready_allocation",
]

ALLOCATION_CLAIM_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_ALLOCATION_CLAIM_TERMS",
        "guard_name": "Allocation Claim Keyword Guard",
        "detection_target": "unsubstantiated_allocation_claims",
        "description": "Gercek sermaye tahsisi veya canli agirlik dagitimi iddialarini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_NO_LIVE_WEIGHT_DEPLOY",
        "guard_name": "No Live Weight Deployment Guard",
        "detection_target": "live_weight_deployment_attempts",
        "description": "Agirliklarin canli ortama dagitilmasini engelleyen muhafiz.",
    },
]


def build_portfolio_allocation_claim_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio allocation claim guards."""
    rows: List[Dict[str, Any]] = []

    for g in ALLOCATION_CLAIM_GUARDS:
        rows.append({
            "guard_id": g["guard_id"],
            "guard_name": g["guard_name"],
            "detection_target": g["detection_target"],
            "description": g["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "is_active": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_GUARD_DOMAIN,
        "guard_category": "allocation_claim",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_allocation_claims(text_or_claims: List[str]) -> Dict[str, Any]:
    """Validate that claims do not assert real capital deployment or live rebalancing."""
    violations: List[str] = []
    for item in text_or_claims:
        low = str(item).lower()
        for pat in ALLOCATION_CLAIM_TERMS:
            if pat in low:
                violations.append(item)
                break

    is_clean = len(violations) == 0
    return {
        "is_clean": is_clean,
        "violations_detected": not is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "BLOCKED_BY_ALLOCATION_CLAIM_GUARD",
        "contract_only": True,
    }
