# -*- coding: utf-8 -*-
"""Phase 153: Per-Regime Risk Budget Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    REGIME_RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_per_regime_risk_budget_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build per-regime risk budget placeholder registry."""
    items = [
        {"placeholder_id": "REG_BUDGET_NORMAL", "regime_state": "normal_volatility", "risk_multiplier": 1.0, "description": "Normal volatilite rejiminde tam risk butcesi taslagi."},
        {"placeholder_id": "REG_BUDGET_ELEVATED", "regime_state": "elevated_volatility", "risk_multiplier": 0.70, "description": "Yukselen volatilite rejiminde %70 risk butcesi taslagi."},
        {"placeholder_id": "REG_BUDGET_CRISIS", "regime_state": "crisis_regime", "risk_multiplier": 0.35, "description": "Kriz rejiminde %35 risk butcesi taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "regime_state": it["regime_state"],
            "risk_multiplier": it["risk_multiplier"],
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
        "domain": REGIME_RISK_BUDGET_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
