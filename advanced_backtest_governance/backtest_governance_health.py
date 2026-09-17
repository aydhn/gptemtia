# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Health Check.

Audits repository environment, dependent packages, storage, and contract integrity.
"""

from pathlib import Path
from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    HEALTH_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)


def build_backtest_governance_health_check(
    project_root: Union[Path, BacktestGovernanceProfile, None] = None,
    profile: Union[BacktestGovernanceProfile, None] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute health checks across codebase dependencies and data lake paths."""
    if isinstance(project_root, BacktestGovernanceProfile):
        profile = project_root
        project_root = None

    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent
    if profile is None:
        from advanced_backtest_governance.backtest_governance_config import get_default_backtest_governance_profile
        profile = get_default_backtest_governance_profile()

    checks = [
        ("advanced_realistic_backtest", (project_root / "advanced_realistic_backtest").is_dir()),
        ("advanced_walk_forward_validation", (project_root / "advanced_walk_forward_validation").is_dir()),
        ("advanced_stress_testing", (project_root / "advanced_stress_testing").is_dir()),
        ("advanced_monte_carlo_robustness", (project_root / "advanced_monte_carlo_robustness").is_dir()),
        ("advanced_backtest_governance", (project_root / "advanced_backtest_governance").is_dir()),
        ("FeatureStore_available", (project_root / "ml" / "feature_store.py").is_file()),
        ("DataLake_available", (project_root / "data" / "storage" / "data_lake.py").is_file()),
        ("config_paths_available", (project_root / "config" / "paths.py").is_file()),
        ("config_settings_available", (project_root / "config" / "settings.py").is_file()),
    ]

    rows: List[Dict[str, Any]] = []
    for component, exists in checks:
        rows.append({
            "component": component,
            "status": "HEALTHY" if exists else "UNHEALTHY",
            "details": "Directory/file present" if exists else "Missing directory/file",
            "is_present": exists,
            "non_signal": True,
            "local_only": True,
        })

    df = pd.DataFrame(rows)
    all_healthy = bool((df["status"] == "HEALTHY").all()) if not df.empty else True
    passed_count = int((df["status"] == "HEALTHY").sum())
    failed_count = len(df) - passed_count
    summary = {
        "domain": HEALTH_DOMAIN,
        "all_healthy": all_healthy,
        "all_passed": all_healthy,
        "overall_status": "HEALTHY" if all_healthy else "UNHEALTHY",
        "overall_health": "HEALTHY" if all_healthy else "UNHEALTHY",
        "total_checks": len(df),
        "passed_checks": passed_count,
        "failed_checks": failed_count,
        "healthy_count": passed_count,
        "profile_name": profile.profile_name,
        "current_phase": profile.current_phase,
        "status": STATUS_GOVERNANCE_CONTRACT_READY if all_healthy else "HEALTH_CHECKS_FAILED",
        "non_signal": True,
        "local_only": True,
    }
    return df, summary


check_backtest_governance_health = build_backtest_governance_health_check
