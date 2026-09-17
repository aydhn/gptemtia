# -*- coding: utf-8 -*-
"""Phase 153: Liquidity-Aware Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    LIQUIDITY_AWARE_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_liquidity_aware_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build liquidity-aware sizing placeholder registry."""
    items = [
        {"placeholder_id": "LIQ_ADV_CAP_1PCT", "constraint_type": "adv_participation_cap", "max_adv_fraction": 0.01, "description": "Gunluk ortalama hacmin (ADV) en fazla %1'i ile pozisyon sinirlayan taslak."},
        {"placeholder_id": "LIQ_ADV_CAP_2PCT", "constraint_type": "adv_participation_cap", "max_adv_fraction": 0.02, "description": "Gunluk ortalama hacmin (ADV) en fazla %2'si ile pozisyon sinirlayan taslak."},
        {"placeholder_id": "LIQ_SPREAD_DAMPING", "constraint_type": "spread_relative_damping", "max_adv_fraction": 0.005, "description": "Spread genislediginde pozisyon boyutunu otomatik kuculten taslak."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "constraint_type": it["constraint_type"],
            "max_adv_fraction": it["max_adv_fraction"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_lot_generated": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": LIQUIDITY_AWARE_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
