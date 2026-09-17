# -*- coding: utf-8 -*-
"""Phase 153: Sizing Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    POSITION_SIZING_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


SIZING_METRIC_ITEMS = [
    {"metric_id": "METRIC_SIZING_AVERAGE_FRACTION", "metric_name": "Average Position Fraction", "expected_type": "float", "description": "Pozisyon basina ortalama portfoy payi metrik sozlesmesi."},
    {"metric_id": "METRIC_SIZING_MAX_FRACTION", "metric_name": "Maximum Position Fraction", "expected_type": "float", "description": "Pozisyon basina azami portfoy payi metrik sozlesmesi."},
    {"metric_id": "METRIC_SIZING_EFFECTIVE_BETS", "metric_name": "Effective Number of Bets", "expected_type": "float", "description": "Etkin bagimsiz pozisyon sayisi metrik sozlesmesi."},
    {"metric_id": "METRIC_SIZING_TURNOVER_RATE", "metric_name": "Implied Sizing Turnover Rate", "expected_type": "float", "description": "Boyutlandirma degisim devir hizi metrik sozlesmesi."},
]


def build_sizing_metric_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for sizing metric placeholders."""
    rows = []
    for item in SIZING_METRIC_ITEMS:
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
        "domain": POSITION_SIZING_DOMAIN,
        "category": "sizing_metric_placeholders",
        "active_profile": profile.profile_name,
        "total_metrics": len(df),
        "all_calculations_disabled": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
