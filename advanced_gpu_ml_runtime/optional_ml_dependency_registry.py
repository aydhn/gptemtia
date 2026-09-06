"""Phase 136: Optional ML Dependency Registry.

Safely checks optional ML, gradient boosting, explainability, optimization,
and serialisation dependencies without executing training, tracking servers, or network calls.
"""

import importlib
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    OPTIONAL_DEPENDENCY_DOMAIN,
    RUNTIME_READY,
    RUNTIME_PLACEHOLDER_ONLY,
    BACKEND_OPTIONAL_DEPENDENCY_MISSING,
)


OPTIONAL_PACKAGES = [
    "xgboost",
    "lightgbm",
    "catboost",
    "optuna",
    "shap",
    "onnx",
    "skl2onnx",
    "joblib",
    "mlflow",
    "polars",
    "pyarrow",
]


def safe_detect_optional_dependencies(
    package_names: Optional[List[str]] = None,
) -> Dict[str, Dict[str, Any]]:
    """Safely check which optional ML libraries are available in the local environment."""
    target_pkgs = package_names or OPTIONAL_PACKAGES
    results: Dict[str, Dict[str, Any]] = {}

    for pkg in target_pkgs:
        try:
            mod = importlib.import_module(pkg)
            ver = str(getattr(mod, "__version__", "installed"))
            results[pkg] = {
                "installed": True,
                "version": ver,
                "status": RUNTIME_READY,
            }
        except ImportError:
            results[pkg] = {
                "installed": False,
                "version": "not_installed",
                "status": RUNTIME_PLACEHOLDER_ONLY,
            }
        except Exception as ex:
            results[pkg] = {
                "installed": False,
                "version": f"error: {str(ex)[:30]}",
                "status": RUNTIME_PLACEHOLDER_ONLY,
            }

    return results


def build_optional_ml_dependency_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for optional ML dependencies."""
    active = profile or get_gpu_ml_runtime_profile()
    deps = safe_detect_optional_dependencies()

    rows: List[Dict[str, Any]] = []
    for pkg_name, info in deps.items():
        rows.append(
            {
                "dependency_id": f"opt_{pkg_name}",
                "package_name": pkg_name,
                "installed": info["installed"],
                "version": info["version"],
                "backend_label": pkg_name if info["installed"] else BACKEND_OPTIONAL_DEPENDENCY_MISSING,
                "status_label": info["status"],
                "manual_review_required": not info["installed"],
                "non_signal": True,
                "source_preserved": True,
                "details": f"Optional advanced ML component: {pkg_name} ({info['version']}).",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_optional_ml_dependencies(df)
    summary["domain"] = OPTIONAL_DEPENDENCY_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_optional_ml_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize optional ML dependencies DataFrame."""
    inst_count = int(df["installed"].sum()) if not df.empty and "installed" in df.columns else 0
    return {
        "total_optional_packages": len(df),
        "installed_count": inst_count,
        "missing_count": len(df) - inst_count,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
