# -*- coding: utf-8 -*-
"""Phase 153: Liquidity Limit Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_CONSTRUCTION_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


LIQUIDITY_LIMIT_ITEMS = [
    {"limit_id": "LIQ_MIN_ADV_PARTICIPATION", "metric": "Max ADV Participation Rate", "threshold": 0.02, "description": "Gunluk ortalama hacmin (ADV) azami %2'si kadar teorik pozisyon buyuklugu sozlesme esigi."},
    {"limit_id": "LIQ_DAYS_TO_LIQUIDATE_MAX", "metric": "Max Days to Liquidate", "threshold": 2.0, "description": "Normal piyasa kosullarinda bir pozisyonun tasfiye suresinin azami 2 gun olmasi sozlesmesi."},
    {"limit_id": "LIQ_MIN_TURNOVER_BUFFER", "metric": "Minimum Turnover Buffer", "threshold": 0.05, "description": "Portfoy devir hizi guvenlik payi sozlesmesi."},
]


def build_liquidity_limit_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for liquidity limit placeholders."""
    rows = []
    for item in LIQUIDITY_LIMIT_ITEMS:
        rows.append({
            "limit_id": item["limit_id"],
            "metric": item["metric"],
            "threshold": item["threshold"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_liquidity_filtered": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_CONSTRUCTION_DOMAIN,
        "category": "liquidity_limit_placeholders",
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
