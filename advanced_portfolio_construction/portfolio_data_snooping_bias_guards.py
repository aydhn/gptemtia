# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Data Snooping Bias Guards Module.

Guards portfolio construction parameter designs against data snooping bias,
in-sample cherry-picking, and hindsight-selected constraints.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

DATA_SNOOPING_TERMS = [
    "cherry_picked_in_sample",
    "retrospectively_fitted_weights",
    "post_hoc_constraint_tuning",
    "in_sample_snooped_allocation",
]

DATA_SNOOPING_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_PORTFOLIO_DATA_SNOOPING",
        "guard_name": "Portfolio Data Snooping Bias Guard",
        "detection_target": "snooped_parameters_and_weights",
        "description": "Geriye donuk veri madenciligiyle secilmis parametre veya agirlik kullanimini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_PARAM_STABILITY_AUDIT",
        "guard_name": "Parameter Stability Audit Guard",
        "detection_target": "unjustified_parameter_tweaks",
        "description": "Parametre ve sinirlarin onceden belirlenmis sabit kurallara dayanmasini denetleyen muhafiz.",
    },
]


def build_portfolio_data_snooping_bias_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio data snooping bias guards."""
    rows: List[Dict[str, Any]] = []

    for g in DATA_SNOOPING_GUARDS:
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
        "guard_category": "data_snooping_bias",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_data_snooping_claims(text_or_claims: List[str]) -> Dict[str, Any]:
    """Validate that designs do not involve data snooping terms."""
    violations: List[str] = []
    for item in text_or_claims:
        low = str(item).lower()
        for pat in DATA_SNOOPING_TERMS:
            if pat in low:
                violations.append(item)
                break

    is_clean = len(violations) == 0
    return {
        "is_clean": is_clean,
        "violations_detected": not is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "BLOCKED_BY_DATA_SNOOPING_GUARD",
        "contract_only": True,
    }
