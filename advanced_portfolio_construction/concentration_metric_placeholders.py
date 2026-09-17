# -*- coding: utf-8 -*-
"""Phase 153: Concentration Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    CONCENTRATION_LIMIT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


CONCENTRATION_METRIC_ITEMS = [
    {"metric_id": "METRIC_HERFINDAHL_HIRSCHMAN_INDEX", "metric_name": "Herfindahl-Hirschman Index (HHI)", "expected_type": "float", "description": "Portfoy yogunlasma HHI endeksi metrik sozlesmesi."},
    {"metric_id": "METRIC_MAX_ASSET_WEIGHT", "metric_name": "Maximum Asset Weight", "expected_type": "float", "description": "Portfoydeki en buyuk tekil varlik agirligi metrik sozlesmesi."},
    {"metric_id": "METRIC_TOP_3_WEIGHT_SUM", "metric_name": "Top 3 Assets Weight Sum", "expected_type": "float", "description": "En buyuk 3 varligin toplam agirligi metrik sozlesmesi."},
    {"metric_id": "METRIC_GINI_COEFFICIENT", "metric_name": "Asset Allocation Gini Coefficient", "expected_type": "float", "description": "Agirlik dagilim esitsizligi (Gini) metrik sozlesmesi."},
]


def build_concentration_metric_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for concentration metric placeholders."""
    rows = []
    for item in CONCENTRATION_METRIC_ITEMS:
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
        "domain": CONCENTRATION_LIMIT_DOMAIN,
        "category": "concentration_metric_placeholders",
        "active_profile": profile.profile_name,
        "total_metrics": len(df),
        "all_calculations_disabled": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
