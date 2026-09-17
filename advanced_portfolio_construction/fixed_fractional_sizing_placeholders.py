# -*- coding: utf-8 -*-
"""Phase 153: Fixed Fractional Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    FIXED_FRACTIONAL_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_fixed_fractional_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build fixed fractional sizing placeholder registry."""
    items = [
        {"placeholder_id": "FF_CONSERVATIVE", "target_fraction": 0.01, "max_fraction": 0.02, "description": "Muhafazakar sabit fraksiyonel boyutlandirma taslagi (%1 sermaye riski)."},
        {"placeholder_id": "FF_MODERATE", "target_fraction": 0.02, "max_fraction": 0.03, "description": "Dengeli sabit fraksiyonel boyutlandirma taslagi (%2 sermaye riski)."},
        {"placeholder_id": "FF_DYNAMIC_CAP", "target_fraction": 0.015, "max_fraction": 0.025, "description": "Dinamik ust sinirli sabit fraksiyonel boyutlandirma taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "target_fraction": it["target_fraction"],
            "max_fraction": it["max_fraction"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_lot_generated": False,
            "actual_size_calculated": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": FIXED_FRACTIONAL_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_zero_lot_generated": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
