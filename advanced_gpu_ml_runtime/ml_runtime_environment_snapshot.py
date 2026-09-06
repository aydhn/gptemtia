"""Phase 136: ML Runtime Environment Snapshot.

Produces a safe, reproducible operational snapshot of the local ML runtime environment
without reading .env secrets, user credentials, or private path trees.
"""

import platform
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    ENVIRONMENT_SNAPSHOT_DOMAIN,
    RUNTIME_READY,
)
from advanced_gpu_ml_runtime.gpu_capability_registry import safe_detect_gpu_capability
from advanced_gpu_ml_runtime.torch_runtime_capability import safe_detect_torch_runtime
from advanced_gpu_ml_runtime.sklearn_runtime_capability import safe_detect_sklearn_runtime
from advanced_gpu_ml_runtime.numpy_pandas_runtime_capability import safe_detect_numpy_pandas_runtime


def safe_collect_runtime_snapshot() -> Dict[str, Any]:
    """Gather environment snapshot metadata safely."""
    gpu_info = safe_detect_gpu_capability()
    torch_info = safe_detect_torch_runtime()
    sk_info = safe_detect_sklearn_runtime()
    np_pd_info = safe_detect_numpy_pandas_runtime()

    return {
        "python_version": platform.python_version(),
        "platform_safe_name": f"{platform.system()} {platform.machine()}",
        "cuda_available": gpu_info["cuda_available"],
        "gpu_available": gpu_info["cuda_available"],
        "torch_available": torch_info["installed"],
        "sklearn_available": sk_info["installed"],
        "numpy_available": np_pd_info["numpy_installed"],
        "pandas_available": np_pd_info["pandas_installed"],
        "non_production": True,
        "local_only": True,
        "dry_run": True,
        "non_signal": True,
    }


def build_ml_runtime_environment_snapshot(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for ML runtime environment snapshot."""
    active = profile or get_gpu_ml_runtime_profile()
    snap = safe_collect_runtime_snapshot()

    rows: List[Dict[str, Any]] = [
        {"property": "python_version", "value": snap["python_version"], "category": "runtime"},
        {"property": "platform_safe_name", "value": snap["platform_safe_name"], "category": "platform"},
        {"property": "cuda_available", "value": str(snap["cuda_available"]), "category": "accelerator"},
        {"property": "gpu_available", "value": str(snap["gpu_available"]), "category": "accelerator"},
        {"property": "torch_available", "value": str(snap["torch_available"]), "category": "dependency"},
        {"property": "sklearn_available", "value": str(snap["sklearn_available"]), "category": "dependency"},
        {"property": "numpy_available", "value": str(snap["numpy_available"]), "category": "dependency"},
        {"property": "pandas_available", "value": str(snap["pandas_available"]), "category": "dependency"},
        {"property": "non_production", "value": str(snap["non_production"]), "category": "boundary"},
        {"property": "local_only", "value": str(snap["local_only"]), "category": "boundary"},
        {"property": "dry_run", "value": str(snap["dry_run"]), "category": "boundary"},
        {"property": "non_signal", "value": str(snap["non_signal"]), "category": "boundary"},
    ]

    for r in rows:
        r["status_label"] = RUNTIME_READY
        r["non_signal"] = True
        r["source_preserved"] = True

    df = pd.DataFrame(rows)
    summary = summarize_ml_runtime_environment_snapshot(df)
    summary["domain"] = ENVIRONMENT_SNAPSHOT_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_runtime_environment_snapshot(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ML runtime environment snapshot DataFrame."""
    return {
        "total_properties": len(df),
        "status_label": RUNTIME_READY,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
