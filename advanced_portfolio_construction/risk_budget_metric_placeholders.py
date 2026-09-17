# -*- coding: utf-8 -*-
"""Phase 153: Risk Budget Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


RISK_BUDGET_METRIC_ITEMS = [
    {"metric_id": "METRIC_BUDGET_UTILIZATION_PCT", "metric_name": "Risk Budget Utilization Percentage", "expected_type": "float", "description": "Risk butcesi kullanim orani metrik sozlesmesi."},
    {"metric_id": "METRIC_MARGINAL_RISK_CONTRIBUTION", "metric_name": "Marginal Risk Contribution (MRC)", "expected_type": "float", "description": "Marjinal risk katkisi metrik sozlesmesi."},
    {"metric_id": "METRIC_COMPONENT_RISK_CONTRIBUTION", "metric_name": "Component Value at Risk (CVaR)", "expected_type": "float", "description": "Bilesen risk katkisi metrik sozlesmesi."},
    {"metric_id": "METRIC_BUDGET_SLACK", "metric_name": "Risk Budget Slack Buffer", "expected_type": "float", "description": "Kullanilmayan risk butcesi payi metrik sozlesmesi."},
]


def build_risk_budget_metric_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for risk budget metric placeholders."""
    rows = []
    for item in RISK_BUDGET_METRIC_ITEMS:
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
        "domain": RISK_BUDGET_DOMAIN,
        "category": "risk_budget_metric_placeholders",
        "active_profile": profile.profile_name,
        "total_metrics": len(df),
        "all_calculations_disabled": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
