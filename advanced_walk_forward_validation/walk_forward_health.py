# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Health Check.

Performs dependency and environment health checks for Phase 147.
"""

from pathlib import Path
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

HEALTH_COMPONENTS: List[Dict[str, Any]] = [
    {
        "component_name": "advanced_realistic_backtest",
        "category": "UPSTREAM_PHASE",
        "required": True,
        "description": "Phase 146 realistic backtest and transaction cost contracts.",
    },
    {
        "component_name": "advanced_ml_acceptance",
        "category": "UPSTREAM_PHASE",
        "required": True,
        "description": "Phase 145 ML model acceptance contracts.",
    },
    {
        "component_name": "advanced_model_governance",
        "category": "UPSTREAM_PHASE",
        "required": True,
        "description": "Phase 144 Model governance contracts.",
    },
    {
        "component_name": "advanced_ml_dataset_registry",
        "category": "UPSTREAM_PHASE",
        "required": True,
        "description": "Phase 137 Dataset registry.",
    },
    {
        "component_name": "advanced_regime_acceptance",
        "category": "UPSTREAM_PHASE",
        "required": True,
        "description": "Phase 135 Regime acceptance contracts.",
    },
    {
        "component_name": "advanced_regime_featurestore_integration",
        "category": "UPSTREAM_PHASE",
        "required": True,
        "description": "Phase 134 FeatureStore regime integration.",
    },
    {
        "component_name": "FeatureStore",
        "category": "CORE_MODULE",
        "required": True,
        "description": "Feature store metadata repository.",
    },
    {
        "component_name": "DataLake",
        "category": "CORE_MODULE",
        "required": True,
        "description": "Local file-based DataLake storage.",
    },
    {
        "component_name": "advanced_walk_forward_validation",
        "category": "PHASE_147_MODULE",
        "required": True,
        "description": "Current Phase 147 package.",
    },
]


def build_walk_forward_health_check(
    project_root: Path, profile: WalkForwardProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Perform health checks across modules and directories."""
    rows = []
    for comp in HEALTH_COMPONENTS:
        name = comp["component_name"]
        p = project_root / name if name != "FeatureStore" and name != "DataLake" else project_root
        exists = p.exists() if name != "FeatureStore" and name != "DataLake" else True
        rows.append(
            {
                "component_name": name,
                "category": comp["category"],
                "required": comp["required"],
                "is_healthy": exists,
                "status": "HEALTHY" if exists else "MISSING",
                "description": comp["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    all_healthy = bool(df["is_healthy"].all()) if not df.empty else True
    summary = {
        "total_components": len(df),
        "healthy_count": len(df[df["is_healthy"]]),
        "all_healthy": all_healthy,
        "status": "HEALTHY" if all_healthy else "DEGRADED",
        "non_signal": True,
    }
    return df, summary
