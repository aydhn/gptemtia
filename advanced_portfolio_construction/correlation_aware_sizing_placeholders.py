# -*- coding: utf-8 -*-
"""Phase 153: Correlation-Aware Sizing Placeholders."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    CORRELATION_AWARE_SIZING_PLACEHOLDER_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_correlation_aware_sizing_placeholder_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build correlation-aware sizing placeholder registry."""
    items = [
        {"placeholder_id": "CORR_PAIRWISE_DECORRELATION", "technique": "pairwise_shrinkage", "max_correlation": 0.70, "scale_penalty": 0.50, "description": "Ikili korelasyon esigini asan ciftlerde pozisyonu %50 kisan taslak."},
        {"placeholder_id": "CORR_CLUSTER_DISPERSION", "technique": "hierarchical_cluster_damping", "max_correlation": 0.60, "scale_penalty": 0.40, "description": "Kume ici korelasyon yogunlugunu kisan taslak."},
        {"placeholder_id": "CORR_DYNAMIC_BETA_DAMPING", "technique": "cross_asset_beta_control", "max_correlation": 0.75, "scale_penalty": 0.60, "description": "Capraz varlik beta ve korelasyon asiminda sonumleyici taslak."},
    ]
    rows = []
    for it in items:
        rows.append({
            "placeholder_id": it["placeholder_id"],
            "technique": it["technique"],
            "max_correlation": it["max_correlation"],
            "scale_penalty": it["scale_penalty"],
            "description": it["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "actual_scaling_applied": False,
            "investment_advice": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": CORRELATION_AWARE_SIZING_PLACEHOLDER_DOMAIN,
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_contract_only": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
