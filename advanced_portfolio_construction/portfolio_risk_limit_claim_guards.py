# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Risk Limit Claim Guards Module.

Guards against premature claims of active broker margin enforcement,
live clearing house margin calls, or real-time stop-outs.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

RISK_LIMIT_CLAIM_TERMS = [
    "broker_margin_enforced",
    "live_margin_call_active",
    "real_stop_out_executed",
    "clearing_house_margin_applied",
    "exchange_limit_active",
]

RISK_LIMIT_CLAIM_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_RISK_LIMIT_CLAIMS",
        "guard_name": "Risk Limit Claim Guard",
        "detection_target": "unsubstantiated_risk_enforcement_claims",
        "description": "Canli broker teminat denetimi veya takas kurumu teminat iddialarini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_CONTRACT_ONLY_RISK_LIMITS",
        "guard_name": "Contract-Only Risk Limit Guard",
        "detection_target": "non_contract_risk_limits",
        "description": "Risk limitlerinin sadece sozlesme bazli oldugunu dogrulayan muhafiz.",
    },
]


def build_portfolio_risk_limit_claim_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio risk limit claim guards."""
    rows: List[Dict[str, Any]] = []

    for g in RISK_LIMIT_CLAIM_GUARDS:
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
        "guard_category": "risk_limit_claim",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_risk_limit_claims(text_or_claims: List[str]) -> Dict[str, Any]:
    """Validate that claims do not assert live broker margin enforcement."""
    violations: List[str] = []
    for item in text_or_claims:
        low = str(item).lower()
        for pat in RISK_LIMIT_CLAIM_TERMS:
            if pat in low:
                violations.append(item)
                break

    is_clean = len(violations) == 0
    return {
        "is_clean": is_clean,
        "violations_detected": not is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "BLOCKED_BY_RISK_LIMIT_CLAIM_GUARD",
        "contract_only": True,
    }
