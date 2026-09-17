# -*- coding: utf-8 -*-
"""Phase 153: Concentration Limit Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    CONCENTRATION_LIMIT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


CONCENTRATION_LIMITS = [
    {"limit_id": "CONC_MAX_SINGLE_ASSET", "limit_name": "Single Asset Concentration Limit", "max_allowed_weight": 0.15, "description": "Tekil bir varligin portfoydeki agirliginin en fazla %15 olabilecegini tanimlar."},
    {"limit_id": "CONC_TOP_3_ASSETS", "limit_name": "Top 3 Assets Concentration Limit", "max_allowed_weight": 0.40, "description": "En buyuk 3 varligin toplam portfoy agirliginin en fazla %40 olabilecegini tanimlar."},
    {"limit_id": "CONC_SECTOR_COMMODITY", "limit_name": "Commodity Sector Concentration Limit", "max_allowed_weight": 0.60, "description": "Emtia grubu toplam agirliginin en fazla %60 olabilecegini tanimlar."},
    {"limit_id": "CONC_SECTOR_FX", "limit_name": "FX Sector Concentration Limit", "max_allowed_weight": 0.50, "description": "Doviz grubu toplam agirliginin en fazla %50 olabilecegini tanimlar."},
]


def build_concentration_limit_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for concentration limit contracts."""
    rows = []
    for c in CONCENTRATION_LIMITS:
        rows.append({
            "limit_id": c["limit_id"],
            "limit_name": c["limit_name"],
            "max_allowed_weight": c["max_allowed_weight"],
            "description": c["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_limits_assigned": False,
            "investment_advice": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": CONCENTRATION_LIMIT_DOMAIN,
        "active_profile": profile.profile_name,
        "total_limits": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
