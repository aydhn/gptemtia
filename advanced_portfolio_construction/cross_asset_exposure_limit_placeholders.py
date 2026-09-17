# -*- coding: utf-8 -*-
"""Phase 153: Cross-Asset Exposure Limit Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    EXPOSURE_LIMIT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


CROSS_ASSET_LIMIT_ITEMS = [
    {"limit_id": "XAST_COMMODITY_TOTAL", "asset_group": "COMMODITIES", "max_share": 0.65, "description": "Toplam emtia varlik grubu tavan agirlik sozlesmesi."},
    {"limit_id": "XAST_FX_TOTAL", "asset_group": "FX", "max_share": 0.50, "description": "Toplam doviz varlik grubu tavan agirlik sozlesmesi."},
    {"limit_id": "XAST_CROSS_RATIO", "asset_group": "COMMODITY_TO_FX_RATIO", "max_share": 2.00, "description": "Emtia / FX oran dengesi sozlesme siniri."},
]


def build_cross_asset_exposure_limit_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for cross-asset exposure limit placeholders."""
    rows = []
    for item in CROSS_ASSET_LIMIT_ITEMS:
        rows.append({
            "limit_id": item["limit_id"],
            "asset_group": item["asset_group"],
            "max_share": item["max_share"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_cross_asset_hedging": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": EXPOSURE_LIMIT_DOMAIN,
        "category": "cross_asset_exposure_limit_placeholders",
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
