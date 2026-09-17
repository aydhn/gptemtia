# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Overfitting Guards Module.

Guards portfolio construction and sizing definitions against over-parameterization,
curve-fitting, and fragile optimization setups.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

OVERFITTING_TERMS = [
    "overfitted_weights",
    "curve_fitted_sizing",
    "hyper_optimized_allocation",
    "zero_dof_portfolio",
]

OVERFITTING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_PORTFOLIO_OVERFITTING",
        "guard_name": "Portfolio Overfitting Guard",
        "detection_target": "over_parameterized_sizing_rules",
        "description": "Asiri uyum (overfitting) iceren pozisyon ve portfoy kurallarini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_PARSIMONY_SIZING_RULES",
        "guard_name": "Parsimonious Sizing Rule Guard",
        "detection_target": "excessive_complexity_in_rules",
        "description": "Pozisyon boyutlandirma sozlesmelerinde sadelik ve anlasilabilirlik ilkesini denetleyen muhafiz.",
    },
]


def build_portfolio_overfitting_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio overfitting guards."""
    rows: List[Dict[str, Any]] = []

    for g in OVERFITTING_GUARDS:
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
        "guard_category": "overfitting",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_overfitting_claims(text_or_claims: List[str]) -> Dict[str, Any]:
    """Validate that designs do not involve overfitted terms."""
    violations: List[str] = []
    for item in text_or_claims:
        low = str(item).lower()
        for pat in OVERFITTING_TERMS:
            if pat in low:
                violations.append(item)
                break

    is_clean = len(violations) == 0
    return {
        "is_clean": is_clean,
        "violations_detected": not is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "BLOCKED_BY_OVERFITTING_GUARD",
        "contract_only": True,
    }
