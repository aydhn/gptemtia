# -*- coding: utf-8 -*-
"""Phase 153: Portfolio FeatureStore Dependencies."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    DEPENDENCY_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


FEATURESTORE_DEPENDENCIES = [
    {"dep_id": "DEP_FEATURESTORE_INTEGRATION_124", "component": "Phase 124 FeatureStore Integration", "source_module": "ml.feature_store", "status": "SATISFIED", "description": "Merkezi FeatureStore katalog ve varlik kayitlari."},
    {"dep_id": "DEP_DATALAKE_STORAGE", "component": "DataLake Storage Layer", "source_module": "data.storage.data_lake", "status": "SATISFIED", "description": "Guvenli, yerel CSV/JSON tabanli DataLake katmani."},
    {"dep_id": "DEP_FEATURE_ENGINE_116_125", "component": "Phase 116-125 Feature Engine Block", "source_module": "advanced_feature_factor_acceptance", "status": "SATISFIED", "description": "Faktor kataloglari, teknik gostergeler ve capraz varlik matrisleri."},
]


def build_portfolio_featurestore_dependency_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for FeatureStore dependencies."""
    rows = []
    for d in FEATURESTORE_DEPENDENCIES:
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
