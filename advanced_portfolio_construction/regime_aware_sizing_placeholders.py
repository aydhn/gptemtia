# -*- coding: utf-8 -*-
"""Phase 153: Regime-Aware Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    REGIME_AWARE_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_regime_aware_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build regime-aware sizing placeholder registry."""
    items = [
        {"placeholder_id": "REG_HIGH_VOL_SCALER", "regime_type": "high_volatility_crisis", "size_multiplier": 0.40, "description": "Yuksek volatilite/kriz rejiminde pozisyon boyutunu %40'a indiren taslak."},
        {"placeholder_id": "REG_TRENDING_BULL_SCALER", "regime_type": "trending_bull", "size_multiplier": 1.00, "description": "Guclu trend rejiminde standart pozisyon boyutlandirma taslagi."},
        {"placeholder_id": "REG_MEAN_REVERTING_SCALER", "regime_type": "choppy_range_bound", "size_multiplier": 0.60, "description": "Yatay ve dalgali rejimde temkinli boyutlandirma taslagi."},
        {"placeholder_id": "REG_LIQUIDITY_STRESS_SCALER", "regime_type": "liquidity_stress", "size_multiplier": 0.25, "description": "Likidite stresi rejiminde asgari pozisyon boyutlandirma taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "regime_type": it["regime_type"],
            "size_multiplier": it["size_multiplier"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_scaling_applied": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": REGIME_AWARE_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
