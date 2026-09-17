# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Health Check.

Verifies subsystem availability and directory integrity for the realistic backtest contract layer.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

HEALTH_SUBSYSTEMS: List[Dict[str, Any]] = [
    {"subsystem": "advanced_ml_acceptance", "rel_path": "advanced_ml_acceptance", "description": "Phase 145 kabul raporu modulu."},
    {"subsystem": "advanced_model_governance", "rel_path": "advanced_model_governance", "description": "Phase 144 model yonetisim modulu."},
    {"subsystem": "advanced_ml_dataset_registry", "rel_path": "advanced_ml_dataset_registry", "description": "Phase 137 ML veri seti kayit defteri modulu."},
    {"subsystem": "advanced_regime_acceptance", "rel_path": "advanced_regime_acceptance", "description": "Phase 135 rejim kabul modulu."},
    {"subsystem": "advanced_regime_featurestore_integration", "rel_path": "advanced_regime_featurestore_integration", "description": "Phase 134 FeatureStore entegrasyon modulu."},
    {"subsystem": "feature_store", "rel_path": "ml/feature_store.py", "description": "FeatureStore merkezi modulu."},
    {"subsystem": "data_lake", "rel_path": "data/storage/data_lake.py", "description": "DataLake depolama katmani."},
    {"subsystem": "advanced_realistic_backtest", "rel_path": "advanced_realistic_backtest", "description": "Phase 146 gercekci backtest sozlesme modulu."},
    {"subsystem": "config_system", "rel_path": "config/settings.py", "description": "Konfigurasyon ayarlari."},
    {"subsystem": "scripts_directory", "rel_path": "scripts", "description": "Operasyonel CLI betikleri dizini."},
    {"subsystem": "tests_directory", "rel_path": "tests", "description": "Test suitleri dizini."},
    {"subsystem": "docs_directory", "rel_path": "docs", "description": "Proje dokumantasyon dizini."},
]


def build_realistic_backtest_health_check(
    project_root: Any = None,
    profile: Optional[RealisticBacktestProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Perform health checks across essential modules and directories."""
    if isinstance(project_root, RealisticBacktestProfile) and profile is None:
        profile = project_root
        project_root = Path(".")
    elif project_root is None:
        project_root = Path(".")
    root = Path(project_root)
    rows = []
    for sub in HEALTH_SUBSYSTEMS:
        target = root / sub["rel_path"]
        exists = target.exists()
        rows.append(
            {
                "subsystem": sub["subsystem"],
                "target_path": str(sub["rel_path"]),
                "description": sub["description"],
                "exists": exists,
                "status": "HEALTHY" if exists else "MISSING",
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_realistic_backtest_health_check(df)
    return df, summary


def summarize_realistic_backtest_health_check(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check results."""
    total = len(df)
    healthy_count = int((df["status"] == "HEALTHY").sum()) if not df.empty else 0
    all_healthy = (total > 0) and (healthy_count == total)
    return {
        "total_checks": total,
        "healthy_count": healthy_count,
        "all_healthy": all_healthy,
        "system_status": "ALL_SYSTEMS_OPERATIONAL" if all_healthy else "DEGRADED",
        "non_signal": True,
    }
