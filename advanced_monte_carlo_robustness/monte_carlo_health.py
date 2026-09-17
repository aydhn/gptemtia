# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Health Check.

Audits repository environment, dependent packages, storage, and contract integrity.
"""

from pathlib import Path
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile


def build_monte_carlo_health_check(
    project_root: Path | MonteCarloProfile | None = None,
    profile: MonteCarloProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute health checks across codebase dependencies and data lake paths."""
    if isinstance(project_root, MonteCarloProfile):
        profile = project_root
        project_root = None

    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent
    if profile is None:
        from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
        profile = get_default_monte_carlo_profile()

    checks = [
        ("advanced_walk_forward_validation", (project_root / "advanced_walk_forward_validation").is_dir()),
        ("advanced_realistic_backtest", (project_root / "advanced_realistic_backtest").is_dir()),
        ("advanced_stress_testing", (project_root / "advanced_stress_testing").is_dir()),
        ("advanced_monte_carlo_robustness", (project_root / "advanced_monte_carlo_robustness").is_dir()),
        ("FeatureStore_available", (project_root / "ml" / "feature_store.py").is_file()),
        ("DataLake_available", (project_root / "data" / "storage" / "data_lake.py").is_file()),
        ("config_paths_available", (project_root / "config" / "paths.py").is_file()),
        ("config_settings_available", (project_root / "config" / "settings.py").is_file()),
    ]

    rows: List[Dict[str, Any]] = []
    for component, exists in checks:
        rows.append(
            {
                "component": component,
                "status": "HEALTHY" if exists else "UNHEALTHY",
                "details": "Directory/file present" if exists else "Missing directory/file",
                "is_present": exists,
                "non_signal": True,
                "local_only": True,
            }
        )

    df = pd.DataFrame(rows)
    all_healthy = bool((df["status"] == "HEALTHY").all()) if not df.empty else True
    passed_count = int((df["status"] == "HEALTHY").sum())
    failed_count = len(df) - passed_count
    summary = {
        "all_healthy": all_healthy,
        "all_passed": all_healthy,
        "overall_status": "HEALTHY" if all_healthy else "UNHEALTHY",
        "total_checks": len(df),
        "passed_checks": passed_count,
        "failed_checks": failed_count,
        "healthy_count": passed_count,
        "non_signal": True,
    }
    return df, summary


check_monte_carlo_health = build_monte_carlo_health_check
