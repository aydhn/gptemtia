# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Health Check.

Performs verification of all packages, directories, and architectural components.
Enforces that components are intact and properly accessible.
"""

from pathlib import Path
from typing import Dict, Optional, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_HEALTH_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

HEALTH_CHECKS = [
    ("advanced_final_hardening", "package", "Phase 159 final hardening paketi mevcudiyeti"),
    ("advanced_full_system_integration", "package", "Phase 158 full system entegrasyon paketi mevcudiyeti"),
    ("advanced_portfolio_acceptance", "package", "Phase 157 portfoy kabul paketi mevcudiyeti"),
    ("advanced_portfolio_scenario_control", "package", "Phase 156 senaryo kontrol paketi mevcudiyeti"),
    ("advanced_risk_reporting", "package", "Phase 155 risk raporlama paketi mevcudiyeti"),
    ("advanced_portfolio_optimization", "package", "Phase 154 portfoy optimizasyon paketi mevcudiyeti"),
    ("advanced_portfolio_construction", "package", "Phase 153 portfoy insa paketi mevcudiyeti"),
    ("advanced_backtest_acceptance", "package", "Phase 152 backtest kabul paketi mevcudiyeti"),
    ("advanced_benchmark_evaluation", "package", "Phase 149 benchmark degerlendirme paketi mevcudiyeti"),
    ("advanced_backtest_governance", "package", "Phase 149 backtest yonetisim paketi mevcudiyeti"),
    ("advanced_monte_carlo_robustness", "package", "Phase 151 Monte Carlo paketi mevcudiyeti"),
    ("advanced_stress_testing", "package", "Phase 150 stres testi paketi mevcudiyeti"),
    ("advanced_walk_forward_validation", "package", "Phase 148 walk-forward paketi mevcudiyeti"),
    ("advanced_realistic_backtest", "package", "Phase 146 realistic backtest paketi mevcudiyeti"),
    ("advanced_ml_acceptance", "package", "Phase 145 ML kabul paketi mevcudiyeti"),
    ("advanced_model_governance", "package", "Phase 144 model yonetisim paketi mevcudiyeti"),
    ("advanced_feature_factor_acceptance", "package", "Phase 125 feature faktor kabul paketi mevcudiyeti"),
    ("advanced_feature_quality_drift", "package", "Phase 123 feature kalite drift paketi mevcudiyeti"),
    ("FeatureStore", "class", "ml/feature_store.py FeatureStore mevcudiyeti"),
    ("DataLake", "class", "data/storage/data_lake.py DataLake mevcudiyeti"),
    ("advanced_final_delivery", "package", "Phase 160 final delivery paketi mevcudiyeti"),
    ("scripts_present", "directory", "scripts/ CLI betikleri dizini mevcudiyeti"),
    ("tests_present", "directory", "tests/ test paketleri dizini mevcudiyeti"),
    ("docs_present", "directory", "docs/ dokumantasyon dizini mevcudiyeti"),
    ("config_present", "directory", "config/ konfigürasyon dizini mevcudiyeti"),
]


def build_final_delivery_health_check(
    project_root: Optional[Path] = None,
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build health check DataFrame and summary."""
    root = project_root or Path(__file__).resolve().parent.parent
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for check_name, check_type, desc in HEALTH_CHECKS:
        exists = True
        if check_type == "package":
            pkg_path = root / check_name
            exists = pkg_path.exists() and (pkg_path / "__init__.py").exists()
        elif check_type == "directory":
            dir_path = root / check_name.replace("_present", "")
            exists = dir_path.exists() and dir_path.is_dir()
        elif check_type == "class":
            if check_name == "FeatureStore":
                exists = (root / "ml" / "feature_store.py").exists()
            elif check_name == "DataLake":
                exists = (root / "data" / "storage" / "data_lake.py").exists()

        rows.append({
            "check_name": check_name,
            "check_type": check_type,
            "description": desc,
            "status": "HEALTHY" if exists else "DEFECT",
            "is_healthy": exists,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_HEALTH_DOMAIN,
        })

    df = pd.DataFrame(rows)
    all_healthy = bool(df["is_healthy"].all())
    summary = {
        "active_profile": active_profile.profile_name,
        "total_checks": len(rows),
        "healthy_checks": int(df["is_healthy"].sum()),
        "failed_checks": int((~df["is_healthy"]).sum()),
        "overall_status": "HEALTHY" if all_healthy else "UNHEALTHY",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if all_healthy else "HEALTH_CHECK_FAILED",
    }
    return df, summary
