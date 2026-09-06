"""Phase 136: GPU ML Runtime Health Check.

Verifies presence of upstream acceptance modules, FeatureStore integration,
DataLake persistence, scripts, tests, and configuration.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    HEALTH_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
)


HEALTH_COMPONENTS = [
    {"name": "advanced_regime_acceptance", "type": "module", "path": "advanced_regime_acceptance"},
    {"name": "advanced_regime_featurestore_integration", "type": "module", "path": "advanced_regime_featurestore_integration"},
    {"name": "advanced_regime_validation_acceptance", "type": "module", "path": "advanced_regime_validation_acceptance"},
    {"name": "advanced_feature_store_integration", "type": "module", "path": "advanced_feature_store_integration"},
    {"name": "feature_store", "type": "file", "path": "ml/feature_store.py"},
    {"name": "data_lake", "type": "file", "path": "data/storage/data_lake.py"},
    {"name": "advanced_gpu_ml_runtime", "type": "module", "path": "advanced_gpu_ml_runtime"},
    {"name": "scripts", "type": "directory", "path": "scripts"},
    {"name": "tests", "type": "directory", "path": "tests"},
    {"name": "docs", "type": "directory", "path": "docs"},
    {"name": "config", "type": "directory", "path": "config"},
]


def build_gpu_ml_runtime_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for GPU ML runtime health check."""
    active = profile or get_gpu_ml_runtime_profile()
    root = project_root or Path.cwd()

    rows: List[Dict[str, Any]] = []
    for comp in HEALTH_COMPONENTS:
        target_path = root / comp["path"]
        exists = target_path.exists()
        rows.append(
            {
                "component_name": comp["name"],
                "component_type": comp["type"],
                "target_path": str(comp["path"]),
                "exists": exists,
                "status_label": RUNTIME_READY if exists else RUNTIME_READY_WITH_WARNINGS,
                "manual_review_required": not exists,
                "non_signal": True,
                "source_preserved": True,
                "details": f"{comp['name']} is available." if exists else f"{comp['name']} missing from repository.",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_gpu_ml_runtime_health(df)
    summary["domain"] = HEALTH_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_gpu_ml_runtime_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize GPU ML runtime health check DataFrame."""
    all_ok = bool(df["exists"].all()) if not df.empty and "exists" in df.columns else False
    return {
        "total_components": len(df),
        "all_healthy": all_ok,
        "status": "HEALTHY" if all_ok else "DEGRADED",
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
