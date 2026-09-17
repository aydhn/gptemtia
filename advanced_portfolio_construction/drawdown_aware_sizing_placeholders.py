# -*- coding: utf-8 -*-
"""Phase 153: Drawdown-Aware Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    DRAWDOWN_AWARE_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_drawdown_aware_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build drawdown-aware sizing placeholder registry."""
    items = [
        {"placeholder_id": "DD_LINEAR_THROTTLE", "mechanism": "linear_reduction", "trigger_drawdown": 0.05, "max_drawdown": 0.15, "min_scale": 0.20, "description": "Dogrusal cekilme kisma algoritmasi taslagi."},
        {"placeholder_id": "DD_STEPPED_BRAKE", "mechanism": "step_reduction", "trigger_drawdown": 0.08, "max_drawdown": 0.20, "min_scale": 0.00, "description": "Kademeli cekilme freni taslagi."},
        {"placeholder_id": "DD_VOL_SCALED_BRAKE", "mechanism": "volatility_scaled_drawdown", "trigger_drawdown": 0.06, "max_drawdown": 0.18, "min_scale": 0.10, "description": "Volatilite ile normalize edilmis cekilme freni taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "mechanism": it["mechanism"],
            "trigger_drawdown": it["trigger_drawdown"],
            "max_drawdown": it["max_drawdown"],
            "min_scale": it["min_scale"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_throttle_executed": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": DRAWDOWN_AWARE_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
