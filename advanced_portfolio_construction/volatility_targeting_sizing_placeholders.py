# -*- coding: utf-8 -*-
"""Phase 153: Volatility Targeting Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    VOLATILITY_TARGETING_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_volatility_targeting_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build volatility targeting sizing placeholder registry."""
    items = [
        {"placeholder_id": "VT_ANNUAL_10PCT", "target_volatility": 0.10, "lookback_window": 60, "scaling_floor": 0.2, "scaling_cap": 2.0, "description": "Yillik %10 hedef volatilite boyutlandirma taslagi."},
        {"placeholder_id": "VT_ANNUAL_15PCT", "target_volatility": 0.15, "lookback_window": 60, "scaling_floor": 0.2, "scaling_cap": 2.0, "description": "Yillik %15 hedef volatilite boyutlandirma taslagi."},
        {"placeholder_id": "VT_ANNUAL_20PCT", "target_volatility": 0.20, "lookback_window": 30, "scaling_floor": 0.2, "scaling_cap": 2.0, "description": "Yillik %20 hedef volatilite boyutlandirma taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "target_volatility": it["target_volatility"],
            "lookback_window": it["lookback_window"],
            "scaling_floor": it["scaling_floor"],
            "scaling_cap": it["scaling_cap"],
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
        "domain": VOLATILITY_TARGETING_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_zero_lot_generated": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
