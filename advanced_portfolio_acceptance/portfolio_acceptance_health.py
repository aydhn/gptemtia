# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Health Check.

Verifies structural availability and module integrity of all required
system components before declaring acceptance readiness.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    HEALTH_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

HEALTH_CHECKS = [
    ("advanced_portfolio_scenario_control", "Phase 156 Scenario & Drawdown Control module present"),
    ("advanced_risk_reporting", "Phase 155 Risk Reporting module present"),
    ("advanced_portfolio_optimization", "Phase 154 Portfolio Optimization module present"),
    ("advanced_portfolio_construction", "Phase 153 Portfolio Construction module present"),
    ("advanced_backtest_acceptance", "Phase 152 Backtest Acceptance module present"),
    ("advanced_benchmark_evaluation", "Phase 151 Benchmark Evaluation module present"),
    ("advanced_backtest_governance", "Phase 150 Backtest Governance module present"),
    ("advanced_monte_carlo_robustness", "Phase 149 Monte Carlo Robustness module present"),
    ("advanced_stress_testing", "Phase 148 Stress Testing module present"),
    ("advanced_walk_forward_validation", "Phase 147 Walk-Forward Validation module present"),
    ("advanced_realistic_backtest", "Phase 146 Realistic Backtest module present"),
    ("advanced_ml_acceptance", "Phase 145 ML Acceptance module present"),
    ("advanced_model_governance", "Phase 144 Model Governance module present"),
    ("advanced_ml_dataset_registry", "Phase 137 ML Dataset Registry module present"),
    ("advanced_regime_acceptance", "Phase 135 Regime Acceptance module present"),
    ("advanced_regime_featurestore_integration", "Phase 134 Regime FeatureStore module present"),
    ("data_storage_data_lake", "DataLake storage subsystem available"),
    ("ml_feature_store", "FeatureStore subsystem available"),
    ("advanced_portfolio_acceptance", "Phase 157 Portfolio Acceptance module present"),
    ("config_paths_scripts_tests", "Project configuration, paths, scripts, and tests present"),
]


def build_portfolio_acceptance_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute health check verifying all module dependencies exist on filesystem."""
    root = project_root or Path(__file__).resolve().parent.parent
    active = profile or get_portfolio_acceptance_profile()

    records = []
    for check_id, description in HEALTH_CHECKS:
        exists = True
        if check_id == "data_storage_data_lake":
            exists = (root / "data" / "storage" / "data_lake.py").exists()
        elif check_id == "ml_feature_store":
            exists = (root / "ml" / "feature_store.py").exists()
        elif check_id == "config_paths_scripts_tests":
            exists = (root / "config" / "settings.py").exists() and (root / "scripts").exists() and (root / "tests").exists()
        else:
            exists = (root / check_id).exists()

        records.append({
            "check_id": check_id,
            "description": description,
            "status": "PASS" if exists else "FAIL",
            "passed": exists,
            "current_phase": active.current_phase,
        })

    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_health(df)
    return df, summary


def summarize_portfolio_acceptance_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    all_passed = bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False
    passed_count = int(df["passed"].sum()) if not df.empty and "passed" in df.columns else 0
    return {
        "domain": HEALTH_DOMAIN,
        "total_checks": len(df),
        "passed_checks": passed_count,
        "failed_checks": len(df) - passed_count,
        "all_passed": all_passed,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_passed else "HEALTH_DEGRADED",
    }
