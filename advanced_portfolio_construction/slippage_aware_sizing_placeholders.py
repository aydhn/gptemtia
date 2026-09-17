# -*- coding: utf-8 -*-
"""Phase 153: Slippage-Aware Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    SLIPPAGE_AWARE_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_slippage_aware_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build slippage-aware sizing placeholder registry."""
    items = [
        {"placeholder_id": "SLIP_SQRT_IMPACT_MODEL", "impact_model": "square_root_market_impact", "impact_coeff": 0.10, "description": "Karekok piyasa etkisi kayma modeli taslagi."},
        {"placeholder_id": "SLIP_VOL_ADAPTIVE_IMPACT", "impact_model": "volatility_scaled_impact", "impact_coeff": 0.15, "description": "Volatiliteye duyarli kayma etkisi taslagi."},
        {"placeholder_id": "SLIPPAGE_TOLERANCE_CAP", "impact_model": "max_tolerable_slippage_cap", "impact_coeff": 0.05, "description": "Azami tolere edilebilir kayma limiti taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "impact_model": it["impact_model"],
            "impact_coeff": it["impact_coeff"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_slippage_calculated": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": SLIPPAGE_AWARE_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
