# -*- coding: utf-8 -*-
"""Phase 153: Correlation Limit Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_CONSTRUCTION_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


CORRELATION_LIMIT_ITEMS = [
    {"limit_id": "CORR_PAIRWISE_MAX", "metric": "Pairwise Correlation Threshold", "max_allowed": 0.85, "description": "Iki varlik arasindaki korelasyonun bu esigi asmasi durumunda esanli maksimum agirlik kisiti sozlesmesi."},
    {"limit_id": "CORR_CLUSTER_MAX", "metric": "Cluster Average Correlation Threshold", "max_allowed": 0.75, "description": "Bir kume icindeki ortalama korelasyonun bu esigi asmasi durumunda kume tavan kisiti sozlesmesi."},
    {"limit_id": "CORR_ABSORPTION_RATIO_MAX", "metric": "Absorption Ratio Contract Threshold", "max_allowed": 0.80, "description": "Portfoy sistemik kirlilgani temsil eden emilim orani esik sozlesmesi."},
]


def build_correlation_limit_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for correlation limit placeholders."""
    rows = []
    for item in CORRELATION_LIMIT_ITEMS:
        rows.append({
            "limit_id": item["limit_id"],
            "metric": item["metric"],
            "max_allowed": item["max_allowed"],
            "description": item["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "real_correlation_matrix_calculated": False,
            "manual_review_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_CONSTRUCTION_DOMAIN,
        "category": "correlation_limit_placeholders",
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
