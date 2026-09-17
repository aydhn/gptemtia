# -*- coding: utf-8 -*-
"""Phase 153: Exposure Budget Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    EXPOSURE_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_exposure_budget_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build exposure budget placeholder registry."""
    items = [
        {"placeholder_id": "EXP_BUDGET_LONG_SHORT", "max_gross_exposure": 1.50, "max_net_exposure": 0.50, "description": "Long/short maruziyet butcesi: Brut %150, Net %50 taslagi."},
        {"placeholder_id": "EXP_BUDGET_MARKET_NEUTRAL", "max_gross_exposure": 1.00, "max_net_exposure": 0.10, "description": "Piyasa notr maruziyet butcesi: Brut %100, Net %10 taslagi."},
        {"placeholder_id": "EXP_BUDGET_CONSERVATIVE_LONG", "max_gross_exposure": 0.80, "max_net_exposure": 0.80, "description": "Muhafazakar uzun yonlu maruziyet butcesi: Brut %80, Net %80 taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "max_gross_exposure": it["max_gross_exposure"],
            "max_net_exposure": it["max_net_exposure"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_exposure_calculated": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": EXPOSURE_BUDGET_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
