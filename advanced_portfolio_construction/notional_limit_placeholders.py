# -*- coding: utf-8 -*-
"""Phase 153: Notional Limit Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    EXPOSURE_LIMIT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


NOTIONAL_LIMIT_ITEMS = [
    {"limit_id": "NOT_MAX_TOTAL_NOTIONAL", "limit_name": "Maximum Total Notional Exposure", "limit_val": 1000000.0, "description": "Toplam portfoy itibari (notional) buyukluk sozlesme siniri."},
    {"limit_id": "NOT_MAX_PER_ASSET_NOTIONAL", "limit_name": "Maximum Per-Asset Notional Exposure", "limit_val": 200000.0, "description": "Tekil varlik basina azami itibari buyukluk sozlesme siniri."},
    {"limit_id": "NOT_MAX_SUBSECTOR_NOTIONAL", "limit_name": "Maximum Subsector Notional Exposure", "limit_val": 400000.0, "description": "Alt sektor basina azami itibari buyukluk sozlesme siniri."},
]


def build_notional_limit_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for notional limit placeholders."""
    rows = []
    for item in NOTIONAL_LIMIT_ITEMS:
        rows.append({
            "limit_id": item["limit_id"],
            "limit_name": item["limit_name"],
            "limit_val": item["limit_val"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_notional_computed": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": EXPOSURE_LIMIT_DOMAIN,
        "category": "notional_limit_placeholders",
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
