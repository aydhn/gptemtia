# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Multiple Testing Guards Module.

Guards against multiple testing bias, combinatorial selection of portfolio rules,
and unregistered trial mining.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

MULTIPLE_TESTING_TERMS = [
    "p_hacked_weights",
    "unregistered_trial_mining",
    "combinatorial_rule_mining",
    "cherry_picked_sizing_formula",
]

MULTIPLE_TESTING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_PORTFOLIO_MULTIPLE_TESTING",
        "guard_name": "Portfolio Multiple Testing Guard",
        "detection_target": "unregistered_combinations",
        "description": "Coklu test yanliligi ve kayitsiz deneme madenciligini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_PRE_REGISTERED_PORTFOLIO_RULES",
        "guard_name": "Pre-Registered Portfolio Rules Guard",
        "detection_target": "unregistered_rule_additions",
        "description": "Portfoy kurallarinin onceden kaydedilmis olmasini zorunlu kilan muhafiz.",
    },
]


def build_portfolio_multiple_testing_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio multiple testing guards."""
    rows: List[Dict[str, Any]] = []

    for g in MULTIPLE_TESTING_GUARDS:
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
        "guard_category": "multiple_testing",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_multiple_testing_claims(text_or_claims: List[str]) -> Dict[str, Any]:
    """Validate that designs do not involve multiple testing terms."""
    violations: List[str] = []
    for item in text_or_claims:
        low = str(item).lower()
        for pat in MULTIPLE_TESTING_TERMS:
            if pat in low:
                violations.append(item)
                break

    is_clean = len(violations) == 0
    return {
        "is_clean": is_clean,
        "violations_detected": not is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "BLOCKED_BY_MULTIPLE_TESTING_GUARD",
        "contract_only": True,
    }
