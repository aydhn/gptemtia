# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Model Governance Dependencies."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    DEPENDENCY_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


GOVERNANCE_DEPENDENCIES = [
    {"dep_id": "DEP_ML_ACCEPTANCE_145", "component": "Phase 145 ML Acceptance", "source_module": "advanced_ml_acceptance", "status": "SATISFIED", "description": "Makine ogrenimi kabul raporu ve model guvencesi."},
    {"dep_id": "DEP_MODEL_GOVERNANCE_144", "component": "Phase 144 Model Governance", "source_module": "advanced_model_governance", "status": "SATISFIED", "description": "Model risk yonetimi, yasam dongusu ve izinler."},
    {"dep_id": "DEP_EXPLAINABILITY_143", "component": "Phase 143 Explainability Attribution", "source_module": "advanced_explainability_attribution", "status": "SATISFIED", "description": "Oznitelik katki atfi ve aciklanabilirlik."},
    {"dep_id": "DEP_MODEL_DRIFT_142", "component": "Phase 142 Drift Monitoring", "source_module": "advanced_model_drift_monitoring", "status": "SATISFIED", "description": "Model ve kavram kaymasi (concept drift) izleme."},
]


def build_portfolio_model_governance_dependency_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for model governance dependencies."""
    rows = []
    for d in GOVERNANCE_DEPENDENCIES:
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
