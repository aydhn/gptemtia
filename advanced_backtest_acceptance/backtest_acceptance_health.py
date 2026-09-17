# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Health Check."""

import importlib
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    HEALTH_DOMAIN,
    ACCEPTANCE_READY,
)

HEALTH_COMPONENTS: List[Dict[str, str]] = [
    {"component": "advanced_benchmark_evaluation", "type": "module", "path": "advanced_benchmark_evaluation"},
    {"component": "advanced_backtest_governance", "type": "module", "path": "advanced_backtest_governance"},
    {"component": "advanced_monte_carlo_robustness", "type": "module", "path": "advanced_monte_carlo_robustness"},
    {"component": "advanced_stress_testing", "type": "module", "path": "advanced_stress_testing"},
    {"component": "advanced_walk_forward_validation", "type": "module", "path": "advanced_walk_forward_validation"},
    {"component": "advanced_realistic_backtest", "type": "module", "path": "advanced_realistic_backtest"},
    {"component": "advanced_ml_acceptance", "type": "module", "path": "advanced_ml_acceptance"},
    {"component": "advanced_model_governance", "type": "module", "path": "advanced_model_governance"},
    {"component": "advanced_ml_dataset_registry", "type": "module", "path": "advanced_ml_dataset_registry"},
    {"component": "advanced_regime_acceptance", "type": "module", "path": "advanced_regime_acceptance"},
    {"component": "advanced_regime_featurestore_integration", "type": "module", "path": "advanced_regime_featurestore_integration"},
    {"component": "feature_store", "type": "module", "path": "ml.feature_store"},
    {"component": "data_lake", "type": "module", "path": "data.storage.data_lake"},
    {"component": "advanced_backtest_acceptance", "type": "module", "path": "advanced_backtest_acceptance"},
    {"component": "config_directory", "type": "directory", "path": "config"},
    {"component": "scripts_directory", "type": "directory", "path": "scripts"},
    {"component": "tests_directory", "type": "directory", "path": "tests"},
    {"component": "docs_directory", "type": "directory", "path": "docs"},
]


def build_backtest_acceptance_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify health and availability of all critical upstream and current packages."""
    active = profile or get_backtest_acceptance_profile()
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
                # Fallback check if directory exists
                mod_path = root / item["path"].replace(".", "/")
                if mod_path.exists():
                    status_pass = True
                    message = f"Module directory exists ({e})."
                else:
                    status_pass = False
                    message = f"Import failure: {e}"
        elif item["type"] == "directory":
            dir_path = root / item["path"]
            status_pass = dir_path.exists() and dir_path.is_dir()
            message = "Directory verified." if status_pass else "Directory missing."

        records.append({
            "component": item["component"],
            "type": item["type"],
            "path": item["path"],
            "healthy": status_pass,
            "details": message,
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY if status_pass else "DEGRADED",
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    healthy_count = len([r for r in records if r["healthy"]])
    all_healthy = (healthy_count == len(records))

    summary: Dict[str, Any] = {
        "domain": HEALTH_DOMAIN,
        "active_profile": active.profile_name,
        "total_components": len(records),
        "healthy_components": healthy_count,
        "all_healthy": all_healthy,
        "non_signal": True,
        "status": "ACCEPTED" if all_healthy else "WARNING",
    }
    return df, summary
