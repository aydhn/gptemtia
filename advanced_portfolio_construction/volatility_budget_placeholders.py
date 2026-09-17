# -*- coding: utf-8 -*-
"""Phase 153: Volatility Budget Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_volatility_budget_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build volatility budget placeholder registry."""
    items = [
        {"placeholder_id": "VOL_BUDGET_LOW_TARGET", "target_annual_vol": 0.08, "band_pct": 0.02, "description": "Dusuk risk profili icin yillik %8 (+/-%2) volatilite butcesi taslagi."},
        {"placeholder_id": "VOL_BUDGET_MEDIUM_TARGET", "target_annual_vol": 0.12, "band_pct": 0.03, "description": "Orta risk profili icin yillik %12 (+/-%3) volatilite butcesi taslagi."},
        {"placeholder_id": "VOL_BUDGET_HIGH_TARGET", "target_annual_vol": 0.18, "band_pct": 0.04, "description": "Yuksek risk profili icin yillik %18 (+/-%4) volatilite butcesi taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "target_annual_vol": it["target_annual_vol"],
            "band_pct": it["band_pct"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_volatility_calculated": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": RISK_BUDGET_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
