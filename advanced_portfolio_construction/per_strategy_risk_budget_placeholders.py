# -*- coding: utf-8 -*-
"""Phase 153: Per-Strategy Risk Budget Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    STRATEGY_RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_per_strategy_risk_budget_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build per-strategy risk budget placeholder registry."""
    items = [
        {"placeholder_id": "STRAT_TREND_BUDGET", "strategy_family": "trend_following", "risk_budget_share": 0.40, "description": "Trend takip stratejisine %40 risk butcesi taslagi."},
        {"placeholder_id": "STRAT_MEAN_REV_BUDGET", "strategy_family": "mean_reversion", "risk_budget_share": 0.30, "description": "Ortalamaya donus stratejisine %30 risk butcesi taslagi."},
        {"placeholder_id": "STRAT_MACRO_BUDGET", "strategy_family": "macro_event", "risk_budget_share": 0.30, "description": "Makro/haber stratejisine %30 risk butcesi taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "strategy_family": it["strategy_family"],
            "risk_budget_share": it["risk_budget_share"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_budget_calculated": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": STRATEGY_RISK_BUDGET_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
