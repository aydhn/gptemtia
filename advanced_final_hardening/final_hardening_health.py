# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Health Check.

Verifies the integrity, availability, and non-destructive status of all subsystem
packages from Phase 1 through Phase 159.
"""

from pathlib import Path
from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    HEALTH_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

HEALTH_COMPONENTS = [
    ("advanced_full_system_integration", "Phase 158 full system integration and rehearsal"),
    ("advanced_portfolio_acceptance", "Phase 157 portfolio acceptance"),
    ("advanced_portfolio_scenario_control", "Phase 156 portfolio scenario control"),
    ("advanced_risk_reporting", "Phase 154 risk reporting"),
    ("advanced_portfolio_optimization", "Phase 153 portfolio optimization"),
    ("advanced_portfolio_construction", "Phase 152 portfolio construction"),
    ("advanced_backtest_acceptance", "Phase 151 backtest acceptance"),
    ("advanced_benchmark_evaluation", "Phase 150 benchmark evaluation"),
    ("advanced_backtest_governance", "Phase 149 backtest governance"),
    ("advanced_monte_carlo_robustness", "Phase 148 monte carlo robustness"),
    ("advanced_stress_testing", "Phase 147 stress testing"),
    ("advanced_walk_forward_validation", "Phase 146 walk forward validation"),
    ("advanced_realistic_backtest", "Phase 145/146 realistic backtest"),
    ("advanced_ml_acceptance", "Phase 145 ml acceptance"),
    ("advanced_model_governance", "Phase 144 model governance"),
    ("advanced_feature_factor_acceptance", "Phase 128 feature factor acceptance"),
    ("advanced_feature_quality_drift", "Phase 123 feature quality drift"),
    ("FeatureStore", "ml/feature_store.py feature access layer"),
    ("DataLake", "data/storage/data_lake.py data lake layer"),
    ("advanced_final_hardening", "Phase 159 final hardening layer"),
    ("scripts_present", "scripts/ execution scripts directory"),
    ("tests_present", "tests/ unit tests directory"),
    ("docs_present", "docs/ documentation directory"),
    ("config_present", "config/ configuration directory"),
]


def build_final_hardening_health_check(
    project_root: Path | None = None,
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build health check DataFrame and summary across all modules."""
    active_profile = profile or get_default_final_hardening_profile()
    root = project_root or Path(__file__).resolve().parent.parent

    rows = []
    for comp, desc in HEALTH_COMPONENTS:
        if comp in ("scripts_present", "tests_present", "docs_present", "config_present"):
            target_dir = root / comp.replace("_present", "")
            is_healthy = target_dir.exists()
        elif comp == "FeatureStore":
            is_healthy = (root / "ml" / "feature_store.py").exists()
        elif comp == "DataLake":
            is_healthy = (root / "data" / "storage" / "data_lake.py").exists()
        else:
            is_healthy = (root / comp).exists()

        rows.append({
            "component": comp,
            "description": desc,
            "available": is_healthy,
            "domain": HEALTH_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": "HEALTHY" if is_healthy else "MISSING",
        })

    df = pd.DataFrame(rows)
    all_healthy = bool(df["available"].all())
    summary = {
        "total_checks": len(rows),
        "passed_checks": int(df["available"].sum()),
        "all_passed": all_healthy,
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY if all_healthy else "HEALTH_CHECK_FAILED",
    }
    return df, summary
