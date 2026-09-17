# -*- coding: utf-8 -*-
"""Phase 153: Exposure Limit Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    EXPOSURE_LIMIT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


EXPOSURE_LIMITS = [
    {"limit_id": "EXP_GROSS_MAX", "limit_name": "Gross Exposure Contract Limit", "max_allowed": 1.50, "description": "Toplam brut pozisyon maruziyetinin en fazla %150 olabilecegini tanimlar."},
    {"limit_id": "EXP_NET_MAX", "limit_name": "Net Exposure Contract Limit", "max_allowed": 0.80, "description": "Toplam net pozisyon maruziyetinin en fazla %80 olabilecegini tanimlar."},
    {"limit_id": "EXP_ASSET_CLASS_MAX", "limit_name": "Asset Class Exposure Contract Limit", "max_allowed": 0.70, "description": "Tek bir varlik sinifina maksimum %70 brut maruziyet limiti tanimlar."},
    {"limit_id": "EXP_DIRECTIONAL_LONG_MAX", "limit_name": "Long Directional Exposure Limit", "max_allowed": 1.00, "description": "Toplam long yonlu pozisyon maruziyet sinirini tanimlar."},
    {"limit_id": "EXP_DIRECTIONAL_SHORT_MAX", "limit_name": "Short Directional Exposure Limit", "max_allowed": 0.50, "description": "Toplam short yonlu pozisyon maruziyet sinirini tanimlar."},
]


def build_exposure_limit_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for exposure limit contracts."""
    rows = []
    for el in EXPOSURE_LIMITS:
        rows.append({
            "limit_id": el["limit_id"],
            "limit_name": el["limit_name"],
            "max_allowed": el["max_allowed"],
            "description": el["description"],
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
        "domain": EXPOSURE_LIMIT_DOMAIN,
        "active_profile": profile.profile_name,
        "total_limits": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
