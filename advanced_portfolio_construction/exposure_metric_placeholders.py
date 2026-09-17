# -*- coding: utf-8 -*-
"""Phase 153: Exposure Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    EXPOSURE_LIMIT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


EXPOSURE_METRIC_ITEMS = [
    {"metric_id": "METRIC_GROSS_EXPOSURE_RATIO", "metric_name": "Gross Exposure Ratio", "expected_type": "float", "description": "Toplam brut maruziyet orani sozlesmesi."},
    {"metric_id": "METRIC_NET_EXPOSURE_RATIO", "metric_name": "Net Exposure Ratio", "expected_type": "float", "description": "Toplam net maruziyet orani sozlesmesi."},
    {"metric_id": "METRIC_LONG_EXPOSURE_RATIO", "metric_name": "Long Exposure Ratio", "expected_type": "float", "description": "Long yonlu maruziyet orani sozlesmesi."},
    {"metric_id": "METRIC_SHORT_EXPOSURE_RATIO", "metric_name": "Short Exposure Ratio", "expected_type": "float", "description": "Short yonlu maruziyet orani sozlesmesi."},
]


def build_exposure_metric_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for exposure metric placeholders."""
    rows = []
    for item in EXPOSURE_METRIC_ITEMS:
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
        "domain": EXPOSURE_LIMIT_DOMAIN,
        "category": "exposure_metric_placeholders",
        "active_profile": profile.profile_name,
        "total_metrics": len(df),
        "all_calculations_disabled": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
