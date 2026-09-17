# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Health Check."""

import importlib
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_construction_config import (
    PortfolioConstructionProfile,
    get_default_portfolio_construction_profile,
)
from .portfolio_construction_labels import (
    PORTFOLIO_HEALTH_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

HEALTH_COMPONENTS: List[Dict[str, str]] = [
    {"component": "advanced_portfolio_construction", "type": "module", "path": "advanced_portfolio_construction"},
    {"component": "advanced_backtest_acceptance", "type": "module", "path": "advanced_backtest_acceptance"},
    {"component": "advanced_benchmark_evaluation", "type": "module", "path": "advanced_benchmark_evaluation"},
    {"component": "advanced_backtest_governance", "type": "module", "path": "advanced_backtest_governance"},
    {"component": "advanced_model_governance", "type": "module", "path": "advanced_model_governance"},
    {"component": "advanced_regime_featurestore_integration", "type": "module", "path": "advanced_regime_featurestore_integration"},
    {"component": "data_lake", "type": "module", "path": "data.storage.data_lake"},
    {"component": "feature_store", "type": "module", "path": "ml.feature_store"},
    {"component": "config_directory", "type": "directory", "path": "config"},
    {"component": "scripts_directory", "type": "directory", "path": "scripts"},
    {"component": "tests_directory", "type": "directory", "path": "tests"},
    {"component": "docs_directory", "type": "directory", "path": "docs"},
]


def build_portfolio_construction_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[PortfolioConstructionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify health and availability of all critical upstream and current packages."""
    active = profile or get_default_portfolio_construction_profile()
    root = project_root or Path(".")

    records = []
    for item in HEALTH_COMPONENTS:
        status_pass = False
        message = ""

        if item["type"] == "module":
            try:
                importlib.import_module(item["path"])
                status_pass = True
                message = "Module imported successfully."
            except Exception as e:
                mod_path = root / item["path"].replace(".", "/")
                if mod_path.exists() or (mod_path.with_suffix(".py")).exists():
                    status_pass = True
                    message = "Module file exists on path."
                else:
                    message = f"Import error: {str(e)}"
        elif item["type"] == "directory":
            dir_path = root / item["path"]
            if dir_path.exists() and dir_path.is_dir():
                status_pass = True
                message = "Directory exists."
            else:
                message = f"Directory not found: {dir_path}"

        records.append({
            "component": item["component"],
            "type": item["type"],
            "path": item["path"],
            "status_pass": status_pass,
            "message": message,
            "current_phase": active.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": PORTFOLIO_CONTRACT_READY if status_pass else "HEALTH_DEGRADED",
        })

    df = pd.DataFrame(records)
    all_healthy = df["status_pass"].all()

    summary: Dict[str, Any] = {
        "domain": PORTFOLIO_HEALTH_DOMAIN,
        "active_profile": active.profile_name,
        "total_components": len(records),
        "healthy_count": int(df["status_pass"].sum()),
        "all_healthy": bool(all_healthy),
        "status": PORTFOLIO_CONTRACT_READY if all_healthy else "HEALTH_DEGRADED",
    }
    return df, summary
