# -*- coding: utf-8 -*-
"""Phase 153: Risk Parity Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    RISK_PARITY_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_risk_parity_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build risk parity sizing placeholder registry."""
    items = [
        {"placeholder_id": "RP_EQUAL_RISK_CONTRIB", "objective": "equal_risk_contribution", "lookback_window": 120, "description": "Esit risk katkisi (Equal Risk Contribution) pozisyon boyutlandirma taslagi."},
        {"placeholder_id": "RP_INVERSE_VOLATILITY", "objective": "inverse_volatility", "lookback_window": 60, "description": "Ters volatilite agirlikli pozisyon boyutlandirma taslagi."},
        {"placeholder_id": "RP_HIERARCHICAL_RISK", "objective": "hierarchical_risk_parity", "lookback_window": 120, "description": "Hiyerarsik risk esitligi (HRP) pozisyon boyutlandirma taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "objective": it["objective"],
            "lookback_window": it["lookback_window"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_lot_generated": False,
            "actual_weights_calculated": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": RISK_PARITY_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_zero_weights_calculated": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
