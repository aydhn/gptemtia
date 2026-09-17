# -*- coding: utf-8 -*-
"""Phase 153: Drawdown Budget Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_drawdown_budget_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build drawdown budget placeholder registry."""
    items = [
        {"placeholder_id": "DD_BUDGET_SOFT_ALERT", "threshold_pct": 0.05, "action": "alert_and_monitor", "description": "%5 cekilmede uyari ve yakin takip tetikleyen taslak."},
        {"placeholder_id": "DD_BUDGET_MODERATE_BRAKE", "threshold_pct": 0.10, "action": "reduce_exposure_25pct", "description": "%10 cekilmede maruziyeti %25 azaltan fren taslagi."},
        {"placeholder_id": "DD_BUDGET_HARD_STOP", "threshold_pct": 0.15, "action": "reduce_exposure_75pct", "description": "%15 cekilmede acil koruma modunu tetikleyen sert fren taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "threshold_pct": it["threshold_pct"],
            "action": it["action"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_drawdown_calculated": False,
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
