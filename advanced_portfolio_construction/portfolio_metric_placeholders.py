# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_CONSTRUCTION_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


PORTFOLIO_METRIC_ITEMS = [
    {"metric_id": "METRIC_PORTFOLIO_VOLATILITY", "metric_name": "Portfolio Annualized Volatility", "expected_type": "float", "description": "Portfoy yilliklandirilmis oynaklik metrik sozlesmesi."},
    {"metric_id": "METRIC_SHARPE_RATIO", "metric_name": "Portfolio Sharpe Ratio", "expected_type": "float", "description": "Riskten arindirilmis getiri orani metrik sozlesmesi."},
    {"metric_id": "METRIC_SORTINO_RATIO", "metric_name": "Portfolio Sortino Ratio", "expected_type": "float", "description": "Asagi yonlu riske gore duzeltilmis getiri metrik sozlesmesi."},
    {"metric_id": "METRIC_MAX_DRAWDOWN", "metric_name": "Portfolio Maximum Drawdown", "expected_type": "float", "description": "Portfoy maksimum deger kaybi metrik sozlesmesi."},
    {"metric_id": "METRIC_VAR_95", "metric_name": "Value at Risk 95%", "expected_type": "float", "description": "Riske maruz deger (%95 guven) metrik sozlesmesi."},
    {"metric_id": "METRIC_EXPECTED_SHORTFALL_95", "metric_name": "Expected Shortfall (CVaR) 95%", "expected_type": "float", "description": "Kosullu riske maruz deger metrik sozlesmesi."},
    {"metric_id": "METRIC_CALMAR_RATIO", "metric_name": "Portfolio Calmar Ratio", "expected_type": "float", "description": "Yillik getiri / Max Drawdown orani metrik sozlesmesi."},
]


def build_portfolio_metric_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for portfolio metric placeholders."""
    rows = []
    for item in PORTFOLIO_METRIC_ITEMS:
        rows.append({
            "metric_id": item["metric_id"],
            "metric_name": item["metric_name"],
            "expected_type": item["expected_type"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "calculated_value": None,
            "calculation_disabled": True,
            "contract_only": True,
            "non_production": True,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_CONSTRUCTION_DOMAIN,
        "category": "portfolio_metric_placeholders",
        "active_profile": profile.profile_name,
        "total_metrics": len(df),
        "all_calculations_disabled": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
