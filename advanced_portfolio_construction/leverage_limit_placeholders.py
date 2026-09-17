# -*- coding: utf-8 -*-
"""Phase 153: Leverage Limit Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    LEVERAGE_MARGIN_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


LEVERAGE_LIMIT_ITEMS = [
    {"limit_id": "LEV_MAX_ACCOUNT_LEVERAGE", "limit_name": "Maximum Account Leverage", "ceiling": 2.0, "description": "Hesap seviyesinde azami kaldirac tavani sozlesme tanimi."},
    {"limit_id": "LEV_REGIME_STRESS_CEILING", "limit_name": "Stress Regime Leverage Ceiling", "ceiling": 1.0, "description": "Stres rejimi durumunda kaldirac ust sinir sozlesme tanimi."},
    {"limit_id": "LEV_COMMODITY_SUBPORTFOLIO", "limit_name": "Commodity Subportfolio Leverage", "ceiling": 1.5, "description": "Emtia alt portfoyu kaldirac sinir sozlesme tanimi."},
]


def build_leverage_limit_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for leverage limit placeholders."""
    rows = []
    for item in LEVERAGE_LIMIT_ITEMS:
        rows.append({
            "limit_id": item["limit_id"],
            "limit_name": item["limit_name"],
            "ceiling": item["ceiling"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_leverage_enforced": False,
            "broker_leverage_applied": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": LEVERAGE_MARGIN_DOMAIN,
        "category": "leverage_limit_placeholders",
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
