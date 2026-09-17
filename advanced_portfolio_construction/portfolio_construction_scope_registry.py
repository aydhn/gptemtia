# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Scope Registry."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_CONSTRUCTION_SCOPE_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


SCOPES = [
    {"scope_name": "local_offline_research", "target": "Offline research framework", "description": "Strictly local and offline execution boundaries"},
    {"scope_name": "commodity_fx_universe", "target": "Emtia-Doviz asset universe", "description": "Commodity and foreign exchange asset coverage"},
    {"scope_name": "contract_layer_only", "target": "Portfolio and sizing contracts", "description": "Contracts, metadata and placeholders only; zero actual trading or sizing"},
    {"scope_name": "non_production_governance", "target": "All portfolio components", "description": "Strict prohibition of live orders, broker integration, and investment advice"},
    {"scope_name": "phase_154_prerequisites", "target": "Optimization and allocation handoff", "description": "Prerequisite contracts for Phase 154 portfolio optimization"},
]


def build_portfolio_construction_scope_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for portfolio construction scopes."""
    rows = []
    for s in SCOPES:
        rows.append({
            "scope_name": s["scope_name"],
            "target": s["target"],
            "description": s["description"],
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "local_only": profile.local_only,
            "non_production": profile.non_production,
            "non_signal": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_CONSTRUCTION_SCOPE_DOMAIN,
        "active_profile": profile.profile_name,
        "total_scopes": len(df),
        "all_local_only": True,
        "all_non_production": True,
        "all_non_signal": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def summarize_portfolio_construction_scopes(df: pd.DataFrame) -> Dict:
    """Summarize portfolio construction scopes."""
    return {
        "total_scopes": len(df),
        "scopes": df["scope_name"].tolist() if not df.empty else [],
        "non_signal": True,
    }
