# -*- coding: utf-8 -*-
"""Phase 153: Per-Asset Risk Budget Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    ASSET_RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_per_asset_risk_budget_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build per-asset risk budget placeholder registry."""
    items = [
        {"placeholder_id": "ASSET_RISK_CAP_5PCT", "max_risk_contribution": 0.05, "metric_ref": "marginal_var", "description": "Tekil varlik risk katkisini en fazla %5 ile sinirlayan taslak."},
        {"placeholder_id": "ASSET_RISK_CAP_10PCT", "max_risk_contribution": 0.10, "metric_ref": "marginal_var", "description": "Tekil varlik risk katkisini en fazla %10 ile sinirlayan taslak."},
        {"placeholder_id": "ASSET_VOL_WEIGHTED_CAP", "max_risk_contribution": 0.075, "metric_ref": "volatility_weighted_risk", "description": "Volatilite agirlikli tekil varlik risk butcesi taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "max_risk_contribution": it["max_risk_contribution"],
            "metric_ref": it["metric_ref"],
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
        "domain": ASSET_RISK_BUDGET_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
