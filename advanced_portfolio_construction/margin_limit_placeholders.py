# -*- coding: utf-8 -*-
"""Phase 153: Margin Limit Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    LEVERAGE_MARGIN_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


MARGIN_LIMIT_ITEMS = [
    {"limit_id": "MRG_INITIAL_MARGIN_MAX", "limit_name": "Initial Margin Max Utilization", "threshold": 0.50, "description": "Baslangic teminati maksimum kullanim orani sozlesme tanimi."},
    {"limit_id": "MRG_MAINTENANCE_MARGIN_BUFFER", "limit_name": "Maintenance Margin Buffer", "threshold": 0.30, "description": "Surdurme teminati guvenlik tamponu sozlesme tanimi."},
    {"limit_id": "MRG_FREE_MARGIN_MIN", "limit_name": "Free Margin Minimum Floor", "threshold": 0.20, "description": "Serbest teminat minimum alt taban sozlesme tanimi."},
]


def build_margin_limit_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for margin limit placeholders."""
    rows = []
    for item in MARGIN_LIMIT_ITEMS:
        rows.append({
            "limit_id": item["limit_id"],
            "limit_name": item["limit_name"],
            "threshold": item["threshold"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_margin_calculated": False,
            "broker_margin_checked": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": LEVERAGE_MARGIN_DOMAIN,
        "category": "margin_limit_placeholders",
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
