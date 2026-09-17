# -*- coding: utf-8 -*-
"""Phase 153: Currency Exposure Limit Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    EXPOSURE_LIMIT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


CURRENCY_LIMIT_ITEMS = [
    {"limit_id": "CCY_USD_BASE_LIMIT", "currency": "USD", "max_net_share": 0.80, "description": "USD bazli varlik veya sozlesmeler icin azami net pay sozlesmesi."},
    {"limit_id": "CCY_EUR_LIMIT", "currency": "EUR", "max_net_share": 0.40, "description": "EUR bazli varliklar icin azami net pay sozlesmesi."},
    {"limit_id": "CCY_TRY_LIMIT", "currency": "TRY", "max_net_share": 0.25, "description": "TRY bazli varliklar icin azami net pay sozlesmesi."},
    {"limit_id": "CCY_OTHER_G10_LIMIT", "currency": "OTHER_G10", "max_net_share": 0.30, "description": "Diger G10 para birimleri icin azami net pay sozlesmesi."},
]


def build_currency_exposure_limit_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for currency exposure limit placeholders."""
    rows = []
    for item in CURRENCY_LIMIT_ITEMS:
        rows.append({
            "limit_id": item["limit_id"],
            "currency": item["currency"],
            "max_net_share": item["max_net_share"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_currency_hedging_applied": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": EXPOSURE_LIMIT_DOMAIN,
        "category": "currency_exposure_limit_placeholders",
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
