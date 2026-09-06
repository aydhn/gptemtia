"""Phase 136: Scikit-Learn Runtime Capability Report.

Safely detects scikit-learn presence and version without creating estimators,
fitting parameters, predicting values, or modifying features.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    SKLEARN_CAPABILITY_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    BACKEND_SKLEARN_AVAILABLE,
    BACKEND_OPTIONAL_DEPENDENCY_MISSING,
)


def safe_detect_sklearn_runtime() -> Dict[str, Any]:
    """Safely check scikit-learn import and version."""
    installed = False
    version = "not_installed"

    try:
        import sklearn
        installed = True
        version = str(getattr(sklearn, "__version__", "unknown"))
    except ImportError:
        pass
    except Exception:
        pass

    return {
        "installed": installed,
        "version": version,
    }


def build_sklearn_runtime_capability_report(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for scikit-learn capability."""
    active = profile or get_gpu_ml_runtime_profile()
    sk_info = safe_detect_sklearn_runtime()

    status = RUNTIME_READY if sk_info["installed"] else RUNTIME_READY_WITH_WARNINGS
    backend = BACKEND_SKLEARN_AVAILABLE if sk_info["installed"] else BACKEND_OPTIONAL_DEPENDENCY_MISSING

    rows: List[Dict[str, Any]] = [
        {
            "check_id": "sklearn_installed",
            "property_name": "Scikit-Learn Installed",
            "property_value": str(sk_info["installed"]),
            "backend_label": backend,
            "status_label": status,
            "manual_review_required": not sk_info["installed"],
            "non_signal": True,
            "source_preserved": True,
            "details": "Checks if scikit-learn is present in environment.",
        },
        {
            "check_id": "sklearn_version",
            "property_name": "Scikit-Learn Version",
            "property_value": sk_info["version"],
            "backend_label": backend,
            "status_label": status,
            "manual_review_required": False,
            "non_signal": True,
            "source_preserved": True,
            "details": "Installed scikit-learn release version string.",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_sklearn_runtime_capability(df)
    summary["domain"] = SKLEARN_CAPABILITY_DOMAIN
    summary["active_profile"] = active.profile_name
    summary["sklearn_installed"] = sk_info["installed"]
    return df, summary


def summarize_sklearn_runtime_capability(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize scikit-learn capability DataFrame."""
    installed = False
    if not df.empty and "property_name" in df.columns:
        m = df[df["property_name"] == "Scikit-Learn Installed"]
        if not m.empty:
            installed = m.iloc[0]["property_value"] == "True"
    return {
        "total_checks": len(df),
        "sklearn_installed": installed,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
