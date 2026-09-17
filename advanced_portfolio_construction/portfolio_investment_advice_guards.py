# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Investment Advice Guards Module.

Strictly guards against investment advice, financial recommendations,
or prescriptive portfolio allocation calls.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

INVESTMENT_ADVICE_PATTERNS = [
    "buy now",
    "sell now",
    "invest in",
    "guaranteed return",
    "yatirim tavsiyesi",
    "al tavsiyesi",
    "sat tavsiyesi",
    "kesin kazanc",
    "kesin getiri",
    "target price recommendation",
    "hedef fiyat",
    "portfolio advice",
]

INVESTMENT_ADVICE_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_PORTFOLIO_NO_INVESTMENT_ADVICE",
        "guard_name": "Portfolio Investment Advice Guard",
        "detection_target": "investment_advice_keywords",
        "description": "Portfoy sozlesmelerinin yatirim tavsiyesi icermesini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_PORTFOLIO_NON_FINANCIAL_ADVICE_DISCLAIMER",
        "guard_name": "Non-Financial Advice Disclaimer Enforcement Guard",
        "detection_target": "missing_disclaimer",
        "description": "Tum portfoy raporlarinda YTD yasal uyarisinin bulunmasini zorunlu kilan muhafiz.",
    },
]


def build_portfolio_investment_advice_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio investment advice guards."""
    rows: List[Dict[str, Any]] = []

    for g in INVESTMENT_ADVICE_GUARDS:
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
        "guard_category": "investment_advice",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_no_investment_advice(text_content: str) -> Dict[str, Any]:
    """Validate that text does not contain investment advice terms."""
    low = text_content.lower()
    violations: List[str] = []
    for pat in INVESTMENT_ADVICE_PATTERNS:
        if pat in low:
            violations.append(pat)

    is_clean = len(violations) == 0
    return {
        "is_clean": is_clean,
        "advice_detected": not is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "BLOCKED_BY_INVESTMENT_ADVICE_GUARD",
        "contract_only": True,
    }
