# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Regime Dependencies."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    DEPENDENCY_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


REGIME_DEPENDENCIES = [
    {"dep_id": "DEP_REGIME_ACCEPTANCE_135", "component": "Phase 135 Regime Acceptance", "source_module": "advanced_regime_acceptance", "status": "SATISFIED", "description": "Piyasa rejim kabul raporu ve stabilite onaylari."},
    {"dep_id": "DEP_REGIME_FEATURESTORE_134", "component": "Phase 134 Regime FeatureStore", "source_module": "advanced_regime_featurestore_integration", "status": "SATISFIED", "description": "Rejim ozelik matrisinin FeatureStore entegrasyonu."},
    {"dep_id": "DEP_REGIME_TRANSITION_130", "component": "Phase 130 Regime Transition", "source_module": "advanced_regime_transition", "status": "SATISFIED", "description": "Rejim gecis olasiliklari ve kalicilik analizi."},
]


def build_portfolio_regime_dependency_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for regime dependencies."""
    rows = []
    for d in REGIME_DEPENDENCIES:
        rows.append({
            "dep_id": d["dep_id"],
            "component": d["component"],
            "source_module": d["source_module"],
            "status": d["status"],
            "description": d["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": DEPENDENCY_DOMAIN,
        "active_profile": profile.profile_name,
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
