# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Health Check Module.

Verifies repository integrity, availability of upstream phases, and readiness
of dataset registry components without performing network calls or destructive actions.
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)


def build_advanced_ml_dataset_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Run health checks across prerequisites and environment components."""
    root = project_root or Path("c:/Projelerim/gptemtia")
    p = profile or get_default_advanced_ml_dataset_profile()

    checks = []

    def check_path(name: str, rel_path: str, category: str):
        path = root / rel_path
        exists = path.exists()
        checks.append({
            "component": name,
            "category": category,
            "path": str(rel_path),
            "status": "PASS" if exists else "FAIL",
            "exists": exists,
            "non_signal": True,
        })

    # Upstream module checks
    check_path("Phase 136 GPU ML Runtime", "advanced_gpu_ml_runtime", "upstream_dependency")
    check_path("Phase 135 Regime Acceptance", "advanced_regime_acceptance", "upstream_dependency")
    check_path("Phase 134 FeatureStore Integration", "advanced_regime_featurestore_integration", "upstream_dependency")
    check_path("Phase 133 Regime Validation", "advanced_regime_validation_acceptance", "upstream_dependency")
    check_path("Phase 124 Feature Store Integration", "advanced_feature_store_integration", "upstream_dependency")

    # Storage & core services
    check_path("FeatureStore Core", "ml/feature_store.py", "core_service")
    check_path("DataLake Storage", "data/storage/data_lake.py", "core_service")
    check_path("Settings Config", "config/settings.py", "configuration")
    check_path("Paths Config", "config/paths.py", "configuration")

    # Current module checks
    check_path("Phase 137 Module Root", "advanced_ml_dataset_registry", "current_module")
    check_path("Scripts Directory", "scripts", "execution")
    check_path("Tests Directory", "tests", "test_suite")
    check_path("Docs Directory", "docs", "documentation")

    df = pd.DataFrame(checks)
    summary = summarize_advanced_ml_dataset_health(df)
    return df, summary


def summarize_advanced_ml_dataset_health(df: pd.DataFrame) -> Dict:
    """Summarize health check results."""
    total = len(df)
    passed = int((df["status"] == "PASS").sum()) if "status" in df.columns else 0
    all_healthy = (total == passed) and total > 0

    return {
        "total_checks": total,
        "passed_checks": passed,
        "failed_checks": total - passed,
        "overall_health": "HEALTHY" if all_healthy else "DEGRADED",
        "all_healthy": all_healthy,
        "non_signal": True,
    }
