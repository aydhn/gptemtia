# -*- coding: utf-8 -*-
"""Phase 153: Sector Group Exposure Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    EXPOSURE_LIMIT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


SECTOR_GROUP_LIMIT_ITEMS = [
    {"limit_id": "SEC_PRECIOUS_METALS", "sector": "PRECIOUS_METALS", "max_share": 0.35, "description": "Degerli metaller (Altin, Gumus) grubu azami agirlik sozlesmesi."},
    {"limit_id": "SEC_ENERGY", "sector": "ENERGY", "max_share": 0.30, "description": "Enerji (Petrol, Dogalgaz) grubu azami agirlik sozlesmesi."},
    {"limit_id": "SEC_BASE_METALS", "sector": "BASE_METALS", "max_share": 0.25, "description": "Endustriyel metaller grubu azami agirlik sozlesmesi."},
    {"limit_id": "SEC_AGRICULTURE", "sector": "AGRICULTURE", "max_share": 0.20, "description": "Tarmsal emtia grubu azami agirlik sozlesmesi."},
]


def build_sector_group_exposure_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for sector group exposure placeholders."""
    rows = []
    for item in SECTOR_GROUP_LIMIT_ITEMS:
        rows.append({
            "limit_id": item["limit_id"],
            "sector": item["sector"],
            "max_share": item["max_share"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_sector_rebalancing": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": EXPOSURE_LIMIT_DOMAIN,
        "category": "sector_group_exposure_placeholders",
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
