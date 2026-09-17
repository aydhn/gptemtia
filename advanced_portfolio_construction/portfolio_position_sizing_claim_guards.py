# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Position Sizing Claim Guards Module.

Guards against premature claims of real position sizing, trade unit calculation,
lot execution, or live sizing orders.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

SIZING_CLAIM_TERMS = [
    "real_lot_sized",
    "shares_to_buy_now",
    "execute_contracts_count",
    "live_sizing_order",
    "broker_position_sized",
    "automated_lot_sizing_active",
]

SIZING_CLAIM_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_SIZING_CLAIM_TERMS",
        "guard_name": "Position Sizing Claim Keyword Guard",
        "detection_target": "unsubstantiated_sizing_claims",
        "description": "Gercek lot/kontrat boyutlandirma veya canli emir boyutlandirma iddialarini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_NO_REAL_LOT_OUTPUT",
        "guard_name": "No Real Lot Output Guard",
        "detection_target": "real_lot_generation_attempts",
        "description": "Gercek lot ve adet ciktisi uretilmesini engelleyen muhafiz.",
    },
]


def build_portfolio_position_sizing_claim_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio position sizing claim guards."""
    rows: List[Dict[str, Any]] = []

    for g in SIZING_CLAIM_GUARDS:
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
        "guard_category": "position_sizing_claim",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_position_sizing_claims(text_or_claims: List[str]) -> Dict[str, Any]:
    """Validate that claims do not assert real lot sizing or live contract orders."""
    violations: List[str] = []
    for item in text_or_claims:
        low = str(item).lower()
        for pat in SIZING_CLAIM_TERMS:
            if pat in low:
                violations.append(item)
                break

    is_clean = len(violations) == 0
    return {
        "is_clean": is_clean,
        "violations_detected": not is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "BLOCKED_BY_POSITION_SIZING_CLAIM_GUARD",
        "contract_only": True,
    }
