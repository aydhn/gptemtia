# -*- coding: utf-8 -*-
"""Phase 153: Confidence-Aware Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    CONFIDENCE_AWARE_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_confidence_aware_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build confidence-aware sizing placeholder registry."""
    items = [
        {"placeholder_id": "CONF_SIGMOID_SCALER", "scaling_method": "sigmoid_confidence", "min_confidence": 0.55, "max_confidence": 0.85, "description": "Sigmoid guven olcekleme taslagi."},
        {"placeholder_id": "CONF_LINEAR_SCALER", "scaling_method": "linear_clamped", "min_confidence": 0.50, "max_confidence": 0.80, "description": "Dogrusal kirpilmis guven olcekleme taslagi."},
        {"placeholder_id": "CONF_PROBABILITY_SPREAD", "scaling_method": "margin_of_victory", "min_confidence": 0.60, "max_confidence": 0.90, "description": "Olasilik farki marji guven olcekleme taslagi."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "scaling_method": it["scaling_method"],
            "min_confidence": it["min_confidence"],
            "max_confidence": it["max_confidence"],
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
        "domain": CONFIDENCE_AWARE_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
