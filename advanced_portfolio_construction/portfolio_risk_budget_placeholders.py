# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Risk Budget Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_risk_budget_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build portfolio overall risk budget placeholder registry."""
    items = [
        {"placeholder_id": "PORT_VAR_95_BUDGET", "risk_metric": "VaR_95_1day", "budget_limit_pct": 0.02, "description": "Gunluk %95 VaR limitini portfoyun %2'si ile sinirlayan taslak."},
        {"placeholder_id": "PORT_ES_975_BUDGET", "risk_metric": "ES_97.5_1day", "budget_limit_pct": 0.035, "description": "Gunluk %97.5 Beklenen Kayip (ES) limitini %3.5 ile sinirlayan taslak."},
        {"placeholder_id": "PORT_VOL_ANNUAL_BUDGET", "risk_metric": "annualized_volatility", "budget_limit_pct": 0.16, "description": "Yilliklandirilmis toplam volatilite limitini %16 ile sinirlayan taslak."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "risk_metric": it["risk_metric"],
            "budget_limit_pct": it["budget_limit_pct"],
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
        "domain": PORTFOLIO_RISK_BUDGET_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
