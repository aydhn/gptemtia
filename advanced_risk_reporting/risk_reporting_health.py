# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Health Check."""

from pathlib import Path
from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


def build_risk_reporting_health_check(
    project_root: Path = None,
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify integrity of upstream packages, FeatureStore, DataLake, and local Phase 155 structures."""
    if project_root is None:
        project_root = Path(__file__).resolve().parents[1]
    if profile is None:
        profile = get_default_risk_reporting_profile()

    checks = [
        ("advanced_portfolio_optimization", (project_root / "advanced_portfolio_optimization").exists()),
        ("advanced_portfolio_construction", (project_root / "advanced_portfolio_construction").exists()),
        ("advanced_backtest_acceptance", (project_root / "advanced_backtest_acceptance").exists()),
        ("advanced_benchmark_evaluation", (project_root / "advanced_benchmark_evaluation").exists()),
        ("advanced_backtest_governance", (project_root / "advanced_backtest_governance").exists()),
        ("advanced_monte_carlo_robustness", (project_root / "advanced_monte_carlo_robustness").exists()),
        ("advanced_stress_testing", (project_root / "advanced_stress_testing").exists()),
        ("advanced_walk_forward_validation", (project_root / "advanced_walk_forward_validation").exists()),
        ("advanced_realistic_backtest", (project_root / "advanced_realistic_backtest").exists()),
        ("advanced_ml_acceptance", (project_root / "advanced_ml_acceptance").exists()),
        ("advanced_model_governance", (project_root / "advanced_model_governance").exists()),
        ("advanced_ml_dataset_registry", (project_root / "advanced_ml_dataset_registry").exists()),
        ("advanced_regime_acceptance", (project_root / "advanced_regime_acceptance").exists()),
        ("advanced_regime_featurestore_integration", (project_root / "advanced_regime_featurestore_integration").exists()),
        ("FeatureStore", (project_root / "ml" / "feature_store.py").exists()),
        ("DataLake", (project_root / "data" / "storage" / "data_lake.py").exists()),
        ("advanced_risk_reporting", (project_root / "advanced_risk_reporting").exists()),
        ("scripts", (project_root / "scripts").exists()),
        ("tests", (project_root / "tests").exists()),
        ("docs", (project_root / "docs").exists()),
        ("config", (project_root / "config").exists()),
    ]

    rows = []
    for name, passed in checks:
        rows.append({
            "check_item": name,
            "passed": passed,
            "status": "PASS" if passed else "FAIL",
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "next_phase": profile.next_phase,
        })

    df = pd.DataFrame(rows)
    all_passed = bool(df["passed"].all()) if not df.empty else False
    summary = {
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()) if not df.empty else 0,
        "all_passed": all_passed,
        "status": "HEALTHY" if all_passed else "DEGRADED",
    }
    return df, summary
